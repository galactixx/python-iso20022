from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    FundingSourceType1Code,
    ReinvestmentType1Code,
    ReportPeriodActivity1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02"


@dataclass
class ActiveOrHistoricCurrencyAndAmountAuth07100102(ISO20022MessageElement):
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
class GenericIdentification175Auth07100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth07100102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection53Auth07100102(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth07100102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class OrganisationIdentification38Auth07100102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth07100102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class ReinvestedCashTypeAndAmount1Auth07100102(ISO20022MessageElement):
    tp: Optional[ReinvestmentType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    rinvstd_csh_amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth07100102] = field(
        default=None,
        metadata={
            "name": "RinvstdCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )


@dataclass
class ReuseValue1ChoiceAuth07100102(ISO20022MessageElement):
    actl: Optional[ActiveOrHistoricCurrencyAndAmountAuth07100102] = field(
        default=None,
        metadata={
            "name": "Actl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    estmtd: Optional[ActiveOrHistoricCurrencyAndAmountAuth07100102] = field(
        default=None,
        metadata={
            "name": "Estmtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth07100102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth07100102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )


@dataclass
class CashReuseData1Auth07100102(ISO20022MessageElement):
    rinvstd_csh: list[ReinvestedCashTypeAndAmount1Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "RinvstdCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_occurs": 1,
        },
    )
    csh_rinvstmt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CshRinvstmtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class FundingSource3Auth07100102(ISO20022MessageElement):
    tp: Optional[FundingSourceType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    mkt_val: Optional[AmountAndDirection53Auth07100102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth07100102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth07100102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SecurityReuseData1Auth07100102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    reuse_val: Optional[ReuseValue1ChoiceAuth07100102] = field(
        default=None,
        metadata={
            "name": "ReuseVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )


@dataclass
class CollateralType19Auth07100102(ISO20022MessageElement):
    scty: list[SecurityReuseData1Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    csh: list[CashReuseData1Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "Csh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class CounterpartyData87Auth07100102(ISO20022MessageElement):
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth07100102] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth07100102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth07100102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            },
        )
    )


@dataclass
class ReuseDataReportCorrection14Auth07100102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    ctr_pty: Optional[CounterpartyData87Auth07100102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    coll_cmpnt: list[CollateralType19Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "CollCmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    evt_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    fndg_src: list[FundingSource3Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "FndgSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class ReuseDataReportError5Auth07100102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    ctr_pty: Optional[CounterpartyData87Auth07100102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class ReuseDataReportNew6Auth07100102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    ctr_pty: Optional[CounterpartyData87Auth07100102] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    coll_cmpnt: list[CollateralType19Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "CollCmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    evt_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    fndg_src: list[FundingSource3Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "FndgSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class ReuseDataReport6ChoiceAuth07100102(ISO20022MessageElement):
    new: Optional[ReuseDataReportNew6Auth07100102] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    err: Optional[ReuseDataReportError5Auth07100102] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    crrctn: Optional[ReuseDataReportCorrection14Auth07100102] = field(
        default=None,
        metadata={
            "name": "Crrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    coll_reuse_upd: Optional[ReuseDataReportCorrection14Auth07100102] = field(
        default=None,
        metadata={
            "name": "CollReuseUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class TradeData36ChoiceAuth07100102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )
    rpt: list[ReuseDataReport6ChoiceAuth07100102] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class SecuritiesFinancingReportingTransactionReusedCollateralDataReportV02Auth07100102(
    ISO20022MessageElement
):
    trad_data: Optional[TradeData36ChoiceAuth07100102] = field(
        default=None,
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth07100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02",
        },
    )


@dataclass
class Auth07100102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02"

    scties_fincg_rptg_tx_reusd_coll_data_rpt: Optional[
        SecuritiesFinancingReportingTransactionReusedCollateralDataReportV02Auth07100102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgTxReusdCollDataRpt",
            "type": "Element",
            "required": True,
        },
    )
