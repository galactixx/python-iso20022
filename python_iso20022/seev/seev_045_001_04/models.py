from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import AddressType2Code, DateType1Code
from python_iso20022.seev.seev_045_001_04.enums import (
    DateCalculationMethod1Code,
    DisclosureRequestType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04"


@dataclass
class DateAndDateTime2ChoiceSeev04500104:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )


@dataclass
class GenericIdentification30Seev04500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev04500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev04500104:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev04500104:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DateCode20ChoiceSeev04500104:
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Seev04500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )


@dataclass
class OtherIdentification1Seev04500104:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )


@dataclass
class PartyIdentification203ChoiceSeev04500104:
    prtry_id: Optional[GenericIdentification36Seev04500104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PostalAddress1Seev04500104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress26Seev04500104:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RequestShareHeldDate1ChoiceSeev04500104:
    dt_clctn_mtd: Optional[DateCalculationMethod1Code] = field(
        default=None,
        metadata={
            "name": "DtClctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    dt_clctn_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "DtClctnDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SupplementaryData1Seev04500104:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev04500104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )


@dataclass
class DateFormat46ChoiceSeev04500104:
    dt: Optional[DateAndDateTime2ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )


@dataclass
class NameAndAddress5Seev04500104:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev04500104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )


@dataclass
class PartyAddress1Seev04500104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    pstl_adr: Optional[PostalAddress26Seev04500104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class SecurityIdentification19Seev04500104:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev04500104] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PartyIdentification129ChoiceSeev04500104:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev04500104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev04500104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification214Seev04500104:
    id: Optional[PartyIdentification203ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )
    rcpt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    rspn_rcpt_adr: Optional[PartyAddress1Seev04500104] = field(
        default=None,
        metadata={
            "name": "RspnRcptAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )


@dataclass
class ShareholdersIdentificationDisclosureRequestV04Seev04500104:
    issr_dsclsr_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsclsr_req_tp: Optional[DisclosureRequestType1Code] = field(
        default=None,
        metadata={
            "name": "DsclsrReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )
    prvs_dsclsr_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvsDsclsrReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fwd_req_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FwdReqInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    rspn_thrgh_chain_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RspnThrghChainInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    shrhldr_rghts_drctv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShrhldrRghtsDrctvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    plc_of_jursdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    aplbl_law: Optional[str] = field(
        default=None,
        metadata={
            "name": "AplblLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev04500104] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )
    shrhldrs_dsclsr_rcrd_dt: Optional[DateFormat46ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "ShrhldrsDsclsrRcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )
    shrs_qty_thrshld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ShrsQtyThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    req_shr_held_dt: Optional[RequestShareHeldDate1ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "ReqShrHeldDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    dsclsr_rspn_rcpt: Optional[PartyIdentification214Seev04500104] = field(
        default=None,
        metadata={
            "name": "DsclsrRspnRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )
    issr_dsclsr_ddln: Optional[DateFormat46ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
            "required": True,
        },
    )
    dsclsr_rspn_ddln: Optional[DateFormat46ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "DsclsrRspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    issr: Optional[PartyIdentification129ChoiceSeev04500104] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Seev04500104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04",
        },
    )


@dataclass
class Seev04500104:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.045.001.04"

    shrhldrs_id_dsclsr_req: Optional[
        ShareholdersIdentificationDisclosureRequestV04Seev04500104
    ] = field(
        default=None,
        metadata={
            "name": "ShrhldrsIdDsclsrReq",
            "type": "Element",
            "required": True,
        },
    )
