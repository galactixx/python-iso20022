from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.camt_086_001_05.enums import (
    AccountLevel1Code,
    AccountLevel2Code,
    BalanceAdjustmentType1Code,
    BillingChargeMethod1Code,
    BillingCurrencyType1Code,
    BillingCurrencyType2Code,
    BillingStatementStatus1Code,
    BillingSubServiceQualifier1Code,
    BillingTaxCalculationMethod1Code,
    CompensationMethod1Code,
    ServiceAdjustmentType1Code,
    ServicePaymentMethod1Code,
    ServiceTaxDesignation1Code,
)
from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05"


@dataclass
class AccountSchemeName1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveOrHistoricCurrencyAndAmountCamt08600105(ISO20022MessageElement):
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
class BankTransactionCodeStructure6Camt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    sub_fmly_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubFmlyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class BillingBalanceType1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BillingCompensationType1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BillingRateIdentification1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BillingServiceCommonIdentification1Camt08600105(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )


@dataclass
class CashAccountType2ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyExchange6Camt08600105(ISO20022MessageElement):
    src_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trgt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 40,
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cmnts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class DatePeriod1Camt08600105(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt08600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Camt08600105(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class Pagination1Camt08600105(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class ProprietaryBankTransactionCodeStructure1Camt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ResidenceLocation1ChoiceCamt08600105(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    area: Optional[str] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TaxReason1Camt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )
    expltn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Expltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class AccountTax1Camt08600105(ISO20022MessageElement):
    clctn_mtd: Optional[BillingTaxCalculationMethod1Code] = field(
        default=None,
        metadata={
            "name": "ClctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    rgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 40,
        },
    )
    non_res_ctry: Optional[ResidenceLocation1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "NonResCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class AddressType3ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Camt08600105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class AmountAndDirection34Camt08600105(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt08600105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BankTransactionCodeStructure5Camt08600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    fmly: Optional[BankTransactionCodeStructure6Camt08600105] = field(
        default=None,
        metadata={
            "name": "Fmly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingRate1Camt08600105(ISO20022MessageElement):
    id: Optional[BillingRateIdentification1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    days_in_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysInPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    days_in_yr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysInYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class BillingSubServiceQualifier1ChoiceCamt08600105(ISO20022MessageElement):
    cd: Optional[BillingSubServiceQualifier1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt08600105(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Camt08600105(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class GenericAccountIdentification1Camt08600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt08600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Camt08600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountIdentification1Camt08600105(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class ReportHeader6Camt08600105(ISO20022MessageElement):
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_pgntn: Optional[Pagination1Camt08600105] = field(
        default=None,
        metadata={
            "name": "MsgPgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class ServiceTaxDesignation1Camt08600105(ISO20022MessageElement):
    cd: Optional[ServiceTaxDesignation1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    rgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_rsn: list[TaxReason1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "TaxRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt08600105(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BalanceAdjustment1Camt08600105(ISO20022MessageElement):
    tp: Optional[BalanceAdjustmentType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 105,
        },
    )
    bal_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "BalAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    avrg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "AvrgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    err_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ErrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    pstng_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Days",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    earngs_adjstmnt_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "EarngsAdjstmntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BankTransactionCodeStructure4Camt08600105(ISO20022MessageElement):
    domn: Optional[BankTransactionCodeStructure5Camt08600105] = field(
        default=None,
        metadata={
            "name": "Domn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    prtry: Optional[ProprietaryBankTransactionCodeStructure1Camt08600105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingBalance1Camt08600105(ISO20022MessageElement):
    tp: Optional[BillingBalanceType1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    val: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    ccy_tp: Optional[BillingCurrencyType1Code] = field(
        default=None,
        metadata={
            "name": "CcyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingCompensation1Camt08600105(ISO20022MessageElement):
    tp: Optional[BillingCompensationType1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    val: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    ccy_tp: Optional[BillingCurrencyType2Code] = field(
        default=None,
        metadata={
            "name": "CcyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingPrice1Camt08600105(ISO20022MessageElement):
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    unit_pric: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    mtd: Optional[BillingChargeMethod1Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    rule: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 20,
        },
    )


@dataclass
class BillingServicesAmount1Camt08600105(ISO20022MessageElement):
    hst_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "HstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    pricg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "PricgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingServicesAmount2Camt08600105(ISO20022MessageElement):
    hst_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "HstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    sttlm_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    pricg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "PricgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingServicesAmount3Camt08600105(ISO20022MessageElement):
    src_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "SrcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    hst_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "HstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingServicesTax1Camt08600105(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 40,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    hst_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "HstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    pricg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "PricgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingServicesTax2Camt08600105(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 40,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pricg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "PricgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingServicesTax3Camt08600105(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 40,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_tax_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingSubServiceIdentification1Camt08600105(ISO20022MessageElement):
    issr: Optional[BillingSubServiceQualifier1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BillingTaxIdentification3Camt08600105(ISO20022MessageElement):
    vatregn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "VATRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_ctct: Optional[Contact13Camt08600105] = field(
        default=None,
        metadata={
            "name": "TaxCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class FinancialInstitutionIdentification19Camt08600105(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt08600105] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class OrganisationIdentification39Camt08600105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class PostalAddress27Camt08600105(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BillingMethod1Camt08600105(ISO20022MessageElement):
    svc_chrg_hst_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "SvcChrgHstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    svc_tax: Optional[BillingServicesAmount1Camt08600105] = field(
        default=None,
        metadata={
            "name": "SvcTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    ttl_chrg: Optional[BillingServicesAmount2Camt08600105] = field(
        default=None,
        metadata={
            "name": "TtlChrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    tax_id: list[BillingServicesTax1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )


@dataclass
class BillingMethod2Camt08600105(ISO20022MessageElement):
    svc_chrg_hst_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "SvcChrgHstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    svc_tax: Optional[BillingServicesAmount1Camt08600105] = field(
        default=None,
        metadata={
            "name": "SvcTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    tax_id: list[BillingServicesTax1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )


@dataclass
class BillingMethod3Camt08600105(ISO20022MessageElement):
    svc_tax_pric_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "SvcTaxPricAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    tax_id: list[BillingServicesTax2Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )


@dataclass
class BillingServiceAdjustment1Camt08600105(ISO20022MessageElement):
    tp: Optional[ServiceAdjustmentType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    bal_reqrd_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "BalReqrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    err_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ErrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    adjstmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjstmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_svc: Optional[BillingSubServiceIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "SubSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    pric_chng: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "PricChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    orgnl_pric: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "OrgnlPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    new_pric: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "NewPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    vol_chng: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VolChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    orgnl_vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OrgnlVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    new_vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NewVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    orgnl_chrg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "OrgnlChrgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    new_chrg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "NewChrgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingServiceIdentification2Camt08600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_svc: Optional[BillingSubServiceIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "SubSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BillingServiceIdentification3Camt08600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_svc: Optional[BillingSubServiceIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "SubSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    cmon_cd: Optional[BillingServiceCommonIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "CmonCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    bk_tx_cd: Optional[BankTransactionCodeStructure4Camt08600105] = field(
        default=None,
        metadata={
            "name": "BkTxCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    svc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 12,
        },
    )


@dataclass
class BranchData5Camt08600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt08600105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class CashAccount40Camt08600105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    tp: Optional[CashAccountType2ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Camt08600105(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt08600105] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt08600105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt08600105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class Party56ChoiceCamt08600105(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Camt08600105] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    fiid: Optional[FinancialInstitutionIdentification19Camt08600105] = field(
        default=None,
        metadata={
            "name": "FIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class TaxCalculation1Camt08600105(ISO20022MessageElement):
    hst_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    taxbl_svc_chrg_convs: list[BillingServicesAmount3Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "TaxblSvcChrgConvs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
        },
    )
    ttl_taxbl_svc_chrg_hst_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "TtlTaxblSvcChrgHstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    tax_id: list[BillingServicesTax3Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    ttl_tax: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "TtlTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingMethod1ChoiceCamt08600105(ISO20022MessageElement):
    mtd_a: Optional[BillingMethod1Camt08600105] = field(
        default=None,
        metadata={
            "name": "MtdA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    mtd_b: Optional[BillingMethod2Camt08600105] = field(
        default=None,
        metadata={
            "name": "MtdB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    mtd_d: Optional[BillingMethod3Camt08600105] = field(
        default=None,
        metadata={
            "name": "MtdD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingServiceParameters2Camt08600105(ISO20022MessageElement):
    bk_svc: Optional[BillingServiceIdentification2Camt08600105] = field(
        default=None,
        metadata={
            "name": "BkSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    unit_pric: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    svc_chrg_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "SvcChrgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingServiceParameters3Camt08600105(ISO20022MessageElement):
    bk_svc: Optional[BillingServiceIdentification3Camt08600105] = field(
        default=None,
        metadata={
            "name": "BkSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    vol: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Camt08600105(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Camt08600105] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Camt08600105] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class PartyIdentification273Camt08600105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    lgl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt08600105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    id: Optional[Party56ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Camt08600105] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingMethod4Camt08600105(ISO20022MessageElement):
    svc_dtl: list[BillingServiceParameters2Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "SvcDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
        },
    )
    tax_clctn: Optional[TaxCalculation1Camt08600105] = field(
        default=None,
        metadata={
            "name": "TaxClctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingService2Camt08600105(ISO20022MessageElement):
    svc_dtl: Optional[BillingServiceParameters3Camt08600105] = field(
        default=None,
        metadata={
            "name": "SvcDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    pric: Optional[BillingPrice1Camt08600105] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    pmt_mtd: Optional[ServicePaymentMethod1Code] = field(
        default=None,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    orgnl_chrg_pric: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "OrgnlChrgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    orgnl_chrg_sttlm_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "OrgnlChrgSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    bal_reqrd_acct_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "BalReqrdAcctAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    tax_dsgnt: Optional[ServiceTaxDesignation1Camt08600105] = field(
        default=None,
        metadata={
            "name": "TaxDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    tax_clctn: Optional[BillingMethod1ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "TaxClctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class ParentCashAccount5Camt08600105(ISO20022MessageElement):
    lvl: Optional[AccountLevel1Code] = field(
        default=None,
        metadata={
            "name": "Lvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    id: Optional[CashAccount40Camt08600105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    svcr: Optional[BranchAndFinancialInstitutionIdentification8Camt08600105] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class BillingTaxRegion3Camt08600105(ISO20022MessageElement):
    rgn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    rgn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    cstmr_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrTaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    pt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    sndg_fi: Optional[BillingTaxIdentification3Camt08600105] = field(
        default=None,
        metadata={
            "name": "SndgFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 40,
        },
    )
    mtd_c: Optional[BillingMethod4Camt08600105] = field(
        default=None,
        metadata={
            "name": "MtdC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    sttlm_amt: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    tax_due_to_rgn: Optional[AmountAndDirection34Camt08600105] = field(
        default=None,
        metadata={
            "name": "TaxDueToRgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class CashAccountCharacteristics5Camt08600105(ISO20022MessageElement):
    acct_lvl: Optional[AccountLevel2Code] = field(
        default=None,
        metadata={
            "name": "AcctLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccount40Camt08600105] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    acct_svcr: Optional[BranchAndFinancialInstitutionIdentification8Camt08600105] = (
        field(
            default=None,
            metadata={
                "name": "AcctSvcr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            },
        )
    )
    prnt_acct: Optional[ParentCashAccount5Camt08600105] = field(
        default=None,
        metadata={
            "name": "PrntAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    compstn_mtd: Optional[CompensationMethod1Code] = field(
        default=None,
        metadata={
            "name": "CompstnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    dbt_acct: Optional[AccountIdentification4ChoiceCamt08600105] = field(
        default=None,
        metadata={
            "name": "DbtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    delyd_dbt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DelydDbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    sttlm_advc: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_length": 1,
            "max_length": 105,
        },
    )
    acct_bal_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctBalCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sttlm_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    hst_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tax: Optional[AccountTax1Camt08600105] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    acct_svcr_ctct: Optional[Contact13Camt08600105] = field(
        default=None,
        metadata={
            "name": "AcctSvcrCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )


@dataclass
class BillingStatement5Camt08600105(ISO20022MessageElement):
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    fr_to_dt: Optional[DatePeriod1Camt08600105] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    sts: Optional[BillingStatementStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    acct_chrtcs: Optional[CashAccountCharacteristics5Camt08600105] = field(
        default=None,
        metadata={
            "name": "AcctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    rate_data: list[BillingRate1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "RateData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    ccy_xchg: list[CurrencyExchange6Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "CcyXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    bal: list[BillingBalance1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    compstn: list[BillingCompensation1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "Compstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    svc: list[BillingService2Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "Svc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    tax_rgn: list[BillingTaxRegion3Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "TaxRgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    bal_adjstmnt: list[BalanceAdjustment1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "BalAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )
    svc_adjstmnt: list[BillingServiceAdjustment1Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "SvcAdjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
        },
    )


@dataclass
class StatementGroup5Camt08600105(ISO20022MessageElement):
    grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sndr: Optional[PartyIdentification273Camt08600105] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    sndr_indv_ctct: list[Contact13Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "SndrIndvCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "max_occurs": 2,
        },
    )
    rcvr: Optional[PartyIdentification273Camt08600105] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    rcvr_indv_ctct: list[Contact13Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "RcvrIndvCtct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "max_occurs": 2,
        },
    )
    bllg_stmt: list[BillingStatement5Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "BllgStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
        },
    )


@dataclass
class BankServicesBillingStatementV05Camt08600105(ISO20022MessageElement):
    rpt_hdr: Optional[ReportHeader6Camt08600105] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "required": True,
        },
    )
    bllg_stmt_grp: list[StatementGroup5Camt08600105] = field(
        default_factory=list,
        metadata={
            "name": "BllgStmtGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05",
            "min_occurs": 1,
        },
    )


@dataclass
class Camt08600105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05"

    bk_svcs_bllg_stmt: Optional[BankServicesBillingStatementV05Camt08600105] = field(
        default=None,
        metadata={
            "name": "BkSvcsBllgStmt",
            "type": "Element",
            "required": True,
        },
    )
