from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    DistributionPolicy1Code,
    FormOfSecurity1Code,
    OrderOriginatorEligibility1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04"


@dataclass
class DateFormat42ChoiceSetr01800104(ISO20022MessageElement):
    yr_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YrMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    yr_mnth_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "YrMnthDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class Extension1Setr01800104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Setr01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource1ChoiceSetr01800104(ISO20022MessageElement):
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Setr01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
        },
    )


@dataclass
class SubAccount6Setr01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlternateSecurityIdentification7Setr01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSetr01800104] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Setr01800104(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Series1Setr01800104(ISO20022MessageElement):
    srs_dt: Optional[DateFormat42ChoiceSetr01800104] = field(
        default=None,
        metadata={
            "name": "SrsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    srs_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrsNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress5Setr01800104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr01800104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class SecurityIdentification25ChoiceSetr01800104(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Setr01800104] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class FinancialInstrument57Setr01800104(ISO20022MessageElement):
    id: Optional[SecurityIdentification25ChoiceSetr01800104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    srs_id: Optional[Series1Setr01800104] = field(
        default=None,
        metadata={
            "name": "SrsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class PartyIdentification90ChoiceSetr01800104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Setr01800104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Setr01800104] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class PartyIdentification113Setr01800104(ISO20022MessageElement):
    pty: Optional[PartyIdentification90ChoiceSetr01800104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class AdditionalReference8Setr01800104(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification113Setr01800104] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentAccount58Setr01800104(ISO20022MessageElement):
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_id: list[PartyIdentification113Setr01800104] = field(
        default_factory=list,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    acct_svcr: Optional[PartyIdentification113Setr01800104] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    sub_acct_dtls: Optional[SubAccount6Setr01800104] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class InvestmentFundOrder8Setr01800104(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    deal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount58Setr01800104] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument57Setr01800104] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class References62ChoiceSetr01800104(ISO20022MessageElement):
    prvs_ref: list[AdditionalReference8Setr01800104] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "max_occurs": 2,
        },
    )
    othr_ref: list[AdditionalReference8Setr01800104] = field(
        default_factory=list,
        metadata={
            "name": "OthrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "max_occurs": 2,
        },
    )


@dataclass
class MessageAndBusinessReference10Setr01800104(ISO20022MessageElement):
    ref: Optional[References62ChoiceSetr01800104] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    rltd_ref: Optional[AdditionalReference8Setr01800104] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )
    ordr_ref: list[InvestmentFundOrder8Setr01800104] = field(
        default_factory=list,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class RequestForOrderStatusReportV04Setr01800104(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Setr01800104] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "required": True,
        },
    )
    req_dtls: list[MessageAndBusinessReference10Setr01800104] = field(
        default_factory=list,
        metadata={
            "name": "ReqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
            "min_occurs": 1,
        },
    )
    xtnsn: list[Extension1Setr01800104] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04",
        },
    )


@dataclass
class Setr01800104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.018.001.04"

    req_for_ordr_sts_rpt: Optional[RequestForOrderStatusReportV04Setr01800104] = field(
        default=None,
        metadata={
            "name": "ReqForOrdrStsRpt",
            "type": "Element",
            "required": True,
        },
    )
