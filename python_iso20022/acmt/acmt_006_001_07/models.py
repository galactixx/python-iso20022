from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.acmt.acmt_006_001_07.enums import (
    AcceptedStatusReason1Code,
    AccountManagementStatus1Code,
    RejectedStatusReason6Code,
)
from python_iso20022.acmt.enums import (
    BlockedReason2Code,
    ClosedStatusReason1Code,
    ClosurePendingStatusReason1Code,
    DisabledReason2Code,
    EnabledStatusReason1Code,
    InvestmentFundTransactionType1Code,
    PendingOpeningStatusReason1Code,
    PendingStatusReason1Code,
    ProformaStatusReason1Code,
)
from python_iso20022.enums import AddressType2Code, NoReasonCode

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07"


@dataclass
class Extension1Acmt00600107:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Acmt00600107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Acmt00600107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Acmt00600107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class MarketPracticeVersion1Acmt00600107:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Acmt00600107:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )


@dataclass
class AcceptedStatusReason1ChoiceAcmt00600107:
    cd: Optional[AcceptedStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class Account23Acmt00600107:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_acct_dtls: Optional[GenericIdentification1Acmt00600107] = field(
        default=None,
        metadata={
            "name": "RltdAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class BlockedReason2ChoiceAcmt00600107:
    cd: Optional[BlockedReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class ClosedStatusReason2ChoiceAcmt00600107:
    cd: Optional[ClosedStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class ClosurePendingStatusReason2ChoiceAcmt00600107:
    cd: Optional[ClosurePendingStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class DisabledStatusReason2ChoiceAcmt00600107:
    cd: Optional[DisabledReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class EnabledStatusReason2ChoiceAcmt00600107:
    cd: Optional[EnabledStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class OtherAccountStatus1Acmt00600107:
    sts: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    rsn: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class PendingOpeningStatusReason2ChoiceAcmt00600107:
    cd: Optional[PendingOpeningStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class PendingStatusReason2ChoiceAcmt00600107:
    cd: Optional[PendingStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class PostalAddress1Acmt00600107:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProformaStatusReason2ChoiceAcmt00600107:
    cd: Optional[ProformaStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class RejectedReason16ChoiceAcmt00600107:
    cd: Optional[RejectedStatusReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class TransactionType5ChoiceAcmt00600107:
    cd: Optional[InvestmentFundTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class BlockedStatusReason2Acmt00600107:
    tx_tp: Optional[TransactionType5ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    blckd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Blckd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    rsn: list[BlockedReason2ChoiceAcmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ClosedStatusReason1Acmt00600107:
    cd: Optional[ClosedStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ClosurePendingStatusReason1Acmt00600107:
    cd: Optional[ClosurePendingStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DisabledStatusReason1Acmt00600107:
    cd: Optional[DisabledStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class EnabledStatusReason1Acmt00600107:
    cd: Optional[EnabledStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NameAndAddress5Acmt00600107:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Acmt00600107] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class PendingOpeningStatusReason1Acmt00600107:
    cd: Optional[PendingOpeningStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PendingStatusReason14Acmt00600107:
    cd: Optional[PendingStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ProformaStatusReason1Acmt00600107:
    cd: Optional[ProformaStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class RejectionReason31Acmt00600107:
    rsn: Optional[RejectedReason16ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class BlockedStatusReason2ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[BlockedStatusReason2Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class ClosedStatusReason1ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[ClosedStatusReason1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class ClosurePendingStatusReason1ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[ClosurePendingStatusReason1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class DisabledStatusReason1ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[DisabledStatusReason1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class EnabledStatusReason1ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[EnabledStatusReason1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class PartyIdentification125ChoiceAcmt00600107:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Acmt00600107] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Acmt00600107] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class PendingOpeningStatusReason1ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[PendingOpeningStatusReason1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class PendingStatusReason1ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[PendingStatusReason14Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class ProformaStatusReason1ChoiceAcmt00600107:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rsn: list[ProformaStatusReason1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class Status25ChoiceAcmt00600107:
    sts: Optional[AccountManagementStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    rjctd: list[RejectionReason31Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "max_occurs": 10,
        },
    )


@dataclass
class AccountStatus2Acmt00600107:
    nbld: Optional[EnabledStatusReason1ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Nbld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    dsbld: Optional[DisabledStatusReason1ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Dsbld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    pdg: Optional[PendingStatusReason1ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    pdg_opng: Optional[PendingOpeningStatusReason1ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "PdgOpng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    profrm: Optional[ProformaStatusReason1ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Profrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    clsd: Optional[ClosedStatusReason1ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Clsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    clsr_pdg: Optional[ClosurePendingStatusReason1ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "ClsrPdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    othr: list[OtherAccountStatus1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class AdditionalReference13Acmt00600107:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification125ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountManagementStatusAndReason5Acmt00600107:
    sts: Optional[Status25ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    sts_rsn: list[AcceptedStatusReason1ChoiceAcmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    acct_appl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    exstg_acct_id: list[Account23Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "ExstgAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_sts: Optional[AccountStatus2Acmt00600107] = field(
        default=None,
        metadata={
            "name": "AcctSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    blckd_sts: Optional[BlockedStatusReason2ChoiceAcmt00600107] = field(
        default=None,
        metadata={
            "name": "BlckdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    fatcarptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FATCARptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    crsrptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CRSRptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class AccountManagementStatusReportV07Acmt00600107:
    msg_id: Optional[MessageIdentification1Acmt00600107] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    rltd_ref: list[AdditionalReference13Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    sts_rpt: Optional[AccountManagementStatusAndReason5Acmt00600107] = field(
        default=None,
        metadata={
            "name": "StsRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
            "required": True,
        },
    )
    mkt_prctc_vrsn: Optional[MarketPracticeVersion1Acmt00600107] = field(
        default=None,
        metadata={
            "name": "MktPrctcVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )
    xtnsn: list[Extension1Acmt00600107] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07",
        },
    )


@dataclass
class Acmt00600107:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07"

    acct_mgmt_sts_rpt: Optional[AccountManagementStatusReportV07Acmt00600107] = field(
        default=None,
        metadata={
            "name": "AcctMgmtStsRpt",
            "type": "Element",
            "required": True,
        },
    )
