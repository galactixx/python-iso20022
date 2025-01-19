from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, NamePrefix1Code
from python_iso20022.seev.enums import (
    CorporateActionEventType2Code,
    StandingInstructionGrossNet1Code,
    StandingInstructionType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01"


@dataclass
class AlternateSecurityIdentification3Seev02500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification8Seev02500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev02500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev02500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IncludedAccount1Seev02500101(ISO20022MessageElement):
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    incl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InclInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationSeev02500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountIdentification1ChoiceSeev02500101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformationSeev02500101] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class ContactIdentification4Seev02500101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev02500101(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class PostalAddress1Seev02500101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecurityIdentification7Seev02500101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev02500101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class NameAndAddress5Seev02500101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev02500101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev02500101(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev02500101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev02500101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class CashAccount17Seev02500101(ISO20022MessageElement):
    acct_id: Optional[CashAccountIdentification1ChoiceSeev02500101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    pmt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev02500101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    crspdt_bk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrspdtBkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class ContactPerson1Seev02500101(ISO20022MessageElement):
    ctct_prsn: Optional[ContactIdentification4Seev02500101] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    instn_id: Optional[PartyIdentification2ChoiceSeev02500101] = field(
        default=None,
        metadata={
            "name": "InstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev02500101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev02500101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev02500101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class SecuritiesAccount6Seev02500101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev02500101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev02500101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev02500101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionStandingInstruction1Seev02500101(ISO20022MessageElement):
    net_or_grss: Optional[StandingInstructionGrossNet1Code] = field(
        default=None,
        metadata={
            "name": "NetOrGrss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    csh_dstrbtn_dtls: Optional[CashAccount17Seev02500101] = field(
        default=None,
        metadata={
            "name": "CshDstrbtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    scties_dstrbtn_dtls: Optional[SecuritiesAccount6Seev02500101] = field(
        default=None,
        metadata={
            "name": "SctiesDstrbtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionStandingInstructionGeneralInformation1Seev02500101(
    ISO20022MessageElement
):
    stg_instr_tp: Optional[StandingInstructionType1Code] = field(
        default=None,
        metadata={
            "name": "StgInstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    evt_tp: list[CorporateActionEventType2FormatChoiceSeev02500101] = field(
        default_factory=list,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    instg_pty_id: Optional[PartyIdentification2ChoiceSeev02500101] = field(
        default=None,
        metadata={
            "name": "InstgPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    clnt_stg_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntStgInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dtls: list[IncludedAccount1Seev02500101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev02500101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class AgentCastandingInstructionRequestV01Seev02500101(ISO20022MessageElement):
    class Meta:
        name = "AgentCAStandingInstructionRequestV01"

    id: Optional[DocumentIdentification8Seev02500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    stg_instr_gnl_inf: Optional[
        CorporateActionStandingInstructionGeneralInformation1Seev02500101
    ] = field(
        default=None,
        metadata={
            "name": "StgInstrGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    stg_instr_dtls: Optional[CorporateActionStandingInstruction1Seev02500101] = field(
        default=None,
        metadata={
            "name": "StgInstrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
            "required": True,
        },
    )
    ctct_dtls: Optional[ContactPerson1Seev02500101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01",
        },
    )


@dataclass
class Seev02500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01"

    agt_castg_instr_req: Optional[AgentCastandingInstructionRequestV01Seev02500101] = (
        field(
            default=None,
            metadata={
                "name": "AgtCAStgInstrReq",
                "type": "Element",
                "required": True,
            },
        )
    )
