from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    ModificationLevel1Code,
    ReportPeriodActivity1Code,
    TradeRepositoryReportingType1Code,
    TransactionOperationType6Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02"


@dataclass
class ActiveOrHistoricCurrencyAndAmountAuth08500102(ISO20022MessageElement):
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
class GenericIdentification175Auth08500102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth08500102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ContractModification3Auth08500102(ISO20022MessageElement):
    actn_tp: Optional[TransactionOperationType6Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    lvl: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "Lvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class NaturalPersonIdentification2Auth08500102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth08500102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification38Auth08500102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth08500102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PostedMarginOrCollateral4Auth08500102(ISO20022MessageElement):
    initl_mrgn_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth08500102] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    vartn_mrgn_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth08500102] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    xcss_coll_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth08500102] = field(
        default=None,
        metadata={
            "name": "XcssCollPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class ReceivedMarginOrCollateral4Auth08500102(ISO20022MessageElement):
    initl_mrgn_rcvd: Optional[ActiveOrHistoricCurrencyAndAmountAuth08500102] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    vartn_mrgn_rcvd: Optional[ActiveOrHistoricCurrencyAndAmountAuth08500102] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    xcss_coll_rcvd: Optional[ActiveOrHistoricCurrencyAndAmountAuth08500102] = field(
        default=None,
        metadata={
            "name": "XcssCollRcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class ReconciliationFlag2Auth08500102(ISO20022MessageElement):
    rpt_tp: Optional[TradeRepositoryReportingType1Code] = field(
        default=None,
        metadata={
            "name": "RptTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    both_ctr_pties_rptg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BothCtrPtiesRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    paird_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PairdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    ln_rcncltn_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LnRcncltnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    coll_rcncltn_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollRcncltnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    mod_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ModSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth08500102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth08500102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth08500102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth08500102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth08500102(ISO20022MessageElement):
    lgl: Optional[OrganisationIdentification15ChoiceAuth08500102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth08500102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class Counterparty39Auth08500102(ISO20022MessageElement):
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth08500102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[PartyIdentification236ChoiceAuth08500102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth08500102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            },
        )
    )
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth08500102] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class CollateralMarginNew10Auth08500102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    ctr_pty: Optional[Counterparty39Auth08500102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    coll_prtfl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    pstd_mrgn_or_coll: Optional[PostedMarginOrCollateral4Auth08500102] = field(
        default=None,
        metadata={
            "name": "PstdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    rcvd_mrgn_or_coll: Optional[ReceivedMarginOrCollateral4Auth08500102] = field(
        default=None,
        metadata={
            "name": "RcvdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    rcncltn_flg: Optional[ReconciliationFlag2Auth08500102] = field(
        default=None,
        metadata={
            "name": "RcncltnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    ctrct_mod: Optional[ContractModification3Auth08500102] = field(
        default=None,
        metadata={
            "name": "CtrctMod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth08500102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class TradeData38ChoiceAuth08500102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )
    stat: list[CollateralMarginNew10Auth08500102] = field(
        default_factory=list,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class SecuritiesFinancingReportingMarginDataTransactionStateReportV02Auth08500102(
    ISO20022MessageElement
):
    trad_data: Optional[TradeData38ChoiceAuth08500102] = field(
        default=None,
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth08500102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02",
        },
    )


@dataclass
class Auth08500102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02"

    scties_fincg_rptg_mrgn_data_tx_stat_rpt: Optional[
        SecuritiesFinancingReportingMarginDataTransactionStateReportV02Auth08500102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgMrgnDataTxStatRpt",
            "type": "Element",
            "required": True,
        },
    )
