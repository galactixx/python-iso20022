from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.colr.enums import (
    AgreementFramework1Code,
    CollateralAccountType1Code,
    ExposureType11Code,
)
from python_iso20022.enums import CreditDebitCode, Frequency1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05"


@dataclass
class ActiveCurrencyAndAmountColr01500105(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountColr01500105(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceColr01500105(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class DatePeriod2Colr01500105(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )


@dataclass
class GenericIdentification30Colr01500105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Colr01500105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Colr01500105(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )


@dataclass
class PostalAddress2Colr01500105(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Colr01500105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AgreementFramework1ChoiceColr01500105(ISO20022MessageElement):
    agrmt_frmwk: Optional[AgreementFramework1Code] = field(
        default=None,
        metadata={
            "name": "AgrmtFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    prtry_id: Optional[GenericIdentification30Colr01500105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class AmountAndDirection20Colr01500105(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountColr01500105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class CollateralAccountIdentificationType3ChoiceColr01500105(ISO20022MessageElement):
    tp: Optional[CollateralAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    prtry: Optional[GenericIdentification36Colr01500105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class NameAndAddress6Colr01500105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Colr01500105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )


@dataclass
class Statement85Colr01500105(ISO20022MessageElement):
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    frqcy: Optional[Frequency1Code] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    stmt_dt_tm: Optional[DateAndDateTime2ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Colr01500105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Colr01500105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )


@dataclass
class Agreement4Colr01500105(ISO20022MessageElement):
    agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    agrmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    agrmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AgrmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    agrmt_frmwk: Optional[AgreementFramework1ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "AgrmtFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class BlockChainAddressWallet5Colr01500105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CollateralAccount3Colr01500105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PartyIdentification178ChoiceColr01500105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr01500105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Colr01500105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class InterestCalculation5Colr01500105(ISO20022MessageElement):
    clctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    coll_acct_id: Optional[CollateralAccount3Colr01500105] = field(
        default=None,
        metadata={
            "name": "CollAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet5Colr01500105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    fctv_prncpl_amt: Optional[AmountAndDirection20Colr01500105] = field(
        default=None,
        metadata={
            "name": "FctvPrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    prncpl_amt: Optional[AmountAndDirection20Colr01500105] = field(
        default=None,
        metadata={
            "name": "PrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    mvmnt_amt: Optional[AmountAndDirection20Colr01500105] = field(
        default=None,
        metadata={
            "name": "MvmntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    fctv_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FctvRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection20Colr01500105] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    aggtd_intrst_amt: Optional[ActiveCurrencyAndAmountColr01500105] = field(
        default=None,
        metadata={
            "name": "AggtdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class Obligation9Colr01500105(ISO20022MessageElement):
    pty_a: Optional[PartyIdentification178ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "PtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    svcg_pty_a: Optional[PartyIdentification178ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    pty_b: Optional[PartyIdentification178ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "PtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    svcg_pty_b: Optional[PartyIdentification178ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    coll_acct_id: Optional[CollateralAccount3Colr01500105] = field(
        default=None,
        metadata={
            "name": "CollAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet5Colr01500105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    xpsr_tp: Optional[ExposureType11Code] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    valtn_dt: Optional[DateAndDateTime2ChoiceColr01500105] = field(
        default=None,
        metadata={
            "name": "ValtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )


@dataclass
class InterestStatement5Colr01500105(ISO20022MessageElement):
    intrst_prd: Optional[DatePeriod2Colr01500105] = field(
        default=None,
        metadata={
            "name": "IntrstPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    ttl_intrst_amt_due_to_a: Optional[ActiveCurrencyAndAmountColr01500105] = field(
        default=None,
        metadata={
            "name": "TtlIntrstAmtDueToA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    ttl_intrst_amt_due_to_b: Optional[ActiveCurrencyAndAmountColr01500105] = field(
        default=None,
        metadata={
            "name": "TtlIntrstAmtDueToB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    intrst_pmt_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstPmtReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrst_clctn: list[InterestCalculation5Colr01500105] = field(
        default_factory=list,
        metadata={
            "name": "IntrstClctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class InterestPaymentStatementV05Colr01500105(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    agrmt: Optional[Agreement4Colr01500105] = field(
        default=None,
        metadata={
            "name": "Agrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    oblgtn: Optional[Obligation9Colr01500105] = field(
        default=None,
        metadata={
            "name": "Oblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    stmt_params: Optional[Statement85Colr01500105] = field(
        default=None,
        metadata={
            "name": "StmtParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    pgntn: Optional[Pagination1Colr01500105] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )
    intrst_stmt: Optional[InterestStatement5Colr01500105] = field(
        default=None,
        metadata={
            "name": "IntrstStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Colr01500105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05",
        },
    )


@dataclass
class Colr01500105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05"

    intrst_pmt_stmt: Optional[InterestPaymentStatementV05Colr01500105] = field(
        default=None,
        metadata={
            "name": "IntrstPmtStmt",
            "type": "Element",
            "required": True,
        },
    )
