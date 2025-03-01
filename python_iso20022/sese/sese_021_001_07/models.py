from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07"


@dataclass
class GenericIdentification30Sese02100107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese02100107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Identification30Sese02100107(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    mstr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bskt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BsktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    list_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ListId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrgmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese02100107(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese02100107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese02100107] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DocumentNumber5ChoiceSese02100107(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Sese02100107] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )


@dataclass
class PartyIdentification127ChoiceSese02100107(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese02100107] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )


@dataclass
class SecuritiesAccount22Sese02100107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese02100107] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Sese02100107(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese02100107] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "required": True,
        },
    )


@dataclass
class DocumentNumber20Sese02100107(ISO20022MessageElement):
    nb: Optional[DocumentNumber5ChoiceSese02100107] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "required": True,
        },
    )
    refs: list[Identification30Sese02100107] = field(
        default_factory=list,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "min_occurs": 1,
        },
    )


@dataclass
class PartyIdentification144Sese02100107(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese02100107] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SecuritiesTransactionStatusQueryV07Sese02100107(ISO20022MessageElement):
    sts_advc_reqd: Optional[DocumentNumber20Sese02100107] = field(
        default=None,
        metadata={
            "name": "StsAdvcReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese02100107] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount22Sese02100107] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese02100107] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )
    splmtry_data: list[SupplementaryData1Sese02100107] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07",
        },
    )


@dataclass
class Sese02100107(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.021.001.07"

    scties_tx_sts_qry: Optional[SecuritiesTransactionStatusQueryV07Sese02100107] = (
        field(
            default=None,
            metadata={
                "name": "SctiesTxStsQry",
                "type": "Element",
                "required": True,
            },
        )
    )
