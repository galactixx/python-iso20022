from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.camt.enums import PaymentRole1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01"


@dataclass
class ClearingSystemIdentification2ChoiceCamt10400101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt10400101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Camt10400101:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )


@dataclass
class StructuredLongPostalAddress1Camt10400101:
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_bldg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtBldgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rgn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    pob: Optional[str] = field(
        default=None,
        metadata={
            "name": "POB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt10400101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt10400101:
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt10400101] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt10400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt10400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LongPostalAddress1ChoiceCamt10400101:
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[StructuredLongPostalAddress1Camt10400101] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )


@dataclass
class SupplementaryData1Camt10400101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt10400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
        },
    )


@dataclass
class CommunicationAddress8Camt10400101:
    pstl_adr: Optional[LongPostalAddress1ChoiceCamt10400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class MemberIdentification3ChoiceCamt10400101:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt10400101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt10400101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )


@dataclass
class ContactIdentificationAndAddress1Camt10400101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    role: Optional[PaymentRole1Code] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
        },
    )
    com_adr: Optional[CommunicationAddress8Camt10400101] = field(
        default=None,
        metadata={
            "name": "ComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
        },
    )


@dataclass
class Member6Camt10400101:
    mmb_rtr_adr: list[MemberIdentification3ChoiceCamt10400101] = field(
        default_factory=list,
        metadata={
            "name": "MmbRtrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )
    ctct_ref: list[ContactIdentificationAndAddress1Camt10400101] = field(
        default_factory=list,
        metadata={
            "name": "CtctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )
    com_adr: Optional[CommunicationAddress8Camt10400101] = field(
        default=None,
        metadata={
            "name": "ComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )


@dataclass
class CreateMemberV01Camt10400101:
    msg_hdr: Optional[MessageHeader1Camt10400101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
        },
    )
    mmb_id: Optional[MemberIdentification3ChoiceCamt10400101] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
        },
    )
    val_set: Optional[Member6Camt10400101] = field(
        default=None,
        metadata={
            "name": "ValSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt10400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01",
        },
    )


@dataclass
class Camt10400101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01"

    cret_mmb: Optional[CreateMemberV01Camt10400101] = field(
        default=None,
        metadata={
            "name": "CretMmb",
            "type": "Element",
            "required": True,
        },
    )
