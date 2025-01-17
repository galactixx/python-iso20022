from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.camt.enums import PaymentRole1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04"


@dataclass
class ClearingSystemIdentification2ChoiceCamt01500104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt01500104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Camt01500104:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )


@dataclass
class StructuredLongPostalAddress1Camt01500104:
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    strt_bldg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtBldgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rgn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt01500104:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt01500104:
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt01500104] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt01500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt01500104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LongPostalAddress1ChoiceCamt01500104:
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[StructuredLongPostalAddress1Camt01500104] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )


@dataclass
class SupplementaryData1Camt01500104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt01500104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
        },
    )


@dataclass
class CommunicationAddress8Camt01500104:
    pstl_adr: Optional[LongPostalAddress1ChoiceCamt01500104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class MemberIdentification3ChoiceCamt01500104:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt01500104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt01500104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )


@dataclass
class ContactIdentificationAndAddress1Camt01500104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    role: Optional[PaymentRole1Code] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
        },
    )
    com_adr: Optional[CommunicationAddress8Camt01500104] = field(
        default=None,
        metadata={
            "name": "ComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
        },
    )


@dataclass
class Member6Camt01500104:
    mmb_rtr_adr: list[MemberIdentification3ChoiceCamt01500104] = field(
        default_factory=list,
        metadata={
            "name": "MmbRtrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )
    ctct_ref: list[ContactIdentificationAndAddress1Camt01500104] = field(
        default_factory=list,
        metadata={
            "name": "CtctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )
    com_adr: Optional[CommunicationAddress8Camt01500104] = field(
        default=None,
        metadata={
            "name": "ComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )


@dataclass
class ModifyMemberV04Camt01500104:
    msg_hdr: Optional[MessageHeader1Camt01500104] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
        },
    )
    mmb_id: Optional[MemberIdentification3ChoiceCamt01500104] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
        },
    )
    new_mmb_val_set: Optional[Member6Camt01500104] = field(
        default=None,
        metadata={
            "name": "NewMmbValSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt01500104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04",
        },
    )


@dataclass
class Camt01500104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04"

    modfy_mmb: Optional[ModifyMemberV04Camt01500104] = field(
        default=None,
        metadata={
            "name": "ModfyMmb",
            "type": "Element",
            "required": True,
        },
    )
