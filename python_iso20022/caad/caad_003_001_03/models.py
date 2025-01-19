from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.caad.enums import (
    ClearingMethod2Code,
    PartyType23Code,
    UserInterface7Code,
)
from python_iso20022.enums import (
    Algorithm5Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm13Code,
    Algorithm20Code,
    Algorithm23Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    ContentType3Code,
    CreditDebit3Code,
    EncryptedDataFormat1Code,
    EncryptionFormat3Code,
    OutputFormat4Code,
    PartyType9Code,
    PartyType17Code,
    PartyType18Code,
    PartyType26Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03"


@dataclass
class AdditionalData1Caad00300103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class BatchManagementInformation1Caad00300103(ISO20022MessageElement):
    colltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,15}",
        },
    )
    msg_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EncryptedData2ChoiceCaad00300103(ISO20022MessageElement):
    binry: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    hex_binry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HexBinry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )


@dataclass
class Jurisdiction2Caad00300103(ISO20022MessageElement):
    dmst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    dmst_qlfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Caad00300103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Kekidentifier6Caad00300103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier6"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Macdata1Caad00300103(ISO20022MessageElement):
    class Meta:
        name = "MACData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    initlstn_vctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )


@dataclass
class Reconciliation4Caad00300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RecordMessage1ChoiceCaad00300103(ISO20022MessageElement):
    adddm_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AdddmInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    adddm_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AdddmRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    amdmnt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Amdmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    authstn_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthstnInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    authstn_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthstnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    card_mgmt_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "CardMgmtInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    card_mgmt_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "CardMgmtRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    chrg_bck_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ChrgBckInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    chrg_bck_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ChrgBckRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    err: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    fee_colltn_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FeeColltnInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    fee_colltn_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FeeColltnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    file_actn_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FileActnInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    file_actn_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FileActnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    fin_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FinInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    fin_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FinRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    frd_dspstn_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FrdDspstnInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    frd_dspstn_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FrdDspstnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    frd_rptg_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FrdRptgInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    frd_rptg_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "FrdRptgRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    nqry_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NqryInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    nqry_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NqryRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    key_xchg_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "KeyXchgInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    key_xchg_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "KeyXchgRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    ntwk_mgmt_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NtwkMgmtInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    ntwk_mgmt_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NtwkMgmtRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rcncltn_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RcncltnInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rcncltn_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RcncltnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rtrvl_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RtrvlInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rtrvl_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RtrvlRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rtrvl_flfmt_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RtrvlFlfmtInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rtrvl_flfmt_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RtrvlFlfmtRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rvsl_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RvslInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    rvsl_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RvslRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    sttlm_rptg_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SttlmRptgInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    sttlm_rptg_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SttlmRptgRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    vrfctn_initn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "VrfctnInitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )
    vrfctn_rspn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "VrfctnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 2097152,
            "format": "base64",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Caad00300103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AdditionalData2Caad00300103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[AdditionalData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class AdditionalInformation21Caad00300103(ISO20022MessageElement):
    rcpt: Optional[PartyType23Code] = field(
        default=None,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    trgt: list[UserInterface7Code] = field(
        default_factory=list,
        metadata={
            "name": "Trgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    frmt: Optional[OutputFormat4Code] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class AlgorithmIdentification26Caad00300103(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    param: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class ClearingBatchData3Caad00300103(ISO20022MessageElement):
    mtd: Optional[ClearingMethod2Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    othr_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    ttls_cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlsCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttls_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ttls_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlsCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    ttls_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "TtlsCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    intrchng_fee_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    intrchng_fee_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    intrchng_fee_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    agt_fee_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AgtFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    agt_fee_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgtFeeCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    agt_fee_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "AgtFeeCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class ClearingControlTotals3Caad00300103(ISO20022MessageElement):
    cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Cnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class ContentInformationType41Caad00300103(ISO20022MessageElement):
    macdata: Optional[Macdata1Caad00300103] = field(
        default=None,
        metadata={
            "name": "MACData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,8}",
        },
    )


@dataclass
class EncryptedDataElement2Caad00300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: Optional[EncryptedData2ChoiceCaad00300103] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    clear_txt_frmt: Optional[EncryptedDataFormat1Code] = field(
        default=None,
        metadata={
            "name": "ClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    othr_clear_txt_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification183Caad00300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LocalData14Caad00300103(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )
    addtl_data: list[AdditionalData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class OtherAmount5Caad00300103(ISO20022MessageElement):
    clr_cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ClrCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    clr_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ClrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    clr_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    clr_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "ClrCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    intrchng_fee_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    intrchng_fee_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    intrchng_fee_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    agt_fee_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AgtFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    agt_fee_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgtFeeCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    agt_fee_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "AgtFeeCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class Parameter14Caad00300103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat3Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class Parameter7Caad00300103(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class ProcessingResult26Caad00300103(ISO20022MessageElement):
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    addtl_inf: list[AdditionalData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class ProgrammeMode5Caad00300103(ISO20022MessageElement):
    apld_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApldId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class RelativeDistinguishedName1Caad00300103(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementService6Caad00300103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class SupplementaryData1Caad00300103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Caad00300103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )


@dataclass
class Traceability10Caad00300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class AlgorithmIdentification25Caad00300103(ISO20022MessageElement):
    algo: Optional[Algorithm23Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Caad00300103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class AlgorithmIdentification28Caad00300103(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter14Caad00300103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class CertificateIssuer1Caad00300103(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class EncryptedData2Caad00300103(ISO20022MessageElement):
    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_elmt: list[EncryptedDataElement2Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class Header71Caad00300103(ISO20022MessageElement):
    msg_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_trnsmssn_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    btch_mgmt_inf: Optional[BatchManagementInformation1Caad00300103] = field(
        default=None,
        metadata={
            "name": "BtchMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    initg_pty: Optional[GenericIdentification183Caad00300103] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification183Caad00300103] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    trac_data: list[AdditionalData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "TracData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    tracblt: list[Traceability10Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class Parameter13Caad00300103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm20Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification26Caad00300103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class PartyIdentification286Caad00300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "pattern": r"[0-9]{1,11}",
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    lcl_data: Optional[LocalData14Caad00300103] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class Record3Caad00300103(ISO20022MessageElement):
    seq_cntr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "RcrdChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    orgtr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgtrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgtr_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgtrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgtr_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgtrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    orgtr_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgtrShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    dstn_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstnShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clr_mtd: Optional[ClearingMethod2Code] = field(
        default=None,
        metadata={
            "name": "ClrMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    othr_clr_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClrMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clr_prty: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    clr_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ClrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    clr_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    clr_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "ClrCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    intrchng_fee_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    intrchng_fee_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    intrchng_fee_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "IntrchngFeeCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    agt_fee_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AgtFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    agt_fee_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgtFeeCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{3,3}",
        },
    )
    agt_fee_cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "AgtFeeCdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    othr_amt: Optional[OtherAmount5Caad00300103] = field(
        default=None,
        metadata={
            "name": "OthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    rcrd_msg: Optional[RecordMessage1ChoiceCaad00300103] = field(
        default=None,
        metadata={
            "name": "RcrdMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )


@dataclass
class AlgorithmIdentification27Caad00300103(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter13Caad00300103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class EncryptedContent8Caad00300103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification25Caad00300103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    ncrptd_data_elmt: list[EncryptedDataElement2Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdDataElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class IssuerAndSerialNumber1Caad00300103(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Caad00300103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek6Caad00300103(ISO20022MessageElement):
    class Meta:
        name = "KEK6"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier6Caad00300103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification28Caad00300103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Recipient5ChoiceCaad00300103(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caad00300103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Caad00300103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class KeyTransport6Caad00300103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaad00300103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification27Caad00300103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient7ChoiceCaad00300103(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport6Caad00300103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    kek: Optional[Kek6Caad00300103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    key_idr: Optional[Kekidentifier6Caad00300103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class EnvelopedData12Caad00300103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient7ChoiceCaad00300103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent8Caad00300103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class ProtectedData2Caad00300103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType3Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData12Caad00300103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    ncrptd_data: Optional[EncryptedData2Caad00300103] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class BatchTransferInitiationV03Caad00300103(ISO20022MessageElement):
    hdr: Optional[Header71Caad00300103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "required": True,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    orgnl_btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlBtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    nb_of_msgs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfMsgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    btch_chcksm: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "BtchChcksm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    req_ack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReqAck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    orgtr: Optional[PartyIdentification286Caad00300103] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    dstn: Optional[PartyIdentification286Caad00300103] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    prgrmm: list[ProgrammeMode5Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9]{1,12}",
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "length": 12,
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "length": 15,
        },
    )
    clr_btch_data: list[ClearingBatchData3Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "ClrBtchData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    clr_ctrl_ttls: Optional[ClearingControlTotals3Caad00300103] = field(
        default=None,
        metadata={
            "name": "ClrCtrlTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    agt_data: list[AdditionalInformation21Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "AgtData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    rcrd: list[Record3Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    jursdctn: Optional[Jurisdiction2Caad00300103] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    sttlm_svc: Optional[SettlementService6Caad00300103] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    rcncltn: Optional[Reconciliation4Caad00300103] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    orgnl_rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    prcg_rslt: Optional[ProcessingResult26Caad00300103] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    addtl_data: list[AdditionalData2Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    prtctd_data: list[ProtectedData2Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Caad00300103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType41Caad00300103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03",
        },
    )


@dataclass
class Caad00300103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caad.003.001.03"

    btch_trf_initn: Optional[BatchTransferInitiationV03Caad00300103] = field(
        default=None,
        metadata={
            "name": "BtchTrfInitn",
            "type": "Element",
            "required": True,
        },
    )
