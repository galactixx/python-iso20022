from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01"


@dataclass
class GenericIdentification1Admi00600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Admi00600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessQuery1Admi00600101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )


@dataclass
class SequenceRange1Admi00600101(ISO20022MessageElement):
    fr_seq: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    to_seq: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Admi00600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class PostalAddress1Admi00600101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RequestType4ChoiceAdmi00600101(ISO20022MessageElement):
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Admi00600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )


@dataclass
class SequenceRange1ChoiceAdmi00600101(ISO20022MessageElement):
    fr_seq: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    to_seq: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fr_to_seq: list[SequenceRange1Admi00600101] = field(
        default_factory=list,
        metadata={
            "name": "FrToSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    eqseq: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EQSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    neqseq: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NEQSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Admi00600101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Admi00600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
        },
    )


@dataclass
class MessageHeader7Admi00600101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    req_tp: Optional[RequestType4ChoiceAdmi00600101] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Admi00600101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress5Admi00600101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Admi00600101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceAdmi00600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Admi00600101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Admi00600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )


@dataclass
class PartyIdentification136Admi00600101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceAdmi00600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class ResendSearchCriteria2Admi00600101(ISO20022MessageElement):
    biz_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BizDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_rg: Optional[SequenceRange1ChoiceAdmi00600101] = field(
        default=None,
        metadata={
            "name": "SeqRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )
    orgnl_msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    file_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt: Optional[PartyIdentification136Admi00600101] = field(
        default=None,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
        },
    )


@dataclass
class ResendRequestV01Admi00600101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader7Admi00600101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "required": True,
        },
    )
    rsnd_sch_crit: list[ResendSearchCriteria2Admi00600101] = field(
        default_factory=list,
        metadata={
            "name": "RsndSchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Admi00600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01",
        },
    )


@dataclass
class Admi00600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01"

    rsnd_req: Optional[ResendRequestV01Admi00600101] = field(
        default=None,
        metadata={
            "name": "RsndReq",
            "type": "Element",
            "required": True,
        },
    )
