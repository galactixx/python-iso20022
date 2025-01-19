from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code
from python_iso20022.seev.enums import (
    CorporateActionEventProcessingType1Code,
    CorporateActionEventType2Code,
    CorporateActionMandatoryVoluntary1Code,
    ProcessedStatus3Code,
    ProcessedStatus5Code,
)
from python_iso20022.seev.seev_015_001_01.enums import (
    RejectionReason8Code,
    RejectionReason9Code,
    RejectionReason18Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01"


@dataclass
class AlternateSecurityIdentification3Seev01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification8Seev01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionEventProcessingType1FormatChoiceSeev01500101(
    ISO20022MessageElement
):
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev01500101(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary1FormatChoiceSeev01500101(
    ISO20022MessageElement
):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class PostalAddress1Seev01500101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessedStatus3FormatChoiceSeev01500101(ISO20022MessageElement):
    cd: Optional[ProcessedStatus3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class ProcessedStatus5FormatChoiceSeev01500101(ISO20022MessageElement):
    cd: Optional[ProcessedStatus5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class RejectionReason18FormatChoiceSeev01500101(ISO20022MessageElement):
    cd: Optional[RejectionReason18Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class RejectionReason8FormatChoiceSeev01500101(ISO20022MessageElement):
    cd: Optional[RejectionReason8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class RejectionReason9FormatChoiceSeev01500101(ISO20022MessageElement):
    cd: Optional[RejectionReason9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev01500101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev01500101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CorporateActionAmendmentProcessingStatus1Seev01500101(ISO20022MessageElement):
    sts: Optional[ProcessedStatus5FormatChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionAmendmentRejectionStatus1Seev01500101(ISO20022MessageElement):
    rsn: list[RejectionReason8FormatChoiceSeev01500101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionCancellationProcessingStatus1Seev01500101(ISO20022MessageElement):
    sts: Optional[ProcessedStatus5FormatChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionCancellationRejectionStatus1Seev01500101(ISO20022MessageElement):
    rsn: list[RejectionReason9FormatChoiceSeev01500101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionInstructionProcessingStatus1Seev01500101(ISO20022MessageElement):
    sts: Optional[ProcessedStatus3FormatChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionInstructionRejectionStatus1Seev01500101(ISO20022MessageElement):
    rsn: list[RejectionReason18FormatChoiceSeev01500101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NameAndAddress5Seev01500101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev01500101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class ElectionAdviceStatus1ChoiceSeev01500101(ISO20022MessageElement):
    prcd_sts: Optional[CorporateActionInstructionProcessingStatus1Seev01500101] = field(
        default=None,
        metadata={
            "name": "PrcdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    rjctd_sts: Optional[CorporateActionInstructionRejectionStatus1Seev01500101] = field(
        default=None,
        metadata={
            "name": "RjctdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class ElectionAmendmentStatus1ChoiceSeev01500101(ISO20022MessageElement):
    prcd_sts: Optional[CorporateActionAmendmentProcessingStatus1Seev01500101] = field(
        default=None,
        metadata={
            "name": "PrcdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    rjctd_sts: Optional[CorporateActionAmendmentRejectionStatus1Seev01500101] = field(
        default=None,
        metadata={
            "name": "RjctdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class ElectionCancellationStatus1ChoiceSeev01500101(ISO20022MessageElement):
    prcd_sts: Optional[CorporateActionCancellationProcessingStatus1Seev01500101] = (
        field(
            default=None,
            metadata={
                "name": "PrcdSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            },
        )
    )
    rjctd_sts: Optional[CorporateActionCancellationRejectionStatus1Seev01500101] = (
        field(
            default=None,
            metadata={
                "name": "RjctdSts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            },
        )
    )


@dataclass
class PartyIdentification2ChoiceSeev01500101(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev01500101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev01500101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev01500101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev01500101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class CorporateActionInformation1Seev01500101(ISO20022MessageElement):
    agt_id: Optional[PartyIdentification2ChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    issr_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnPrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType2FormatChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary1FormatChoiceSeev01500101
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    evt_prcg_tp: Optional[
        CorporateActionEventProcessingType1FormatChoiceSeev01500101
    ] = field(
        default=None,
        metadata={
            "name": "EvtPrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev01500101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )


@dataclass
class AgentCaelectionStatusAdviceV01Seev01500101(ISO20022MessageElement):
    class Meta:
        name = "AgentCAElectionStatusAdviceV01"

    id: Optional[DocumentIdentification8Seev01500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    agt_caelctn_advc_id: Optional[DocumentIdentification8Seev01500101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    agt_caelctn_cxl_req_id: Optional[DocumentIdentification8Seev01500101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnCxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    agt_caelctn_amdmnt_req_id: Optional[DocumentIdentification8Seev01500101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnAmdmntReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionInformation1Seev01500101] = field(
        default=None,
        metadata={
            "name": "CorpActnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
            "required": True,
        },
    )
    elctn_advc_sts: Optional[ElectionAdviceStatus1ChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "ElctnAdvcSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    elctn_cxl_req_sts: Optional[ElectionCancellationStatus1ChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "ElctnCxlReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )
    elctn_amdmnt_req_sts: Optional[ElectionAmendmentStatus1ChoiceSeev01500101] = field(
        default=None,
        metadata={
            "name": "ElctnAmdmntReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01",
        },
    )


@dataclass
class Seev01500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01"

    agt_caelctn_sts_advc: Optional[AgentCaelectionStatusAdviceV01Seev01500101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
