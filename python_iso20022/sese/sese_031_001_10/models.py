from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AcknowledgementReason5Code,
    DeniedReason6Code,
    LinkageType1Code,
    NoReasonCode,
    PendingReason6Code,
    Registration2Code,
    RejectionReason71Code,
    SettlementTransactionCondition5Code,
)
from python_iso20022.sese.enums import (
    AutoBorrowing2Code,
    MatchingProcess1Code,
    ProcessingPosition4Code,
    RestrictionReference1Code,
    SecuritiesTransactionType5Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10"


@dataclass
class GenericIdentification30Sese03100110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese03100110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class References30Sese03100110(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )


@dataclass
class References81ChoiceSese03100110(ISO20022MessageElement):
    scties_sttlm_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intra_pos_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraPosMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intra_bal_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraBalMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trad_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    othr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Sese03100110(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class AutomaticBorrowing7ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[AutoBorrowing2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class BlockChainAddressWallet3Sese03100110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DeniedReason15ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[DeniedReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class DocumentNumber5ChoiceSese03100110(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Sese03100110] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class LinkageType3ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[LinkageType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class MatchingDenied3ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[MatchingProcess1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class PartyIdentification127ChoiceSese03100110(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese03100110] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class PendingReason28ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[PendingReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class PriorityNumeric4ChoiceSese03100110(ISO20022MessageElement):
    nmrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nmrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "pattern": r"[0-9]{4}",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class ProcessingPosition8ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[ProcessingPosition4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class ProprietaryReason4Sese03100110(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Registration10ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[Registration2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class RejectionAndRepairReason37ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[RejectionReason71Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class RestrictionIdentification1Sese03100110(ISO20022MessageElement):
    cd: Optional[RestrictionReference1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese03100110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesRtgs4ChoiceSese03100110(ISO20022MessageElement):
    class Meta:
        name = "SecuritiesRTGS4Choice"

    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class SupplementaryData1Sese03100110(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Sese03100110] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )


@dataclass
class UnilateralSplit3ChoiceSese03100110(ISO20022MessageElement):
    cd: Optional[SecuritiesTransactionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class AcknowledgementReason9Sese03100110(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason12ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class DeniedReason10Sese03100110(ISO20022MessageElement):
    cd: Optional[DeniedReason15ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Linkages74Sese03100110(ISO20022MessageElement):
    prcg_pos: Optional[ProcessingPosition8ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "PrcgPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    msg_nb: Optional[DocumentNumber5ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    ref: Optional[References81ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    ref_ownr: Optional[PartyIdentification127ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "RefOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class PartyIdentification144Sese03100110(ISO20022MessageElement):
    id: Optional[PartyIdentification127ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PendingReason16Sese03100110(ISO20022MessageElement):
    cd: Optional[PendingReason28ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Sese03100110(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Sese03100110] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class RegistrationReason5Sese03100110(ISO20022MessageElement):
    cd: Optional[Registration10ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionOrRepairReason37Sese03100110(ISO20022MessageElement):
    cd: Optional[RejectionAndRepairReason37ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus21ChoiceSese03100110(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    rsn: list[AcknowledgementReason9Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class DeniedStatus15ChoiceSese03100110(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    rsn: list[DeniedReason10Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class HoldIndicator6Sese03100110(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    rsn: list[RegistrationReason5Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class PendingStatus38ChoiceSese03100110(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    rsn: list[PendingReason16Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class RejectionOrRepairStatus42ChoiceSese03100110(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    rsn: list[RejectionOrRepairReason37Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class ProcessingStatus85ChoiceSese03100110(ISO20022MessageElement):
    ackd_accptd: Optional[AcknowledgedAcceptedStatus21ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    rjctd: Optional[RejectionOrRepairStatus42ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    cmpltd: Optional[ProprietaryReason4Sese03100110] = field(
        default=None,
        metadata={
            "name": "Cmpltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    dnd: Optional[DeniedStatus15ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Dnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    pdg: Optional[PendingStatus38ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Sese03100110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class RequestDetails32Sese03100110(ISO20022MessageElement):
    ref: Optional[References30Sese03100110] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    rstrctn_ref: list[RestrictionIdentification1Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "RstrctnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    automtc_brrwg: Optional[AutomaticBorrowing7ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "AutomtcBrrwg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    rtn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RtnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    lkg: Optional[LinkageType3ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Lkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prty: Optional[PriorityNumeric4ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    othr_prcg: list[GenericIdentification30Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "OthrPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prtl_sttlm_ind: Optional[SettlementTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    scties_rtgs: Optional[SecuritiesRtgs4ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "SctiesRTGS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    hld_ind: Optional[HoldIndicator6Sese03100110] = field(
        default=None,
        metadata={
            "name": "HldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    mtchg_dnl: Optional[MatchingDenied3ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "MtchgDnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    unltrl_splt: Optional[UnilateralSplit3ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "UnltrlSplt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    lnkgs: list[Linkages74Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "Lnkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class SecuritiesSettlementConditionModificationStatusAdviceV10Sese03100110(
    ISO20022MessageElement
):
    req_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification144Sese03100110] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese03100110] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Sese03100110] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    req_dtls: Optional[RequestDetails32Sese03100110] = field(
        default=None,
        metadata={
            "name": "ReqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )
    prcg_sts: Optional[ProcessingStatus85ChoiceSese03100110] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Sese03100110] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10",
        },
    )


@dataclass
class Sese03100110(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10"

    scties_sttlm_cond_mod_sts_advc: Optional[
        SecuritiesSettlementConditionModificationStatusAdviceV10Sese03100110
    ] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmCondModStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
