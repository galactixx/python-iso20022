from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, AllocationIndicator1Code
from python_iso20022.fxtr.enums import (
    CollateralisationIndicator1Code,
    CorporateSectorIdentifier1Code,
    FxamountType1Code,
    SideIndicator1Code,
    StatusSubType2Code,
    TradeStatus6Code,
    TradeStatus7Code,
    UnderlyingProductIdentifier1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06"


@dataclass
class ActiveCurrencyAndAmountFxtr03000106(ISO20022MessageElement):
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
class ClearingSystemIdentification2ChoiceFxtr03000106(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceFxtr03000106(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )


@dataclass
class IdentificationSource3ChoiceFxtr03000106(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Fxtr03000106(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )


@dataclass
class PartyIdentification265Fxtr03000106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Fxtr03000106(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class UniqueTransactionIdentifier3Fxtr03000106(ISO20022MessageElement):
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prr_unq_tx_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PrrUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )


@dataclass
class AmountOrRate4ChoiceFxtr03000106(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountFxtr03000106] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ClearingBrokerIdentification1Fxtr03000106(ISO20022MessageElement):
    sd_ind: Optional[SideIndicator1Code] = field(
        default=None,
        metadata={
            "name": "SdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )
    clr_brkr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrBrkrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FxamountType1ChoiceFxtr03000106(ISO20022MessageElement):
    class Meta:
        name = "FXAmountType1Choice"

    cd: Optional[FxamountType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherIdentification1Fxtr03000106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )


@dataclass
class PartyIdentification266Fxtr03000106(ISO20022MessageElement):
    pty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 34,
        },
    )
    any_bic: Optional[PartyIdentification265Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 34,
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 105,
        },
    )
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PostalAddress1Fxtr03000106(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProductIdentifier3ChoiceFxtr03000106(ISO20022MessageElement):
    undrlyg_pdct_idr: Optional[UnderlyingProductIdentifier1Code] = field(
        default=None,
        metadata={
            "name": "UndrlygPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    unq_pdct_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 12,
        },
    )


@dataclass
class Status27ChoiceFxtr03000106(ISO20022MessageElement):
    cd: Optional[TradeStatus6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Status28ChoiceFxtr03000106(ISO20022MessageElement):
    cd: Optional[TradeStatus7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Fxtr03000106(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )


@dataclass
class FxcommissionOrFee1Fxtr03000106(ISO20022MessageElement):
    class Meta:
        name = "FXCommissionOrFee1"

    tp: Optional[FxamountType1ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )
    amt_or_rate: Optional[AmountOrRate4ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "AmtOrRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )


@dataclass
class NameAndAddress8Fxtr03000106(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecurityIdentification19Fxtr03000106(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class StatusAndSubStatus2Fxtr03000106(ISO20022MessageElement):
    sts_cd: Optional[Status27ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "StsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )
    sub_sts_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubStsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )


@dataclass
class PartyIdentification242ChoiceFxtr03000106(ISO20022MessageElement):
    nm_and_adr: Optional[NameAndAddress8Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    any_bic: Optional[PartyIdentification265Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    pty_id: Optional[PartyIdentification266Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )


@dataclass
class TradeData45Fxtr03000106(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sts_orgtr: Optional[str] = field(
        default=None,
        metadata={
            "name": "StsOrgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cur_sts: Optional[StatusAndSubStatus2Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "CurSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )
    cur_sts_sub_tp: Optional[StatusSubType2Code] = field(
        default=None,
        metadata={
            "name": "CurStsSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    cur_sts_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CurStsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )
    prvs_sts: Optional[Status28ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "PrvsSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    prvs_sts_sub_tp: Optional[StatusSubType2Code] = field(
        default=None,
        metadata={
            "name": "PrvsStsSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sttlm_ssn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmSsnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )


@dataclass
class CounterpartySideTransactionReporting3Fxtr03000106(ISO20022MessageElement):
    rptg_jursdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_pty: Optional[PartyIdentification242ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "RptgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    ctr_pty_sd_unq_tx_idr: list[UniqueTransactionIdentifier3Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "CtrPtySdUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )


@dataclass
class TradingSideTransactionReporting3Fxtr03000106(ISO20022MessageElement):
    rptg_jursdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_pty: Optional[PartyIdentification242ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "RptgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    tradg_sd_unq_tx_idr: list[UniqueTransactionIdentifier3Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "TradgSdUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )


@dataclass
class RegulatoryReporting8Fxtr03000106(ISO20022MessageElement):
    tradg_sd_tx_rptg: list[TradingSideTransactionReporting3Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "TradgSdTxRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    ctr_pty_sd_tx_rptg: list[CounterpartySideTransactionReporting3Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "CtrPtySdTxRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    cntrl_ctr_pty_clr_hs: Optional[PartyIdentification242ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "CntrlCtrPtyClrHs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    clr_brkr: Optional[PartyIdentification242ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "ClrBrkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    clr_xcptn_pty: Optional[PartyIdentification242ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "ClrXcptnPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    clr_brkr_id: Optional[ClearingBrokerIdentification1Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "ClrBrkrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    clr_thrshld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    clrd_pdct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrdPdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_idr: Optional[ProductIdentifier3ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "PdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    allcn_ind: Optional[AllocationIndicator1Code] = field(
        default=None,
        metadata={
            "name": "AllcnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    collstn_ind: Optional[CollateralisationIndicator1Code] = field(
        default=None,
        metadata={
            "name": "CollstnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    exctn_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExctnVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    exctn_tmstmp: Optional[DateAndDateTime2ChoiceFxtr03000106] = field(
        default=None,
        metadata={
            "name": "ExctnTmstmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    non_std_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonStdFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    lk_swp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkSwpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "length": 42,
        },
    )
    fin_ntr_of_the_ctr_pty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinNtrOfTheCtrPtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    coll_prtfl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollPrtflInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    coll_prtfl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 10,
        },
    )
    prtfl_cmprssn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtflCmprssnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    corp_sctr_ind: Optional[CorporateSectorIdentifier1Code] = field(
        default=None,
        metadata={
            "name": "CorpSctrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    trad_wth_non_eeactr_pty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TradWthNonEEACtrPtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    ntrgrp_trad_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtrgrpTradInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    comrcl_or_trsr_fincg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ComrclOrTrsrFincgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    conf_dt_and_tmstmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ConfDtAndTmstmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    clr_tmstmp: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ClrTmstmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    comssns_and_fees: list[FxcommissionOrFee1Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "ComssnsAndFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    addtl_rptg_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRptgInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class TradeData44Fxtr03000106(ISO20022MessageElement):
    orgtr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgtrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtchg_sys_unq_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtchgSysUnqRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtchg_sys_mtchg_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtchgSysMtchgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtchg_sys_mtchd_sd_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtchgSysMtchdSdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cur_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CurSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    new_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NewSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    cur_sts_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CurStsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sttlm_ssn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmSsnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    rgltry_rptg: Optional[RegulatoryReporting8Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "RgltryRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )


@dataclass
class TradeDataReport2Fxtr03000106(ISO20022MessageElement):
    lkd_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_data: list[TradeData44Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_occurs": 1,
        },
    )


@dataclass
class ForeignExchangeTradeBulkStatusNotificationV06Fxtr03000106(ISO20022MessageElement):
    sts_dtls: Optional[TradeData45Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "StsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "required": True,
        },
    )
    trad_data_rpt: list[TradeDataReport2Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "TradDataRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
            "min_occurs": 1,
        },
    )
    msg_pgntn: Optional[Pagination1Fxtr03000106] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr03000106] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06",
        },
    )


@dataclass
class Fxtr03000106(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06"

    fxtrad_blk_sts_ntfctn: Optional[
        ForeignExchangeTradeBulkStatusNotificationV06Fxtr03000106
    ] = field(
        default=None,
        metadata={
            "name": "FXTradBlkStsNtfctn",
            "type": "Element",
            "required": True,
        },
    )
