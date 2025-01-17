from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import AdjustmentDirection1Code
from python_iso20022.tsmt.enums import AdjustmentType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02"


@dataclass
class AccountSchemeName1ChoiceTsmt04400102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Bicidentification1Tsmt04400102:
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class CashAccountType2ChoiceTsmt04400102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyAndAmountTsmt04400102:
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
class DocumentIdentification7Tsmt04400102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class InvoiceIdentification1Tsmt04400102:
    invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class MessageIdentification1Tsmt04400102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class PostalAddress2Tsmt04400102:
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt04400102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdjustmentType1ChoiceTsmt04400102:
    tp: Optional[AdjustmentType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    othr_adjstmnt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAdjstmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericAccountIdentification1Tsmt04400102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTsmt04400102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress6Tsmt04400102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceTsmt04400102:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )


@dataclass
class Adjustment6Tsmt04400102:
    tp: Optional[AdjustmentType1ChoiceTsmt04400102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    drctn: Optional[AdjustmentDirection1Code] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    amt: Optional[CurrencyAndAmountTsmt04400102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class FinancialInstitutionIdentification4ChoiceTsmt04400102:
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )


@dataclass
class CashAccount24Tsmt04400102:
    id: Optional[AccountIdentification4ChoiceTsmt04400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2ChoiceTsmt04400102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ReportLine5Tsmt04400102:
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    adjstmnt: list[Adjustment6Tsmt04400102] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    net_amt: Optional[CurrencyAndAmountTsmt04400102] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class ReportLine7Tsmt04400102:
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    adjstmnt: list[Adjustment6Tsmt04400102] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    net_amt: Optional[CurrencyAndAmountTsmt04400102] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class ReportLine6Tsmt04400102:
    comrcl_doc_ref: Optional[InvoiceIdentification1Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "ComrclDocRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    adjstmnt: list[Adjustment6Tsmt04400102] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    net_amt: Optional[CurrencyAndAmountTsmt04400102] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    brkdwn_by_purchs_ordr: list[ReportLine7Tsmt04400102] = field(
        default_factory=list,
        metadata={
            "name": "BrkdwnByPurchsOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class SettlementTerms3Tsmt04400102:
    cdtr_agt: Optional[FinancialInstitutionIdentification4ChoiceTsmt04400102] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    cdtr_acct: Optional[CashAccount24Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class BreakDown1ChoiceTsmt04400102:
    by_purchs_ordr: Optional[ReportLine5Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "ByPurchsOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    by_comrcl_invc: Optional[ReportLine6Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "ByComrclInvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )


@dataclass
class IntentToPay2Tsmt04400102:
    brkdwn: Optional[BreakDown1ChoiceTsmt04400102] = field(
        default=None,
        metadata={
            "name": "Brkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    xpctd_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    sttlm_terms: Optional[SettlementTerms3Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "SttlmTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )


@dataclass
class IntentToPayNotificationV02Tsmt04400102:
    ntfctn_id: Optional[MessageIdentification1Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "NtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt04400102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt04400102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
        },
    )
    buyr_bk: Optional[Bicidentification1Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "BuyrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    sellr_bk: Optional[Bicidentification1Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "SellrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )
    intt_to_pay: Optional[IntentToPay2Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "InttToPay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt04400102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.044.001.02"

    intt_to_pay_ntfctn: Optional[IntentToPayNotificationV02Tsmt04400102] = field(
        default=None,
        metadata={
            "name": "InttToPayNtfctn",
            "type": "Element",
            "required": True,
        },
    )
