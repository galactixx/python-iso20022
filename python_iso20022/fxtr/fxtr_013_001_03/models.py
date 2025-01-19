from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.fxtr.fxtr_013_001_03.enums import WithdrawalReason1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03"


@dataclass
class SupplementaryDataEnvelope1Fxtr01300103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SupplementaryData1Fxtr01300103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Fxtr01300103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
            "required": True,
        },
    )


@dataclass
class WithdrawalReason1Fxtr01300103(ISO20022MessageElement):
    wdrwl_rsn_cd: Optional[WithdrawalReason1Code] = field(
        default=None,
        metadata={
            "name": "WdrwlRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
            "required": True,
        },
    )
    wdrwl_rsn_sub_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "WdrwlRsnSubCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class ForeignExchangeTradeWithdrawalNotificationV03Fxtr01300103(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mtchg_sys_unq_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtchgSysUnqRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    wdrwl_rsn: Optional[WithdrawalReason1Fxtr01300103] = field(
        default=None,
        metadata={
            "name": "WdrwlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
        },
    )
    sttlm_ssn_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmSsnIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    splmtry_data: list[SupplementaryData1Fxtr01300103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03",
        },
    )


@dataclass
class Fxtr01300103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03"

    fxtrad_wdrwl_ntfctn: Optional[
        ForeignExchangeTradeWithdrawalNotificationV03Fxtr01300103
    ] = field(
        default=None,
        metadata={
            "name": "FXTradWdrwlNtfctn",
            "type": "Element",
            "required": True,
        },
    )
