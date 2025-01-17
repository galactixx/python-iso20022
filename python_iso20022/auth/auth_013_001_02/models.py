from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_013_001_02.enums import (
    FinancialInstrumentProductType1Code,
)
from python_iso20022.auth.enums import (
    BrokeredDeal1Code,
    InterestRateType1Code,
    MoneyMarketTransactionType1Code,
    NovationStatus1Code,
    ReportPeriodActivity3Code,
    TransactionOperationType1Code,
)
from python_iso20022.enums import OptionType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02"


@dataclass
class ActiveCurrencyAndAmountAuth01300102:
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
class DateAndDateTimeChoiceAuth01300102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )


@dataclass
class DateTimePeriod1Auth01300102:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )


@dataclass
class FloatingRateNote2Auth01300102:
    ref_rate_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefRateIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    bsis_pt_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class NameAndLocation1Auth01300102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OptionDateOrPeriod1ChoiceAuth01300102:
    earlst_exrc_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstExrcDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )
    ntce_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NtcePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class SectorAndLocation1Auth01300102:
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth01300102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CounterpartyIdentification3ChoiceAuth01300102:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sctr_and_lctn: Optional[SectorAndLocation1Auth01300102] = field(
        default=None,
        metadata={
            "name": "SctrAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )
    nm_and_lctn: Optional[NameAndLocation1Auth01300102] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )


@dataclass
class MoneyMarketReportHeader1Auth01300102:
    rptg_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    ref_prd: Optional[DateTimePeriod1Auth01300102] = field(
        default=None,
        metadata={
            "name": "RefPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )


@dataclass
class Option12Auth01300102:
    tp: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    dt_or_prd: Optional[OptionDateOrPeriod1ChoiceAuth01300102] = field(
        default=None,
        metadata={
            "name": "DtOrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth01300102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth01300102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )


@dataclass
class UnsecuredMarketTransaction4Auth01300102:
    rptd_tx_sts: Optional[TransactionOperationType1Code] = field(
        default=None,
        metadata={
            "name": "RptdTxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    nvtn_sts: Optional[NovationStatus1Code] = field(
        default=None,
        metadata={
            "name": "NvtnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )
    brnch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    ctr_pty_prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyPrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    ctr_pty_id: Optional[CounterpartyIdentification3ChoiceAuth01300102] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    trad_dt: Optional[DateAndDateTimeChoiceAuth01300102] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    tx_tp: Optional[MoneyMarketTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    instrm_tp: Optional[FinancialInstrumentProductType1Code] = field(
        default=None,
        metadata={
            "name": "InstrmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    tx_nmnl_amt: Optional[ActiveCurrencyAndAmountAuth01300102] = field(
        default=None,
        metadata={
            "name": "TxNmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    deal_pric: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DealPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rate_tp: Optional[InterestRateType1Code] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    deal_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DealRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg_rate_note: Optional[FloatingRateNote2Auth01300102] = field(
        default=None,
        metadata={
            "name": "FltgRateNote",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )
    brkrd_deal: Optional[BrokeredDeal1Code] = field(
        default=None,
        metadata={
            "name": "BrkrdDeal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )
    call_put_optn: list[Option12Auth01300102] = field(
        default_factory=list,
        metadata={
            "name": "CallPutOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "max_occurs": 2,
        },
    )
    splmtry_data: list[SupplementaryData1Auth01300102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )


@dataclass
class UnsecuredMarketReport4ChoiceAuth01300102:
    data_set_actn: Optional[ReportPeriodActivity3Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )
    tx: list[UnsecuredMarketTransaction4Auth01300102] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )


@dataclass
class MoneyMarketUnsecuredMarketStatisticalReportV02Auth01300102:
    rpt_hdr: Optional[MoneyMarketReportHeader1Auth01300102] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    uscrd_mkt_rpt: Optional[UnsecuredMarketReport4ChoiceAuth01300102] = field(
        default=None,
        metadata={
            "name": "UscrdMktRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth01300102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02",
        },
    )


@dataclass
class Auth01300102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.013.001.02"

    mny_mkt_uscrd_mkt_sttstcl_rpt: Optional[
        MoneyMarketUnsecuredMarketStatisticalReportV02Auth01300102
    ] = field(
        default=None,
        metadata={
            "name": "MnyMktUscrdMktSttstclRpt",
            "type": "Element",
            "required": True,
        },
    )
