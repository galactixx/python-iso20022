from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01"


@dataclass
class DateAndDateTime2ChoiceReda04500101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class GenericIdentification30Reda04500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda04500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceReda04500101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Reda04500101:
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda04500101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BlockChainAddressWallet3Reda04500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Reda04500101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class OtherIdentification1Reda04500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Reda04500101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecuritiesAccount19Reda04500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda04500101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Reda04500101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda04500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )


@dataclass
class IssuanceAccount3Reda04500101:
    issnc_acct: Optional[SecuritiesAccount19Reda04500101] = field(
        default=None,
        metadata={
            "name": "IssncAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    issnc_blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Reda04500101] = (
        field(
            default=None,
            metadata={
                "name": "IssncBlckChainAdrOrWllt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            },
        )
    )
    pmry_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmryAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Reda04500101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda04500101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class SecurityIdentification19Reda04500101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Reda04500101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PartyIdentification120ChoiceReda04500101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda04500101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda04500101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class PartyIdentification136Reda04500101:
    id: Optional[PartyIdentification120ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SystemPartyIdentification8Reda04500101:
    id: Optional[PartyIdentification136Reda04500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda04500101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class SystemPartyIdentification2ChoiceReda04500101:
    org_id: Optional[PartyIdentification136Reda04500101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    cmbnd_id: Optional[SystemPartyIdentification8Reda04500101] = field(
        default=None,
        metadata={
            "name": "CmbndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class IssuerOrInvestor2ChoiceReda04500101:
    issr_csd: Optional[SystemPartyIdentification2ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "IssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    invstr_csd: Optional[SystemPartyIdentification2ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "InvstrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class SecurityCsdlink12Reda04500101:
    class Meta:
        name = "SecurityCSDLink12"

    fin_instrm_id: Optional[SecurityIdentification19Reda04500101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )
    issr_invstr_csd: Optional[IssuerOrInvestor2ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "IssrInvstrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )
    tech_issr_csd: Optional[SystemPartyIdentification2ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "TechIssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    scty_mntnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctyMntnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )
    issnc_acct: list[IssuanceAccount3Reda04500101] = field(
        default_factory=list,
        metadata={
            "name": "IssncAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    dflt_lk: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DfltLk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    vld_fr: Optional[DateAndDateTime2ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "required": True,
        },
    )
    vld_to: Optional[DateAndDateTime2ChoiceReda04500101] = field(
        default=None,
        metadata={
            "name": "VldTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class SecurityCsdlinkCreationRequestV01Reda04500101:
    class Meta:
        name = "SecurityCSDLinkCreationRequestV01"

    msg_hdr: Optional[MessageHeader1Reda04500101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )
    scty_csdlk: list[SecurityCsdlink12Reda04500101] = field(
        default_factory=list,
        metadata={
            "name": "SctyCSDLk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Reda04500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01",
        },
    )


@dataclass
class Reda04500101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.045.001.01"

    scty_csdlk_cre_req: Optional[SecurityCsdlinkCreationRequestV01Reda04500101] = field(
        default=None,
        metadata={
            "name": "SctyCSDLkCreReq",
            "type": "Element",
            "required": True,
        },
    )
