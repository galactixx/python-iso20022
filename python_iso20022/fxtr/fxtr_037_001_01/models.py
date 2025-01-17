from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    OptionParty1Code,
    OptionParty3Code,
    PartyType3Code,
    PartyType4Code,
    Side1Code,
)
from python_iso20022.fxtr.enums import (
    AccountInformationType1Code,
    ClearingMethod1Code,
    ConfirmationRequest1Code,
    IdentificationType1Code,
    IdentificationType2Code,
    PartyIdentificationType1Code,
    SettlementDateCode,
    TradeConfirmationStatus1Code,
    TradingMethodType1Code,
    TradingModeType1Code,
    UnderlyingProductIdentifier1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01"


@dataclass
class ActiveCurrencyAnd13DecimalAmountFxtr03700101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
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
class ActiveCurrencyAndAmountFxtr03700101:
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
class AgreedRate3Fxtr03700101:
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CurrencyAndAmountFxtr03700101:
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
class IdentificationSource1ChoiceFxtr03700101:
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Fxtr03700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentificationFxtr03700101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification44Fxtr03700101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Fxtr03700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Fxtr03700101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification26Fxtr03700101:
    prtry: Optional[SimpleIdentificationInformation4Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class AdditionalReferencesFxtr03700101:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentificationFxtr03700101] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )


@dataclass
class AlternateIdentification1Fxtr03700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceFxtr03700101] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class Confirmation1Fxtr03700101:
    conf_sts: Optional[TradeConfirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "ConfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    conf_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ConfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    trad_pty_conf_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TradPtyConfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    initg_pty_conf_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InitgPtyConfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    conf_tp: Optional[ConfirmationRequest1Code] = field(
        default=None,
        metadata={
            "name": "ConfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    req_id: Optional[MessageIdentification1Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    qry_start_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryStartNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[0-9]{1,35}",
        },
    )
    ttl_nb_of_rpts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRpts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[0-9]{1,35}",
        },
    )
    qry_pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryPgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[0-9]{1,35}",
        },
    )
    msg_nb_of_cur_pg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MsgNbOfCurPg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    list_ordr_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ListOrdrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    last_rpt_reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastRptReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification32Fxtr03700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    issr: Optional[PartyType4Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification78Fxtr03700101:
    pty_src: Optional[IdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "PtySrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    trad_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification90Fxtr03700101:
    id_tp: Optional[PartyIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress1Fxtr03700101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecurityIdentification18Fxtr03700101:
    scty_id_src: Optional[IdentificationType2Code] = field(
        default=None,
        metadata={
            "name": "SctyIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    scty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Fxtr03700101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class AccountIdentification30Fxtr03700101:
    acct_tp: Optional[AccountInformationType1Code] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    id: Optional[AccountIdentification26Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class Header23Fxtr03700101:
    frmt_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    initg_pty: Optional[GenericIdentification32Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification32Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    msg_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MsgSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class InstrumentLeg6Fxtr03700101:
    leg_sd: Optional[Side1Code] = field(
        default=None,
        metadata={
            "name": "LegSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_sttlm_tp: Optional[SettlementDateCode] = field(
        default=None,
        metadata={
            "name": "LegSttlmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_sttlm_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LegSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_last_pric: Optional[ActiveCurrencyAnd13DecimalAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "LegLastPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    leg_ordr_qty: Optional[CurrencyAndAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "LegOrdrQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_fwd_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LegFwdPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    leg_clctd_ctr_pty_ccy_last_qty: Optional[CurrencyAndAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "LegClctdCtrPtyCcyLastQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_rsk_amt: Optional[ActiveCurrencyAndAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "LegRskAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_valtn_rate: Optional[AgreedRate3Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "LegValtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LegValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    leg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    leg_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    leg_scty_id: Optional[SecurityIdentification18Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "LegSctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress8Fxtr03700101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecurityIdentification22ChoiceFxtr03700101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrn_id: Optional[AlternateIdentification1Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 12,
        },
    )


@dataclass
class Trade3Fxtr03700101:
    exctn_pric: Optional[ActiveCurrencyAnd13DecimalAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "ExctnPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    last_qty: Optional[CurrencyAndAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "LastQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    sttlm_tp: Optional[SettlementDateCode] = field(
        default=None,
        metadata={
            "name": "SttlmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    valtn_rate: Optional[AgreedRate3Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "ValtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    fwd_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FwdPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    clctd_ctr_pty_ccy_last_qty: Optional[CurrencyAndAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "ClctdCtrPtyCcyLastQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    rsk_amt: Optional[ActiveCurrencyAndAmountFxtr03700101] = field(
        default=None,
        metadata={
            "name": "RskAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    scty_id: Optional[SecurityIdentification18Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    fxg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "FxgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    dlta_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DltaInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    assoctd_trad_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdTradRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PartyIdentification19ChoiceFxtr03700101:
    nm_and_adr: Optional[NameAndAddress8Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    any_bic: Optional[PartyIdentification44Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )


@dataclass
class PartyIdentificationAndAccount119Fxtr03700101:
    pty_id: list[PartyIdentification90Fxtr03700101] = field(
        default_factory=list,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_occurs": 1,
        },
    )
    acct_id: list[AccountIdentification30Fxtr03700101] = field(
        default_factory=list,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class Trade2Fxtr03700101:
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    fxtrad_pdct: Optional[UnderlyingProductIdentifier1Code] = field(
        default=None,
        metadata={
            "name": "FXTradPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    tradg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tradg_mtd: Optional[TradingMethodType1Code] = field(
        default=None,
        metadata={
            "name": "TradgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    tradg_md: Optional[TradingModeType1Code] = field(
        default=None,
        metadata={
            "name": "TradgMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    clr_mtd: Optional[ClearingMethod1Code] = field(
        default=None,
        metadata={
            "name": "ClrMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Symb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_conf: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    fxdtls: Optional[Trade3Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    swp_leg: list[InstrumentLeg6Fxtr03700101] = field(
        default_factory=list,
        metadata={
            "name": "SwpLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    pdct_id: Optional[SecurityIdentification22ChoiceFxtr03700101] = field(
        default=None,
        metadata={
            "name": "PdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    assoctd_trad_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdTradRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class FundIdentification3Fxtr03700101:
    fnd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_id_wth_ctdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctIdWthCtdn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctdn_id: Optional[PartyIdentification19ChoiceFxtr03700101] = field(
        default=None,
        metadata={
            "name": "CtdnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )


@dataclass
class TradePartyIdentification7Fxtr03700101:
    fnd_inf: Optional[FundIdentification3Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "FndInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    buyr_or_sellr_ind: Optional[OptionParty1Code] = field(
        default=None,
        metadata={
            "name": "BuyrOrSellrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    initr_ind: Optional[OptionParty3Code] = field(
        default=None,
        metadata={
            "name": "InitrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    trad_pty_id: Optional[PartyIdentification78Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "TradPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    submitg_pty: Optional[PartyIdentificationAndAccount119Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "SubmitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeTradeConfirmationStatusAdviceV01Fxtr03700101:
    hdr: Optional[Header23Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    advc_id: Optional[MessageIdentification1Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "AdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    tradg_sd_id: Optional[TradePartyIdentification7Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "TradgSdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    ctr_pty_sd_id: Optional[TradePartyIdentification7Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "CtrPtySdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    trad_dtl: Optional[Trade2Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "TradDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    conf_inf: Optional[Confirmation1Fxtr03700101] = field(
        default=None,
        metadata={
            "name": "ConfInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
            "required": True,
        },
    )
    ref: Optional[AdditionalReferencesFxtr03700101] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr03700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01",
        },
    )


@dataclass
class Fxtr03700101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.037.001.01"

    fxtrad_conf_sts_advc: Optional[
        ForeignExchangeTradeConfirmationStatusAdviceV01Fxtr03700101
    ] = field(
        default=None,
        metadata={
            "name": "FXTradConfStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
