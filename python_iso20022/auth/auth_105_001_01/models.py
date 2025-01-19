from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.auth.auth_105_001_01.enums import TradeMarket2Code
from python_iso20022.auth.enums import (
    CollateralQualityType1Code,
    CollateralType6Code,
    ExposureType10Code,
    PriceStatus1Code,
    RateBasis1Code,
    ReinvestmentType1Code,
    ReportPeriodActivity1Code,
    SpecialCollateral1Code,
    SpecialPurpose2Code,
    TradeRepositoryReportingType1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import CollateralRole1Code, NoReasonCode

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01"


@dataclass
class ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10500101(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 25,
            "fraction_digits": 20,
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
class ActiveOrHistoricCurrencyAndAmountAuth10500101(ISO20022MessageElement):
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
class GenericIdentification175Auth10500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 72,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IssuerJurisdiction1ChoiceAuth10500101(ISO20022MessageElement):
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesLendingType3ChoiceAuth10500101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesTransactionPrice5Auth10500101(ISO20022MessageElement):
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth10500101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection107Auth10500101(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class AmountAndDirection53Auth10500101(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class MaturityTerm2Auth10500101(ISO20022MessageElement):
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class OrganisationIdentification38Auth10500101(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth10500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PostedMarginOrCollateral4Auth10500101(ISO20022MessageElement):
    initl_mrgn_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    vartn_mrgn_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    xcss_coll_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "XcssCollPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PrincipalAmount3Auth10500101(ISO20022MessageElement):
    val_dt_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "ValDtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mtrty_dt_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "MtrtyDtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class Rates1ChoiceAuth10500101(ISO20022MessageElement):
    fxd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    fltg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class ReconciliationFlag2Auth10500101(ISO20022MessageElement):
    rpt_tp: Optional[TradeRepositoryReportingType1Code] = field(
        default=None,
        metadata={
            "name": "RptTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    both_ctr_pties_rptg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BothCtrPtiesRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    paird_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PairdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    ln_rcncltn_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LnRcncltnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    coll_rcncltn_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollRcncltnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mod_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ModSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class ReinvestedCashTypeAndAmount2Auth10500101(ISO20022MessageElement):
    tp: Optional[ReinvestmentType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    rinvstd_csh_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RinvstdCshCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class ReuseValue1ChoiceAuth10500101(ISO20022MessageElement):
    actl: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "Actl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    estmtd: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "Estmtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth10500101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth10500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )


@dataclass
class TradingVenueType1ChoiceAuth10500101(ISO20022MessageElement):
    on_vn: Optional[TradeMarket2Code] = field(
        default=None,
        metadata={
            "name": "OnVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    off_vn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "OffVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class ExposureMetrics4Auth10500101(ISO20022MessageElement):
    prncpl_amt: Optional[PrincipalAmount3Auth10500101] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    ln_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "LnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth10500101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    outsdng_mrgn_ln_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = (
        field(
            default=None,
            metadata={
                "name": "OutsdngMrgnLnAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            },
        )
    )
    shrt_mkt_val_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "ShrtMktValAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mrgn_ln: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "MrgnLn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    csh_coll_amt: Optional[AmountAndDirection53Auth10500101] = field(
        default=None,
        metadata={
            "name": "CshCollAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    coll_mkt_val: Optional[AmountAndDirection53Auth10500101] = field(
        default=None,
        metadata={
            "name": "CollMktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class ExposureMetrics5Auth10500101(ISO20022MessageElement):
    csh_coll_amt: Optional[AmountAndDirection53Auth10500101] = field(
        default=None,
        metadata={
            "name": "CshCollAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    coll_mkt_val: Optional[AmountAndDirection53Auth10500101] = field(
        default=None,
        metadata={
            "name": "CollMktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class ExposureMetrics6Auth10500101(ISO20022MessageElement):
    pstd_mrgn_or_coll: Optional[PostedMarginOrCollateral4Auth10500101] = field(
        default=None,
        metadata={
            "name": "PstdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth10500101(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth10500101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class QuantityNominalValue2ChoiceAuth10500101(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    nmnl_val: Optional[AmountAndDirection53Auth10500101] = field(
        default=None,
        metadata={
            "name": "NmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class SecuritiesTransactionPrice18ChoiceAuth10500101(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection107Auth10500101] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class SecuritiesTransactionPrice19ChoiceAuth10500101(ISO20022MessageElement):
    mntry_val: Optional[AmountAndDirection107Auth10500101] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dcml: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pdg_pric: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "PdgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    othr: Optional[SecuritiesTransactionPrice5Auth10500101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class TimeToMaturityPeriod2Auth10500101(ISO20022MessageElement):
    start: Optional[MaturityTerm2Auth10500101] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    end: Optional[MaturityTerm2Auth10500101] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class VolumeMetrics4Auth10500101(ISO20022MessageElement):
    reuse_val: Optional[ReuseValue1ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "ReuseVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    rinvstd_csh_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth10500101] = field(
        default=None,
        metadata={
            "name": "RinvstdCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class CounterpartyIdentification10Auth10500101(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    sd: Optional[CollateralRole1Code] = field(
        default=None,
        metadata={
            "name": "Sd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSetDimensions15Auth10500101(ISO20022MessageElement):
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    othr_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    coll_prtfl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 52,
        },
    )
    otlrs_incl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OtlrsIncl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSetMetrics10Auth10500101(ISO20022MessageElement):
    vol_mtrcs: Optional[ExposureMetrics6Auth10500101] = field(
        default=None,
        metadata={
            "name": "VolMtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSetMetrics11Auth10500101(ISO20022MessageElement):
    vol_mtrcs: Optional[VolumeMetrics4Auth10500101] = field(
        default=None,
        metadata={
            "name": "VolMtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    csh_rinvstmt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CshRinvstmtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class Rates3Auth10500101(ISO20022MessageElement):
    fxd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    buy_sell_bck: Optional[SecuritiesTransactionPrice18ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "BuySellBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class SecurityIssuer4Auth10500101(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    jursdctn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "JursdctnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class TimeToMaturity2ChoiceAuth10500101(ISO20022MessageElement):
    prd: Optional[TimeToMaturityPeriod2Auth10500101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    spcl: Optional[SpecialPurpose2Code] = field(
        default=None,
        metadata={
            "name": "Spcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class VolumeMetrics5Auth10500101(ISO20022MessageElement):
    nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    xpsr: Optional[ExposureMetrics4Auth10500101] = field(
        default=None,
        metadata={
            "name": "Xpsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class VolumeMetrics6Auth10500101(ISO20022MessageElement):
    postv: Optional[ExposureMetrics5Auth10500101] = field(
        default=None,
        metadata={
            "name": "Postv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    neg: Optional[ExposureMetrics5Auth10500101] = field(
        default=None,
        metadata={
            "name": "Neg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class ContractTerm6ChoiceAuth10500101(ISO20022MessageElement):
    opn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Opn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    fxd: Optional[TimeToMaturity2ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class CounterpartyData86Auth10500101(ISO20022MessageElement):
    rptg_ctr_pty: Optional[CounterpartyIdentification10Auth10500101] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    othr_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    trpty_agt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    agt_lndr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AgtLndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSet20Auth10500101(ISO20022MessageElement):
    dmnsns: Optional[PositionSetDimensions15Auth10500101] = field(
        default=None,
        metadata={
            "name": "Dmnsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    mtrcs: Optional[PositionSetMetrics10Auth10500101] = field(
        default=None,
        metadata={
            "name": "Mtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )


@dataclass
class PositionSetMetrics12Auth10500101(ISO20022MessageElement):
    vol_mtrcs: Optional[VolumeMetrics6Auth10500101] = field(
        default=None,
        metadata={
            "name": "VolMtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    hrcut_or_mrgn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HrcutOrMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qty_or_nmnl_amt: Optional[QuantityNominalValue2ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "QtyOrNmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSetMetrics7Auth10500101(ISO20022MessageElement):
    vol_mtrcs: Optional[VolumeMetrics5Auth10500101] = field(
        default=None,
        metadata={
            "name": "VolMtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )


@dataclass
class PriceMetrics3Auth10500101(ISO20022MessageElement):
    rates: Optional[Rates3Auth10500101] = field(
        default=None,
        metadata={
            "name": "Rates",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    lndg_fee: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LndgFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class Security49Auth10500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    qty_or_nmnl_val: Optional[QuantityNominalValue2ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "QtyOrNmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    unit_pric: Optional[SecuritiesTransactionPrice19ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth10500101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    qlty: Optional[CollateralQualityType1Code] = field(
        default=None,
        metadata={
            "name": "Qlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mtrty: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Mtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    issr: Optional[SecurityIssuer4Auth10500101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    tp: list[SecuritiesLendingType3ChoiceAuth10500101] = field(
        default_factory=list,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    exclsv_arrgmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExclsvArrgmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class CollateralData33Auth10500101(ISO20022MessageElement):
    net_xpsr_collstn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NetXpsrCollstnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    cmpnt_tp: Optional[CollateralType6Code] = field(
        default=None,
        metadata={
            "name": "CmpntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    csh_coll_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshCollCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    pric_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qlty: Optional[CollateralQualityType1Code] = field(
        default=None,
        metadata={
            "name": "Qlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mtrty: Optional[ContractTerm6ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "Mtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    issr_jursdctn: Optional[IssuerJurisdiction1ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "IssrJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    tp: Optional[SecuritiesLendingType3ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    trad_rpstry: Optional[OrganisationIdentification15ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "TradRpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    rcncltn_flg: Optional[ReconciliationFlag2Auth10500101] = field(
        default=None,
        metadata={
            "name": "RcncltnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    rinvstd_csh: Optional[ReinvestedCashTypeAndAmount2Auth10500101] = field(
        default=None,
        metadata={
            "name": "RinvstdCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class LoanData134Auth10500101(ISO20022MessageElement):
    ctrct_tp: Optional[ExposureType10Code] = field(
        default=None,
        metadata={
            "name": "CtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    clrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Clrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    prtfl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 52,
        },
    )
    tradg_vn: Optional[TradingVenueType1ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mstr_agrmt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrAgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    gnl_coll: Optional[SpecialCollateral1Code] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    term: Optional[ContractTerm6ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    rates: Optional[Rates1ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "Rates",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    prncpl_amt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrncplAmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    pric_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    scty: Optional[Security49Auth10500101] = field(
        default=None,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    outsdng_mrgn_ln_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OutsdngMrgnLnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class PositionSetMetrics13Auth10500101(ISO20022MessageElement):
    vol_mtrcs: Optional[VolumeMetrics5Auth10500101] = field(
        default=None,
        metadata={
            "name": "VolMtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    pric_mtrcs: Optional[PriceMetrics3Auth10500101] = field(
        default=None,
        metadata={
            "name": "PricMtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSetDimensions12Auth10500101(ISO20022MessageElement):
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    coll_data: Optional[CollateralData33Auth10500101] = field(
        default=None,
        metadata={
            "name": "CollData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    otlrs_incl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OtlrsIncl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSetDimensions14Auth10500101(ISO20022MessageElement):
    ctr_pty_data: Optional[CounterpartyData86Auth10500101] = field(
        default=None,
        metadata={
            "name": "CtrPtyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    ln_data: Optional[LoanData134Auth10500101] = field(
        default=None,
        metadata={
            "name": "LnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    coll_data: Optional[CollateralData33Auth10500101] = field(
        default=None,
        metadata={
            "name": "CollData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    otlrs_incl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OtlrsIncl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSet16Auth10500101(ISO20022MessageElement):
    dmnsns: Optional[PositionSetDimensions14Auth10500101] = field(
        default=None,
        metadata={
            "name": "Dmnsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    mtrcs: Optional[PositionSetMetrics7Auth10500101] = field(
        default=None,
        metadata={
            "name": "Mtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )


@dataclass
class PositionSet17Auth10500101(ISO20022MessageElement):
    dmnsns: Optional[PositionSetDimensions14Auth10500101] = field(
        default=None,
        metadata={
            "name": "Dmnsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    mtrcs: Optional[PositionSetMetrics13Auth10500101] = field(
        default=None,
        metadata={
            "name": "Mtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )


@dataclass
class PositionSet18Auth10500101(ISO20022MessageElement):
    dmnsns: Optional[PositionSetDimensions14Auth10500101] = field(
        default=None,
        metadata={
            "name": "Dmnsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    mtrcs: Optional[PositionSetMetrics12Auth10500101] = field(
        default=None,
        metadata={
            "name": "Mtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )


@dataclass
class PositionSet19Auth10500101(ISO20022MessageElement):
    dmnsns: Optional[PositionSetDimensions12Auth10500101] = field(
        default=None,
        metadata={
            "name": "Dmnsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    mtrcs: Optional[PositionSetMetrics11Auth10500101] = field(
        default=None,
        metadata={
            "name": "Mtrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )


@dataclass
class NamedPosition3Auth10500101(ISO20022MessageElement):
    ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    gnl_inf: list[PositionSet16Auth10500101] = field(
        default_factory=list,
        metadata={
            "name": "GnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    ln: list[PositionSet17Auth10500101] = field(
        default_factory=list,
        metadata={
            "name": "Ln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    coll: list[PositionSet18Auth10500101] = field(
        default_factory=list,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    mrgn: list[PositionSet20Auth10500101] = field(
        default_factory=list,
        metadata={
            "name": "Mrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    reuse: list[PositionSet19Auth10500101] = field(
        default_factory=list,
        metadata={
            "name": "Reuse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class PositionSetReport3ChoiceAuth10500101(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )
    rpt: Optional[NamedPosition3Auth10500101] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class SecuritiesFinancingReportingPositionSetReportV01Auth10500101(
    ISO20022MessageElement
):
    aggtd_poss: Optional[PositionSetReport3ChoiceAuth10500101] = field(
        default=None,
        metadata={
            "name": "AggtdPoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth10500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01",
        },
    )


@dataclass
class Auth10500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01"

    scties_fincg_rptg_pos_set_rpt: Optional[
        SecuritiesFinancingReportingPositionSetReportV01Auth10500101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgPosSetRpt",
            "type": "Element",
            "required": True,
        },
    )
