from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AcknowledgementReason3Code, NoReasonCode
from python_iso20022.sese.enums import RejectionReason77Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06"


@dataclass
class GenericIdentification30Sese02200106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese02200106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Identification28Sese02200106(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 52,
        },
    )
    mstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bskt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BsktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrgmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese02200106(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcknowledgementReason15ChoiceSese02200106(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Sese02200106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese02200106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese02200106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DocumentNumber5ChoiceSese02200106(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Sese02200106] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class PartyIdentification127ChoiceSese02200106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02200106] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class ProprietaryReason4Sese02200106(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Sese02200106] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionAndRepairReason39ChoiceSese02200106(ISO20022MessageElement):
    cd: Optional[RejectionReason77Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Sese02200106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class SecuritiesAccount19Sese02200106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese02200106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Sese02200106(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese02200106] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )


@dataclass
class AcknowledgementReason12Sese02200106(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason15ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class DocumentIdentification54Sese02200106(ISO20022MessageElement):
    msg_nb: Optional[DocumentNumber5ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentNumber13Sese02200106(ISO20022MessageElement):
    nb: Optional[DocumentNumber5ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )


@dataclass
class DocumentNumber18Sese02200106(ISO20022MessageElement):
    nb: Optional[DocumentNumber5ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )
    refs: list[Identification28Sese02200106] = field(
        default_factory=list,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_occurs": 1,
        },
    )


@dataclass
class PartyIdentification144Sese02200106(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class ProprietaryStatusAndReason6Sese02200106(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Sese02200106] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Sese02200106] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class RejectionOrRepairReason39Sese02200106(ISO20022MessageElement):
    cd: Optional[RejectionAndRepairReason39ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus24ChoiceSese02200106(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    rsn: list[AcknowledgementReason12Sese02200106] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class RejectionOrRepairStatus44ChoiceSese02200106(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    rsn: list[RejectionOrRepairReason39Sese02200106] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class StatusOrStatement11ChoiceSese02200106(ISO20022MessageElement):
    sts_advc: Optional[DocumentNumber18Sese02200106] = field(
        default=None,
        metadata={
            "name": "StsAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    stmt: Optional[DocumentNumber13Sese02200106] = field(
        default=None,
        metadata={
            "name": "Stmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class ProcessingStatus89ChoiceSese02200106(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus24ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    rjctd: Optional[RejectionOrRepairStatus44ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese02200106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class SecuritiesStatusOrStatementQueryStatusAdviceV06Sese02200106(
    ISO20022MessageElement
):
    qry_dtls: Optional[DocumentIdentification54Sese02200106] = field(
        default=None,
        metadata={
            "name": "QryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese02200106] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese02200106] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese02200106] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    sts_or_stmt_reqd: Optional[StatusOrStatement11ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "StsOrStmtReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )
    prcg_sts: Optional[ProcessingStatus89ChoiceSese02200106] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Sese02200106] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06",
        },
    )


@dataclass
class Sese02200106(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.022.001.06"

    scties_sts_or_stmt_qry_sts_advc: Optional[
        SecuritiesStatusOrStatementQueryStatusAdviceV06Sese02200106
    ] = field(
        default=None,
        metadata={
            "name": "SctiesStsOrStmtQryStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
