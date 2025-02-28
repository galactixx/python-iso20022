from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    DateType8Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
)
from python_iso20022.seev.enums import (
    AdditionalBusinessProcess8Code,
    CorporateActionCancellationReason1Code,
    CorporateActionEventStage4Code,
    CorporateActionEventType35Code,
    CorporateActionMandatoryVoluntary1Code,
    EventCompletenessStatus1Code,
    EventConfirmationStatus1Code,
    LotteryType1Code,
    SafekeepingAccountIdentification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13"


@dataclass
class GenericIdentification47Seev03900213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Seev03900213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 34,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSeev03900213(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class NameAndAddress12Seev03900213(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03900213(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification10Seev03900213(ISO20022MessageElement):
    id_cd: Optional[SafekeepingAccountIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )


@dataclass
class AdditionalBusinessProcessFormat16ChoiceSeev03900213(ISO20022MessageElement):
    cd: Optional[AdditionalBusinessProcess8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03900213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class CorporateActionEventStageFormat15ChoiceSeev03900213(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03900213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class CorporateActionEventStatus1Seev03900213(ISO20022MessageElement):
    evt_cmpltns_sts: Optional[EventCompletenessStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtCmpltnsSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    evt_conf_sts: Optional[EventConfirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "EvtConfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )


@dataclass
class CorporateActionEventType113ChoiceSeev03900213(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType35Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03900213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary4ChoiceSeev03900213(ISO20022MessageElement):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03900213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class DateCode22ChoiceSeev03900213(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03900213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class GenericIdentification85Seev03900213(ISO20022MessageElement):
    tp: Optional[GenericIdentification47Seev03900213] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class LotteryTypeFormat5ChoiceSeev03900213(ISO20022MessageElement):
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    prtry: Optional[GenericIdentification47Seev03900213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class OtherIdentification2Seev03900213(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 31,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,31}",
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSeev03900213(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03900213] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class PartyIdentification137ChoiceSeev03900213(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Seev03900213] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Seev03900213] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03900213(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText9Seev03900213(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SupplementaryData1Seev03900213(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03900213] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )


@dataclass
class CorporateActionCancellation4Seev03900213(ISO20022MessageElement):
    cxl_rsn_cd: Optional[CorporateActionCancellationReason1Code] = field(
        default=None,
        metadata={
            "name": "CxlRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    cxl_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    prcg_sts: Optional[CorporateActionEventStatus1Seev03900213] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )


@dataclass
class DateFormat41ChoiceSeev03900213(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    dt_cd: Optional[DateCode22ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class SafekeepingPlaceFormat57ChoiceSeev03900213(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText9Seev03900213] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03900213] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    prtry: Optional[GenericIdentification85Seev03900213] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class SecurityIdentification20Seev03900213(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Seev03900213] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class AccountIdentification72Seev03900213(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    acct_ownr: Optional[PartyIdentification136ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat57ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class CorporateActionDate89Seev03900213(ISO20022MessageElement):
    rcrd_dt: Optional[DateFormat41ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    ex_dvdd_dt: Optional[DateFormat41ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class CorporateActionGeneralInformation184Seev03900213(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    evt_tp: Optional[CorporateActionEventType113ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary4ChoiceSeev03900213
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification20Seev03900213] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )


@dataclass
class AccountIdentification74ChoiceSeev03900213(ISO20022MessageElement):
    for_all_accts: Optional[AccountIdentification10Seev03900213] = field(
        default=None,
        metadata={
            "name": "ForAllAccts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    accts_list: list[AccountIdentification72Seev03900213] = field(
        default_factory=list,
        metadata={
            "name": "AcctsList",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class CorporateAction74Seev03900213(ISO20022MessageElement):
    dt_dtls: Optional[CorporateActionDate89Seev03900213] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    evt_stag: Optional[CorporateActionEventStageFormat15ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    addtl_biz_prc_ind: list[AdditionalBusinessProcessFormat16ChoiceSeev03900213] = (
        field(
            default_factory=list,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            },
        )
    )
    ltry_tp: Optional[LotteryTypeFormat5ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class CorporateActionCancellationAdvice002V13Seev03900213(ISO20022MessageElement):
    cxl_advc_gnl_inf: Optional[CorporateActionCancellation4Seev03900213] = field(
        default=None,
        metadata={
            "name": "CxlAdvcGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation184Seev03900213] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
                "required": True,
            },
        )
    )
    accts_dtls: Optional[AccountIdentification74ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "AcctsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction74Seev03900213] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
            "min_length": 1,
            "max_length": 8000,
            "pattern": r'[0-9a-zA-Z!"%&\*;<> \.,\(\)\n\r/=\'\+:\?@#\{\-_]{1,8000}',
        },
    )
    issr_agt: list[PartyIdentification137ChoiceSeev03900213] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    png_agt: list[PartyIdentification137ChoiceSeev03900213] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    sub_png_agt: list[PartyIdentification137ChoiceSeev03900213] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    regar: Optional[PartyIdentification137ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "Regar",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    rsellng_agt: list[PartyIdentification137ChoiceSeev03900213] = field(
        default_factory=list,
        metadata={
            "name": "RsellngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    phys_scties_agt: Optional[PartyIdentification137ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "PhysSctiesAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    drp_agt: Optional[PartyIdentification137ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "DrpAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    slctn_agt: list[PartyIdentification137ChoiceSeev03900213] = field(
        default_factory=list,
        metadata={
            "name": "SlctnAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    inf_agt: Optional[PartyIdentification137ChoiceSeev03900213] = field(
        default=None,
        metadata={
            "name": "InfAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03900213] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13",
        },
    )


@dataclass
class Seev03900213(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.039.002.13"

    corp_actn_cxl_advc: Optional[
        CorporateActionCancellationAdvice002V13Seev03900213
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnCxlAdvc",
            "type": "Element",
            "required": True,
        },
    )
