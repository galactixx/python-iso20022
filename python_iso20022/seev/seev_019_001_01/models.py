from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import AddressType2Code, CreditDebitCode, FormOfSecurity1Code
from python_iso20022.seev.enums import (
    CorporateActionEventProcessingType1Code,
    CorporateActionEventType2Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionOptionType1Code,
    DistributionInstructionType1Code,
    SecuritiesBalanceType9Code,
    SecuritiesBalanceType10Code,
    StampDutyType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01"


@dataclass
class AccountIdentification2ChoiceSeev01900101:
    csh_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev01900101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
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
class ActiveCurrencyAndAmountSeev01900101:
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
class AlternateSecurityIdentification3Seev01900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification8Seev01900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev01900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev01900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionEventProcessingType1FormatChoiceSeev01900101:
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev01900101:
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary1FormatChoiceSeev01900101:
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class CorporateActionOption1FormatChoiceSeev01900101:
    cd: Optional[CorporateActionOptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class ForeignExchangeTerms9Seev01900101:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    orgnl_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class PostalAddress1Seev01900101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Seev01900101:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesBalanceType10FormatChoiceSeev01900101:
    cd: Optional[SecuritiesBalanceType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class SecuritiesBalanceType9FormatChoiceSeev01900101:
    cd: Optional[SecuritiesBalanceType9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev01900101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev01900101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class StampDutyType1FormatChoiceSeev01900101:
    cd: Optional[StampDutyType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class UnitOrFaceAmount1ChoiceSeev01900101:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class NameAndAddress5Seev01900101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev01900101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class TaxVoucher1Seev01900101:
    tax_vchr_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxVchrRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tax_cdt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "TaxCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    tax_ddctn: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "TaxDdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    grss_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    rcrd_dt_hldg: Optional[UnitOrFaceAmount1ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "RcrdDtHldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    tax_cdt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxCdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    whldg_tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    scrip_dvdd_rinvstmt_pric_per_shr: Optional[PriceValue1Seev01900101] = field(
        default=None,
        metadata={
            "name": "ScripDvddRinvstmtPricPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    csh_amt_brght_fwd: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "CshAmtBrghtFwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    alltd_shrs_cost: Optional[PriceValue1Seev01900101] = field(
        default=None,
        metadata={
            "name": "AlltdShrsCost",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    csh_amt_crrd_fwd: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "CshAmtCrrdFwd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    ntnl_tax: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "NtnlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    ntnl_dvdd_pybl: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "NtnlDvddPybl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    brgn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BrgnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    brgn_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BrgnSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    stmp_dty_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    chrg_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "ChrgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    comssn_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "ComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    fxdtls: Optional[ForeignExchangeTerms9Seev01900101] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev01900101:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev01900101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev01900101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class CashAccount19Seev01900101:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    acct_id: Optional[AccountIdentification2ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )


@dataclass
class CorporateActionMovement1Seev01900101:
    ordr_tp: Optional[DistributionInstructionType1Code] = field(
        default=None,
        metadata={
            "name": "OrdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    hgh_prty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HghPrtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    reqd_exctn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    confd_bal_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "ConfdBalSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev01900101:
    scty_id: Optional[SecurityIdentification7Seev01900101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class SecuritiesAccount10Seev01900101:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    acct_ownr_ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrNtlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal_tp: Optional[SecuritiesBalanceType9FormatChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    scty_hldg_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctyHldgForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class SecuritiesAccount8Seev01900101:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal_tp: Optional[SecuritiesBalanceType10FormatChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    scty_hldg_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctyHldgForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    stmp_dty: Optional[StampDutyType1FormatChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "StmpDty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class CashMovement2Seev01900101:
    amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    acct_dtls: list[CashAccount19Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class CashProceeds1Seev01900101:
    pstng_amt: Optional[ActiveCurrencyAndAmountSeev01900101] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    rcncltn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    acct_dtls: list[CashAccount19Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class CorporateActionInformation1Seev01900101:
    agt_id: Optional[PartyIdentification2ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    issr_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnPrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType2FormatChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary1FormatChoiceSeev01900101
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    evt_prcg_tp: Optional[
        CorporateActionEventProcessingType1FormatChoiceSeev01900101
    ] = field(
        default=None,
        metadata={
            "name": "EvtPrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev01900101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )


@dataclass
class SecuritiesProceeds1Seev01900101:
    scty_id: Optional[SecurityIdentification7Seev01900101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    pstng_qty: Optional[UnitOrFaceAmount1ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    acct_dtls: list[SecuritiesAccount10Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    rcncltn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class UnderlyingSecurityMovement1Seev01900101:
    scty_id: Optional[SecurityIdentification7Seev01900101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev01900101] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    acct_dtls: list[SecuritiesAccount8Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class ProceedsMovement1Seev01900101:
    csh_prcds_mvmnt_dtls: list[CashProceeds1Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "CshPrcdsMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    scties_prcds_mvmnt_dtls: list[SecuritiesProceeds1Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesPrcdsMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    tax_dtls: Optional[TaxVoucher1Seev01900101] = field(
        default=None,
        metadata={
            "name": "TaxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class AgentCamovementInstructionV01Seev01900101:
    class Meta:
        name = "AgentCAMovementInstructionV01"

    id: Optional[DocumentIdentification8Seev01900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    agt_caelctn_advc_id: Optional[DocumentIdentification8Seev01900101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionInformation1Seev01900101] = field(
        default=None,
        metadata={
            "name": "CorpActnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    mvmnt_gnl_inf: Optional[CorporateActionMovement1Seev01900101] = field(
        default=None,
        metadata={
            "name": "MvmntGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
            "required": True,
        },
    )
    undrlyg_scties_mvmnt_dtls: list[UnderlyingSecurityMovement1Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygSctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    undrlyg_csh_mvmnt_dtls: list[CashMovement2Seev01900101] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygCshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )
    prcds_mvmnt_dtls: Optional[ProceedsMovement1Seev01900101] = field(
        default=None,
        metadata={
            "name": "PrcdsMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
        },
    )


@dataclass
class Seev01900101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01"

    agt_camvmnt_instr: Optional[AgentCamovementInstructionV01Seev01900101] = field(
        default=None,
        metadata={
            "name": "AgtCAMvmntInstr",
            "type": "Element",
            "required": True,
        },
    )
