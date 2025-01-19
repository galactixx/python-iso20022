from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    DateType8Code,
    PartyType3Code,
    PartyType4Code,
    Side1Code,
)
from python_iso20022.fxtr.enums import (
    ClearingMethod1Code,
    ConfirmationRequest1Code,
    IdentificationType2Code,
    QueryTradeStatus1Code,
    SettlementDateCode,
    TradingMethodType1Code,
    TradingModeType1Code,
    UnderlyingProductIdentifier1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01"


@dataclass
class ActiveCurrencyAnd13DecimalAmountFxtr03400101(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountFxtr03400101(ISO20022MessageElement):
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
class AgreedRate3Fxtr03400101(ISO20022MessageElement):
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CurrencyAndAmountFxtr03400101(ISO20022MessageElement):
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
class DateAndDateTimeChoiceFxtr03400101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )


@dataclass
class IdentificationSource1ChoiceFxtr03400101(ISO20022MessageElement):
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Fxtr03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Fxtr03400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AlternateIdentification1Fxtr03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceFxtr03400101] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )


@dataclass
class DateFormat18ChoiceFxtr03400101(ISO20022MessageElement):
    dt: Optional[DateAndDateTimeChoiceFxtr03400101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    not_spcfd_dt: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )


@dataclass
class GenericIdentification32Fxtr03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    issr: Optional[PartyType4Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecurityIdentification18Fxtr03400101(ISO20022MessageElement):
    scty_id_src: Optional[IdentificationType2Code] = field(
        default=None,
        metadata={
            "name": "SctyIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    scty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Fxtr03400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )


@dataclass
class Header23Fxtr03400101(ISO20022MessageElement):
    frmt_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    initg_pty: Optional[GenericIdentification32Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification32Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    msg_seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MsgSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )


@dataclass
class InstrumentLeg6Fxtr03400101(ISO20022MessageElement):
    leg_sd: Optional[Side1Code] = field(
        default=None,
        metadata={
            "name": "LegSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_sttlm_tp: Optional[SettlementDateCode] = field(
        default=None,
        metadata={
            "name": "LegSttlmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_sttlm_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LegSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_last_pric: Optional[ActiveCurrencyAnd13DecimalAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "LegLastPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    leg_ordr_qty: Optional[CurrencyAndAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "LegOrdrQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_fwd_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LegFwdPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    leg_clctd_ctr_pty_ccy_last_qty: Optional[CurrencyAndAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "LegClctdCtrPtyCcyLastQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_rsk_amt: Optional[ActiveCurrencyAndAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "LegRskAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_valtn_rate: Optional[AgreedRate3Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "LegValtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LegValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    leg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    leg_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    leg_scty_id: Optional[SecurityIdentification18Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "LegSctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )


@dataclass
class Period4Fxtr03400101(ISO20022MessageElement):
    start_dt: Optional[DateFormat18ChoiceFxtr03400101] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat18ChoiceFxtr03400101] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )


@dataclass
class SecurityIdentification22ChoiceFxtr03400101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrn_id: Optional[AlternateIdentification1Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 12,
        },
    )


@dataclass
class Trade3Fxtr03400101(ISO20022MessageElement):
    exctn_pric: Optional[ActiveCurrencyAnd13DecimalAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "ExctnPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    last_qty: Optional[CurrencyAndAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "LastQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    sttlm_tp: Optional[SettlementDateCode] = field(
        default=None,
        metadata={
            "name": "SttlmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    valtn_rate: Optional[AgreedRate3Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "ValtnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    fwd_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FwdPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    clctd_ctr_pty_ccy_last_qty: Optional[CurrencyAndAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "ClctdCtrPtyCcyLastQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    rsk_amt: Optional[ActiveCurrencyAndAmountFxtr03400101] = field(
        default=None,
        metadata={
            "name": "RskAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    scty_id: Optional[SecurityIdentification18Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    fxg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "FxgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    optn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    dlta_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DltaInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    assoctd_trad_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdTradRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Trade2Fxtr03400101(ISO20022MessageElement):
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    fxtrad_pdct: Optional[UnderlyingProductIdentifier1Code] = field(
        default=None,
        metadata={
            "name": "FXTradPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    tradg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tradg_mtd: Optional[TradingMethodType1Code] = field(
        default=None,
        metadata={
            "name": "TradgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    tradg_md: Optional[TradingModeType1Code] = field(
        default=None,
        metadata={
            "name": "TradgMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    clr_mtd: Optional[ClearingMethod1Code] = field(
        default=None,
        metadata={
            "name": "ClrMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Symb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_conf: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    fxdtls: Optional[Trade3Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    swp_leg: list[InstrumentLeg6Fxtr03400101] = field(
        default_factory=list,
        metadata={
            "name": "SwpLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    pdct_id: Optional[SecurityIdentification22ChoiceFxtr03400101] = field(
        default=None,
        metadata={
            "name": "PdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )
    assoctd_trad_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AssoctdTradRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ForeignExchangeTradeConfirmationRequestV01Fxtr03400101(ISO20022MessageElement):
    hdr: Optional[Header23Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    req_id: Optional[MessageIdentification1Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "ReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    trad_dtl: Optional[Trade2Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "TradDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    conf_tp: Optional[ConfirmationRequest1Code] = field(
        default=None,
        metadata={
            "name": "ConfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    qry_prd: Optional[Period4Fxtr03400101] = field(
        default=None,
        metadata={
            "name": "QryPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    qry_start_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryStartNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
            "pattern": r"[0-9]{1,35}",
        },
    )
    qry_trad_sts: Optional[QueryTradeStatus1Code] = field(
        default=None,
        metadata={
            "name": "QryTradSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr03400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01",
        },
    )


@dataclass
class Fxtr03400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.01"

    fxtrad_conf_req: Optional[
        ForeignExchangeTradeConfirmationRequestV01Fxtr03400101
    ] = field(
        default=None,
        metadata={
            "name": "FXTradConfReq",
            "type": "Element",
            "required": True,
        },
    )
