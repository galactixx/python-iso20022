from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.enums import AddressType2Code
from python_iso20022.seev.enums import (
    BeneficiaryCertificationType1Code,
    PersonIdentificationType3Code,
    ProcessedStatus5Code,
)
from python_iso20022.seev.seev_024_001_01.enums import RejectionReason15Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01"


@dataclass
class ActiveCurrencyAndAmountSeev02400101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class AlternateSecurityIdentification3Seev02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification8Seev02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformationSeev02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BeneficiaryCertificationType1FormatChoiceSeev02400101:
    cd: Optional[BeneficiaryCertificationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class CashAccountIdentification1ChoiceSeev02400101:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformationSeev02400101] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class PersonIdentificationType3ChoiceSeev02400101:
    cd: Optional[PersonIdentificationType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class PostalAddress1Seev02400101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessedStatus5FormatChoiceSeev02400101:
    cd: Optional[ProcessedStatus5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class RejectionReason15FormatChoiceSeev02400101:
    cd: Optional[RejectionReason15Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev02400101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev02400101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class UnitOrFaceAmount1ChoiceSeev02400101:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountSeev02400101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class CorporateActionInformationProcessingStatus1Seev02400101:
    sts: Optional[ProcessedStatus5FormatChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionInformationRejectedStatus1Seev02400101:
    rsn: list[RejectionReason15FormatChoiceSeev02400101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification16Seev02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[PersonIdentificationType3ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress5Seev02400101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev02400101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class CorporateActionInformationStatus1ChoiceSeev02400101:
    prcd_sts: Optional[CorporateActionInformationProcessingStatus1Seev02400101] = field(
        default=None,
        metadata={
            "name": "PrcdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    rjctd_sts: Optional[CorporateActionInformationRejectedStatus1Seev02400101] = field(
        default=None,
        metadata={
            "name": "RjctdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev02400101:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev02400101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev02400101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class BeneficialOwner1Seev02400101:
    bnfcl_ownr_id: Optional[PartyIdentification2ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
        },
    )
    addtl_id: Optional[GenericIdentification16Seev02400101] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dmcl_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    non_dmcl_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    certfctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    certfctn_tp: Optional[BeneficiaryCertificationType1FormatChoiceSeev02400101] = (
        field(
            default=None,
            metadata={
                "name": "CertfctnTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            },
        )
    )
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    scty_id: Optional[SecurityIdentification7Seev02400101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    elctd_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "ElctdSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
        },
    )


@dataclass
class ProceedsDelivery1Seev02400101:
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_acct_id: Optional[CashAccountIdentification1ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    acct_svcr_id: Optional[PartyIdentification2ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "AcctSvcrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )


@dataclass
class CorporateActionAdditionalInformation1Seev02400101:
    bnfcl_ownr_dtls: list[BeneficialOwner1Seev02400101] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    rcvr_id: Optional[PartyIdentification2ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "RcvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    certfctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    certfctn_tp: Optional[BeneficiaryCertificationType1FormatChoiceSeev02400101] = (
        field(
            default=None,
            metadata={
                "name": "CertfctnTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            },
        )
    )
    dlvry_dtls: list[ProceedsDelivery1Seev02400101] = field(
        default_factory=list,
        metadata={
            "name": "DlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
        },
    )
    addtl_instr: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AgentCainformationStatusAdviceV01Seev02400101:
    class Meta:
        name = "AgentCAInformationStatusAdviceV01"

    id: Optional[DocumentIdentification8Seev02400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
        },
    )
    agt_cainf_advc_id: Optional[DocumentIdentification8Seev02400101] = field(
        default=None,
        metadata={
            "name": "AgtCAInfAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
        },
    )
    corp_actn_addtl_inf: Optional[CorporateActionAdditionalInformation1Seev02400101] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnAddtlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            },
        )
    )
    inf_sts_dtls: Optional[CorporateActionInformationStatus1ChoiceSeev02400101] = field(
        default=None,
        metadata={
            "name": "InfStsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01",
            "required": True,
        },
    )


@dataclass
class Seev02400101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.024.001.01"

    agt_cainf_sts_advc: Optional[AgentCainformationStatusAdviceV01Seev02400101] = field(
        default=None,
        metadata={
            "name": "AgtCAInfStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
