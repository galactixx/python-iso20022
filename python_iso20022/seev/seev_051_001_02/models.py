from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import SafekeepingPlace1Code, SafekeepingPlace2Code
from python_iso20022.seev.enums import CorporateActionEventType39Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02"


@dataclass
class DocumentIdentification9Seev05100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Seev05100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev05100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev05100102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class References26Seev05100102(ISO20022MessageElement):
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev05100102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CorporateActionEventType111ChoiceSeev05100102(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType39Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Seev05100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )


@dataclass
class GenericIdentification78Seev05100102(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev05100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherIdentification1Seev05100102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev05100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev05100102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev05100102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev05100102(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev05100102(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Seev05100102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev05100102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev05100102(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev05100102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev05100102] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )
    prtry: Optional[GenericIdentification78Seev05100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )


@dataclass
class SecurityIdentification19Seev05100102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev05100102] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AccountIdentification70Seev05100102(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev05100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev05100102] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )


@dataclass
class CorporateActionGeneralInformation181Seev05100102(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType111ChoiceSeev05100102] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev05100102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )


@dataclass
class MarketClaimCancellationRequestV02Seev05100102(ISO20022MessageElement):
    mkt_clm_cre_id: Optional[DocumentIdentification9Seev05100102] = field(
        default=None,
        metadata={
            "name": "MktClmCreId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )
    tx_ref: Optional[References26Seev05100102] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation181Seev05100102] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountIdentification70Seev05100102] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Seev05100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02",
        },
    )


@dataclass
class Seev05100102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02"

    mkt_clm_cxl_req: Optional[MarketClaimCancellationRequestV02Seev05100102] = field(
        default=None,
        metadata={
            "name": "MktClmCxlReq",
            "type": "Element",
            "required": True,
        },
    )
