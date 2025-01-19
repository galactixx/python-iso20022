from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code
from python_iso20022.seev.enums import (
    CorporateActionEventType2Code,
    ProcessedStatus3Code,
    StandingInstructionType1Code,
)
from python_iso20022.seev.seev_027_001_01.enums import (
    ProcessedStatus4Code,
    RejectionReason10Code,
    RejectionReason20Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01"


@dataclass
class AlternateSecurityIdentification3Seev02700101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification8Seev02700101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev02700101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev02700101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IncludedAccount1Seev02700101(ISO20022MessageElement):
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev02700101(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class PostalAddress1Seev02700101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessedStatus3FormatChoiceSeev02700101(ISO20022MessageElement):
    cd: Optional[ProcessedStatus3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class ProcessedStatus4FormatChoiceSeev02700101(ISO20022MessageElement):
    cd: Optional[ProcessedStatus4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class RejectionReason10FormatChoiceSeev02700101(ISO20022MessageElement):
    cd: Optional[RejectionReason10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class RejectionReason20FormatChoiceSeev02700101(ISO20022MessageElement):
    cd: Optional[RejectionReason20Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev02700101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev02700101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CorporateActionStandingInstructionCancellationProcessingStatus1Seev02700101(
    ISO20022MessageElement
):
    sts: Optional[ProcessedStatus4FormatChoiceSeev02700101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionStandingInstructionCancellationRejectionStatus1Seev02700101(
    ISO20022MessageElement
):
    rsn: list[RejectionReason10FormatChoiceSeev02700101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionStandingInstructionProcessingStatus1Seev02700101(
    ISO20022MessageElement
):
    sts: Optional[ProcessedStatus3FormatChoiceSeev02700101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionStandingInstructionRejectionStatus1Seev02700101(
    ISO20022MessageElement
):
    rsn: list[RejectionReason20FormatChoiceSeev02700101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NameAndAddress5Seev02700101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev02700101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev02700101(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev02700101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev02700101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class StandingInstructionCancellationStatus1ChoiceSeev02700101(ISO20022MessageElement):
    prcd_sts: Optional[
        CorporateActionStandingInstructionCancellationProcessingStatus1Seev02700101
    ] = field(
        default=None,
        metadata={
            "name": "PrcdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    rjctd_sts: Optional[
        CorporateActionStandingInstructionCancellationRejectionStatus1Seev02700101
    ] = field(
        default=None,
        metadata={
            "name": "RjctdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class StandingInstructionStatus1ChoiceSeev02700101(ISO20022MessageElement):
    prcd_sts: Optional[
        CorporateActionStandingInstructionProcessingStatus1Seev02700101
    ] = field(
        default=None,
        metadata={
            "name": "PrcdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    rjctd_sts: Optional[
        CorporateActionStandingInstructionRejectionStatus1Seev02700101
    ] = field(
        default=None,
        metadata={
            "name": "RjctdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev02700101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev02700101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev02700101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class CorporateActionStandingInstructionGeneralInformation1Seev02700101(
    ISO20022MessageElement
):
    stg_instr_tp: Optional[StandingInstructionType1Code] = field(
        default=None,
        metadata={
            "name": "StgInstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )
    evt_tp: list[CorporateActionEventType2FormatChoiceSeev02700101] = field(
        default_factory=list,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    instg_pty_id: Optional[PartyIdentification2ChoiceSeev02700101] = field(
        default=None,
        metadata={
            "name": "InstgPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )
    clnt_stg_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntStgInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dtls: list[IncludedAccount1Seev02700101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev02700101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class AgentCastandingInstructionStatusAdviceV01Seev02700101(ISO20022MessageElement):
    class Meta:
        name = "AgentCAStandingInstructionStatusAdviceV01"

    id: Optional[DocumentIdentification8Seev02700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )
    agt_castg_instr_req_id: Optional[DocumentIdentification8Seev02700101] = field(
        default=None,
        metadata={
            "name": "AgtCAStgInstrReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    agt_castg_instr_cxl_req_id: Optional[DocumentIdentification8Seev02700101] = field(
        default=None,
        metadata={
            "name": "AgtCAStgInstrCxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    stg_instr_gnl_inf: Optional[
        CorporateActionStandingInstructionGeneralInformation1Seev02700101
    ] = field(
        default=None,
        metadata={
            "name": "StgInstrGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
            "required": True,
        },
    )
    stg_instr_req_sts: Optional[StandingInstructionStatus1ChoiceSeev02700101] = field(
        default=None,
        metadata={
            "name": "StgInstrReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )
    stg_instr_cxl_req_sts: Optional[
        StandingInstructionCancellationStatus1ChoiceSeev02700101
    ] = field(
        default=None,
        metadata={
            "name": "StgInstrCxlReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01",
        },
    )


@dataclass
class Seev02700101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01"

    agt_castg_instr_sts_advc: Optional[
        AgentCastandingInstructionStatusAdviceV01Seev02700101
    ] = field(
        default=None,
        metadata={
            "name": "AgtCAStgInstrStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
