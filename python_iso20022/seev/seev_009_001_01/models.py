from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    EucapitalGain2Code,
    NamePrefix1Code,
    ProcessingPosition2Code,
    RateType12Code,
    TaxableIncomePerShareCalculated2Code,
)
from python_iso20022.seev.enums import (
    AgentRole2Code,
    AmountPriceType1Code,
    BeneficiaryCertificationType1Code,
    ConversionType1Code,
    CorporateActionCalculationMethod1Code,
    CorporateActionChangeType1Code,
    CorporateActionEventProcessingType1Code,
    CorporateActionEventStage1Code,
    CorporateActionEventStatus2Code,
    CorporateActionEventType2Code,
    CorporateActionFrequencyType1Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionNotificationType1Code,
    CorporateActionOptionType1Code,
    DateType6Code,
    DistributionType1Code,
    ElectionMovementType1Code,
    FractionDispositionType1Code,
    GrossDividendRateType1Code,
    IntermediateSecurityDistributionType1Code,
    LotteryType1Code,
    NetDividendRateType1Code,
    OfferType1Code,
    OptionFeatures1Code,
    PriceRateType3Code,
    PriceValueType5Code,
    PriceValueType6Code,
    Quantity1Code,
    RateValueType2Code,
    RateValueType6Code,
    RenounceableStatus1Code,
    ShareRanking1Code,
    TaxType3Code,
)
from python_iso20022.seev.seev_009_001_01.enums import ProcessingStatus1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01"


@dataclass
class AccountIdentification2ChoiceSeev00900101:
    csh_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev00900101:
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
class ActiveCurrencyAndAmountSeev00900101:
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
class AlternateSecurityIdentification3Seev00900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionNarrative2Seev00900101:
    inf_conds: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    inf_to_cmply_wth: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxtn_conds: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DateAndDateTimeChoiceSeev00900101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class DocumentIdentification8Seev00900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev00900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev00900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class QuantityToQuantityRatio1Seev00900101:
    qty1: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty2: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class AgentRole1FormatChoiceSeev00900101:
    cd: Optional[AgentRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class AmountAndQuantityRatio1Seev00900101:
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class AmountPriceType1FormatChoiceSeev00900101:
    cd: Optional[AmountPriceType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class AmountToAmountRatio1Seev00900101:
    amt1: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    amt2: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class BeneficiaryCertificationType1FormatChoiceSeev00900101:
    cd: Optional[BeneficiaryCertificationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class ContactIdentification4Seev00900101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class ConversionType1FormatChoiceSeev00900101:
    cd: Optional[ConversionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionAmounts1Seev00900101:
    grss_csh_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrssCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    net_csh_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "NetCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    isse_dscnt_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "IsseDscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    slctn_fees: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "SlctnFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    csh_in_lieu_of_shr: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    orgnl_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    cptl_gn: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    intrst_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "IntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    indmnty_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "IndmntyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    red_prm_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "RedPrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    manfctrd_dvdd_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "ManfctrdDvddAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prncpl_or_crps: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "PrncplOrCrps",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rinvstmt_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "RinvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    mkt_clm_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "MktClmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    fully_frnkd_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "FullyFrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ufrnkd_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "UfrnkdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    sndry_or_othr_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "SndryOrOthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    spcl_cncssn_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "SpclCncssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    entitld_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "EntitldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    csh_incntiv: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "CshIncntiv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_sbcpt_cost: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "AddtlSbcptCost",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tax_free_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxFreeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tax_dfrrd_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxDfrrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax1_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax1Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax2_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax2Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax3_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax3Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax4_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax4Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    stock_xchg_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "StockXchgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    trf_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "TrfTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tx_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "TxTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    val_added_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "ValAddedTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    eurtntn_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "EURtntnTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    lcl_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "LclTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pmt_levy_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "PmtLevyTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ctry_ntl_fdrl_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "CtryNtlFdrlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    stmp_dty_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "StmpDtyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tax_rclm_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxRclmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tax_cdt_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    whldg_of_frgn_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "WhldgOfFrgnTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    whldg_of_lcl_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "WhldgOfLclTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "AddtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    fscl_stmp_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "FsclStmpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    exctg_brkr_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "ExctgBrkrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    png_agt_comssn_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "PngAgtComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    lcl_brkr_comssn_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "LclBrkrComssnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pstg_fee_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "PstgFeeAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rgltry_fees_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "RgltryFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    shppg_fees_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "ShppgFeesAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    chrgs_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionCalculationMethod1FormatChoiceSeev00900101:
    cd: Optional[CorporateActionCalculationMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionChangeType1FormatChoiceSeev00900101:
    cd: Optional[CorporateActionChangeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionEventProcessingType1FormatChoiceSeev00900101:
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionEventStage1FormatChoiceSeev00900101:
    cd: Optional[CorporateActionEventStage1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionEventStatus2FormatChoiceSeev00900101:
    cd: Optional[CorporateActionEventStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev00900101:
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionFrequencyType1FormatChoiceSeev00900101:
    cd: Optional[CorporateActionFrequencyType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary1FormatChoiceSeev00900101:
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionOption1FormatChoiceSeev00900101:
    cd: Optional[CorporateActionOptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class DateFormat4ChoiceSeev00900101:
    dt: Optional[DateAndDateTimeChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd_dt: Optional[DateType6Code] = field(
        default=None,
        metadata={
            "name": "NotSpcfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class DistributionType1FormatChoiceSeev00900101:
    cd: Optional[DistributionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class ElectionMovementType1FormatChoiceSeev00900101:
    cd: Optional[ElectionMovementType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class ForeignExchangeTerms8Seev00900101:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class FractionDispositionType1FormatChoiceSeev00900101:
    cd: Optional[FractionDispositionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class GrossDividendRateType1FormatChoiceSeev00900101:
    cd: Optional[GrossDividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class IntermediateSecurityDistributionType1FormatChoiceSeev00900101:
    cd: Optional[IntermediateSecurityDistributionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class LotteryType1FormatChoiceSeev00900101:
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class NetDividendRateType1FormatChoiceSeev00900101:
    cd: Optional[NetDividendRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class OfferType1FormatChoiceSeev00900101:
    cd: Optional[OfferType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class OptionFeatures1FormatChoiceSeev00900101:
    cd: Optional[OptionFeatures1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PostalAddress1Seev00900101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateType3FormatChoiceSeev00900101:
    cd: Optional[PriceRateType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PriceValueType5FormatChoiceSeev00900101:
    cd: Optional[PriceValueType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PriceValueType6FormatChoiceSeev00900101:
    cd: Optional[PriceValueType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class ProcessingPosition2FormatChoiceSeev00900101:
    cd: Optional[ProcessingPosition2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class ProcessingStatus1FormatChoiceSeev00900101:
    cd: Optional[ProcessingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RateType12FormatChoiceSeev00900101:
    cd: Optional[RateType12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RateValueType2FormatChoiceSeev00900101:
    cd: Optional[RateValueType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RateValueType6FormatChoiceSeev00900101:
    cd: Optional[RateValueType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RenounceableStatus1FormatChoiceSeev00900101:
    cd: Optional[RenounceableStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev00900101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev00900101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ShareRanking1FormatChoiceSeev00900101:
    cd: Optional[ShareRanking1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class TaxType3FormatChoiceSeev00900101:
    cd: Optional[TaxType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class UnitOrFaceAmount1ChoiceSeev00900101:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class UnitOrFaceAmountOrCode1ChoiceSeev00900101:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    cd: Optional[Quantity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class AmountAndRateFormat2ChoiceSeev00900101:
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd_rate: Optional[RateType12FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class AmountAndRateFormat3ChoiceSeev00900101:
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd_rate: Optional[RateValueType6FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class AmountPrice1Seev00900101:
    amt_pric_tp: Optional[AmountPriceType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class AmountPricePerAmount1Seev00900101:
    amt_pric_tp: Optional[AmountPriceType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class AmountPricePerFinancialInstrumentQuantity1Seev00900101:
    amt_pric_tp: Optional[AmountPriceType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AmtPricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    pric_val: Optional[ActiveCurrencyAnd13DecimalAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "PricVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    fin_instrm_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class CorporateActionDate2Seev00900101:
    rcrd_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    fctv_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    cover_xprtn_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CoverXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    equlstn_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "EqulstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    mrgn_fxg_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MrgnFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ltry_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "LtryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtct_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PrtctDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ucondl_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "UcondlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    whly_ucondl_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "WhlyUcondlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rslts_pblctn_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RsltsPblctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    crt_apprvl_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CrtApprvlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    early_clsg_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "EarlyClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ex_dvdd_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    indx_fxg_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "IndxFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    mtrty_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tradg_sspd_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "TradgSspdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    certfctn_ddln: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CertfctnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    red_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RedDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    regn_ddln: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RegnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prratn_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PrratnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ddln_for_tax_brkdwn_instr: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "DdlnForTaxBrkdwnInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    lpsd_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "LpsdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grnted_prtcptn_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrntedPrtcptnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    elctn_to_ctr_pty_ddln: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "ElctnToCtrPtyDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    spcl_ex_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "SpclExDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionDate3Seev00900101:
    pmt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    avlbl_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    dvdd_rnkg_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "DvddRnkgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prpss_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PrpssDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    frst_dealg_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FrstDealgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    earlst_pmt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionDate4Seev00900101:
    cpn_clpng_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CpnClpngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    cnsnt_xprtn_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CnsntXprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    cnsnt_rcrd_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CnsntRcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pmt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    earlst_pmt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    mkt_ddln: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MktDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rspn_ddln: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RspnDdln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ddln_to_splt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "DdlnToSplt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    xpry_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    qtn_setng_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "QtnSetngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    sbcpt_cost_dbt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "SbcptCostDbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionDate5Seev00900101:
    fxrate_fxg_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FXRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    val_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pmt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    earlst_pmt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionNotification1Seev00900101:
    anncmnt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    frthr_dtld_anncmnt_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FrthrDtldAnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    offcl_anncmnt_pblctn_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "OffclAnncmntPblctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prcg_sts: Optional[ProcessingStatus1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class GrossDividendRate2Seev00900101:
    rate_tp: Optional[GrossDividendRateType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class LinkedCorporateAction1Seev00900101:
    ntfctn_tp: Optional[CorporateActionNotificationType1Code] = field(
        default=None,
        metadata={
            "name": "NtfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    lkd_agt_cantfctn_advc_id: Optional[DocumentIdentification8Seev00900101] = field(
        default=None,
        metadata={
            "name": "LkdAgtCANtfctnAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    lkg_tp: Optional[ProcessingPosition2FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    lkd_issr_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdIssrCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkd_corp_actn_prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdCorpActnPrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress5Seev00900101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class NetDividendRate2Seev00900101:
    rate_tp: Optional[NetDividendRateType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class Period1Seev00900101:
    start_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    end_dt: Optional[DateFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class PriceRate1Seev00900101:
    rate_tp: Optional[PriceRateType3FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class RateAndAmountFormat1ChoiceSeev00900101:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd_rate: Optional[RateType12FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RateFormat1ChoiceSeev00900101:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    not_spcfd_rate: Optional[RateType12FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RatioFormat1ChoiceSeev00900101:
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev00900101] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio1Seev00900101] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd_rate: Optional[RateType12FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RatioFormat2ChoiceSeev00900101:
    qty_to_qty: Optional[QuantityToQuantityRatio1Seev00900101] = field(
        default=None,
        metadata={
            "name": "QtyToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    amt_to_amt: Optional[AmountToAmountRatio1Seev00900101] = field(
        default=None,
        metadata={
            "name": "AmtToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    amt_to_qty: Optional[AmountAndQuantityRatio1Seev00900101] = field(
        default=None,
        metadata={
            "name": "AmtToQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    qty_to_amt: Optional[AmountAndQuantityRatio1Seev00900101] = field(
        default=None,
        metadata={
            "name": "QtyToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd_rate: Optional[RateType12FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class RelatedTaxType1Seev00900101:
    tax_tp: Optional[TaxType3FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )


@dataclass
class CashOption1Seev00900101:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[CorporateActionDate5Seev00900101] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    amt_dtls: Optional[CorporateActionAmounts1Seev00900101] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    xchg_rate: Optional[ForeignExchangeTerms8Seev00900101] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionPeriod1Seev00900101:
    actn_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    cmplsry_purchs_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "CmplsryPurchsPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    intrst_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "IntrstPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    blckg_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "BlckgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pric_clctn_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionPeriod2Seev00900101:
    assntd_line_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "AssntdLinePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    actn_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "ActnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prvlg_sspnsn_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "PrvlgSspnsnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    parll_tradg_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "ParllTradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    sell_thru_issr_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "SellThruIssrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rvcblty_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "RvcbltyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pric_clctn_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "PricClctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionRate1Seev00900101:
    intrst: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rltd_indx: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RltdIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pctg_sght: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PctgSght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rinvstmt_dscnt_to_mkt: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "RinvstmtDscntToMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    sprd: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    bid_intrvl: Optional[AmountAndRateFormat3ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "BidIntrvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    chrgs: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class GrossDividendRate1ChoiceSeev00900101:
    not_spcfd_rate: Optional[RateValueType2FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate_tp_amt: Optional[GrossDividendRate2Seev00900101] = field(
        default=None,
        metadata={
            "name": "RateTpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class NetDividendRate1ChoiceSeev00900101:
    not_spcfd_rate: Optional[RateValueType6FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate_tp_amt: Optional[NetDividendRate2Seev00900101] = field(
        default=None,
        metadata={
            "name": "RateTpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev00900101:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev00900101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev00900101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PriceFormat1ChoiceSeev00900101:
    amt: Optional[AmountPrice1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt_pric_per_fin_instrm_qty: Optional[
        AmountPricePerFinancialInstrumentQuantity1Seev00900101
    ] = field(
        default=None,
        metadata={
            "name": "AmtPricPerFinInstrmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    amt_pric_per_amt: Optional[AmountPricePerAmount1Seev00900101] = field(
        default=None,
        metadata={
            "name": "AmtPricPerAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd: Optional[PriceValueType6FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PriceFormat2ChoiceSeev00900101:
    amt: Optional[AmountPrice1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate: Optional[PriceRate1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd: Optional[PriceValueType5FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PriceFormat3ChoiceSeev00900101:
    amt: Optional[AmountPrice1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate: Optional[PriceRate1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class PriceFormat4ChoiceSeev00900101:
    amt: Optional[AmountPrice1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate: Optional[PriceRate1Seev00900101] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    not_spcfd: Optional[PriceValueType5FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NotSpcfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    indx_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class ContactPerson1Seev00900101:
    ctct_prsn: Optional[ContactIdentification4Seev00900101] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    instn_id: Optional[PartyIdentification2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "InstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionAgent1Seev00900101:
    agt_id: Optional[PartyIdentification2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    agt_role: Optional[AgentRole1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AgtRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    ctct_prsn: Optional[NameAndAddress5Seev00900101] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionNarrative1Seev00900101:
    inf_conds: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    inf_to_cmply_wth: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfToCmplyWth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxtn_conds: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    new_cpny_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewCpnyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    offerr: Optional[PartyIdentification2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "Offerr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )
    addtl_txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CorporateActionPrice1Seev00900101:
    exrc_pric: Optional[PriceFormat4ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    isse_pric: Optional[PriceFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    csh_in_lieu_of_shr_pric: Optional[PriceFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CshInLieuOfShrPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    taxbl_incm_per_dvdd_shr: Optional[AmountPrice1Seev00900101] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerDvddShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    gnc_csh_pric_rcvd_per_pdct: Optional[PriceFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GncCshPricRcvdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    gnc_csh_pric_pd_per_pdct: Optional[PriceFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GncCshPricPdPerPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    over_sbcpt_dpst_pric: Optional[PriceFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "OverSbcptDpstPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionPrice2Seev00900101:
    max_pric: Optional[PriceFormat3ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MaxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    min_pric: Optional[PriceFormat3ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MinPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionPrice4Seev00900101:
    indctv_pric: Optional[PriceFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "IndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    mkt_pric: Optional[PriceFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MktPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionRate2Seev00900101:
    whldg_tax: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "WhldgTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    whldg_of_frgn_tax: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "WhldgOfFrgnTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    whldg_of_lcl_tax: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "WhldgOfLclTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax1: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax2: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax3: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grmn_lcl_tax4: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrmnLclTax4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tax_on_incm: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxOnIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tax_on_prft: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxOnPrft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tax_rclm: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "TaxRclm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    fscl_stmp: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FsclStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prratn: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "Prratn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    new_to_od: Optional[RatioFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NewToOd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    new_scties_to_undrlyg_scties: Optional[RatioFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NewSctiesToUndrlygScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_qty_for_exstg_scties: Optional[RatioFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[RatioFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForSbcbdRsltntScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rltd_tax: Optional[RelatedTaxType1Seev00900101] = field(
        default=None,
        metadata={
            "name": "RltdTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    non_resdt_rate: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NonResdtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    chrgs: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    intrst_for_usd_pmt: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "IntrstForUsdPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    indx_fctr: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "IndxFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    fully_frnkd: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FullyFrnkd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    grss_dvdd: Optional[GrossDividendRate1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "GrssDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    net_dvdd: Optional[NetDividendRate1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NetDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    fnl_dvdd: Optional[AmountAndRateFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FnlDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prvsnl_dvdd: Optional[AmountAndRateFormat2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "PrvsnlDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    csh_incntiv: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "CshIncntiv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    slctn_fee: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "SlctnFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    max_allwd_ovrsbcpt: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MaxAllwdOvrsbcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_tax: Optional[RateAndAmountFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AddtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    orgnl_amt: Optional[ActiveCurrencyAndAmountSeev00900101] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    xchg_rate: Optional[ForeignExchangeTerms8Seev00900101] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    aplbl_rate: Optional[RateFormat1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AplblRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev00900101:
    scty_id: Optional[SecurityIdentification7Seev00900101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateAction2Seev00900101:
    evt_stag: list[CorporateActionEventStage1FormatChoiceSeev00900101] = field(
        default_factory=list,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    dflt_optn_tp: Optional[CorporateActionOption1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "DfltOptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    dflt_optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DfltOptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    clctn_mtd: Optional[CorporateActionCalculationMethod1FormatChoiceSeev00900101] = (
        field(
            default=None,
            metadata={
                "name": "ClctnMtd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            },
        )
    )
    bck_end_odd_lot_scties_qty: Optional[UnitOrFaceAmountOrCode1ChoiceSeev00900101] = (
        field(
            default=None,
            metadata={
                "name": "BckEndOddLotSctiesQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            },
        )
    )
    frnt_end_odd_lot_scties_qty: Optional[UnitOrFaceAmountOrCode1ChoiceSeev00900101] = (
        field(
            default=None,
            metadata={
                "name": "FrntEndOddLotSctiesQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            },
        )
    )
    min_exrcbl_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MinExrcblSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    min_exrcbl_mltpl_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MinExrcblMltplSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    incrmtl_dnmtn: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "IncrmtlDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    new_dnmtn_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NewDnmtnSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    new_brd_lot_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NewBrdLotSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    scties_qty_sght: Optional[UnitOrFaceAmountOrCode1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "SctiesQtySght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    base_dnmtn: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "BaseDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    chng_tp: list[CorporateActionChangeType1FormatChoiceSeev00900101] = field(
        default_factory=list,
        metadata={
            "name": "ChngTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    offer_tp: list[OfferType1FormatChoiceSeev00900101] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rstrctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prtl_elctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlElctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    elctn_tp: Optional[ElectionMovementType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "ElctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ltry_tp: Optional[LotteryType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    incm_tp: Optional[GenericIdentification13Seev00900101] = field(
        default=None,
        metadata={
            "name": "IncmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    dvdd_tp: Optional[CorporateActionFrequencyType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "DvddTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecurityDistributionType1FormatChoiceSeev00900101
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    cpn_nb: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CpnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[0-9]{1,3}",
        },
    )
    intrst_acrd_nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstAcrdNbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    new_dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewDnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dt_dtls: Optional[CorporateActionDate2Seev00900101] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pric_dtls: list[CorporateActionPrice2Seev00900101] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod1Seev00900101] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate1Seev00900101] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    corp_actn_addtl_inf: Optional[CorporateActionNarrative1Seev00900101] = field(
        default=None,
        metadata={
            "name": "CorpActnAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    certfctn_reqrd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnReqrdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    certfctn_tp: Optional[BeneficiaryCertificationType1FormatChoiceSeev00900101] = (
        field(
            default=None,
            metadata={
                "name": "CertfctnTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            },
        )
    )
    cptl_gn: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "CptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    new_plc_of_incorprtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewPlcOfIncorprtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rnncbl_entitlmnt_sts_tp: Optional[RenounceableStatus1FormatChoiceSeev00900101] = (
        field(
            default=None,
            metadata={
                "name": "RnncblEntitlmntStsTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            },
        )
    )
    convs_tp: Optional[ConversionType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "ConvsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    red_chrgs_apld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RedChrgsApldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    dstrbtn_tp: Optional[DistributionType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "DstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionInformation2Seev00900101:
    agt_id: Optional[PartyIdentification2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    issr_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnPrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType2FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    evt_prcg_tp: Optional[
        CorporateActionEventProcessingType1FormatChoiceSeev00900101
    ] = field(
        default=None,
        metadata={
            "name": "EvtPrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary1FormatChoiceSeev00900101
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev00900101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    othr_undrlyg_scty: list[FinancialInstrumentDescription3Seev00900101] = field(
        default_factory=list,
        metadata={
            "name": "OthrUndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class SecurityOption1Seev00900101:
    scty_id: Optional[FinancialInstrumentDescription3Seev00900101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    min_exrcbl_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MinExrcblSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    min_exrcbl_mltpl_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "MinExrcblMltplSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    new_dnmtn_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NewDnmtnSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    new_brd_lot_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "NewBrdLotSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    shr_rnkg: Optional[ShareRanking1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "ShrRnkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_qty_for_sbcbd_rsltnt_scties: Optional[
        QuantityToQuantityRatio1Seev00900101
    ] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForSbcbdRsltntScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    dt_dtls: Optional[CorporateActionDate3Seev00900101] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pric_dtls: Optional[CorporateActionPrice4Seev00900101] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    tradg_prd: Optional[Period1Seev00900101] = field(
        default=None,
        metadata={
            "name": "TradgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_qty_for_exstg_scties: Optional[QuantityToQuantityRatio1Seev00900101] = field(
        default=None,
        metadata={
            "name": "AddtlQtyForExstgScties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    temp_fin_instrm_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempFinInstrmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class CorporateActionOption1Seev00900101:
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    optn_avlbty_sts: Optional[CorporateActionEventStatus2FormatChoiceSeev00900101] = (
        field(
            default=None,
            metadata={
                "name": "OptnAvlbtySts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
                "required": True,
            },
        )
    )
    certfctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    certfctn_tp: Optional[BeneficiaryCertificationType1FormatChoiceSeev00900101] = (
        field(
            default=None,
            metadata={
                "name": "CertfctnTp",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            },
        )
    )
    assntd_line_scty_id: Optional[SecurityIdentification7Seev00900101] = field(
        default=None,
        metadata={
            "name": "AssntdLineSctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    agt_scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgtSctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    agt_csh_acct_id: Optional[AccountIdentification2ChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "AgtCshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    offer_tp: list[OfferType1FormatChoiceSeev00900101] = field(
        default_factory=list,
        metadata={
            "name": "OfferTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecurityDistributionType1FormatChoiceSeev00900101
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    wdrwl_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WdrwlAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    chng_allwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChngAllwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    dt_dtls: Optional[CorporateActionDate4Seev00900101] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    rate_and_amt_dtls: Optional[CorporateActionRate2Seev00900101] = field(
        default=None,
        metadata={
            "name": "RateAndAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    pric_dtls: Optional[CorporateActionPrice1Seev00900101] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    prd_dtls: Optional[CorporateActionPeriod2Seev00900101] = field(
        default=None,
        metadata={
            "name": "PrdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    scties_mvmnt_dtls: list[SecurityOption1Seev00900101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    csh_mvmnt_dtls: list[CashOption1Seev00900101] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    corp_actn_othr_agt_dtls: list[CorporateActionAgent1Seev00900101] = field(
        default_factory=list,
        metadata={
            "name": "CorpActnOthrAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    frctn_dspstn: Optional[FractionDispositionType1FormatChoiceSeev00900101] = field(
        default=None,
        metadata={
            "name": "FrctnDspstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    red_chrgs_apld_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RedChrgsApldInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    optn_featrs: list[OptionFeatures1FormatChoiceSeev00900101] = field(
        default_factory=list,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    corp_actn_addtl_inf: Optional[CorporateActionNarrative1Seev00900101] = field(
        default=None,
        metadata={
            "name": "CorpActnAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class AgentCanotificationAdviceV01Seev00900101:
    class Meta:
        name = "AgentCANotificationAdviceV01"

    id: Optional[DocumentIdentification8Seev00900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    ntfctn_tp_and_lkg: Optional[LinkedCorporateAction1Seev00900101] = field(
        default=None,
        metadata={
            "name": "NtfctnTpAndLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    ntfctn_gnl_inf: Optional[CorporateActionNotification1Seev00900101] = field(
        default=None,
        metadata={
            "name": "NtfctnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionInformation2Seev00900101] = field(
        default=None,
        metadata={
            "name": "CorpActnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction2Seev00900101] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
            "required": True,
        },
    )
    corp_actn_optn_dtls: list[CorporateActionOption1Seev00900101] = field(
        default_factory=list,
        metadata={
            "name": "CorpActnOptnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    ctct_dtls: list[ContactPerson1Seev00900101] = field(
        default_factory=list,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative2Seev00900101] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01",
        },
    )


@dataclass
class Seev00900101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.009.001.01"

    agt_cantfctn_advc: Optional[AgentCanotificationAdviceV01Seev00900101] = field(
        default=None,
        metadata={
            "name": "AgtCANtfctnAdvc",
            "type": "Element",
            "required": True,
        },
    )
