from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, NoReasonCode
from python_iso20022.semt.semt_042_001_01.enums import (
    HoldingAccountLevel1Code,
    HoldingRejectionReason41Code,
    ReportItemStatus1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01"


@dataclass
class DateAndDateTimeChoiceSemt04200101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class GenericIdentification30Semt04200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt04200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt04200101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Semt04200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )


@dataclass
class PaginationSemt04200101(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt04200101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class NumberOfItemsPerStatus1Semt04200101(ISO20022MessageElement):
    sts: Optional[ReportItemStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    nb_of_itms: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfItms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )


@dataclass
class OtherIdentification1Semt04200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt04200101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Semt04200101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ReportItemRejectionReason1ChoiceSemt04200101(ISO20022MessageElement):
    cd: Optional[HoldingRejectionReason41Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Semt04200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class SecuritiesAccount19Semt04200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt04200101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class StatementReference1Semt04200101(ISO20022MessageElement):
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_dt_tm: Optional[DateAndDateTimeChoiceSemt04200101] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    pgntn: Optional[PaginationSemt04200101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class SupplementaryData1Semt04200101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt04200101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Semt04200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt04200101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class SecurityIdentification19Semt04200101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt04200101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PartyIdentification71ChoiceSemt04200101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt04200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt04200101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class ReportItem1Semt04200101(ISO20022MessageElement):
    acct_id: Optional[SecuritiesAccount19Semt04200101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    acct_lvl: Optional[HoldingAccountLevel1Code] = field(
        default=None,
        metadata={
            "name": "AcctLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Semt04200101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    itm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ItmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class PartyIdentification100Semt04200101(ISO20022MessageElement):
    id: Optional[PartyIdentification71ChoiceSemt04200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class ReportItemStatus1Semt04200101(ISO20022MessageElement):
    xcptn: Optional[ReportItemRejectionReason1ChoiceSemt04200101] = field(
        default=None,
        metadata={
            "name": "Xcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "min_length": 1,
            "max_length": 210,
        },
    )
    rpt_itm: list[ReportItem1Semt04200101] = field(
        default_factory=list,
        metadata={
            "name": "RptItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class ReportItemStatus1ChoiceSemt04200101(ISO20022MessageElement):
    accptd: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Accptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    accptd_wth_xcptn: list[ReportItemStatus1Semt04200101] = field(
        default_factory=list,
        metadata={
            "name": "AccptdWthXcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    rjctd: Optional[ReportItemStatus1Semt04200101] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class SecuritiesBalanceTransparencyReportStatusAdviceV01Semt04200101(
    ISO20022MessageElement
):
    msg_id: Optional[MessageIdentification1Semt04200101] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    sndr_id: Optional[PartyIdentification100Semt04200101] = field(
        default=None,
        metadata={
            "name": "SndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    rcvr_id: Optional[PartyIdentification100Semt04200101] = field(
        default=None,
        metadata={
            "name": "RcvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )
    rltd_stmt: Optional[StatementReference1Semt04200101] = field(
        default=None,
        metadata={
            "name": "RltdStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    sts: Optional[ReportItemStatus1ChoiceSemt04200101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "required": True,
        },
    )
    nb_of_itms_per_sts: list[NumberOfItemsPerStatus1Semt04200101] = field(
        default_factory=list,
        metadata={
            "name": "NbOfItmsPerSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
            "max_occurs": 2,
        },
    )
    splmtry_data: list[SupplementaryData1Semt04200101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01",
        },
    )


@dataclass
class Semt04200101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01"

    scties_bal_trnsprncy_rpt_sts_advc: Optional[
        SecuritiesBalanceTransparencyReportStatusAdviceV01Semt04200101
    ] = field(
        default=None,
        metadata={
            "name": "SctiesBalTrnsprncyRptStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
