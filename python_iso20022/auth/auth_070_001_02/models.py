from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import ReportPeriodActivity1Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02"


@dataclass
class ActiveOrHistoricCurrencyAndAmountAuth07000102(ISO20022MessageElement):
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
class GenericIdentification175Auth07000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth07000102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class NaturalPersonIdentification2Auth07000102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth07000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification38Auth07000102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth07000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PostedMarginOrCollateral4Auth07000102(ISO20022MessageElement):
    initl_mrgn_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth07000102] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    vartn_mrgn_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth07000102] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    xcss_coll_pstd: Optional[ActiveOrHistoricCurrencyAndAmountAuth07000102] = field(
        default=None,
        metadata={
            "name": "XcssCollPstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class ReceivedMarginOrCollateral4Auth07000102(ISO20022MessageElement):
    initl_mrgn_rcvd: Optional[ActiveOrHistoricCurrencyAndAmountAuth07000102] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    vartn_mrgn_rcvd: Optional[ActiveOrHistoricCurrencyAndAmountAuth07000102] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    xcss_coll_rcvd: Optional[ActiveOrHistoricCurrencyAndAmountAuth07000102] = field(
        default=None,
        metadata={
            "name": "XcssCollRcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth07000102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth07000102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth07000102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth07000102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth07000102(ISO20022MessageElement):
    lgl: Optional[OrganisationIdentification15ChoiceAuth07000102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth07000102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class Counterparty39Auth07000102(ISO20022MessageElement):
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth07000102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[PartyIdentification236ChoiceAuth07000102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth07000102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            },
        )
    )
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth07000102] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class CollateralMarginCorrection6Auth07000102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    ctr_pty: Optional[Counterparty39Auth07000102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    coll_prtfl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    pstd_mrgn_or_coll: Optional[PostedMarginOrCollateral4Auth07000102] = field(
        default=None,
        metadata={
            "name": "PstdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    rcvd_mrgn_or_coll: Optional[ReceivedMarginOrCollateral4Auth07000102] = field(
        default=None,
        metadata={
            "name": "RcvdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Auth07000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class CollateralMarginError4Auth07000102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    ctr_pty: Optional[Counterparty39Auth07000102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    coll_prtfl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    splmtry_data: list[SupplementaryData1Auth07000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class CollateralMarginMarginUpdate5Auth07000102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    ctr_pty: Optional[Counterparty39Auth07000102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    coll_prtfl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    pstd_mrgn_or_coll: Optional[PostedMarginOrCollateral4Auth07000102] = field(
        default=None,
        metadata={
            "name": "PstdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    rcvd_mrgn_or_coll: Optional[ReceivedMarginOrCollateral4Auth07000102] = field(
        default=None,
        metadata={
            "name": "RcvdMrgnOrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Auth07000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class TradeReport21ChoiceAuth07000102(ISO20022MessageElement):
    new: Optional[CollateralMarginCorrection6Auth07000102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    err: Optional[CollateralMarginError4Auth07000102] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    crrctn: Optional[CollateralMarginCorrection6Auth07000102] = field(
        default=None,
        metadata={
            "name": "Crrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    trad_upd: Optional[CollateralMarginMarginUpdate5Auth07000102] = field(
        default=None,
        metadata={
            "name": "TradUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class TradeData39ChoiceAuth07000102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )
    rpt: list[TradeReport21ChoiceAuth07000102] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class SecuritiesFinancingReportingTransactionMarginDataReportV02Auth07000102(
    ISO20022MessageElement
):
    trad_data: Optional[TradeData39ChoiceAuth07000102] = field(
        default=None,
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth07000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02",
        },
    )


@dataclass
class Auth07000102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02"

    scties_fincg_rptg_tx_mrgn_data_rpt: Optional[
        SecuritiesFinancingReportingTransactionMarginDataReportV02Auth07000102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgTxMrgnDataRpt",
            "type": "Element",
            "required": True,
        },
    )
