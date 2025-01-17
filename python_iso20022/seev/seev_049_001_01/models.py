from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import DateType1Code, NoReasonCode
from python_iso20022.seev.seev_049_001_01.enums import RejectionReason52Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01"


@dataclass
class DateAndDateTime2ChoiceSeev04900101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )


@dataclass
class GenericIdentification30Seev04900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev04900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev04900101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev04900101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcceptedStatus1Seev04900101:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )


@dataclass
class DateCode20ChoiceSeev04900101:
    cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Seev04900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )


@dataclass
class OtherIdentification1Seev04900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification195ChoiceSeev04900101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev04900101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class RejectedReason30ChoiceSeev04900101:
    cd: Optional[RejectionReason52Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Seev04900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )


@dataclass
class SupplementaryData1Seev04900101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev04900101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )


@dataclass
class DateFormat46ChoiceSeev04900101:
    dt: Optional[DateAndDateTime2ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    dt_cd: Optional[DateCode20ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )


@dataclass
class PartyIdentification215Seev04900101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    id: Optional[PartyIdentification195ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )


@dataclass
class RejectedStatusReason29Seev04900101:
    rsn_cd: Optional[RejectedReason30ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecurityIdentification19Seev04900101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev04900101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DisclosureRequestIdentification1Seev04900101:
    issr_dsclsr_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev04900101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )
    shrhldrs_dsclsr_rcrd_dt: Optional[DateFormat46ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "ShrhldrsDsclsrRcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )


@dataclass
class RejectedStatus29ChoiceSeev04900101:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    rsn: list[RejectedStatusReason29Seev04900101] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )


@dataclass
class ResponseProcessingStatus1ChoiceSeev04900101:
    accptd: Optional[AcceptedStatus1Seev04900101] = field(
        default=None,
        metadata={
            "name": "Accptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )
    rjctd: Optional[RejectedStatus29ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )


@dataclass
class ShareholderIdentificationDisclosureResponseStatusAdviceV01Seev04900101:
    dsclsr_rspn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DsclsrRspnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr_dsclsr_req_ref: Optional[DisclosureRequestIdentification1Seev04900101] = field(
        default=None,
        metadata={
            "name": "IssrDsclsrReqRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )
    rspndg_intrmy: Optional[PartyIdentification215Seev04900101] = field(
        default=None,
        metadata={
            "name": "RspndgIntrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )
    rspn_rcptn_sts: Optional[ResponseProcessingStatus1ChoiceSeev04900101] = field(
        default=None,
        metadata={
            "name": "RspnRcptnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Seev04900101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01",
        },
    )


@dataclass
class Seev04900101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01"

    shrhldr_id_dsclsr_rspn_sts_advc: Optional[
        ShareholderIdentificationDisclosureResponseStatusAdviceV01Seev04900101
    ] = field(
        default=None,
        metadata={
            "name": "ShrhldrIdDsclsrRspnStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
