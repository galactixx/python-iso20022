from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code
from python_iso20022.reda.reda_026_001_01.enums import EligibilityType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01"


@dataclass
class GenericIdentification36Reda02600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Reda02600101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda02600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class PostalAddress1Reda02600101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Reda02600101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda02600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Reda02600101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda02600101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceReda02600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda02600101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda02600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )


@dataclass
class PartyIdentification136Reda02600101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceReda02600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SystemPartyIdentification8Reda02600101(ISO20022MessageElement):
    id: Optional[PartyIdentification136Reda02600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda02600101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )


@dataclass
class SystemPartyIdentification2ChoiceReda02600101(ISO20022MessageElement):
    org_id: Optional[PartyIdentification136Reda02600101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )
    cmbnd_id: Optional[SystemPartyIdentification8Reda02600101] = field(
        default=None,
        metadata={
            "name": "CmbndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )


@dataclass
class EligibilityIdentification3ChoiceReda02600101(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    fin_instrm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    issr_csdid: Optional[SystemPartyIdentification2ChoiceReda02600101] = field(
        default=None,
        metadata={
            "name": "IssrCSDId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )


@dataclass
class EligibleCounterpart3Reda02600101(ISO20022MessageElement):
    issr_id: Optional[SystemPartyIdentification2ChoiceReda02600101] = field(
        default=None,
        metadata={
            "name": "IssrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )
    elgbl_cntrpt_id: Optional[SystemPartyIdentification2ChoiceReda02600101] = field(
        default=None,
        metadata={
            "name": "ElgblCntrptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )
    vld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )
    vld_to: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )
    elgblty_tp: Optional[EligibilityType1Code] = field(
        default=None,
        metadata={
            "name": "ElgbltyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )
    elgblty_id: Optional[EligibilityIdentification3ChoiceReda02600101] = field(
        default=None,
        metadata={
            "name": "ElgbltyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )


@dataclass
class EligibleCounterpartCsdcreationRequestV01Reda02600101(ISO20022MessageElement):
    class Meta:
        name = "EligibleCounterpartCSDCreationRequestV01"

    msg_hdr: Optional[MessageHeader1Reda02600101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )
    elgbl_cntrpt_csd: Optional[EligibleCounterpart3Reda02600101] = field(
        default=None,
        metadata={
            "name": "ElgblCntrptCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda02600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01",
        },
    )


@dataclass
class Reda02600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.026.001.01"

    elgbl_cntrpt_csdcre_req: Optional[
        EligibleCounterpartCsdcreationRequestV01Reda02600101
    ] = field(
        default=None,
        metadata={
            "name": "ElgblCntrptCSDCreReq",
            "type": "Element",
            "required": True,
        },
    )
