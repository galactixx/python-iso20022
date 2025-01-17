from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.colr.colr_009_001_05.enums import (
    DisputeResolutionType1Code,
    DisputeResolutionType2Code,
)
from python_iso20022.colr.enums import CollateralAccountType1Code, ExposureType11Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05"


@dataclass
class ActiveCurrencyAndAmountColr00900105:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
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
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceColr00900105:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class GenericIdentification30Colr00900105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Colr00900105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress2Colr00900105:
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Colr00900105:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CollateralAccountIdentificationType3ChoiceColr00900105:
    tp: Optional[CollateralAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    prtry: Optional[GenericIdentification36Colr00900105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class Dispute1Colr00900105:
    mrgn_call_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrgnCallReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsptd_amt: Optional[ActiveCurrencyAndAmountColr00900105] = field(
        default=None,
        metadata={
            "name": "DsptdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    dspt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DsptDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )


@dataclass
class DisputeResolutionType1ChoiceColr00900105:
    cd: Optional[DisputeResolutionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    prtry_id: Optional[GenericIdentification30Colr00900105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class DisputeResolutionType2ChoiceColr00900105:
    cd: Optional[DisputeResolutionType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    prtry_id: Optional[GenericIdentification30Colr00900105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class NameAndAddress6Colr00900105:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Colr00900105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Colr00900105:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Colr00900105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )


@dataclass
class BlockChainAddressWallet5Colr00900105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CollateralAccount3Colr00900105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PartyIdentification178ChoiceColr00900105:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr00900105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Colr00900105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class SegregatedIndependentAmountDispute2Colr00900105:
    dspt_dtls: Optional[Dispute1Colr00900105] = field(
        default=None,
        metadata={
            "name": "DsptDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    dspt_rsltn_tp1_chc: list[DisputeResolutionType1ChoiceColr00900105] = field(
        default_factory=list,
        metadata={
            "name": "DsptRsltnTp1Chc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class VariationMarginDispute1Colr00900105:
    dspt_dtls: Optional[Dispute1Colr00900105] = field(
        default=None,
        metadata={
            "name": "DsptDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    rsltn_tp_dtls: list[DisputeResolutionType2ChoiceColr00900105] = field(
        default_factory=list,
        metadata={
            "name": "RsltnTpDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class DisputeNotification2Colr00900105:
    vartn_mrgn_dspt: Optional[VariationMarginDispute1Colr00900105] = field(
        default=None,
        metadata={
            "name": "VartnMrgnDspt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    sgrtd_indpdnt_amt_dspt: Optional[
        SegregatedIndependentAmountDispute2Colr00900105
    ] = field(
        default=None,
        metadata={
            "name": "SgrtdIndpdntAmtDspt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class Obligation9Colr00900105:
    pty_a: Optional[PartyIdentification178ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "PtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    svcg_pty_a: Optional[PartyIdentification178ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    pty_b: Optional[PartyIdentification178ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "PtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    svcg_pty_b: Optional[PartyIdentification178ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    coll_acct_id: Optional[CollateralAccount3Colr00900105] = field(
        default=None,
        metadata={
            "name": "CollAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet5Colr00900105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    xpsr_tp: Optional[ExposureType11Code] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    valtn_dt: Optional[DateAndDateTime2ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "ValtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )


@dataclass
class DisputeNotification2ChoiceColr00900105:
    dspt_ntfctn_dtls: Optional[DisputeNotification2Colr00900105] = field(
        default=None,
        metadata={
            "name": "DsptNtfctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )
    sgrtd_indpdnt_amt_dspt_dtls: Optional[
        SegregatedIndependentAmountDispute2Colr00900105
    ] = field(
        default=None,
        metadata={
            "name": "SgrtdIndpdntAmtDsptDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class MarginCallDisputeNotificationV05Colr00900105:
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    oblgtn: Optional[Obligation9Colr00900105] = field(
        default=None,
        metadata={
            "name": "Oblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    dspt_ntfctn: Optional[DisputeNotification2ChoiceColr00900105] = field(
        default=None,
        metadata={
            "name": "DsptNtfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Colr00900105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05",
        },
    )


@dataclass
class Colr00900105:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05"

    mrgn_call_dspt_ntfctn: Optional[MarginCallDisputeNotificationV05Colr00900105] = (
        field(
            default=None,
            metadata={
                "name": "MrgnCallDsptNtfctn",
                "type": "Element",
                "required": True,
            },
        )
    )
