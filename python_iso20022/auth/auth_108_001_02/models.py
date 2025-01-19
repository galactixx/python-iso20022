from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    CollateralisationType3Code,
    FinancialPartySectorType3Code,
    NotApplicable1Code,
    ReportPeriodActivity1Code,
    TradeCounterpartyType1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    NoReasonCode,
    OptionParty1Code,
    OptionParty3Code,
    TradingCapacity7Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02"


@dataclass
class ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102(ISO20022MessageElement):
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
class GenericIdentification175Auth10800102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Auth10800102(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )


@dataclass
class PortfolioIdentification3Auth10800102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class ReportingExemption1Auth10800102(ISO20022MessageElement):
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth10800102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TechnicalAttributes6Auth10800102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rpt_rct_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptRctTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class TradeCounterpartyRelationship1ChoiceAuth10800102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class Direction2Auth10800102(ISO20022MessageElement):
    drctn_of_the_frst_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheFrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    drctn_of_the_scnd_leg: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "DrctnOfTheScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class FinancialPartyClassification2ChoiceAuth10800102(ISO20022MessageElement):
    cd: Optional[FinancialPartySectorType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    prtry: Optional[GenericIdentification175Auth10800102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class NaturalPersonIdentification2Auth10800102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth10800102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class NonFinancialInstitutionSector10Auth10800102(ISO20022MessageElement):
    sctr: list[GenericIdentification175Auth10800102] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_occurs": 1,
        },
    )
    clr_thrshld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    drctly_lkd_actvty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DrctlyLkdActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    fdrl_instn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FdrlInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class OrganisationIdentification38Auth10800102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth10800102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PortfolioCode3ChoiceAuth10800102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class PortfolioCode5ChoiceAuth10800102(ISO20022MessageElement):
    prtfl: Optional[PortfolioIdentification3Auth10800102] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class PostedMarginOrCollateral6Auth10800102(ISO20022MessageElement):
    initl_mrgn_pstd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    initl_mrgn_pstd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    vartn_mrgn_pstd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    vartn_mrgn_pstd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    xcss_coll_pstd: Optional[ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102] = (
        field(
            default=None,
            metadata={
                "name": "XcssCollPstd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            },
        )
    )


@dataclass
class ReceivedMarginOrCollateral6Auth10800102(ISO20022MessageElement):
    initl_mrgn_rcvd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRcvdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    initl_mrgn_rcvd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRcvdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    vartn_mrgn_rcvd_pre_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRcvdPreHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    vartn_mrgn_rcvd_pst_hrcut: Optional[
        ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102
    ] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRcvdPstHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    xcss_coll_rcvd: Optional[ActiveOrHistoricCurrencyAnd20DecimalAmountAuth10800102] = (
        field(
            default=None,
            metadata={
                "name": "XcssCollRcvd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            },
        )
    )


@dataclass
class SupplementaryData1Auth10800102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth10800102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )


@dataclass
class TradeCounterpartyRelationshipRecord1Auth10800102(ISO20022MessageElement):
    start_rltsh_pty: Optional[TradeCounterpartyType1Code] = field(
        default=None,
        metadata={
            "name": "StartRltshPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    end_rltsh_pty: Optional[TradeCounterpartyType1Code] = field(
        default=None,
        metadata={
            "name": "EndRltshPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    rltsh_tp: Optional[TradeCounterpartyRelationship1ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "RltshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class UniqueTransactionIdentifier2ChoiceAuth10800102(ISO20022MessageElement):
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification175Auth10800102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class Direction4ChoiceAuth10800102(ISO20022MessageElement):
    drctn: Optional[Direction2Auth10800102] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    ctr_pty_sd: Optional[OptionParty1Code] = field(
        default=None,
        metadata={
            "name": "CtrPtySd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class FinancialInstitutionSector1Auth10800102(ISO20022MessageElement):
    sctr: list[FinancialPartyClassification2ChoiceAuth10800102] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_occurs": 1,
        },
    )
    clr_thrshld: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class MarginPortfolio4Auth10800102(ISO20022MessageElement):
    initl_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    vartn_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class NaturalPersonIdentification3Auth10800102(ISO20022MessageElement):
    id: Optional[NaturalPersonIdentification2Auth10800102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth10800102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth10800102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class CollateralPortfolioCode6ChoiceAuth10800102(ISO20022MessageElement):
    prtfl: Optional[PortfolioCode3ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    mrgn_prtfl_cd: Optional[MarginPortfolio4Auth10800102] = field(
        default=None,
        metadata={
            "name": "MrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class CounterpartyTradeNature15ChoiceAuth10800102(ISO20022MessageElement):
    fi: Optional[FinancialInstitutionSector1Auth10800102] = field(
        default=None,
        metadata={
            "name": "FI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    nfi: Optional[NonFinancialInstitutionSector10Auth10800102] = field(
        default=None,
        metadata={
            "name": "NFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    cntrl_cntr_pty: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "CntrlCntrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    othr: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class LegalPersonIdentification1Auth10800102(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class TradeReportHeader4Auth10800102(ISO20022MessageElement):
    rpt_exctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    msg_pgntn: Optional[Pagination1Auth10800102] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    nb_rcrds: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cmptnt_authrty: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )
    new_trad_rpstry_idr: Optional[OrganisationIdentification15ChoiceAuth10800102] = (
        field(
            default=None,
            metadata={
                "name": "NewTradRpstryIdr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            },
        )
    )
    rptg_purp: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RptgPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "min_length": 1,
            "max_length": 100,
        },
    )


@dataclass
class MarginCollateralReport5Auth10800102(ISO20022MessageElement):
    coll_prtfl_cd: Optional[CollateralPortfolioCode6ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    collstn_ctgy: Optional[CollateralisationType3Code] = field(
        default=None,
        metadata={
            "name": "CollstnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class PartyIdentification248ChoiceAuth10800102(ISO20022MessageElement):
    lgl: Optional[LegalPersonIdentification1Auth10800102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification3Auth10800102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class Counterparty45Auth10800102(ISO20022MessageElement):
    id: Optional[PartyIdentification248ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    ntr: Optional[CounterpartyTradeNature15ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    tradg_cpcty: Optional[TradingCapacity7Code] = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    drctn_or_sd: Optional[Direction4ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "DrctnOrSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    tradr_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    bookg_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rptg_xmptn: Optional[ReportingExemption1Auth10800102] = field(
        default=None,
        metadata={
            "name": "RptgXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class Counterparty46Auth10800102(ISO20022MessageElement):
    id_tp: Optional[PartyIdentification248ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    ntr: Optional[CounterpartyTradeNature15ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    rptg_oblgtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RptgOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class TradeCounterpartyReport20Auth10800102(ISO20022MessageElement):
    rptg_ctr_pty: Optional[Counterparty45Auth10800102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[Counterparty46Auth10800102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    brkr: Optional[OrganisationIdentification15ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    submitg_agt: Optional[OrganisationIdentification15ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "SubmitgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    clr_mmb: Optional[PartyIdentification248ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    bnfcry: list[PartyIdentification248ChoiceAuth10800102] = field(
        default_factory=list,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "max_occurs": 2,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth10800102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            },
        )
    )
    exctn_agt: list[OrganisationIdentification15ChoiceAuth10800102] = field(
        default_factory=list,
        metadata={
            "name": "ExctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "max_occurs": 2,
        },
    )
    rltsh_rcrd: list[TradeCounterpartyRelationshipRecord1Auth10800102] = field(
        default_factory=list,
        metadata={
            "name": "RltshRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class MarginReportData9Auth10800102(ISO20022MessageElement):
    rptg_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    ctr_pty_id: Optional[TradeCounterpartyReport20Auth10800102] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    tx_id: Optional[UniqueTransactionIdentifier2ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    coll: Optional[MarginCollateralReport5Auth10800102] = field(
        default=None,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    pstd_mrgn_or_coll: Optional[PostedMarginOrCollateral6Auth10800102] = field(
        default=None,
        metadata={
            "name": "PstdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    rcvd_mrgn_or_coll: Optional[ReceivedMarginOrCollateral6Auth10800102] = field(
        default=None,
        metadata={
            "name": "RcvdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    ctr_pty_ratg_trggr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtrPtyRatgTrggrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    ctr_pty_ratg_thrshld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtrPtyRatgThrshldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    tech_attrbts: Optional[TechnicalAttributes6Auth10800102] = field(
        default=None,
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Auth10800102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class TradeReport34ChoiceAuth10800102(ISO20022MessageElement):
    new: Optional[MarginReportData9Auth10800102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    mrgn_upd: Optional[MarginReportData9Auth10800102] = field(
        default=None,
        metadata={
            "name": "MrgnUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    err: Optional[MarginReportData9Auth10800102] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    crrctn: Optional[MarginReportData9Auth10800102] = field(
        default=None,
        metadata={
            "name": "Crrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class TradeData61ChoiceAuth10800102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )
    rpt: list[TradeReport34ChoiceAuth10800102] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class DerivativesTradeMarginDataReportV02Auth10800102(ISO20022MessageElement):
    rpt_hdr: Optional[TradeReportHeader4Auth10800102] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    trad_data: Optional[TradeData61ChoiceAuth10800102] = field(
        default=None,
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth10800102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02",
        },
    )


@dataclass
class Auth10800102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.108.001.02"

    derivs_trad_mrgn_data_rpt: Optional[
        DerivativesTradeMarginDataReportV02Auth10800102
    ] = field(
        default=None,
        metadata={
            "name": "DerivsTradMrgnDataRpt",
            "type": "Element",
            "required": True,
        },
    )
