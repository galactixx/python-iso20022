from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.camt.camt_062_001_03.enums import Entry2Code
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03"


@dataclass
class ActiveCurrencyAndAmountCamt06200103:
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
class AgreedRate2Camt06200103:
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt06200103:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification44Camt06200103:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt06200103:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BalanceStatus2Camt06200103:
    bal: Optional[ActiveCurrencyAndAmountCamt06200103] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )


@dataclass
class CurrencyFactors1Camt06200103:
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    shrt_pos_lmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ShrtPosLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    min_pay_in_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinPayInAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    voltly_mrgn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VoltlyMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rate: Optional[AgreedRate2Camt06200103] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )


@dataclass
class PartyIdentification59Camt06200103:
    pty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 34,
        },
    )
    any_bic: Optional[PartyIdentification44Camt06200103] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 34,
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 105,
        },
    )
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt06200103] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PayInScheduleItems1Camt06200103:
    amt: Optional[ActiveCurrencyAndAmountCamt06200103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )
    ddln: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Ddln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Camt06200103:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ReportData4Camt06200103:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )
    dt_and_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtAndTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )
    tp: Optional[Entry2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )
    schdl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchdlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    sttlm_ssn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmSsnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )


@dataclass
class SupplementaryData1Camt06200103:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt06200103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )


@dataclass
class NameAndAddress8Camt06200103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Camt06200103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PayInFactors1Camt06200103:
    aggt_shrt_pos_lmt: Optional[ActiveCurrencyAndAmountCamt06200103] = field(
        default=None,
        metadata={
            "name": "AggtShrtPosLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )
    ccy_fctrs: list[CurrencyFactors1Camt06200103] = field(
        default_factory=list,
        metadata={
            "name": "CcyFctrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class PartyIdentification73ChoiceCamt06200103:
    nm_and_adr: Optional[NameAndAddress8Camt06200103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    any_bic: Optional[PartyIdentification44Camt06200103] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    pty_id: Optional[PartyIdentification59Camt06200103] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )


@dataclass
class PayInScheduleV03Camt06200103:
    pty_id: Optional[PartyIdentification73ChoiceCamt06200103] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )
    rpt_data: Optional[ReportData4Camt06200103] = field(
        default=None,
        metadata={
            "name": "RptData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
            "required": True,
        },
    )
    pay_in_schdl_lng_bal: list[BalanceStatus2Camt06200103] = field(
        default_factory=list,
        metadata={
            "name": "PayInSchdlLngBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    pay_in_schdl_itm: list[PayInScheduleItems1Camt06200103] = field(
        default_factory=list,
        metadata={
            "name": "PayInSchdlItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    pay_in_fctrs: Optional[PayInFactors1Camt06200103] = field(
        default=None,
        metadata={
            "name": "PayInFctrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Camt06200103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03",
        },
    )


@dataclass
class Camt06200103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.062.001.03"

    pay_in_schdl: Optional[PayInScheduleV03Camt06200103] = field(
        default=None,
        metadata={
            "name": "PayInSchdl",
            "type": "Element",
            "required": True,
        },
    )
