from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    AnyMic1Code,
    CollateralType6Code,
    ExposureType10Code,
    FinancialPartySectorType2Code,
    Frequency14Code,
    NotReported1Code,
    Operation3Code,
    PartyNatureType1Code,
    TransactionOperationType6Code,
    WeekDay3Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02"


@dataclass
class DatePeriod1Auth09400102(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )


@dataclass
class DateTimePeriod1Auth09400102(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )


@dataclass
class GenericIdentification1Auth09400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth09400102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CorporateSectorCriteria5Auth09400102(ISO20022MessageElement):
    fisctr: list[FinancialPartySectorType2Code] = field(
        default_factory=list,
        metadata={
            "name": "FISctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    nfisctr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NFISctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-U]{1,1}",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class DateOrBlankQuery2ChoiceAuth09400102(ISO20022MessageElement):
    rg: Optional[DatePeriod1Auth09400102] = field(
        default=None,
        metadata={
            "name": "Rg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class PostalAddress1Auth09400102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecuritiesTradeVenueCriteria1ChoiceAuth09400102(ISO20022MessageElement):
    mic: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    any_mic: Optional[AnyMic1Code] = field(
        default=None,
        metadata={
            "name": "AnyMIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class SupplementaryData1Auth09400102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth09400102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )


@dataclass
class TradePartyIdentificationQuery8Auth09400102(ISO20022MessageElement):
    lei: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    any_bic: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradePartyIdentificationQuery9Auth09400102(ISO20022MessageElement):
    lei: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    ctry_cd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    any_bic: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clnt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradeQueryExecutionFrequency3Auth09400102(ISO20022MessageElement):
    frqcy_tp: Optional[Frequency14Code] = field(
        default=None,
        metadata={
            "name": "FrqcyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    dlvry_day: list[WeekDay3Code] = field(
        default_factory=list,
        metadata={
            "name": "DlvryDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    day_of_mnth: list[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "DayOfMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "min_inclusive": Decimal("1"),
            "max_inclusive": Decimal("31"),
        },
    )


@dataclass
class TradeTypeQueryCriteria2Auth09400102(ISO20022MessageElement):
    oprtr: Optional[Operation3Code] = field(
        default=None,
        metadata={
            "name": "Oprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    scties_fincg_tx_tp: list[ExposureType10Code] = field(
        default_factory=list,
        metadata={
            "name": "SctiesFincgTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    coll_cmpnt_tp: list[CollateralType6Code] = field(
        default_factory=list,
        metadata={
            "name": "CollCmpntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class NameAndAddress5Auth09400102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Auth09400102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradeAdditionalQueryCriteria7Auth09400102(ISO20022MessageElement):
    actn_tp: list[TransactionOperationType6Code] = field(
        default_factory=list,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    exctn_vn: Optional[SecuritiesTradeVenueCriteria1ChoiceAuth09400102] = field(
        default=None,
        metadata={
            "name": "ExctnVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    ntr_of_ctr_pty: list[PartyNatureType1Code] = field(
        default_factory=list,
        metadata={
            "name": "NtrOfCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    corp_sctr: list[CorporateSectorCriteria5Auth09400102] = field(
        default_factory=list,
        metadata={
            "name": "CorpSctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradeDateTimeQueryCriteria2Auth09400102(ISO20022MessageElement):
    rptg_dt_tm: Optional[DateTimePeriod1Auth09400102] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    exctn_dt_tm: Optional[DateTimePeriod1Auth09400102] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    mtrty_dt: Optional[DateOrBlankQuery2ChoiceAuth09400102] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    termntn_dt: Optional[DateOrBlankQuery2ChoiceAuth09400102] = field(
        default=None,
        metadata={
            "name": "TermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradePartyQueryCriteria5Auth09400102(ISO20022MessageElement):
    oprtr: Optional[Operation3Code] = field(
        default=None,
        metadata={
            "name": "Oprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    rptg_ctr_pty: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    rptg_ctr_pty_brnch: Optional[TradePartyIdentificationQuery9Auth09400102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPtyBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    othr_ctr_pty: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    othr_ctr_pty_brnch: Optional[TradePartyIdentificationQuery9Auth09400102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPtyBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    bnfcry: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    submitg_agt: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "SubmitgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    brkr: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    ccp: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    agt_lndr: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "AgtLndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    trpty_agt: Optional[TradePartyIdentificationQuery8Auth09400102] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradeRecurrentQuery5Auth09400102(ISO20022MessageElement):
    qry_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 1000,
        },
    )
    frqcy: Optional[TradeQueryExecutionFrequency3Auth09400102] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    vld_until: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldUntil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentification121ChoiceAuth09400102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Auth09400102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    prtry_id: Optional[GenericIdentification1Auth09400102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradeQueryCriteria10Auth09400102(ISO20022MessageElement):
    trad_life_cycl_hstry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TradLifeCyclHstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    outsdng_trad_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OutsdngTradInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    trad_pty_crit: Optional[TradePartyQueryCriteria5Auth09400102] = field(
        default=None,
        metadata={
            "name": "TradPtyCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    trad_tp_crit: Optional[TradeTypeQueryCriteria2Auth09400102] = field(
        default=None,
        metadata={
            "name": "TradTpCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    tm_crit: Optional[TradeDateTimeQueryCriteria2Auth09400102] = field(
        default=None,
        metadata={
            "name": "TmCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    othr_crit: Optional[TradeAdditionalQueryCriteria7Auth09400102] = field(
        default=None,
        metadata={
            "name": "OthrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class TradeReportQuery13ChoiceAuth09400102(ISO20022MessageElement):
    ad_hoc_qry: Optional[TradeQueryCriteria10Auth09400102] = field(
        default=None,
        metadata={
            "name": "AdHocQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )
    rcrnt_qry: Optional[TradeRecurrentQuery5Auth09400102] = field(
        default=None,
        metadata={
            "name": "RcrntQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class SecuritiesFinancingReportingTransactionQueryV02Auth09400102(
    ISO20022MessageElement
):
    rqstng_authrty: Optional[PartyIdentification121ChoiceAuth09400102] = field(
        default=None,
        metadata={
            "name": "RqstngAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    trad_qry_data: Optional[TradeReportQuery13ChoiceAuth09400102] = field(
        default=None,
        metadata={
            "name": "TradQryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth09400102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02",
        },
    )


@dataclass
class Auth09400102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.094.001.02"

    scties_fincg_rptg_tx_qry: Optional[
        SecuritiesFinancingReportingTransactionQueryV02Auth09400102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgTxQry",
            "type": "Element",
            "required": True,
        },
    )
