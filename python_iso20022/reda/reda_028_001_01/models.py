from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.reda.enums import Status6Code
from python_iso20022.reda.reda_028_001_01.enums import Status10Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01"


@dataclass
class GenericIdentification1Reda02800101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceReda02800101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessInstruction1Reda02800101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )


@dataclass
class StatusReason6ChoiceReda02800101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda02800101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class MessageHeader12Reda02800101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Reda02800101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )


@dataclass
class OtherIdentification1Reda02800101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceReda02800101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "required": True,
        },
    )


@dataclass
class StatusReason7ChoiceReda02800101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda02800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )


@dataclass
class StatusReasonInformation10Reda02800101(ISO20022MessageElement):
    rsn: Optional[StatusReason6ChoiceReda02800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SupplementaryData1Reda02800101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda02800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "required": True,
        },
    )


@dataclass
class CollateralStatusReason1Reda02800101(ISO20022MessageElement):
    sts: Optional[Status6Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "required": True,
        },
    )
    rsn: list[StatusReasonInformation10Reda02800101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )


@dataclass
class SecurityIdentification19Reda02800101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Reda02800101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class StatusReasonInformation13Reda02800101(ISO20022MessageElement):
    rsn: Optional[StatusReason7ChoiceReda02800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "required": True,
        },
    )
    fin_instrm: Optional[SecurityIdentification19Reda02800101] = field(
        default=None,
        metadata={
            "name": "FinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CollateralStatusReason2Reda02800101(ISO20022MessageElement):
    sts: Optional[Status10Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
            "required": True,
        },
    )
    rsn: list[StatusReasonInformation13Reda02800101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )
    elgblty_set_prfl: Optional[GenericIdentification1Reda02800101] = field(
        default=None,
        metadata={
            "name": "ElgbltySetPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )


@dataclass
class CollateralDataStatusAdviceV01Reda02800101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader12Reda02800101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )
    sts_rsn: Optional[CollateralStatusReason1Reda02800101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )
    sts_rsn_and_fin_instrm: Optional[CollateralStatusReason2Reda02800101] = field(
        default=None,
        metadata={
            "name": "StsRsnAndFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Reda02800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01",
        },
    )


@dataclass
class Reda02800101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.028.001.01"

    coll_data_sts_advc: Optional[CollateralDataStatusAdviceV01Reda02800101] = field(
        default=None,
        metadata={
            "name": "CollDataStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
