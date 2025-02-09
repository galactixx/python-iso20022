from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.enums import LimitType4Code
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01"


@dataclass
class AccountSchemeName1ChoiceCamt06400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Camt06400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Camt06400101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt06400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class GenericAccountIdentification1Camt06400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt06400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress1Camt06400101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Camt06400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt06400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt06400101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt06400101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )


@dataclass
class NameAndAddress5Camt06400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Camt06400101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceCamt06400101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Camt06400101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Camt06400101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )


@dataclass
class PartyIdentification136Camt06400101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceCamt06400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SystemPartyIdentification8Camt06400101(ISO20022MessageElement):
    id: Optional[PartyIdentification136Camt06400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Camt06400101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )


@dataclass
class LimitUtilisationJournalSearchCriteria2Camt06400101(ISO20022MessageElement):
    lmt_tp: list[LimitType4Code] = field(
        default_factory=list,
        metadata={
            "name": "LmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )
    jrnl_actvty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "JrnlActvtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
        },
    )
    acct_id: Optional[AccountIdentification4ChoiceCamt06400101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )
    lmt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_ownr: Optional[PartyIdentification136Camt06400101] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )
    bil_lmt_ctr_pty_id: Optional[SystemPartyIdentification8Camt06400101] = field(
        default=None,
        metadata={
            "name": "BilLmtCtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
        },
    )


@dataclass
class LimitUtilisationJournalQueryV01Camt06400101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Camt06400101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )
    sch_crit: Optional[LimitUtilisationJournalSearchCriteria2Camt06400101] = field(
        default=None,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt06400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01",
        },
    )


@dataclass
class Camt06400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01"

    lmt_utlstn_jrnl_qry: Optional[LimitUtilisationJournalQueryV01Camt06400101] = field(
        default=None,
        metadata={
            "name": "LmtUtlstnJrnlQry",
            "type": "Element",
            "required": True,
        },
    )
