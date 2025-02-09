from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.enums import LimitType4Code
from python_iso20022.enums import AddressType2Code, CreditDebitCode

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01"


@dataclass
class AccountSchemeName1ChoiceCamt06500101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountCamt06500101(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceCamt06500101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class ErrorHandling3ChoiceCamt06500101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Camt06500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessInstruction1Camt06500101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class Pagination1Camt06500101(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt06500101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Amount2ChoiceCamt06500101(ISO20022MessageElement):
    amt_wtht_ccy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtWthtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amt_wth_ccy: Optional[ActiveCurrencyAndAmountCamt06500101] = field(
        default=None,
        metadata={
            "name": "AmtWthCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class ErrorHandling5Camt06500101(ISO20022MessageElement):
    err: Optional[ErrorHandling3ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GenericAccountIdentification1Camt06500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader12Camt06500101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Camt06500101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class PostalAddress1Camt06500101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Camt06500101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt06500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt06500101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt06500101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class CreditDebitAmount1Camt06500101(ISO20022MessageElement):
    amt: Optional[Amount2ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )


@dataclass
class LimitJournalEntry3Camt06500101(ISO20022MessageElement):
    jrnl_dt: Optional[DateAndDateTime2ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "JrnlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    amt: Optional[Amount2ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_ntry_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlNtryInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class NameAndAddress5Camt06500101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Camt06500101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class LimitAmount1Camt06500101(ISO20022MessageElement):
    amt: Optional[CreditDebitAmount1Camt06500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    utlstn_amt: Optional[CreditDebitAmount1Camt06500101] = field(
        default=None,
        metadata={
            "name": "UtlstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    avlbl_amt: Optional[CreditDebitAmount1Camt06500101] = field(
        default=None,
        metadata={
            "name": "AvlblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification120ChoiceCamt06500101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Camt06500101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Camt06500101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class LimitJournal3Camt06500101(ISO20022MessageElement):
    lmt: Optional[LimitAmount1Camt06500101] = field(
        default=None,
        metadata={
            "name": "Lmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    jrnl_actvty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "JrnlActvtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    jrnl_ntry: list[LimitJournalEntry3Camt06500101] = field(
        default_factory=list,
        metadata={
            "name": "JrnlNtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class PartyIdentification136Camt06500101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class LimitJournalReportOrError8ChoiceCamt06500101(ISO20022MessageElement):
    lmt_jrnl: Optional[LimitJournal3Camt06500101] = field(
        default=None,
        metadata={
            "name": "LmtJrnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    biz_err: list[ErrorHandling5Camt06500101] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class SystemPartyIdentification8Camt06500101(ISO20022MessageElement):
    id: Optional[PartyIdentification136Camt06500101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Camt06500101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class LimitIdentification7Camt06500101(ISO20022MessageElement):
    acct_id: Optional[AccountIdentification4ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    tp: Optional[LimitType4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    lmt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    acct_ownr: Optional[PartyIdentification136Camt06500101] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    bil_lmt_ctr_pty_id: Optional[SystemPartyIdentification8Camt06500101] = field(
        default=None,
        metadata={
            "name": "BilLmtCtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class LimitJournalReport4Camt06500101(ISO20022MessageElement):
    lmt_id: Optional[LimitIdentification7Camt06500101] = field(
        default=None,
        metadata={
            "name": "LmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    lmt_rpt: Optional[LimitJournalReportOrError8ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "LmtRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )


@dataclass
class LimitJournalReportOrError7ChoiceCamt06500101(ISO20022MessageElement):
    biz_rpt: list[LimitJournalReport4Camt06500101] = field(
        default_factory=list,
        metadata={
            "name": "BizRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    oprl_err: list[ErrorHandling5Camt06500101] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class LimitUtilisationJournalReportV01Camt06500101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader12Camt06500101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    pgntn: Optional[Pagination1Camt06500101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )
    rpt_or_err: Optional[LimitJournalReportOrError7ChoiceCamt06500101] = field(
        default=None,
        metadata={
            "name": "RptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt06500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01",
        },
    )


@dataclass
class Camt06500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01"

    lmt_utlstn_jrnl_rpt: Optional[LimitUtilisationJournalReportV01Camt06500101] = field(
        default=None,
        metadata={
            "name": "LmtUtlstnJrnlRpt",
            "type": "Element",
            "required": True,
        },
    )
