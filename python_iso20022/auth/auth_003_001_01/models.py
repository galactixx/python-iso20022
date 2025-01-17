from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01"


@dataclass
class SupplementaryDataEnvelope1Auth00300101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SupplementaryData1Auth00300101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth00300101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01",
            "required": True,
        },
    )


@dataclass
class InformationRequestStatusChangeNotificationV01Auth00300101:
    orgnl_biz_qry: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cnfdtlty_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CnfdtltySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth00300101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01",
        },
    )


@dataclass
class Auth00300101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01"

    inf_req_sts_chng_ntfctn: Optional[
        InformationRequestStatusChangeNotificationV01Auth00300101
    ] = field(
        default=None,
        metadata={
            "name": "InfReqStsChngNtfctn",
            "type": "Element",
            "required": True,
        },
    )
