from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.auth.auth_054_001_01.enums import (
    ClearingAccountType3Code,
    CreditQuality1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01"


@dataclass
class GenericIdentification168Auth05400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class PartyIdentification118ChoiceAuth05400101(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prtry: Optional[GenericIdentification168Auth05400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth05400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )


@dataclass
class PositionAccount1Auth05400101(ISO20022MessageElement):
    id: Optional[PartyIdentification118ChoiceAuth05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )


@dataclass
class MarginAccount1Auth05400101(ISO20022MessageElement):
    id: Optional[PartyIdentification118ChoiceAuth05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )
    pos_acct: list[PositionAccount1Auth05400101] = field(
        default_factory=list,
        metadata={
            "name": "PosAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class CollateralAccount5Auth05400101(ISO20022MessageElement):
    id: Optional[PartyIdentification118ChoiceAuth05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )
    rltd_mrgn_acct: list[MarginAccount1Auth05400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdMrgnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_occurs": 1,
        },
    )
    titl_trf_coll_arrgmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TitlTrfCollArrgmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
        },
    )
    coll_sgrtn_by_val: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollSgrtnByVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
        },
    )


@dataclass
class ClearingAccount1Auth05400101(ISO20022MessageElement):
    acct_tp: Optional[ClearingAccountType3Code] = field(
        default=None,
        metadata={
            "name": "AcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )
    coll_acct_ownr: list[CollateralAccount5Auth05400101] = field(
        default_factory=list,
        metadata={
            "name": "CollAcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class ClearingMember1Auth05400101(ISO20022MessageElement):
    id: Optional[PartyIdentification118ChoiceAuth05400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )
    cdt_qlty: Optional[CreditQuality1Code] = field(
        default=None,
        metadata={
            "name": "CdtQlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )
    ultmt_prnt_id: Optional[PartyIdentification118ChoiceAuth05400101] = field(
        default=None,
        metadata={
            "name": "UltmtPrntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
        },
    )
    futrs_comssn_mrchnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FutrsComssnMrchntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )
    mmbsh_vld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MmbshVldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "required": True,
        },
    )
    mmbsh_vld_to: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MmbshVldTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
        },
    )
    spnsrg_clr_mmb_id: Optional[PartyIdentification118ChoiceAuth05400101] = field(
        default=None,
        metadata={
            "name": "SpnsrgClrMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
        },
    )
    clr_acct_ownr: list[ClearingAccount1Auth05400101] = field(
        default_factory=list,
        metadata={
            "name": "ClrAcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class CcpclearingMemberReportV01Auth05400101(ISO20022MessageElement):
    class Meta:
        name = "CCPClearingMemberReportV01"

    clr_mmb: list[ClearingMember1Auth05400101] = field(
        default_factory=list,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01",
        },
    )


@dataclass
class Auth05400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.054.001.01"

    ccpclr_mmb_rpt: Optional[CcpclearingMemberReportV01Auth05400101] = field(
        default=None,
        metadata={
            "name": "CCPClrMmbRpt",
            "type": "Element",
            "required": True,
        },
    )
