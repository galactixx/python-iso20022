from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.enums import PaymentType3Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07"


@dataclass
class ActiveCurrencyAndAmountCamt02300107(ISO20022MessageElement):
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
class ClearingSystemIdentification2ChoiceCamt02300107(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt02300107(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketInfrastructureIdentification1ChoiceCamt02300107(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Camt02300107(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt02300107(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Amount2ChoiceCamt02300107(ISO20022MessageElement):
    amt_wtht_ccy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtWthtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amt_wth_ccy: Optional[ActiveCurrencyAndAmountCamt02300107] = field(
        default=None,
        metadata={
            "name": "AmtWthCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt02300107(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt02300107] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt02300107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt02300107] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentType4ChoiceCamt02300107(ISO20022MessageElement):
    cd: Optional[PaymentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Camt02300107(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt02300107] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "required": True,
        },
    )


@dataclass
class SystemIdentification2ChoiceCamt02300107(ISO20022MessageElement):
    mkt_infrstrctr_id: Optional[
        MarketInfrastructureIdentification1ChoiceCamt02300107
    ] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class MemberIdentification3ChoiceCamt02300107(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt02300107] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt02300107] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )


@dataclass
class PaymentInstruction13Camt02300107(ISO20022MessageElement):
    reqd_exctn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    pmt_tp: Optional[PaymentType4ChoiceCamt02300107] = field(
        default=None,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )


@dataclass
class SystemMember3Camt02300107(ISO20022MessageElement):
    sys_id: Optional[SystemIdentification2ChoiceCamt02300107] = field(
        default=None,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    mmb_id: Optional[MemberIdentification3ChoiceCamt02300107] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "required": True,
        },
    )


@dataclass
class BackupPaymentV07Camt02300107(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Camt02300107] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "required": True,
        },
    )
    orgnl_msg_id: Optional[MessageHeader1Camt02300107] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    instr_inf: Optional[PaymentInstruction13Camt02300107] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    trfd_amt: Optional[Amount2ChoiceCamt02300107] = field(
        default=None,
        metadata={
            "name": "TrfdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "required": True,
        },
    )
    cdtr: Optional[SystemMember3Camt02300107] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
            "required": True,
        },
    )
    cdtr_agt: Optional[SystemMember3Camt02300107] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    dbtr_agt: Optional[SystemMember3Camt02300107] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )
    splmtry_data: list[SupplementaryData1Camt02300107] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07",
        },
    )


@dataclass
class Camt02300107(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07"

    bckp_pmt: Optional[BackupPaymentV07Camt02300107] = field(
        default=None,
        metadata={
            "name": "BckpPmt",
            "type": "Element",
            "required": True,
        },
    )
