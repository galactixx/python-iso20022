from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    DeliveryReceiptType2Code,
    DistributionPolicy1Code,
    FormOfSecurity1Code,
    InvestmentFundFee1Code,
    NoReasonCode,
    OrderOriginatorEligibility1Code,
)
from python_iso20022.setr.enums import GateHoldBack1Code, RedemptionCompletion1Code
from python_iso20022.setr.setr_016_001_04.enums import (
    CancelledStatusReason2Code,
    ConditionallyAcceptedStatusReason2Code,
    InRepairStatusReason1Code,
    OrderStatus4Code,
    RejectedStatusReason11Code,
    SettledStatusReason2Code,
    SuspendedStatusReason3Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04"


@dataclass
class ActiveCurrencyAndAmountSetr01600104(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSetr01600104(ISO20022MessageElement):
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
class DateAndDateTimeChoiceSetr01600104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class DateFormat42ChoiceSetr01600104(ISO20022MessageElement):
    yr_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YrMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    yr_mnth_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "YrMnthDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class Extension1Setr01600104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Setr01600104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Setr01600104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceSetr01600104(ISO20022MessageElement):
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LegIdentification1ChoiceSetr01600104(ISO20022MessageElement):
    red_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RedLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sbcpt_leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SbcptLegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Setr01600104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )


@dataclass
class SubAccount6Setr01600104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalAmount1ChoiceSetr01600104(ISO20022MessageElement):
    addtl_csh_in: Optional[ActiveOrHistoricCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "AddtlCshIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rsltg_csh_out: Optional[ActiveOrHistoricCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "RsltgCshOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class AlternateSecurityIdentification7Setr01600104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )


@dataclass
class CancelledReason12ChoiceSetr01600104(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtry: Optional[GenericIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class ChargeType5ChoiceSetr01600104(ISO20022MessageElement):
    cd: Optional[InvestmentFundFee1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtry: Optional[GenericIdentification47Setr01600104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class ConditionallyAcceptedStatusReason3ChoiceSetr01600104(ISO20022MessageElement):
    cd: Optional[ConditionallyAcceptedStatusReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtry: Optional[GenericIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class ExpectedExecutionDetails2Setr01600104(ISO20022MessageElement):
    xpctd_trad_dt_tm: Optional[DateAndDateTimeChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "XpctdTradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    xpctd_csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdCshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class ExpectedExecutionDetails4Setr01600104(ISO20022MessageElement):
    xpctd_trad_dt_tm: Optional[DateAndDateTimeChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "XpctdTradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    xpctd_csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdCshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class InRepairStatusReason5ChoiceSetr01600104(ISO20022MessageElement):
    cd: Optional[InRepairStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtry: Optional[GenericIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class PartiallySettled21ChoiceSetr01600104(ISO20022MessageElement):
    cd: Optional[SettledStatusReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtry: Optional[GenericIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class PostalAddress1Setr01600104(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RejectedReason20ChoiceSetr01600104(ISO20022MessageElement):
    cd: Optional[RejectedStatusReason11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtry: Optional[GenericIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class Series1Setr01600104(ISO20022MessageElement):
    srs_dt: Optional[DateFormat42ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "SrsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    srs_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrsNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SuspendedStatusReason5ChoiceSetr01600104(ISO20022MessageElement):
    cd: Optional[SuspendedStatusReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtry: Optional[GenericIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class CancelledStatusReason16Setr01600104(ISO20022MessageElement):
    rsn: Optional[CancelledReason12ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ConditionallyAcceptedStatusReason3Setr01600104(ISO20022MessageElement):
    rsn: Optional[ConditionallyAcceptedStatusReason3ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Fee3Setr01600104(ISO20022MessageElement):
    tp: Optional[ChargeType5ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rprd_std_amt: Optional[ActiveCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "RprdStdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rprd_std_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RprdStdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rprd_dscnt_amt: Optional[ActiveCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "RprdDscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rprd_dscnt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RprdDscntRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rprd_reqd_amt: Optional[ActiveCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "RprdReqdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rprd_reqd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RprdReqdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_comrcl_agrmt_ref_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NewComrclAgrmtRefInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class FundOrderData6Setr01600104(ISO20022MessageElement):
    sttlm_amt: Optional[ActiveCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    sttlm_mtd: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    addtl_amt: Optional[AdditionalAmount1ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "AddtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class InRepairStatusReason4Setr01600104(ISO20022MessageElement):
    rsn: Optional[InRepairStatusReason5ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NameAndAddress5Setr01600104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01600104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class PartiallySettledStatus10Setr01600104(ISO20022MessageElement):
    rsn: Optional[PartiallySettled21ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class RejectedStatus9Setr01600104(ISO20022MessageElement):
    rsn: Optional[RejectedReason20ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecurityIdentification25ChoiceSetr01600104(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Setr01600104] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class SuspendedStatusReason4Setr01600104(ISO20022MessageElement):
    rsn: Optional[SuspendedStatusReason5ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ConditionallyAcceptedStatus3ChoiceSetr01600104(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rsn_dtls: list[ConditionallyAcceptedStatusReason3Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "RsnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 5,
        },
    )


@dataclass
class FinancialInstrument57Setr01600104(ISO20022MessageElement):
    id: Optional[SecurityIdentification25ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    srs_id: Optional[Series1Setr01600104] = field(
        default=None,
        metadata={
            "name": "SrsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class HoldBackInformation3Setr01600104(ISO20022MessageElement):
    tp: Optional[GateHoldBack1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    xpctd_rls_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdRlsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification25ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    fin_instrm_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    red_cmpltn: Optional[RedemptionCompletion1Code] = field(
        default=None,
        metadata={
            "name": "RedCmpltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class InRepairStatusReason4ChoiceSetr01600104(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rsn_dtls: list[InRepairStatusReason4Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "RsnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 5,
        },
    )


@dataclass
class PartyIdentification90ChoiceSetr01600104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Setr01600104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class SuspendedStatusReason4ChoiceSetr01600104(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rsn_dtls: list[SuspendedStatusReason4Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "RsnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 5,
        },
    )


@dataclass
class OrderStatus3ChoiceSetr01600104(ISO20022MessageElement):
    sts: Optional[OrderStatus4Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    canc: Optional[CancelledStatusReason16Setr01600104] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    condly_accptd: Optional[ConditionallyAcceptedStatus3ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "CondlyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rjctd: list[RejectedStatus9Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 10,
        },
    )
    sspd: Optional[SuspendedStatusReason4ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Sspd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtly_sttld: Optional[PartiallySettledStatus10Setr01600104] = field(
        default=None,
        metadata={
            "name": "PrtlySttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class OrderStatus4ChoiceSetr01600104(ISO20022MessageElement):
    sts: Optional[OrderStatus4Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    canc: Optional[CancelledStatusReason16Setr01600104] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    condly_accptd: Optional[ConditionallyAcceptedStatus3ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "CondlyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rjctd: list[RejectedStatus9Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 10,
        },
    )
    sspd: Optional[SuspendedStatusReason4ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Sspd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    in_rpr: Optional[InRepairStatusReason4ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "InRpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtly_sttld: Optional[PartiallySettledStatus10Setr01600104] = field(
        default=None,
        metadata={
            "name": "PrtlySttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class OrderStatus5ChoiceSetr01600104(ISO20022MessageElement):
    sts: Optional[OrderStatus4Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    canc: Optional[CancelledStatusReason16Setr01600104] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    condly_accptd: Optional[ConditionallyAcceptedStatus3ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "CondlyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    rjctd: list[RejectedStatus9Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 10,
        },
    )
    sspd: Optional[SuspendedStatusReason4ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Sspd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    in_rpr: Optional[InRepairStatusReason4ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "InRpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    prtly_sttld: Optional[PartiallySettledStatus10Setr01600104] = field(
        default=None,
        metadata={
            "name": "PrtlySttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class PartyIdentification113Setr01600104(ISO20022MessageElement):
    pty: Optional[PartyIdentification90ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class AdditionalReference8Setr01600104(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification113Setr01600104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentAccount58Setr01600104(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_id: list[PartyIdentification113Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    acct_svcr: Optional[PartyIdentification113Setr01600104] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    sub_acct_dtls: Optional[SubAccount6Setr01600104] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class OrderStatusAndReason10Setr01600104(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_sts: Optional[OrderStatus3ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "OrdrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    sts_initr: Optional[PartyIdentification113Setr01600104] = field(
        default=None,
        metadata={
            "name": "StsInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class FundOrderData5Setr01600104(ISO20022MessageElement):
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01600104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01600104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    net_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    grss_amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    hldgs_red_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HldgsRedRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    sttlm_amt: Optional[ActiveCurrencyAndAmountSetr01600104] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class References61ChoiceSetr01600104(ISO20022MessageElement):
    rltd_ref: list[AdditionalReference8Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 2,
        },
    )
    othr_ref: list[AdditionalReference8Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "OthrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 2,
        },
    )


@dataclass
class SwitchLegReferences2Setr01600104(ISO20022MessageElement):
    leg_id: Optional[LegIdentification1ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "LegId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    leg_rjctn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegRjctnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    rprd_fee: list[Fee3Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "RprdFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 10,
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01600104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01600104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class IndividualOrderStatusAndReason7Setr01600104(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    deal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_sts: Optional[OrderStatus5ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "OrdrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    rprd_fee: list[Fee3Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "RprdFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "max_occurs": 10,
        },
    )
    sts_initr: Optional[PartyIdentification113Setr01600104] = field(
        default=None,
        metadata={
            "name": "StsInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    ordr_data: Optional[FundOrderData5Setr01600104] = field(
        default=None,
        metadata={
            "name": "OrdrData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    new_dtls: Optional[ExpectedExecutionDetails4Setr01600104] = field(
        default=None,
        metadata={
            "name": "NewDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    gtg_or_hld_bck_dtls: Optional[HoldBackInformation3Setr01600104] = field(
        default=None,
        metadata={
            "name": "GtgOrHldBckDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class SwitchOrderStatusAndReason2Setr01600104(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    deal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_sts: Optional[OrderStatus4ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "OrdrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    leg_inf: list[SwitchLegReferences2Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "LegInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    sts_initr: Optional[PartyIdentification113Setr01600104] = field(
        default=None,
        metadata={
            "name": "StsInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    ordr_data: Optional[FundOrderData6Setr01600104] = field(
        default=None,
        metadata={
            "name": "OrdrData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    new_dtls: Optional[ExpectedExecutionDetails2Setr01600104] = field(
        default=None,
        metadata={
            "name": "NewDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class Status24ChoiceSetr01600104(ISO20022MessageElement):
    ordr_dtls_rpt: Optional[OrderStatusAndReason10Setr01600104] = field(
        default=None,
        metadata={
            "name": "OrdrDtlsRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    indv_ordr_dtls_rpt: list[IndividualOrderStatusAndReason7Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "IndvOrdrDtlsRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    swtch_ordr_dtls_rpt: list[SwitchOrderStatusAndReason2Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "SwtchOrdrDtlsRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class OrderInstructionStatusReportV04Setr01600104(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Setr01600104] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    ref: Optional[References61ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )
    sts_rpt: Optional[Status24ChoiceSetr01600104] = field(
        default=None,
        metadata={
            "name": "StsRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
            "required": True,
        },
    )
    xtnsn: list[Extension1Setr01600104] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04",
        },
    )


@dataclass
class Setr01600104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.016.001.04"

    ordr_instr_sts_rpt: Optional[OrderInstructionStatusReportV04Setr01600104] = field(
        default=None,
        metadata={
            "name": "OrdrInstrStsRpt",
            "type": "Element",
            "required": True,
        },
    )
