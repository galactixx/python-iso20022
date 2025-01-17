from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    DerivativeEventType3Code,
    Frequency19Code,
    NotApplicable1Code,
    ReportPeriodActivity1Code,
    TransactionOperationType10Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01"


@dataclass
class ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10600101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 25,
            "fraction_digits": 19,
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
class AgreementType2ChoiceAuth10600101:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class DateAndDateTime2ChoiceAuth10600101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class GenericIdentification175Auth10600101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PortfolioIdentification3Auth10600101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtfl_tx_xmptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtflTxXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth10600101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection106Auth10600101:
    amt: Optional[ActiveOrHistoricCurrencyAnd19DecimalAmountAuth10600101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class MasterAgreement8Auth10600101:
    tp: Optional[AgreementType2ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NaturalPersonIdentification2Auth10600101:
    id: Optional[GenericIdentification175Auth10600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification38Auth10600101:
    id: Optional[GenericIdentification175Auth10600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PortfolioCode3ChoiceAuth10600101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 52,
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class PortfolioCode5ChoiceAuth10600101:
    prtfl: Optional[PortfolioIdentification3Auth10600101] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth10600101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth10600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )


@dataclass
class UniqueTransactionIdentifier2ChoiceAuth10600101:
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification175Auth10600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class UnitOfMeasure8ChoiceAuth10600101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification175Auth10600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class MarginPortfolio3Auth10600101:
    initl_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    vartn_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class NaturalPersonIdentification3Auth10600101:
    id: Optional[NaturalPersonIdentification2Auth10600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth10600101:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth10600101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class QuantityTerm1Auth10600101:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    tm_unit: Optional[Frequency19Code] = field(
        default=None,
        metadata={
            "name": "TmUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class Schedule10Auth10600101:
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    uadjstd_fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    uadjstd_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class Schedule11Auth10600101:
    uadjstd_fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    uadjstd_end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    amt: Optional[AmountAndDirection106Auth10600101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )


@dataclass
class CollateralPortfolioCode5ChoiceAuth10600101:
    prtfl: Optional[PortfolioCode3ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    mrgn_prtfl_cd: Optional[MarginPortfolio3Auth10600101] = field(
        default=None,
        metadata={
            "name": "MrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class CounterpartyData92Auth10600101:
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth10600101] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            },
        )
    )


@dataclass
class LegalPersonIdentification1Auth10600101:
    id: Optional[OrganisationIdentification15ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class NotionalAmount5Auth10600101:
    amt: Optional[AmountAndDirection106Auth10600101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    schdl_prd: list[Schedule11Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class NotionalAmount6Auth10600101:
    amt: Optional[AmountAndDirection106Auth10600101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    schdl_prd: list[Schedule11Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class QuantityOrTerm1ChoiceAuth10600101:
    schdl_prd: list[Schedule10Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    term: Optional[QuantityTerm1Auth10600101] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class NotionalAmountLegs5Auth10600101:
    frst_leg: Optional[NotionalAmount5Auth10600101] = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    scnd_leg: Optional[NotionalAmount6Auth10600101] = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class NotionalQuantity9Auth10600101:
    ttl_qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "total_digits": 25,
            "fraction_digits": 19,
        },
    )
    unit_of_measr: Optional[UnitOfMeasure8ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    dtls: Optional[QuantityOrTerm1ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class PartyIdentification248ChoiceAuth10600101:
    lgl: Optional[LegalPersonIdentification1Auth10600101] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    ntrl: Optional[NaturalPersonIdentification3Auth10600101] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class NotionalQuantityLegs5Auth10600101:
    frst_leg: Optional[NotionalQuantity9Auth10600101] = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    scnd_leg: Optional[NotionalQuantity9Auth10600101] = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class TradeTransactionIdentification24Auth10600101:
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    actn_tp: Optional[TransactionOperationType10Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    rptg_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    deriv_evt_tp: Optional[DerivativeEventType3Code] = field(
        default=None,
        metadata={
            "name": "DerivEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    deriv_evt_tm_stmp: Optional[DateAndDateTime2ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "DerivEvtTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    othr_ctr_pty: Optional[PartyIdentification248ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    unq_idr: Optional[UniqueTransactionIdentifier2ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "UnqIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    mstr_agrmt: Optional[MasterAgreement8Auth10600101] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    coll_prtfl_cd: Optional[CollateralPortfolioCode5ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class AbnormalValuesTransactionData2Auth10600101:
    tx_id: Optional[TradeTransactionIdentification24Auth10600101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    ntnl_amt: Optional[NotionalAmountLegs5Auth10600101] = field(
        default=None,
        metadata={
            "name": "NtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    ntnl_qty: Optional[NotionalQuantityLegs5Auth10600101] = field(
        default=None,
        metadata={
            "name": "NtnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class MissingMarginTransactionData2Auth10600101:
    tx_id: Optional[TradeTransactionIdentification24Auth10600101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    coll_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CollTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class MissingValuationsTransactionData2Auth10600101:
    tx_id: Optional[TradeTransactionIdentification24Auth10600101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    valtn_amt: Optional[AmountAndDirection106Auth10600101] = field(
        default=None,
        metadata={
            "name": "ValtnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    valtn_tm_stmp: Optional[DateAndDateTime2ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "ValtnTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class AbnormalValuesData4Auth10600101:
    ctr_pty_id: Optional[CounterpartyData92Auth10600101] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    nb_of_derivs_rptd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDerivsRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_derivs_rptd_wth_otlrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDerivsRptdWthOtlrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tx_dtls: list[AbnormalValuesTransactionData2Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class MissingMarginData2Auth10600101:
    ctr_pty_id: Optional[CounterpartyData92Auth10600101] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    nb_of_outsdng_derivs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_no_mrgn_inf: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthNoMrgnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_outdtd_mrgn_inf: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthOutdtdMrgnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tx_dtls: list[MissingMarginTransactionData2Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class MissingValuationsData2Auth10600101:
    ctr_pty_id: Optional[CounterpartyData92Auth10600101] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    nb_of_outsdng_derivs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_no_valtn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthNoValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_outdtd_valtn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthOutdtdValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tx_dtls: list[MissingValuationsTransactionData2Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class DetailedTransactionStatistics26Auth10600101:
    nb_of_outsdng_derivs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_no_mrgn_inf: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthNoMrgnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_outdtd_mrgn_inf: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthOutdtdMrgnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    wrnngs: list[MissingMarginData2Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "Wrnngs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class DetailedTransactionStatistics27Auth10600101:
    nb_of_outsdng_derivs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_no_valtn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthNoValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_outsdng_derivs_wth_outdtd_valtn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfOutsdngDerivsWthOutdtdValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    wrnngs: list[MissingValuationsData2Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "Wrnngs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class DetailedTransactionStatistics28Auth10600101:
    nb_of_derivs_rptd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDerivsRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_derivs_rptd_wth_otlrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDerivsRptdWthOtlrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    wrnngs: list[AbnormalValuesData4Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "Wrnngs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class DetailedAbnormalValuesStatistics4ChoiceAuth10600101:
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    rpt: Optional[DetailedTransactionStatistics28Auth10600101] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class DetailedMissingMarginInformationStatistics4ChoiceAuth10600101:
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    rpt: Optional[DetailedTransactionStatistics26Auth10600101] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class DetailedMissingValuationsStatistics4ChoiceAuth10600101:
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    rpt: Optional[DetailedTransactionStatistics27Auth10600101] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class DetailedStatisticsPerCounterparty17Auth10600101:
    ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    mssng_valtn: Optional[DetailedMissingValuationsStatistics4ChoiceAuth10600101] = (
        field(
            default=None,
            metadata={
                "name": "MssngValtn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
                "required": True,
            },
        )
    )
    mssng_mrgn_inf: Optional[
        DetailedMissingMarginInformationStatistics4ChoiceAuth10600101
    ] = field(
        default=None,
        metadata={
            "name": "MssngMrgnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    abnrml_vals: Optional[DetailedAbnormalValuesStatistics4ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "AbnrmlVals",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )


@dataclass
class StatisticsPerCounterparty16ChoiceAuth10600101:
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )
    rpt: Optional[DetailedStatisticsPerCounterparty17Auth10600101] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class DerivativesTradeWarningsReportV01Auth10600101:
    wrnngs_sttstcs: Optional[StatisticsPerCounterparty16ChoiceAuth10600101] = field(
        default=None,
        metadata={
            "name": "WrnngsSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth10600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01",
        },
    )


@dataclass
class Auth10600101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.106.001.01"

    derivs_trad_wrnngs_rpt: Optional[DerivativesTradeWarningsReportV01Auth10600101] = (
        field(
            default=None,
            metadata={
                "name": "DerivsTradWrnngsRpt",
                "type": "Element",
                "required": True,
            },
        )
    )
