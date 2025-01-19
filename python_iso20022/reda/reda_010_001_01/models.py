from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code
from python_iso20022.reda.enums import SecurityStatus2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01"


@dataclass
class DatePeriod2Reda01000101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification1Reda01000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda01000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda01000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceReda01000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Reda01000101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class SecuritiesReturnCriteria1Reda01000101(ISO20022MessageElement):
    fin_instrm_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    isoscty_lng_nm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ISOSctyLngNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    isoscty_shrt_nm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ISOSctyShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    clssfctn_fin_instrm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    mtrty_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    isse_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    isse_ccy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    ctry_of_isse: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtryOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    scty_sts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    invstr_csd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InvstrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    issr_csd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    tech_issr_csd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TechIssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    csd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    scties_qty_tp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctiesQtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    min_dnmtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MinDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    min_mltpl_qty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MinMltplQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    devtg_sttlm_unit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DevtgSttlmUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda01000101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class DatePeriodSearch1ChoiceReda01000101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    fr_to_dt: Optional[DatePeriod2Reda01000101] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    eqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    neqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NEQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class OtherIdentification1Reda01000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Reda01000101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecurityStatus3ChoiceReda01000101(ISO20022MessageElement):
    cd: Optional[SecurityStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01000101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class SupplementaryData1Reda01000101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda01000101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Reda01000101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda01000101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class SecurityIdentification39Reda01000101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Reda01000101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PartyIdentification120ChoiceReda01000101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda01000101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda01000101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class PartyIdentification136Reda01000101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SystemPartyIdentification8Reda01000101(ISO20022MessageElement):
    id: Optional[PartyIdentification136Reda01000101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda01000101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class SystemPartyIdentification2ChoiceReda01000101(ISO20022MessageElement):
    org_id: Optional[PartyIdentification136Reda01000101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    cmbnd_id: Optional[SystemPartyIdentification8Reda01000101] = field(
        default=None,
        metadata={
            "name": "CmbndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class SecuritiesSearchCriteria4Reda01000101(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification39Reda01000101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    mtrty_dt: Optional[DatePeriodSearch1ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    isse_dt: Optional[DatePeriodSearch1ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    isse_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "IsseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ctry_of_isse: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    scty_sts: Optional[SecurityStatus3ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "SctySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    mntng_csd: Optional[SystemPartyIdentification2ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "MntngCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    invstr_csd: Optional[SystemPartyIdentification2ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "InvstrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    issr_csd: Optional[SystemPartyIdentification2ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "IssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    tech_issr_csd: Optional[SystemPartyIdentification2ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "TechIssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    csd: Optional[SystemPartyIdentification2ChoiceReda01000101] = field(
        default=None,
        metadata={
            "name": "CSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class SecurityQueryV01Reda01000101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Reda01000101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    req_tp: Optional[GenericIdentification1Reda01000101] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    sch_crit: Optional[SecuritiesSearchCriteria4Reda01000101] = field(
        default=None,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
            "required": True,
        },
    )
    sml_set_rtr_crit: Optional[SecuritiesReturnCriteria1Reda01000101] = field(
        default=None,
        metadata={
            "name": "SmlSetRtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Reda01000101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01",
        },
    )


@dataclass
class Reda01000101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01"

    scty_qry: Optional[SecurityQueryV01Reda01000101] = field(
        default=None,
        metadata={
            "name": "SctyQry",
            "type": "Element",
            "required": True,
        },
    )
