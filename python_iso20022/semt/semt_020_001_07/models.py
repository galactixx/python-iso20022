from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.enums import DeliveryReceiptType2Code, ReceiveDelivery1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07"


@dataclass
class GenericIdentification30Semt02000107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt02000107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt02000107:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BlockChainAddressWallet3Semt02000107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt02000107] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt02000107:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt02000107] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )


@dataclass
class SecuritiesAccount19Semt02000107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt02000107] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SettlementTypeAndIdentification18Semt02000107:
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Semt02000107:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt02000107] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
        },
    )


@dataclass
class PartyIdentification144Semt02000107:
    id: Optional[PartyIdentification127ChoiceSemt02000107] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class References69ChoiceSemt02000107:
    scties_sttlm_tx_conf_id: Optional[SettlementTypeAndIdentification18Semt02000107] = (
        field(
            default=None,
            metadata={
                "name": "SctiesSttlmTxConfId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            },
        )
    )
    intra_pos_mvmnt_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraPosMvmntConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_bal_acctg_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesBalAcctgRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_bal_ctdy_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesBalCtdyRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intra_pos_mvmnt_pstng_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraPosMvmntPstngRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_fincg_conf_id: Optional[SettlementTypeAndIdentification18Semt02000107] = (
        field(
            default=None,
            metadata={
                "name": "SctiesFincgConfId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            },
        )
    )
    scties_tx_pdg_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesTxPdgRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_tx_pstng_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesTxPstngRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_sttlm_tx_allgmt_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxAllgmtRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_sttlm_tx_allgmt_ntfctn_tx_id: Optional[
        SettlementTypeAndIdentification18Semt02000107
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxAllgmtNtfctnTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )
    prtfl_trf_ntfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtflTrfNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_sttlm_tx_gnrtn_ntfctn_id: Optional[
        SettlementTypeAndIdentification18Semt02000107
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxGnrtnNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )
    othr_msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_prtfl_valtn_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlPrtflValtnRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_coll_tx_instr_prcg_sts_advc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyCollTxInstrPrcgStsAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_coll_sts_advc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyCollStsAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_coll_and_xpsr_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyCollAndXpsrRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesMessageCancellationAdviceV07Semt02000107:
    ref: Optional[References69ChoiceSemt02000107] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Semt02000107] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Semt02000107] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt02000107] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )
    splmtry_data: list[SupplementaryData1Semt02000107] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07",
        },
    )


@dataclass
class Semt02000107:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.020.001.07"

    scties_msg_cxl_advc: Optional[
        SecuritiesMessageCancellationAdviceV07Semt02000107
    ] = field(
        default=None,
        metadata={
            "name": "SctiesMsgCxlAdvc",
            "type": "Element",
            "required": True,
        },
    )
