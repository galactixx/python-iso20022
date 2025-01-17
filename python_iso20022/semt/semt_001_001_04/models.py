from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.enums import AddressType2Code
from python_iso20022.semt.semt_001_001_04.enums import MessageRejectedReason2Code

__NAMESPACE__ = "urn:swift:xsd:semt.001.001.04"


@dataclass
class GenericIdentification36Semt00100104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
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
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentNumber5ChoiceSemt00100104:
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Semt00100104] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )


@dataclass
class PostalAddress1Semt00100104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
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
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class NameAndAddress5Semt00100104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt00100104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )


@dataclass
class PartyIdentification247ChoiceSemt00100104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt00100104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt00100104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )


@dataclass
class AdditionalReference14Semt00100104:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification247ChoiceSemt00100104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nb: Optional[DocumentNumber5ChoiceSemt00100104] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
        },
    )


@dataclass
class LinkedMessage6ChoiceSemt00100104:
    prvs_ref: Optional[AdditionalReference14Semt00100104] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )
    othr_ref: Optional[AdditionalReference14Semt00100104] = field(
        default=None,
        metadata={
            "name": "OthrRef",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )
    rltd_ref: Optional[AdditionalReference14Semt00100104] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )


@dataclass
class RejectionReason69Semt00100104:
    rsn: Optional[MessageRejectedReason2Code] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    lkd_msg: Optional[LinkedMessage6ChoiceSemt00100104] = field(
        default=None,
        metadata={
            "name": "LkdMsg",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
        },
    )


@dataclass
class SecuritiesMessageRejectionV04Semt00100104:
    rltd_ref: Optional[AdditionalReference14Semt00100104] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
        },
    )
    rsn: Optional[RejectionReason69Semt00100104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:swift:xsd:semt.001.001.04",
            "required": True,
        },
    )


@dataclass
class Semt00100104:
    class Meta:
        namespace = "urn:swift:xsd:semt.001.001.04"

    scties_msg_rjctn: Optional[SecuritiesMessageRejectionV04Semt00100104] = field(
        default=None,
        metadata={
            "name": "SctiesMsgRjctn",
            "type": "Element",
            "required": True,
        },
    )
