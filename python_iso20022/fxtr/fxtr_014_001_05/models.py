from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, AllocationIndicator1Code
from python_iso20022.fxtr.enums import (
    CollateralisationIndicator1Code,
    CorporateSectorIdentifier1Code,
    FxamountType1Code,
    SideIndicator1Code,
    Trading1MethodCode,
    UnderlyingProductIdentifier1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05"


@dataclass
class ActiveCurrencyAndAmountFxtr01400105(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountFxtr01400105(ISO20022MessageElement):
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
class AgreedRate3Fxtr01400105(ISO20022MessageElement):
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class AgreementConditions1Fxtr01400105(ISO20022MessageElement):
    agrmt_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "pattern": r"[a-zA-Z]{1,6}",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[0-9]{4}",
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceFxtr01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactInformation1Fxtr01400105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    tel_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TelNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateAndDateTime2ChoiceFxtr01400105(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class DigitalTokenAmount1Fxtr01400105(ISO20022MessageElement):
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[1-9B-DF-HJ-NP-XZ][0-9B-DF-HJ-NP-XZ]{8,8}",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "max_length": 30,
        },
    )


@dataclass
class IdentificationSource3ChoiceFxtr01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification265Fxtr01400105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementRateSource1Fxtr01400105(ISO20022MessageElement):
    rate_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "RateSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "pattern": r"[a-zA-Z]{3}[0-9]{1,2}",
        },
    )
    tm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[0-9]{4}",
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    lctn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LctnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[a-zA-Z0-9]{2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Fxtr01400105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TradeAgreement14Fxtr01400105(ISO20022MessageElement):
    trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    orgtr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgtrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    opr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    opr_scp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OprScp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    pdct_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sttlm_ssn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmSsnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    pmt_vrss_pmt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtVrssPmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class UniqueTransactionIdentifier2Fxtr01400105(ISO20022MessageElement):
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    prr_unq_tx_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PrrUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class AmountOrRate4ChoiceFxtr01400105(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountFxtr01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ClearingBrokerIdentification1Fxtr01400105(ISO20022MessageElement):
    sd_ind: Optional[SideIndicator1Code] = field(
        default=None,
        metadata={
            "name": "SdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    clr_brkr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrBrkrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyOrDigitalTokenAmount1ChoiceFxtr01400105(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountFxtr01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    dgtl_tkn_amt: Optional[DigitalTokenAmount1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "DgtlTknAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class FxamountType1ChoiceFxtr01400105(ISO20022MessageElement):
    class Meta:
        name = "FXAmountType1Choice"

    cd: Optional[FxamountType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OpeningConditions1Fxtr01400105(ISO20022MessageElement):
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    valtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    sttlm_rate_src: list[SettlementRateSource1Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "SttlmRateSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class OtherIdentification1Fxtr01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )


@dataclass
class PartyIdentification266Fxtr01400105(ISO20022MessageElement):
    pty_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 34,
        },
    )
    any_bic: Optional[PartyIdentification265Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    acct_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 34,
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 105,
        },
    )
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PostalAddress1Fxtr01400105(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Fxtr01400105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )


@dataclass
class AmountsAndValueDate6Fxtr01400105(ISO20022MessageElement):
    tradg_sd_buy_amt: Optional[CurrencyOrDigitalTokenAmount1ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "TradgSdBuyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    tradg_sd_sell_amt: Optional[CurrencyOrDigitalTokenAmount1ChoiceFxtr01400105] = (
        field(
            default=None,
            metadata={
                "name": "TradgSdSellAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
                "required": True,
            },
        )
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )


@dataclass
class FxcommissionOrFee1Fxtr01400105(ISO20022MessageElement):
    class Meta:
        name = "FXCommissionOrFee1"

    tp: Optional[FxamountType1ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    amt_or_rate: Optional[AmountOrRate4ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "AmtOrRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class NdfopeningFixing1ChoiceFxtr01400105(ISO20022MessageElement):
    class Meta:
        name = "NDFOpeningFixing1Choice"

    opng_conds: Optional[OpeningConditions1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "OpngConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    opng_conf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OpngConfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress8Fxtr01400105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecurityIdentification19Fxtr01400105(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class NonDeliverableForwardConditions1Fxtr01400105(ISO20022MessageElement):
    opng_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OpngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    opng_fxg_conds: Optional[NdfopeningFixing1ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "OpngFxgConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )


@dataclass
class PartyIdentification242ChoiceFxtr01400105(ISO20022MessageElement):
    nm_and_adr: Optional[NameAndAddress8Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    any_bic: Optional[PartyIdentification265Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    pty_id: Optional[PartyIdentification266Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class PartyIdentification60Fxtr01400105(ISO20022MessageElement):
    fnd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm_and_adr: Optional[NameAndAddress8Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class CounterpartySideTransactionReporting2Fxtr01400105(ISO20022MessageElement):
    rptg_jursdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_pty: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "RptgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    ctr_pty_sd_unq_tx_idr: list[UniqueTransactionIdentifier2Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "CtrPtySdUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class FundIdentification5Fxtr01400105(ISO20022MessageElement):
    fnd_id: Optional[PartyIdentification60Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "FndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    acct_id_wth_ctdn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctIdWthCtdn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctdn_id: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "CtdnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class GeneralInformation8Fxtr01400105(ISO20022MessageElement):
    blck_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BlckInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    rltd_trad_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdTradRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dealg_mtd: Optional[Trading1MethodCode] = field(
        default=None,
        metadata={
            "name": "DealgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    brkr_id: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "BrkrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    ctr_pty_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brkrs_comssn: Optional[ActiveCurrencyAndAmountFxtr01400105] = field(
        default=None,
        metadata={
            "name": "BrkrsComssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    sndr_to_rcvr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "SndrToRcvrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )
    dealg_brnch_tradg_sd: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "DealgBrnchTradgSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    dealg_brnch_ctr_pty_sd: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "DealgBrnchCtrPtySd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    ctct_inf: Optional[ContactInformation1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "CtctInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    agrmt_dtls: Optional[AgreementConditions1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "AgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    defs_yr: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "DefsYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    brkrs_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrkrsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementParties120Fxtr01400105(ISO20022MessageElement):
    dlvry_agt: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "DlvryAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    intrmy: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    rcvg_agt: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "RcvgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    bnfcry_instn: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "BnfcryInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class TradingSideTransactionReporting2Fxtr01400105(ISO20022MessageElement):
    rptg_jursdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_pty: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "RptgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    tradg_sd_unq_tx_idr: list[UniqueTransactionIdentifier2Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "TradgSdUnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class RegulatoryReporting7Fxtr01400105(ISO20022MessageElement):
    tradg_sd_tx_rptg: list[TradingSideTransactionReporting2Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "TradgSdTxRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    ctr_pty_sd_tx_rptg: list[CounterpartySideTransactionReporting2Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "CtrPtySdTxRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    cntrl_ctr_pty_clr_hs: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "CntrlCtrPtyClrHs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    clr_brkr: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "ClrBrkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    clr_xcptn_pty: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "ClrXcptnPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    clr_brkr_id: Optional[ClearingBrokerIdentification1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "ClrBrkrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    clr_thrshld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClrThrshldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    clrd_pdct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrdPdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    undrlyg_pdct_idr: Optional[UnderlyingProductIdentifier1Code] = field(
        default=None,
        metadata={
            "name": "UndrlygPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    allcn_ind: Optional[AllocationIndicator1Code] = field(
        default=None,
        metadata={
            "name": "AllcnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    collstn_ind: Optional[CollateralisationIndicator1Code] = field(
        default=None,
        metadata={
            "name": "CollstnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    exctn_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExctnVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    exctn_tmstmp: Optional[DateAndDateTime2ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "ExctnTmstmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    non_std_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonStdFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    lk_swp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkSwpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "length": 42,
        },
    )
    fin_ntr_of_the_ctr_pty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinNtrOfTheCtrPtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    coll_prtfl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollPrtflInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    coll_prtfl_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 10,
        },
    )
    prtfl_cmprssn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtflCmprssnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    corp_sctr_ind: Optional[CorporateSectorIdentifier1Code] = field(
        default=None,
        metadata={
            "name": "CorpSctrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    trad_wth_non_eeactr_pty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TradWthNonEEACtrPtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    ntrgrp_trad_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtrgrpTradInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    comrcl_or_trsr_fincg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ComrclOrTrsrFincgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    conf_dt_and_tmstmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ConfDtAndTmstmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    clr_tmstmp: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ClrTmstmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    comssns_and_fees: list[FxcommissionOrFee1Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "ComssnsAndFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    addtl_rptg_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRptgInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class TradePartyIdentification8Fxtr01400105(ISO20022MessageElement):
    submitg_pty: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "SubmitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    trad_pty: Optional[PartyIdentification242ChoiceFxtr01400105] = field(
        default=None,
        metadata={
            "name": "TradPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    fnd_id: list[FundIdentification5Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "FndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class ForeignExchangeTradeInstructionV05Fxtr01400105(ISO20022MessageElement):
    trad_inf: Optional[TradeAgreement14Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "TradInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    tradg_sd_id: Optional[TradePartyIdentification8Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "TradgSdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    ctr_pty_sd_id: Optional[TradePartyIdentification8Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "CtrPtySdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    trad_amts: Optional[AmountsAndValueDate6Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "TradAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    agrd_rate: Optional[AgreedRate3Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "AgrdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
            "required": True,
        },
    )
    ndfconds: Optional[NonDeliverableForwardConditions1Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "NDFConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    tradg_sd_sttlm_instrs: Optional[SettlementParties120Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "TradgSdSttlmInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    ctr_pty_sd_sttlm_instrs: Optional[SettlementParties120Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "CtrPtySdSttlmInstrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    optnl_gnl_inf: Optional[GeneralInformation8Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "OptnlGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    rgltry_rptg: Optional[RegulatoryReporting7Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "RgltryRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr01400105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05",
        },
    )


@dataclass
class Fxtr01400105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.014.001.05"

    fxtrad_instr: Optional[ForeignExchangeTradeInstructionV05Fxtr01400105] = field(
        default=None,
        metadata={
            "name": "FXTradInstr",
            "type": "Element",
            "required": True,
        },
    )
