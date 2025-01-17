from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.acmt.enums import (
    BalanceTransferWindow1Code,
    SwitchStatus1Code,
    SwitchType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01"


@dataclass
class MessageIdentification1Acmt03600101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
        },
    )


@dataclass
class ResponseDetails1Acmt03600101:
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Acmt03600101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountSwitchDetails1Acmt03600101:
    unq_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rtg_unq_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtgUnqRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    swtch_rcvd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SwtchRcvdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
        },
    )
    swtch_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SwtchDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
        },
    )
    swtch_tp: Optional[SwitchType1Code] = field(
        default=None,
        metadata={
            "name": "SwtchTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
        },
    )
    swtch_sts: Optional[SwitchStatus1Code] = field(
        default=None,
        metadata={
            "name": "SwtchSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
        },
    )
    bal_trf_wndw: Optional[BalanceTransferWindow1Code] = field(
        default=None,
        metadata={
            "name": "BalTrfWndw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
        },
    )
    rspn: list[ResponseDetails1Acmt03600101] = field(
        default_factory=list,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
        },
    )


@dataclass
class SupplementaryData1Acmt03600101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Acmt03600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
        },
    )


@dataclass
class AccountSwitchTerminationSwitchV01Acmt03600101:
    msg_id: Optional[MessageIdentification1Acmt03600101] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
        },
    )
    acct_swtch_dtls: Optional[AccountSwitchDetails1Acmt03600101] = field(
        default=None,
        metadata={
            "name": "AcctSwtchDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Acmt03600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01",
        },
    )


@dataclass
class Acmt03600101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:acmt.036.001.01"

    acct_swtch_termntn_swtch: Optional[
        AccountSwitchTerminationSwitchV01Acmt03600101
    ] = field(
        default=None,
        metadata={
            "name": "AcctSwtchTermntnSwtch",
            "type": "Element",
            "required": True,
        },
    )
