from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.enums import (
    QueryType2Code,
    StandingOrderQueryType1Code,
    StandingOrderType1Code,
)
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05"


@dataclass
class AccountSchemeName1ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountType2ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DatePeriod2Camt06900105(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt06900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt06900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class StandingOrderReturnCriteria1Camt06900105(ISO20022MessageElement):
    stg_ordr_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StgOrdrIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    tp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    sys_mmb_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SysMmbInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    rspnsbl_pty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    ccy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CcyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    dbtr_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DbtrAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    cdtr_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CdtrAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    assoctd_pool_acct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AssoctdPoolAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    frqcy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrqcyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    exctn_tp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExctnTpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    vldty_fr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VldtyFrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    vld_to_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VldToInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    lk_set_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LkSetIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    lk_set_ordr_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LkSetOrdrIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    lk_set_ordr_seq_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LkSetOrdrSeqInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    ttl_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TtlAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    zero_sweep_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZeroSweepInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt06900105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Camt06900105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt06900105(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DatePeriod2ChoiceCamt06900105(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    fr_to_dt: Optional[DatePeriod2Camt06900105] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class GenericAccountIdentification1Camt06900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt06900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountIdentification1Camt06900105(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class RequestType3ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[StandingOrderQueryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    prtry: Optional[GenericIdentification1Camt06900105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class StandingOrderType1ChoiceCamt06900105(ISO20022MessageElement):
    cd: Optional[StandingOrderType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    prtry: Optional[GenericIdentification1Camt06900105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class SupplementaryData1Camt06900105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt06900105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt06900105(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt06900105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class MessageHeader4Camt06900105(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    req_tp: Optional[RequestType3ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class PostalAddress27Camt06900105(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BranchData5Camt06900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt06900105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class CashAccount40Camt06900105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    tp: Optional[CashAccountType2ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Camt06900105] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Camt06900105(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt06900105] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt06900105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt06900105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Camt06900105(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Camt06900105] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Camt06900105] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class StandingOrderSearchCriteria5Camt06900105(ISO20022MessageElement):
    key_attrbts_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeyAttrbtsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    stg_ordr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StgOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[StandingOrderType1ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    acct: Optional[CashAccount40Camt06900105] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    vldty_prd: Optional[DatePeriod2ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    sys_mmb: Optional[BranchAndFinancialInstitutionIdentification8Camt06900105] = field(
        default=None,
        metadata={
            "name": "SysMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    rspnsbl_pty: Optional[BranchAndFinancialInstitutionIdentification8Camt06900105] = (
        field(
            default=None,
            metadata={
                "name": "RspnsblPty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            },
        )
    )
    assoctd_pool_acct: Optional[AccountIdentification4ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "AssoctdPoolAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    lk_set_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lk_set_ordr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkSetOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lk_set_ordr_seq: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LkSetOrdrSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    zero_sweep_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZeroSweepInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class StandingOrderCriteria5Camt06900105(ISO20022MessageElement):
    new_qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewQryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sch_crit: list[StandingOrderSearchCriteria5Camt06900105] = field(
        default_factory=list,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    rtr_crit: Optional[StandingOrderReturnCriteria1Camt06900105] = field(
        default=None,
        metadata={
            "name": "RtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class StandingOrderCriteria5ChoiceCamt06900105(ISO20022MessageElement):
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_crit: Optional[StandingOrderCriteria5Camt06900105] = field(
        default=None,
        metadata={
            "name": "NewCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class StandingOrderQuery5Camt06900105(ISO20022MessageElement):
    qry_tp: Optional[QueryType2Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    stg_ordr_crit: Optional[StandingOrderCriteria5ChoiceCamt06900105] = field(
        default=None,
        metadata={
            "name": "StgOrdrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class GetStandingOrderV05Camt06900105(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader4Camt06900105] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
            "required": True,
        },
    )
    stg_ordr_qry_def: Optional[StandingOrderQuery5Camt06900105] = field(
        default=None,
        metadata={
            "name": "StgOrdrQryDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )
    splmtry_data: list[SupplementaryData1Camt06900105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05",
        },
    )


@dataclass
class Camt06900105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05"

    get_stg_ordr: Optional[GetStandingOrderV05Camt06900105] = field(
        default=None,
        metadata={
            "name": "GetStgOrdr",
            "type": "Element",
            "required": True,
        },
    )
