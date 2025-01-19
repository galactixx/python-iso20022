from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09"


@dataclass
class GenericIdentification1Sese01400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketPracticeVersion1Sese01400109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Sese01400109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Sese01400109(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class NameAndAddress5Sese01400109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese01400109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )


@dataclass
class PartyIdentification125ChoiceSese01400109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese01400109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese01400109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )


@dataclass
class PartyIdentification139Sese01400109(ISO20022MessageElement):
    pty: Optional[PartyIdentification125ChoiceSese01400109] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class AdditionalReference10Sese01400109(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese01400109] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference11Sese01400109(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese01400109] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransferReference14Sese01400109(ISO20022MessageElement):
    trf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[AdditionalReference10Sese01400109] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    ctr_pty_ref: Optional[AdditionalReference10Sese01400109] = field(
        default=None,
        metadata={
            "name": "CtrPtyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    trf_conf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfConfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PortfolioTransferCancellationRequestV09Sese01400109(ISO20022MessageElement):
    msg_ref: Optional[MessageIdentification1Sese01400109] = field(
        default=None,
        metadata={
            "name": "MsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference11Sese01400109] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    prvs_ref: Optional[AdditionalReference10Sese01400109] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    rltd_ref: Optional[AdditionalReference10Sese01400109] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trf_refs: Optional[TransferReference14Sese01400109] = field(
        default=None,
        metadata={
            "name": "TrfRefs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
            "required": True,
        },
    )
    mkt_prctc_vrsn: Optional[MarketPracticeVersion1Sese01400109] = field(
        default=None,
        metadata={
            "name": "MktPrctcVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09",
        },
    )


@dataclass
class Sese01400109(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.014.001.09"

    prtfl_trf_cxl_req: Optional[PortfolioTransferCancellationRequestV09Sese01400109] = (
        field(
            default=None,
            metadata={
                "name": "PrtflTrfCxlReq",
                "type": "Element",
                "required": True,
            },
        )
    )
