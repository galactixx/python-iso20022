from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import (
    ReportPeriodActivity1Code,
    TransactionOperationType4Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01"


@dataclass
class Contact9Auth10000101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DatePeriod2Auth10000101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class IdentificationSource3ChoiceAuth10000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementDataRate2Auth10000101(ISO20022MessageElement):
    vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SettlementDataVolume2Auth10000101(ISO20022MessageElement):
    vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 2,
        },
    )


@dataclass
class SettlementFailureReason2Auth10000101(ISO20022MessageElement):
    main_rsns: Optional[str] = field(
        default=None,
        metadata={
            "name": "MainRsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )
    effcncy_imprvmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffcncyImprvmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth10000101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class OtherIdentification1Auth10000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesSettlementSystemIdentification2Auth10000101(ISO20022MessageElement):
    sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sys_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_of_jursdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    csdlgl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CSDLglNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    rspnsbl_pty: list[Contact9Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "RspnsblPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )


@dataclass
class SettlementFailureReason3Auth10000101(ISO20022MessageElement):
    avrg_drtn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AvrgDrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9.9"),
            "total_digits": 2,
            "fraction_digits": 1,
        },
    )
    desc: list[SettlementFailureReason2Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class SettlementTotalData1Auth10000101(ISO20022MessageElement):
    sttld: Optional[SettlementDataVolume2Auth10000101] = field(
        default=None,
        metadata={
            "name": "Sttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    faild: Optional[SettlementDataVolume2Auth10000101] = field(
        default=None,
        metadata={
            "name": "Faild",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    ttl: Optional[SettlementDataVolume2Auth10000101] = field(
        default=None,
        metadata={
            "name": "Ttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    faild_rate: Optional[SettlementDataRate2Auth10000101] = field(
        default=None,
        metadata={
            "name": "FaildRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth10000101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth10000101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SecurityIdentification19Auth10000101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementFailsCurrency2Auth10000101(ISO20022MessageElement):
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    data: Optional[SettlementTotalData1Auth10000101] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsParticipant1Auth10000101(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    rank: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    aggt: Optional[SettlementTotalData1Auth10000101] = field(
        default=None,
        metadata={
            "name": "Aggt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsReportHeader2Auth10000101(ISO20022MessageElement):
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[DatePeriod2Auth10000101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    rpt_sts: Optional[TransactionOperationType4Code] = field(
        default=None,
        metadata={
            "name": "RptSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    scties_sttlm_sys: Optional[
        SecuritiesSettlementSystemIdentification2Auth10000101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementTotalData1ChoiceAuth10000101(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    data: Optional[SettlementTotalData1Auth10000101] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )


@dataclass
class SettlementDailyFailureReason3Auth10000101(ISO20022MessageElement):
    faild_scties: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "FaildScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    faild_csh: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "FaildCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsInstrument2Auth10000101(ISO20022MessageElement):
    eqty: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Eqty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    svrgn_debt: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "SvrgnDebt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    bd: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Bd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    othr_trfbl_scties: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "OthrTrfblScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    xchg_tradd_fnds: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "XchgTraddFnds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    cllctv_invstmt_udrtkgs: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "CllctvInvstmtUdrtkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    mny_mkt_instrm: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "MnyMktInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    emssn_allwnc: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "EmssnAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    othr: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsParticipantRange1Auth10000101(ISO20022MessageElement):
    hghst_in_vol: list[SettlementFailsParticipant1Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "HghstInVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_occurs": 1,
        },
    )
    hghst_in_val: list[SettlementFailsParticipant1Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "HghstInVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class SettlementFailsSecurities1Auth10000101(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Auth10000101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    rank: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )


@dataclass
class SettlementFailsTransactionType2Auth10000101(ISO20022MessageElement):
    scties_buy_or_sell: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "SctiesBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    coll_mgmt_opr: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "CollMgmtOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    scties_lndg_or_brrwg: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "SctiesLndgOrBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    rp_agrmt: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "RpAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    othr: Optional[SettlementTotalData1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementDailyFailureReason1ChoiceAuth10000101(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    data: Optional[SettlementDailyFailureReason3Auth10000101] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )


@dataclass
class SettlementFailsSecuritiesRange1Auth10000101(ISO20022MessageElement):
    hghst_in_vol: list[SettlementFailsSecurities1Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "HghstInVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_occurs": 1,
        },
    )
    hghst_in_val: list[SettlementFailsSecurities1Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "HghstInVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class SettlementFailsDailyInstructionType3Auth10000101(ISO20022MessageElement):
    dlvry_vrss_pmt: Optional[SettlementDailyFailureReason1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "DlvryVrssPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    dlvry_wth_pmt: Optional[SettlementDailyFailureReason1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "DlvryWthPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    pmt_free_of_dlvry: Optional[SettlementDailyFailureReason1ChoiceAuth10000101] = (
        field(
            default=None,
            metadata={
                "name": "PmtFreeOfDlvry",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
                "required": True,
            },
        )
    )
    free_of_pmt: Optional[SettlementDailyFailureReason1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "FreeOfPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsData3Auth10000101(ISO20022MessageElement):
    ttl: Optional[SettlementTotalData1Auth10000101] = field(
        default=None,
        metadata={
            "name": "Ttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    ptcpt_in_fail: Optional[SettlementFailsParticipantRange1Auth10000101] = field(
        default=None,
        metadata={
            "name": "PtcptInFail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    fls_per_ccy: list[SettlementFailsCurrency2Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "FlsPerCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    fls_per_fin_instrm_tp: Optional[SettlementFailsInstrument2Auth10000101] = field(
        default=None,
        metadata={
            "name": "FlsPerFinInstrmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    scties_in_fail: Optional[SettlementFailsSecuritiesRange1Auth10000101] = field(
        default=None,
        metadata={
            "name": "SctiesInFail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    fls_per_tx_tp: Optional[SettlementFailsTransactionType2Auth10000101] = field(
        default=None,
        metadata={
            "name": "FlsPerTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    ttl_sttlm_pnlties: Optional[SettlementDataVolume2Auth10000101] = field(
        default=None,
        metadata={
            "name": "TtlSttlmPnlties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    failr_rsn: Optional[SettlementFailureReason3Auth10000101] = field(
        default=None,
        metadata={
            "name": "FailrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsDailyInstructionType1ChoiceAuth10000101(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    data: Optional[SettlementFailsDailyInstructionType3Auth10000101] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )


@dataclass
class SettlementFailsDailyCsd3Auth10000101(ISO20022MessageElement):
    class Meta:
        name = "SettlementFailsDailyCSD3"

    intra_csd: Optional[SettlementFailsDailyInstructionType1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "IntraCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    cross_csd: Optional[SettlementFailsDailyInstructionType1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "CrossCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsDailyCsd1ChoiceAuth10000101(ISO20022MessageElement):
    class Meta:
        name = "SettlementFailsDailyCSD1Choice"

    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    data: Optional[SettlementFailsDailyCsd3Auth10000101] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )


@dataclass
class SettlementFailsDailyTransactionType3Auth10000101(ISO20022MessageElement):
    scties_buy_or_sell: Optional[SettlementFailsDailyCsd1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "SctiesBuyOrSell",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    coll_mgmt_opr: Optional[SettlementFailsDailyCsd1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "CollMgmtOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    scties_lndg_or_brrwg: Optional[SettlementFailsDailyCsd1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "SctiesLndgOrBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    rp_agrmt: Optional[SettlementFailsDailyCsd1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "RpAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    othr: Optional[SettlementFailsDailyCsd1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsDailyTransactionType1ChoiceAuth10000101(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )
    data: Optional[SettlementFailsDailyTransactionType3Auth10000101] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )


@dataclass
class SettlementFailsDailyInstrument3Auth10000101(ISO20022MessageElement):
    eqty: Optional[SettlementFailsDailyTransactionType1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Eqty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    svrgn_debt: Optional[SettlementFailsDailyTransactionType1ChoiceAuth10000101] = (
        field(
            default=None,
            metadata={
                "name": "SvrgnDebt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
                "required": True,
            },
        )
    )
    bd: Optional[SettlementFailsDailyTransactionType1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Bd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    othr_trfbl_scties: Optional[
        SettlementFailsDailyTransactionType1ChoiceAuth10000101
    ] = field(
        default=None,
        metadata={
            "name": "OthrTrfblScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    xchg_tradd_fnds: Optional[
        SettlementFailsDailyTransactionType1ChoiceAuth10000101
    ] = field(
        default=None,
        metadata={
            "name": "XchgTraddFnds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    cllctv_invstmt_udrtkgs: Optional[
        SettlementFailsDailyTransactionType1ChoiceAuth10000101
    ] = field(
        default=None,
        metadata={
            "name": "CllctvInvstmtUdrtkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    mny_mkt_instrm: Optional[SettlementFailsDailyTransactionType1ChoiceAuth10000101] = (
        field(
            default=None,
            metadata={
                "name": "MnyMktInstrm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
                "required": True,
            },
        )
    )
    emssn_allwnc: Optional[SettlementFailsDailyTransactionType1ChoiceAuth10000101] = (
        field(
            default=None,
            metadata={
                "name": "EmssnAllwnc",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
                "required": True,
            },
        )
    )
    othr: Optional[SettlementFailsDailyTransactionType1ChoiceAuth10000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsDailyData3Auth10000101(ISO20022MessageElement):
    rptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    daly_rcrd: Optional[SettlementFailsDailyInstrument3Auth10000101] = field(
        default=None,
        metadata={
            "name": "DalyRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsMonthlyReportV01Auth10000101(ISO20022MessageElement):
    rpt_hdr: Optional[SettlementFailsReportHeader2Auth10000101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    mnthly_aggt: Optional[SettlementFailsData3Auth10000101] = field(
        default=None,
        metadata={
            "name": "MnthlyAggt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "required": True,
        },
    )
    daly_data: list[SettlementFailsDailyData3Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "DalyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth10000101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01",
        },
    )


@dataclass
class Auth10000101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.100.001.01"

    sttlm_fls_mnthly_rpt: Optional[SettlementFailsMonthlyReportV01Auth10000101] = field(
        default=None,
        metadata={
            "name": "SttlmFlsMnthlyRpt",
            "type": "Element",
            "required": True,
        },
    )
