from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_012_001_02.enums import (
    CollateralPool1Code,
    SpecialCollateral2Code,
)
from python_iso20022.auth.enums import (
    BrokeredDeal1Code,
    InterestRateType1Code,
    MoneyMarketTransactionType1Code,
    NovationStatus1Code,
    ReportPeriodActivity3Code,
    TransactionOperationType1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02"


@dataclass
class ActiveCurrencyAndAmountAuth01200102(ISO20022MessageElement):
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
class DateAndDateTimeChoiceAuth01200102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class DateTimePeriod1Auth01200102(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )


@dataclass
class FloatingRateNote2Auth01200102(ISO20022MessageElement):
    ref_rate_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefRateIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    bsis_pt_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class NameAndLocation1Auth01200102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SectorAndLocation1Auth01200102(ISO20022MessageElement):
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth01200102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CollateralValuation6Auth01200102(ISO20022MessageElement):
    nmnl_amt: Optional[ActiveCurrencyAndAmountAuth01200102] = field(
        default=None,
        metadata={
            "name": "NmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class CollateralValuation7Auth01200102(ISO20022MessageElement):
    pool_sts: Optional[CollateralPool1Code] = field(
        default=None,
        metadata={
            "name": "PoolSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
            "pattern": r"[A-Z]{6,6}",
        },
    )
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    nmnl_amt: Optional[ActiveCurrencyAndAmountAuth01200102] = field(
        default=None,
        metadata={
            "name": "NmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class CounterpartyIdentification3ChoiceAuth01200102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sctr_and_lctn: Optional[SectorAndLocation1Auth01200102] = field(
        default=None,
        metadata={
            "name": "SctrAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    nm_and_lctn: Optional[NameAndLocation1Auth01200102] = field(
        default=None,
        metadata={
            "name": "NmAndLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class MoneyMarketReportHeader1Auth01200102(ISO20022MessageElement):
    rptg_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    ref_prd: Optional[DateTimePeriod1Auth01200102] = field(
        default=None,
        metadata={
            "name": "RefPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth01200102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth01200102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )


@dataclass
class SecuredCollateral2ChoiceAuth01200102(ISO20022MessageElement):
    sngl_coll: Optional[CollateralValuation6Auth01200102] = field(
        default=None,
        metadata={
            "name": "SnglColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    mltpl_coll: list[CollateralValuation6Auth01200102] = field(
        default_factory=list,
        metadata={
            "name": "MltplColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    pool_coll: Optional[CollateralValuation6Auth01200102] = field(
        default=None,
        metadata={
            "name": "PoolColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    othr_coll: list[CollateralValuation7Auth01200102] = field(
        default_factory=list,
        metadata={
            "name": "OthrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class Collateral18Auth01200102(ISO20022MessageElement):
    valtn: Optional[SecuredCollateral2ChoiceAuth01200102] = field(
        default=None,
        metadata={
            "name": "Valtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    spcl_coll_ind: Optional[SpecialCollateral2Code] = field(
        default=None,
        metadata={
            "name": "SpclCollInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class SecuredMarketTransaction4Auth01200102(ISO20022MessageElement):
    rptd_tx_sts: Optional[TransactionOperationType1Code] = field(
        default=None,
        metadata={
            "name": "RptdTxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    nvtn_sts: Optional[NovationStatus1Code] = field(
        default=None,
        metadata={
            "name": "NvtnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    brnch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    ctr_pty_prtry_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyPrtryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    ctr_pty_id: Optional[CounterpartyIdentification3ChoiceAuth01200102] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    trpty_agt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    trad_dt: Optional[DateAndDateTimeChoiceAuth01200102] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    tx_tp: Optional[MoneyMarketTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    tx_nmnl_amt: Optional[ActiveCurrencyAndAmountAuth01200102] = field(
        default=None,
        metadata={
            "name": "TxNmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    rate_tp: Optional[InterestRateType1Code] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    deal_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DealRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg_rate_rp_agrmt: Optional[FloatingRateNote2Auth01200102] = field(
        default=None,
        metadata={
            "name": "FltgRateRpAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    brkrd_deal: Optional[BrokeredDeal1Code] = field(
        default=None,
        metadata={
            "name": "BrkrdDeal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    coll: Optional[Collateral18Auth01200102] = field(
        default=None,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth01200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class SecuredMarketReport4ChoiceAuth01200102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity3Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )
    tx: list[SecuredMarketTransaction4Auth01200102] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class MoneyMarketSecuredMarketStatisticalReportV02Auth01200102(ISO20022MessageElement):
    rpt_hdr: Optional[MoneyMarketReportHeader1Auth01200102] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    scrd_mkt_rpt: Optional[SecuredMarketReport4ChoiceAuth01200102] = field(
        default=None,
        metadata={
            "name": "ScrdMktRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth01200102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02",
        },
    )


@dataclass
class Auth01200102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.012.001.02"

    mny_mkt_scrd_mkt_sttstcl_rpt: Optional[
        MoneyMarketSecuredMarketStatisticalReportV02Auth01200102
    ] = field(
        default=None,
        metadata={
            "name": "MnyMktScrdMktSttstclRpt",
            "type": "Element",
            "required": True,
        },
    )
