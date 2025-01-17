from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_014_001_02.enums import SecuritiesTransactionType15Code
from python_iso20022.auth.enums import (
    NovationStatus1Code,
    ReportPeriodActivity3Code,
    TransactionOperationType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02"


@dataclass
class ActiveCurrencyAndAmountAuth01400102:
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
class DateAndDateTimeChoiceAuth01400102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )


@dataclass
class DateTimePeriod1Auth01400102:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )


@dataclass
class ForeignExchange1Auth01400102:
    frgn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrgnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_spot_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgSpotRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    xchg_fwd_pt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgFwdPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class NameAndLocation1Auth01400102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SectorAndLocation1Auth01400102:
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth01400102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CounterpartyIdentification3ChoiceAuth01400102:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sctr_and_lctn: Optional[SectorAndLocation1Auth01400102] = field(
        default=None,
        metadata={
            "name": "SctrAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )
    nm_and_lctn: Optional[NameAndLocation1Auth01400102] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )


@dataclass
class MoneyMarketReportHeader1Auth01400102:
    rptg_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    ref_prd: Optional[DateTimePeriod1Auth01400102] = field(
        default=None,
        metadata={
            "name": "RefPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth01400102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth01400102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeSwapTransaction3Auth01400102:
    rptd_tx_sts: Optional[TransactionOperationType1Code] = field(
        default=None,
        metadata={
            "name": "RptdTxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    nvtn_sts: Optional[NovationStatus1Code] = field(
        default=None,
        metadata={
            "name": "NvtnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )
    brnch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 105,
        },
    )
    rltd_prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdPrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    ctr_pty_prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyPrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    ctr_pty_id: Optional[CounterpartyIdentification3ChoiceAuth01400102] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    trad_dt: Optional[DateAndDateTimeChoiceAuth01400102] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    spot_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SpotValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    tx_tp: Optional[SecuritiesTransactionType15Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    tx_nmnl_amt: Optional[ActiveCurrencyAndAmountAuth01400102] = field(
        default=None,
        metadata={
            "name": "TxNmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    fx: Optional[ForeignExchange1Auth01400102] = field(
        default=None,
        metadata={
            "name": "FX",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth01400102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )


@dataclass
class ForeignExchangeSwap3ChoiceAuth01400102:
    data_set_actn: Optional[ReportPeriodActivity3Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )
    tx: list[ForeignExchangeSwapTransaction3Auth01400102] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )


@dataclass
class MoneyMarketForeignExchangeSwapsStatisticalReportV02Auth01400102:
    rpt_hdr: Optional[MoneyMarketReportHeader1Auth01400102] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    fxswps_rpt: Optional[ForeignExchangeSwap3ChoiceAuth01400102] = field(
        default=None,
        metadata={
            "name": "FXSwpsRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth01400102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02",
        },
    )


@dataclass
class Auth01400102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.014.001.02"

    mny_mkt_fxswps_sttstcl_rpt: Optional[
        MoneyMarketForeignExchangeSwapsStatisticalReportV02Auth01400102
    ] = field(
        default=None,
        metadata={
            "name": "MnyMktFXSwpsSttstclRpt",
            "type": "Element",
            "required": True,
        },
    )
