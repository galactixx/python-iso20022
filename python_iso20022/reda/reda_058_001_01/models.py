from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.enums import AddressType2Code, NoReasonCode

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01"


@dataclass
class EffectiveDate1Reda05800101:
    fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    fctv_dt_param: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDtParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class GenericIdentification1Reda05800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda05800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Reda05800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda05800101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcceptedReason7ChoiceReda05800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification36Reda05800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class AccountIdentification26Reda05800101:
    prtry: Optional[SimpleIdentificationInformation4Reda05800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )


@dataclass
class ClassificationType1ChoiceReda05800101:
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification1Reda05800101] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class PendingProcessingReason8ChoiceReda05800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification36Reda05800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class PostalAddress1Reda05800101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProprietaryReason1ChoiceReda05800101:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    rsn: list[GenericIdentification36Reda05800101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class Purpose3ChoiceReda05800101:
    scties_purp_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesPurpCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda05800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class ReceivedReason2ChoiceReda05800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification36Reda05800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class RejectedReason7ChoiceReda05800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification36Reda05800101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class SupplementaryData1Reda05800101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda05800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )


@dataclass
class AcceptedReason8ChoiceReda05800101:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    rsn: Optional[AcceptedReason7ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class MarketIdentification87Reda05800101:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    clssfctn_tp: Optional[ClassificationType1ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    sttlm_purp: Optional[Purpose3ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "SttlmPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class NameAndAddress5Reda05800101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda05800101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class PendingProcessingReason9ChoiceReda05800101:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    rsn: list[PendingProcessingReason8ChoiceReda05800101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class ProprietaryStatusAndReason5Reda05800101:
    sts: Optional[GenericIdentification36Reda05800101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    rsn: Optional[ProprietaryReason1ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ReceivedReason1ChoiceReda05800101:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    rsn: Optional[ReceivedReason2ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class RejectedReason8ChoiceReda05800101:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    rsn: list[RejectedReason7ChoiceReda05800101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class AcceptedStatusReason7Reda05800101:
    rsn: Optional[AcceptedReason8ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class MarketIdentificationOrCashPurpose1ChoiceReda05800101:
    sttlm_instr_mkt_id: Optional[MarketIdentification87Reda05800101] = field(
        default=None,
        metadata={
            "name": "SttlmInstrMktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    csh_ssipurp: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CshSSIPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class PartyIdentification75ChoiceReda05800101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda05800101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PendingProcessingStatusReason1Reda05800101:
    rsn: Optional[PendingProcessingReason9ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ReceivedStatusReason1Reda05800101:
    rsn: Optional[ReceivedReason1ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectedStatusReason12Reda05800101:
    rsn: Optional[RejectedReason8ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PartyIdentification63Reda05800101:
    pty_id: Optional[PartyIdentification75ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProcessingStatus43ChoiceReda05800101:
    rcvd: Optional[ReceivedStatusReason1Reda05800101] = field(
        default=None,
        metadata={
            "name": "Rcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    accptd: Optional[AcceptedStatusReason7Reda05800101] = field(
        default=None,
        metadata={
            "name": "Accptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    pdg_prcg: Optional[PendingProcessingStatusReason1Reda05800101] = field(
        default=None,
        metadata={
            "name": "PdgPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    rjctd: Optional[RejectedStatusReason12Reda05800101] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason5Reda05800101] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class PartyOrCurrency1ChoiceReda05800101:
    dpstry: Optional[PartyIdentification63Reda05800101] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class StandingSettlementInstructionStatusAdviceV01Reda05800101:
    fctv_dt_dtls: Optional[EffectiveDate1Reda05800101] = field(
        default=None,
        metadata={
            "name": "FctvDtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )
    acct_id: list[AccountIdentification26Reda05800101] = field(
        default_factory=list,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "min_occurs": 1,
        },
    )
    mkt_id: Optional[MarketIdentificationOrCashPurpose1ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "MktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    sttlm_dtls: Optional[PartyOrCurrency1ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "SttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    rltd_msg_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdMsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_sts: Optional[ProcessingStatus43ChoiceReda05800101] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda05800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
        },
    )


@dataclass
class Reda05800101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01"

    stg_sttlm_instr_sts_advc: Optional[
        StandingSettlementInstructionStatusAdviceV01Reda05800101
    ] = field(
        default=None,
        metadata={
            "name": "StgSttlmInstrStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
