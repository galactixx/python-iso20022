from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.acmt.acmt_005_001_06.enums import AccountManagementType3Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    GenderCode,
    PartyIdentificationType7Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06"


@dataclass
class GenericIdentification1Acmt00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Acmt00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class MessageIdentification1Acmt00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
        },
    )


@dataclass
class Account23Acmt00500106(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_acct_dtls: Optional[GenericIdentification1Acmt00500106] = field(
        default=None,
        metadata={
            "name": "RltdAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class IndividualPerson30Acmt00500106(ISO20022MessageElement):
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    gndr: Optional[GenderCode] = field(
        default=None,
        metadata={
            "name": "Gndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class OtherIdentification3ChoiceAcmt00500106(ISO20022MessageElement):
    cd: Optional[PartyIdentificationType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00500106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class PostalAddress1Acmt00500106(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class GenericIdentification81Acmt00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[OtherIdentification3ChoiceAcmt00500106] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Acmt00500106(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Acmt00500106] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class IndividualPersonIdentification2ChoiceAcmt00500106(ISO20022MessageElement):
    id_nb: Optional[GenericIdentification81Acmt00500106] = field(
        default=None,
        metadata={
            "name": "IdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    prsn_nm: Optional[IndividualPerson30Acmt00500106] = field(
        default=None,
        metadata={
            "name": "PrsnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class PartyIdentification125ChoiceAcmt00500106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Acmt00500106] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Acmt00500106] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class AdditionalReference13Acmt00500106(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification125ChoiceAcmt00500106] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification139Acmt00500106(ISO20022MessageElement):
    pty: Optional[PartyIdentification125ChoiceAcmt00500106] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class LinkedMessage5ChoiceAcmt00500106(ISO20022MessageElement):
    prvs_ref: Optional[AdditionalReference13Acmt00500106] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    othr_ref: Optional[AdditionalReference13Acmt00500106] = field(
        default=None,
        metadata={
            "name": "OthrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class OwnerIdentification3ChoiceAcmt00500106(ISO20022MessageElement):
    indv_ownr_id: Optional[IndividualPersonIdentification2ChoiceAcmt00500106] = field(
        default=None,
        metadata={
            "name": "IndvOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    org_ownr_id: Optional[PartyIdentification139Acmt00500106] = field(
        default=None,
        metadata={
            "name": "OrgOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class InvestmentAccount77Acmt00500106(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_id: Optional[OwnerIdentification3ChoiceAcmt00500106] = field(
        default=None,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    acct_svcr: Optional[PartyIdentification125ChoiceAcmt00500106] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class AccountManagementMessageReference5Acmt00500106(ISO20022MessageElement):
    lkd_ref: Optional[LinkedMessage5ChoiceAcmt00500106] = field(
        default=None,
        metadata={
            "name": "LkdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    sts_req_tp: Optional[AccountManagementType3Code] = field(
        default=None,
        metadata={
            "name": "StsReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
        },
    )
    acct_appl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    exstg_acct_id: Optional[Account23Acmt00500106] = field(
        default=None,
        metadata={
            "name": "ExstgAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )
    invstmt_acct: Optional[InvestmentAccount77Acmt00500106] = field(
        default=None,
        metadata={
            "name": "InvstmtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
        },
    )


@dataclass
class RequestForAccountManagementStatusReportV06Acmt00500106(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Acmt00500106] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
        },
    )
    req_dtls: Optional[AccountManagementMessageReference5Acmt00500106] = field(
        default=None,
        metadata={
            "name": "ReqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06",
            "required": True,
        },
    )


@dataclass
class Acmt00500106(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06"

    req_for_acct_mgmt_sts_rpt: Optional[
        RequestForAccountManagementStatusReportV06Acmt00500106
    ] = field(
        default=None,
        metadata={
            "name": "ReqForAcctMgmtStsRpt",
            "type": "Element",
            "required": True,
        },
    )
