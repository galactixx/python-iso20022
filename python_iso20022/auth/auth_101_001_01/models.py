from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.enums import TransactionOperationType4Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01"


@dataclass
class Contact9Auth10100101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DatePeriod2Auth10100101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementDataRate1ChoiceAuth10100101:
    nb_of_instrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    val_of_instrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValOfInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SettlementDataRate2Auth10100101:
    vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SettlementDataVolume2Auth10100101:
    vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 2,
        },
    )


@dataclass
class SettlementFailureReason2Auth10100101:
    main_rsns: Optional[str] = field(
        default=None,
        metadata={
            "name": "MainRsns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth10100101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SecuritiesSettlementSystemIdentification2Auth10100101:
    sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_of_jursdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    csdlgl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CSDLglNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    rspnsbl_pty: list[Contact9Auth10100101] = field(
        default_factory=list,
        metadata={
            "name": "RspnsblPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
        },
    )


@dataclass
class SettlementFailsJustification1Auth10100101:
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 2,
        },
    )
    rate: Optional[SettlementDataRate1ChoiceAuth10100101] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailureReason3Auth10100101:
    avrg_drtn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AvrgDrtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9.9"),
            "total_digits": 2,
            "fraction_digits": 1,
        },
    )
    desc: list[SettlementFailureReason2Auth10100101] = field(
        default_factory=list,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class SettlementTotalData1Auth10100101:
    sttld: Optional[SettlementDataVolume2Auth10100101] = field(
        default=None,
        metadata={
            "name": "Sttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    faild: Optional[SettlementDataVolume2Auth10100101] = field(
        default=None,
        metadata={
            "name": "Faild",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    ttl: Optional[SettlementDataVolume2Auth10100101] = field(
        default=None,
        metadata={
            "name": "Ttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    faild_rate: Optional[SettlementDataRate2Auth10100101] = field(
        default=None,
        metadata={
            "name": "FaildRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth10100101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth10100101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsDerogation1Auth10100101:
    elgblty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ElgbltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    justfn: Optional[SettlementFailsJustification1Auth10100101] = field(
        default=None,
        metadata={
            "name": "Justfn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
        },
    )


@dataclass
class SettlementFailsReportHeader2Auth10100101:
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    rptg_prd: Optional[DatePeriod2Auth10100101] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    rpt_sts: Optional[TransactionOperationType4Code] = field(
        default=None,
        metadata={
            "name": "RptSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    scties_sttlm_sys: Optional[
        SecuritiesSettlementSystemIdentification2Auth10100101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsData4Auth10100101:
    ttl: Optional[SettlementTotalData1Auth10100101] = field(
        default=None,
        metadata={
            "name": "Ttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    failr_rsn: Optional[SettlementFailureReason3Auth10100101] = field(
        default=None,
        metadata={
            "name": "FailrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    elgbl_for_drgtn: Optional[SettlementFailsDerogation1Auth10100101] = field(
        default=None,
        metadata={
            "name": "ElgblForDrgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementFailsAnnualReportV01Auth10100101:
    rpt_hdr: Optional[SettlementFailsReportHeader2Auth10100101] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    anl_aggt: Optional[SettlementFailsData4Auth10100101] = field(
        default=None,
        metadata={
            "name": "AnlAggt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth10100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01",
        },
    )


@dataclass
class Auth10100101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.101.001.01"

    sttlm_fls_anl_rpt: Optional[SettlementFailsAnnualReportV01Auth10100101] = field(
        default=None,
        metadata={
            "name": "SttlmFlsAnlRpt",
            "type": "Element",
            "required": True,
        },
    )
