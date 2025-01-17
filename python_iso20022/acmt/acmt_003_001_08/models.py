from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.acmt.acmt_003_001_08.enums import (
    AccountStatusUpdateInstruction1Code,
    AccountStatusUpdateRequestReason1Code,
    DataModification2Code,
)
from python_iso20022.acmt.enums import (
    AccountingStatus1Code,
    AccountOwnershipType4Code,
    AccountUsageType2Code,
    BlockedReason2Code,
    CashAccountType5Code,
    CertificateType2Code,
    CivilStatus1Code,
    Collateral1Code,
    CommunicationMethod1Code,
    CompanyLink1Code,
    ConsolidationType1Code,
    CrsformType1Code,
    CrssourceStatus1Code,
    Crsstatus1Code,
    Eligible1Code,
    EventFrequency9Code,
    EventFrequency10Code,
    FatcaformType1Code,
    FatcasourceStatus1Code,
    Fatcastatus1Code,
    FundCashAccount4Code,
    FundIntention1Code,
    FundOwnership1Code,
    GdprdataConsent1Code,
    Gender1Code,
    Holding1Code,
    InformationDistribution2Code,
    Insurance1Code,
    InvestmentAccountCategory1Code,
    InvestmentFundRole6Code,
    InvestmentFundRole7Code,
    InvestmentFundTransactionType1Code,
    InvestorProfileStatus1Code,
    KnowYourCustomerCheckType1Code,
    LevelOfControl1Code,
    Liability1Code,
    MailType1Code,
    MoneyLaunderingCheck1Code,
    OperationalStatus1Code,
    OrganisationType1Code,
    PartyRole1Code,
    PlanStatus1Code,
    PoliticalExposureType2Code,
    PoliticallyExposedPersonStatus1Code,
    PositionEffect3Code,
    ProfileType1Code,
    Provided1Code,
    Rank1Code,
    Referred1Code,
    RestrictionStatus1Code,
    RoundingDirection1Code,
    SettlementInstructionReason1Code,
    TaxExemptReason3Code,
    TaxWithholdingMethod3Code,
)
from python_iso20022.enums import (
    AddressType1Code,
    AddressType2Code,
    CardType1Code,
    ConductClassification1Code,
    CreditDebit3Code,
    DataModification1Code,
    DistributionPolicy1Code,
    EventFrequency1Code,
    EventFrequency8Code,
    FormOfSecurity1Code,
    IncomePreference2Code,
    NamePrefix1Code,
    NoReasonCode,
    OrderOriginatorEligibility1Code,
    PartyIdentificationType7Code,
    ResidentialStatus1Code,
    RiskLevel1Code,
    TransactionChannel2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08"


@dataclass
class AccountSchemeName1ChoiceAcmt00300108:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountAcmt00300108:
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
class ActiveCurrencyAndAmountAcmt00300108:
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
class CitizenshipInformation2Acmt00300108:
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    mnr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MnrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class ClearingSystemMemberIdentification4ChoiceAcmt00300108:
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"AU[0-9]{6,6}",
        },
    )


@dataclass
class DataBaseCheck1Acmt00300108:
    dbchck: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DBChck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime1ChoiceAcmt00300108:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class DateTimePeriod2Acmt00300108:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class DeMinimusApplicable1Acmt00300108:
    new_isse_prmssn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NewIssePrmssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class DeMinimusNotApplicable1Acmt00300108:
    rstrctd_prsn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RstrctdPrsnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Extension1Acmt00300108:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FiscalYear1ChoiceAcmt00300108:
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class GenericIdentification1Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceAcmt00300108:
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketPracticeVersion1Acmt00300108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class OwnershipBeneficiaryRate1Acmt00300108:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    frctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Frctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonalInformation1Acmt00300108:
    nm_of_fthr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmOfFthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdn_nm_of_mthr: Optional[str] = field(
        default=None,
        metadata={
            "name": "MdnNmOfMthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm_of_prtnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmOfPrtnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RegulatoryInformation1Acmt00300108:
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Grp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Account23Acmt00300108:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_acct_dtls: Optional[GenericIdentification1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "RltdAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountDesignation1ChoiceAcmt00300108:
    cd: Optional[Rank1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountStatusUpdateInstruction1ChoiceAcmt00300108:
    cd: Optional[AccountStatusUpdateInstruction1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountStatusUpdateInstructionReason2ChoiceAcmt00300108:
    cd: Optional[AccountStatusUpdateRequestReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountType2ChoiceAcmt00300108:
    cd: Optional[FundCashAccount4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountUsageType2ChoiceAcmt00300108:
    cd: Optional[AccountUsageType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountingStatus1ChoiceAcmt00300108:
    cd: Optional[AccountingStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AddressType1ChoiceAcmt00300108:
    cd: Optional[AddressType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AddressType2ChoiceAcmt00300108:
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AlternateSecurityIdentification7Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class BlockedHoldingDetails2Acmt00300108:
    blckd_hldg: Optional[Holding1Code] = field(
        default=None,
        metadata={
            "name": "BlckdHldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    prtl_hldg_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrtlHldgUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    hldg_cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgCertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BlockedReason2ChoiceAcmt00300108:
    cd: Optional[BlockedReason2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Crsform1ChoiceAcmt00300108:
    class Meta:
        name = "CRSForm1Choice"

    cd: Optional[CrsformType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Crssource1ChoiceAcmt00300108:
    class Meta:
        name = "CRSSource1Choice"

    cd: Optional[CrssourceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Crsstatus3ChoiceAcmt00300108:
    class Meta:
        name = "CRSStatus3Choice"

    cd: Optional[Crsstatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class CashAccountType3ChoiceAcmt00300108:
    cd: Optional[CashAccountType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class CertificationType1ChoiceAcmt00300108:
    cd: Optional[CertificateType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class CivilStatus1ChoiceAcmt00300108:
    cd: Optional[CivilStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class CommunicationMethod3ChoiceAcmt00300108:
    cd: Optional[CommunicationMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class CompanyLink1ChoiceAcmt00300108:
    cd: Optional[CompanyLink1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ConsolidationType1ChoiceAcmt00300108:
    cd: Optional[ConsolidationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class CountryAndResidentialStatusType2Acmt00300108:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    resdtl_sts: Optional[ResidentialStatus1Code] = field(
        default=None,
        metadata={
            "name": "ResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class CustomerConductClassification1ChoiceAcmt00300108:
    cd: Optional[ConductClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class DateAndAmount1Acmt00300108:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class DeMinimus1ChoiceAcmt00300108:
    de_mnms_aplbl: Optional[DeMinimusApplicable1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "DeMnmsAplbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    de_mnms_not_aplbl: Optional[DeMinimusNotApplicable1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "DeMnmsNotAplbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Fatcaform1ChoiceAcmt00300108:
    class Meta:
        name = "FATCAForm1Choice"

    cd: Optional[FatcaformType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Fatcasource1ChoiceAcmt00300108:
    class Meta:
        name = "FATCASource1Choice"

    cd: Optional[FatcasourceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Fatcastatus2ChoiceAcmt00300108:
    class Meta:
        name = "FATCAStatus2Choice"

    cd: Optional[Fatcastatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Frequency20ChoiceAcmt00300108:
    cd: Optional[EventFrequency8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class GdprdataConsent1ChoiceAcmt00300108:
    class Meta:
        name = "GDPRDataConsent1Choice"

    cd: Optional[GdprdataConsent1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class GenericAccountIdentification1Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IndividualPerson35Acmt00300108:
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    gndr: Optional[Gender1Code] = field(
        default=None,
        metadata={
            "name": "Gndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InformationDistribution1ChoiceAcmt00300108:
    cd: Optional[InformationDistribution2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InitialAmount1ChoiceAcmt00300108:
    initl_nb_of_instlmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitlNbOfInstlmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InsuranceType2ChoiceAcmt00300108:
    cd: Optional[Insurance1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InvestmentAccountCategory1ChoiceAcmt00300108:
    cd: Optional[InvestmentAccountCategory1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InvestorProfileStatus1ChoiceAcmt00300108:
    cd: Optional[InvestorProfileStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class KyccheckType1ChoiceAcmt00300108:
    class Meta:
        name = "KYCCheckType1Choice"

    cd: Optional[KnowYourCustomerCheckType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class LetterIntent1Acmt00300108:
    lttr_intt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LttrInttRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class LevelOfControl1ChoiceAcmt00300108:
    cd: Optional[LevelOfControl1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Liability1ChoiceAcmt00300108:
    cd: Optional[Liability1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class MailType1ChoiceAcmt00300108:
    cd: Optional[MailType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class MarketMakerProfile2Acmt00300108:
    ctrct_prd: Optional[DateTimePeriod2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "CtrctPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cmplc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cmplc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    max_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Dscnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class MiFidclassification1Acmt00300108:
    class Meta:
        name = "MiFIDClassification1"

    clssfctn: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ModificationScope39Acmt00300108:
    mod_scp_indctn: Optional[DataModification2Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    ctznsh: Optional[CitizenshipInformation2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Ctznsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class MoneyLaunderingCheck1ChoiceAcmt00300108:
    cd: Optional[MoneyLaunderingCheck1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class NamePrefix1ChoiceAcmt00300108:
    cd: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class OrganisationType1ChoiceAcmt00300108:
    cd: Optional[OrganisationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class OtherIdentification3ChoiceAcmt00300108:
    cd: Optional[PartyIdentificationType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class OwnershipType2ChoiceAcmt00300108:
    cd: Optional[AccountOwnershipType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PartyIdentification177ChoiceAcmt00300108:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PartyRole2ChoiceAcmt00300108:
    cd: Optional[InvestmentFundRole6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PartyRole4ChoiceAcmt00300108:
    cd: Optional[InvestmentFundRole7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PartyRole5ChoiceAcmt00300108:
    cd: Optional[PartyRole1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PlanStatus2ChoiceAcmt00300108:
    cd: Optional[PlanStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PoliticalExposureType2ChoiceAcmt00300108:
    cd: Optional[PoliticalExposureType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PoliticallyExposedPersonStatus1ChoiceAcmt00300108:
    cd: Optional[PoliticallyExposedPersonStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PostalAddress1Acmt00300108:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProfileType1ChoiceAcmt00300108:
    cd: Optional[ProfileType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class RestrictionStatus1ChoiceAcmt00300108:
    cd: Optional[RestrictionStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class RiskLevel2ChoiceAcmt00300108:
    cd: Optional[RiskLevel1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class RoundingParameters1Acmt00300108:
    rndg_mdlus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RndgMdlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    rndg_drctn: Optional[RoundingDirection1Code] = field(
        default=None,
        metadata={
            "name": "RndgDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class SettlementFrequency1ChoiceAcmt00300108:
    cd: Optional[EventFrequency10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class SettlementInstructionReason1ChoiceAcmt00300108:
    cd: Optional[SettlementInstructionReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class StatementFrequencyReason2ChoiceAcmt00300108:
    cd: Optional[EventFrequency9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class TaxExemptionReason2ChoiceAcmt00300108:
    cd: Optional[TaxExemptReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class TransactionChannelType1ChoiceAcmt00300108:
    cd: Optional[TransactionChannel2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class TransactionType5ChoiceAcmt00300108:
    cd: Optional[InvestmentFundTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtry: Optional[GenericIdentification47Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class UnitsOrAmount1ChoiceAcmt00300108:
    amt: Optional[ActiveCurrencyAndAmountAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class UnitsOrAmountOrPercentage1ChoiceAcmt00300108:
    amt: Optional[ActiveCurrencyAndAmountAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AccountIdentification4ChoiceAcmt00300108:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountStatusUpdateInstructionReason1Acmt00300108:
    cd: Optional[AccountStatusUpdateInstructionReason2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class BlockedStatusReason2Acmt00300108:
    tx_tp: Optional[TransactionType5ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    blckd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Blckd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    rsn: list[BlockedReason2ChoiceAcmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class BranchData4Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: Optional[PostalAddress1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Crsstatus4Acmt00300108:
    class Meta:
        name = "CRSStatus4"

    tp: Optional[Crsstatus3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    src: Optional[Crssource1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Src",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    xcptnl_rptg_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "XcptnlRptgCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class CommunicationAddress6Acmt00300108:
    adr_tp: Optional[AddressType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mob",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    tlx_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TlxAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class Fatcastatus2Acmt00300108:
    class Meta:
        name = "FATCAStatus2"

    tp: Optional[Fatcastatus2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    src: Optional[Fatcasource1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Src",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Gdprdata1Acmt00300108:
    class Meta:
        name = "GDPRData1"

    cnsnt_tp: Optional[GdprdataConsent1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CnsntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    cnsnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CnsntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    cnsnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CnsntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class GenericIdentification81Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[OtherIdentification3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class GenericIdentification82Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[OtherIdentification3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    issr_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class HighFrequencyTradingProfile1Acmt00300108:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    sttlm_frqcy: Optional[SettlementFrequency1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "SttlmFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cnsldtn_tp: Optional[ConsolidationType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CnsldtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class NameAndAddress4Acmt00300108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Acmt00300108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class NewIssueAllocation2Acmt00300108:
    rstrctd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Rstrctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    xmpt_prsn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmptPrsnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    de_mnms: Optional[DeMinimus1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "DeMnms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Notification2Acmt00300108:
    ntfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    dstrbtn_tp: Optional[InformationDistribution1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "DstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PartyProfileInformation5Acmt00300108:
    certfctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    vldtng_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "VldtngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    chckng_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rspnsbl_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnsblPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    cert_tp: Optional[CertificationType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CertTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    chckng_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ChckngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    chckng_frqcy: Optional[EventFrequency1Code] = field(
        default=None,
        metadata={
            "name": "ChckngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    nxt_rvsn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtRvsnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    slry_rg: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlryRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    src_of_wlth: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrcOfWlth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    cstmr_cndct_clssfctn: Optional[CustomerConductClassification1ChoiceAcmt00300108] = (
        field(
            default=None,
            metadata={
                "name": "CstmrCndctClssfctn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            },
        )
    )
    rsk_lvl: Optional[RiskLevel2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "RskLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    know_your_cstmr_chck_tp: Optional[KyccheckType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "KnowYourCstmrChckTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    know_your_cstmr_dbchck: Optional[DataBaseCheck1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "KnowYourCstmrDBChck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PoliticallyExposedPerson1Acmt00300108:
    pltcly_xpsd_prsn_tp: Optional[PoliticalExposureType2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "PltclyXpsdPrsnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    pltcly_xpsd_prsn_sts: Optional[
        PoliticallyExposedPersonStatus1ChoiceAcmt00300108
    ] = field(
        default=None,
        metadata={
            "name": "PltclyXpsdPrsnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PostalAddress21Acmt00300108:
    adr_tp: Optional[AddressType2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    mlng_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MlngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    regn_adr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RegnAdrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 10,
        },
    )
    sd_in_bldg: Optional[str] = field(
        default=None,
        metadata={
            "name": "SdInBldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    suite_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SuiteId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 10,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vllg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vllg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Stat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecurityIdentification25ChoiceAcmt00300108:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Acmt00300108] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class TreasuryProfile1Acmt00300108:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    tradr_tp: Optional[PartyRole5ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TradrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class AccountIdentificationAndName5Acmt00300108:
    id: Optional[AccountIdentification4ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountStatusUpdateInstructionReason1ChoiceAcmt00300108:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    rsn: list[AccountStatusUpdateInstructionReason1Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class BlockedStatusReason2ChoiceAcmt00300108:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    rsn: list[BlockedStatusReason2Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Cheque4Acmt00300108:
    pyee_id: Optional[NameAndAddress5Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class FinancialInstitutionIdentification11ChoiceAcmt00300108:
    nm_and_adr: Optional[NameAndAddress5Acmt00300108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification4ChoiceAcmt00300108] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            },
        )
    )
    prtry_id: Optional[SimpleIdentificationInformation4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class FinancialInstrument55Acmt00300108:
    id: Optional[SecurityIdentification25ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class IndividualPerson29Acmt00300108:
    nm_prfx: Optional[NamePrefix1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    pstl_adr: list[PostalAddress21Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )


@dataclass
class IndividualPersonIdentification3ChoiceAcmt00300108:
    id_nb: Optional[GenericIdentification81Acmt00300108] = field(
        default=None,
        metadata={
            "name": "IdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prsn_nm: Optional[IndividualPerson35Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PrsnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InvestorProfile2Acmt00300108:
    tp: Optional[ProfileType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    sts: Optional[InvestorProfileStatus1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    trsr: Optional[TreasuryProfile1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Trsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    hgh_frqcy_tradg: Optional[HighFrequencyTradingProfile1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "HghFrqcyTradg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    mkt_makr: Optional[MarketMakerProfile2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "MktMakr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ModificationScope21Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    isse_allcn: Optional[NewIssueAllocation2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "IsseAllcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class ModificationScope27Acmt00300108:
    mod_scp_indctn: Optional[DataModification2Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    invstr_prfl_vldtn: Optional[PartyProfileInformation5Acmt00300108] = field(
        default=None,
        metadata={
            "name": "InvstrPrflVldtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class ModificationScope34Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    pstl_adr: Optional[PostalAddress21Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class NameAndAddress15Acmt00300108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    pstl_adr: Optional[PostalAddress21Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Organisation23Acmt00300108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: list[PostalAddress21Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )


@dataclass
class PartyIdentification125ChoiceAcmt00300108:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Acmt00300108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Account32Acmt00300108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class AccountStatusUpdateInstruction1Acmt00300108:
    upd_instr: Optional[AccountStatusUpdateInstruction1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "UpdInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    upd_instr_rsn: Optional[AccountStatusUpdateInstructionReason1ChoiceAcmt00300108] = (
        field(
            default=None,
            metadata={
                "name": "UpdInstrRsn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            },
        )
    )


@dataclass
class AdditionalReference13Acmt00300108:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditiononalInformation13Acmt00300108:
    lmttn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lmttn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    acct_vldtn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctVldtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rgltr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Rgltr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    sts: Optional[RestrictionStatus1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prd: Optional[DateTimePeriod2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class CashAccount204Acmt00300108:
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    id: Optional[AccountIdentificationAndName5Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_svcr: Optional[FinancialInstitutionIdentification11ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_svcr_brnch: Optional[BranchData4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctSvcrBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_ownr_othr_id: list[GenericIdentification82Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "AcctOwnrOthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    invstmt_acct_tp: Optional[AccountType2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    sttlm_instr_rsn: Optional[SettlementInstructionReason1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "SttlmInstrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    csh_acct_purp: Optional[CashAccountType3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CshAcctPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    csh_acct_dsgnt: Optional[AccountDesignation1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CshAcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dvdd_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DvddPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("100"),
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class DirectDebitMandate7Acmt00300108:
    dbtr_acct: Optional[AccountIdentificationAndName5Acmt00300108] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    dbtr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dbtr_tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrTaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrNtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdtr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification11ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    dbtr_agt_brnch: Optional[BranchData4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "DbtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification11ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cdtr_agt_brnch: Optional[BranchData4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "CdtrAgtBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentToSend4Acmt00300108:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    rcpt: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    mtd_of_trnsmssn: Optional[CommunicationMethod3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "MtdOfTrnsmssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class IndividualPerson38Acmt00300108:
    nm_prfx: Optional[NamePrefix1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mddl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MddlNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    nm_sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmSfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    gndr: Optional[Gender1Code] = field(
        default=None,
        metadata={
            "name": "Gndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prfssn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prfssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    modfd_pstl_adr: list[ModificationScope34Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdPstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_ctznsh: list[ModificationScope39Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdCtznsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 3,
        },
    )
    emplng_cpny: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmplngCpny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    biz_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pltcly_xpsd_prsn: Optional[PoliticallyExposedPerson1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PltclyXpsdPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cvl_sts: Optional[CivilStatus1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CvlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    edctn_lvl: Optional[str] = field(
        default=None,
        metadata={
            "name": "EdctnLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fmly_inf: Optional[PersonalInformation1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "FmlyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    gdprdata: list[Gdprdata1Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "GDPRData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ModificationScope46Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    invstr_prfl: Optional[InvestorProfile2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "InvstrPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class Organisation40Acmt00300108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[PartyIdentification177ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_pstl_adr: list[ModificationScope34Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdPstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tp_of_org: Optional[OrganisationType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TpOfOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    plc_of_listg: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )


@dataclass
class PartyIdentification182ChoiceAcmt00300108:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    nm_and_adr: Optional[NameAndAddress15Acmt00300108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard29Acmt00300108:
    tp: Optional[CardType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    hldr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    start_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    xpry_dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    card_issr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardIssrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    card_issr_id: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CardIssrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    scty_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class PaymentInstrument19ChoiceAcmt00300108:
    chq_dtls: Optional[Cheque4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    bkrs_drft_dtls: Optional[Cheque4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "BkrsDrftDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ReferredAgent3Acmt00300108:
    rfrd: Optional[Referred1Code] = field(
        default=None,
        metadata={
            "name": "Rfrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    rfrd_plcmnt_agt: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "RfrdPlcmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class RegisteredShareholderName1ChoiceAcmt00300108:
    indv_prsn: Optional[IndividualPerson29Acmt00300108] = field(
        default=None,
        metadata={
            "name": "IndvPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    org: Optional[Organisation23Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Org",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ThirdPartyRights2Acmt00300108:
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    hldr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Hldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrument87Acmt00300108:
    id: Optional[SecurityIdentification25ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    blckd_hldg_dtls: Optional[BlockedHoldingDetails2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "BlckdHldgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    pldgg: Optional[Eligible1Code] = field(
        default=None,
        metadata={
            "name": "Pldgg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    coll: Optional[Collateral1Code] = field(
        default=None,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    thrd_pty_rghts: Optional[ThirdPartyRights2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "ThrdPtyRghts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    fnd_ownrsh: Optional[FundOwnership1Code] = field(
        default=None,
        metadata={
            "name": "FndOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    fnd_intntn: Optional[FundIntention1Code] = field(
        default=None,
        metadata={
            "name": "FndIntntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    oprl_sts: Optional[OperationalStatus1Code] = field(
        default=None,
        metadata={
            "name": "OprlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Intermediary46Acmt00300108:
    id: Optional[PartyIdentification177ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    acct: Optional[Account32Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    wvd_trlr_comssn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WvdTrlrComssnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    role: Optional[PartyRole2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    pmry_com_adr: list[CommunicationAddress6Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "PmryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    scndry_com_adr: list[CommunicationAddress6Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ScndryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    nm_and_adr: Optional[NameAndAddress4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Intermediary47Acmt00300108:
    id: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    acct: Optional[Account32Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InvestmentAccountModification4Acmt00300108:
    mod_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    acct_appl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_ref: Optional[AdditionalReference13Acmt00300108] = field(
        default=None,
        metadata={
            "name": "CtrPtyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    exstg_acct_id: list[Account23Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ExstgAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ModificationScope43Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    plcmnt: Optional[ReferredAgent3Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Plcmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class ModificationScope44Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    svc_lvl_agrmt: Optional[DocumentToSend4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "SvcLvlAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class ModificationScope45Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    addtl_inf: list[AdditiononalInformation13Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_occurs": 1,
        },
    )


@dataclass
class Party48ChoiceAcmt00300108:
    org: Optional[Organisation40Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Org",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    indv_prsn: Optional[IndividualPerson38Acmt00300108] = field(
        default=None,
        metadata={
            "name": "IndvPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class PartyIdentification220Acmt00300108:
    id: Optional[PartyIdentification182ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PaymentInstrument24ChoiceAcmt00300108:
    pmt_card_dtls: Optional[PaymentCard29Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PmtCardDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    drct_dbt_dtls: Optional[DirectDebitMandate7Acmt00300108] = field(
        default=None,
        metadata={
            "name": "DrctDbtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    chq: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Chq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    bkrs_drft: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BkrsDrft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class TaxReporting3Acmt00300108:
    taxtn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tax_pyer: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TaxPyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tax_rcpt: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TaxRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    csh_acct_dtls: Optional[CashAccount204Acmt00300108] = field(
        default=None,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AccountOwner3ChoiceAcmt00300108:
    indv_ownr_id: Optional[IndividualPersonIdentification3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "IndvOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    org_ownr_id: Optional[PartyIdentification220Acmt00300108] = field(
        default=None,
        metadata={
            "name": "OrgOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InvestmentAccountOwnershipInformation17Acmt00300108:
    pty: Optional[Party48ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    mny_lndrg_chck: Optional[MoneyLaunderingCheck1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "MnyLndrgChck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_invstr_prfl_vldtn: list[ModificationScope27Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdInvstrPrflVldtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ownrsh_bnfcry_rate: Optional[OwnershipBeneficiaryRate1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "OwnrshBnfcryRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    clnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fscl_xmptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FsclXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    sgntry_rght_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SgntryRghtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    mi_fidclssfctn: Optional[MiFidclassification1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "MiFIDClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ntfctn: list[Notification2Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Ntfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    fatcaform_tp: list[Fatcaform1ChoiceAcmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "FATCAFormTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    fatcasts: list[Fatcastatus2Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "FATCASts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    fatcarptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FATCARptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    crsform_tp: list[Crsform1ChoiceAcmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "CRSFormTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    crssts: list[Crsstatus4Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "CRSSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    crsrptg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CRSRptgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    othr_id: list[GenericIdentification82Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tax_xmptn: Optional[TaxExemptionReason2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TaxXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tax_rptg: list[TaxReporting3Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "TaxRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    mail_tp: Optional[MailType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "MailTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ctry_and_resdtl_sts: Optional[CountryAndResidentialStatusType2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "CtryAndResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    mntry_wlth: Optional[DateAndAmount1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "MntryWlth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    eqty_val: Optional[DateAndAmount1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "EqtyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    workg_cptl: Optional[DateAndAmount1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "WorkgCptl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    cpny_lk: Optional[CompanyLink1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "CpnyLk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    elctrnc_mlng_svc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncMlngSvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pmry_com_adr: list[CommunicationAddress6Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "PmryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    scndry_com_adr: list[CommunicationAddress6Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ScndryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    addtl_rgltry_inf: Optional[RegulatoryInformation1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "AddtlRgltryInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acctg_sts: Optional[AccountingStatus1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    addtl_inf: list[AdditiononalInformation13Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ctrlg_pty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtrlgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ModificationScope40Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    intrmy: Optional[Intermediary46Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class ModificationScope42Acmt00300108:
    mod_scp_indctn: Optional[DataModification2Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument87Acmt00300108] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class PaymentInstrument17Acmt00300108:
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dvdd_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DvddPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("100"),
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    sbcpt_pmt_instrm: Optional[PaymentInstrument24ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "SbcptPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    red_pmt_instrm: Optional[PaymentInstrument19ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "RedPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    dvdd_pmt_instrm: Optional[PaymentInstrument19ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "DvddPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    svgs_plan_pmt_instrm: Optional[PaymentInstrument24ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "SvgsPlanPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    intrst_pmt_instrm: Optional[PaymentInstrument19ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "IntrstPmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Reinvestment4Acmt00300108:
    fin_instrm_dtls: Optional[FinancialInstrument87Acmt00300108] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    rinvstmt_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RinvstmtPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class Repartition6Acmt00300108:
    qty: Optional[UnitsOrAmountOrPercentage1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    fin_instrm: Optional[FinancialInstrument87Acmt00300108] = field(
        default=None,
        metadata={
            "name": "FinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    ccy_of_plan: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOfPlan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class AccountParties13ChoiceAcmt00300108:
    pmry_ownr: Optional[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PmryOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    trstee: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Trstee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 5,
        },
    )
    nmnee: Optional[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default=None,
        metadata={
            "name": "Nmnee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    jnt_ownr: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "JntOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 5,
        },
    )


@dataclass
class CashSettlement4Acmt00300108:
    mod_scp_indctn: Optional[DataModification2Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    csh_acct_dtls: list[CashAccount204Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    othr_csh_sttlm_dtls: list[PaymentInstrument17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "OthrCshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ExtendedParty15Acmt00300108:
    xtnded_pty_role: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedPtyRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    othr_pty_dtls: Optional[InvestmentAccountOwnershipInformation17Acmt00300108] = (
        field(
            default=None,
            metadata={
                "name": "OthrPtyDtls",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
                "required": True,
            },
        )
    )


@dataclass
class InvestmentAccount75Acmt00300108:
    acct_sts_upd_instr: Optional[AccountStatusUpdateInstruction1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctStsUpdInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[AccountType2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ownrsh_tp: Optional[OwnershipType2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "OwnrshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tax_xmptn: Optional[TaxExemptionReason2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TaxXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    stmt_frqcy: Optional[StatementFrequencyReason2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "StmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ref_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    incm_pref: Optional[IncomePreference2Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    rinvstmt_dtls: list[Reinvestment4Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "RinvstmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tax_whldg_mtd: Optional[TaxWithholdingMethod3Code] = field(
        default=None,
        metadata={
            "name": "TaxWhldgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tax_rptg: list[TaxReporting3Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "TaxRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    lttr_intt_dtls: Optional[LetterIntent1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "LttrInttDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acmltn_rght_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcmltnRghtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqrd_sgntries_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReqrdSgntriesNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    fnd_fmly_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FndFmlyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    modfd_fin_instrm_dtls: list[ModificationScope42Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdFinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    rndg_dtls: Optional[RoundingParameters1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "RndgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_svcr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    blckd_sts: Optional[BlockedStatusReason2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "BlckdSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_usg_tp: Optional[AccountUsageType2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctUsgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    frgn_sts_certfctn: Optional[Provided1Code] = field(
        default=None,
        metadata={
            "name": "FrgnStsCertfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_sgntr_dt_tm: Optional[DateAndDateTime1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctSgntrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    tx_chanl_tp: Optional[TransactionChannelType1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "TxChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    invstmt_acct_ctgy: Optional[InvestmentAccountCategory1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    pldgg: Optional[Eligible1Code] = field(
        default=None,
        metadata={
            "name": "Pldgg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    coll: Optional[Collateral1Code] = field(
        default=None,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    thrd_pty_rghts: Optional[ThirdPartyRights2Acmt00300108] = field(
        default=None,
        metadata={
            "name": "ThrdPtyRghts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    pwr_of_attny_lvl_of_ctrl: Optional[LevelOfControl1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "PwrOfAttnyLvlOfCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acctg_sts: Optional[AccountingStatus1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    opng_dt: Optional[DateAndDateTime1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "OpngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    clsg_dt: Optional[DateAndDateTime1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    neg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NegInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prcg_ordr: Optional[PositionEffect3Code] = field(
        default=None,
        metadata={
            "name": "PrcgOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    lblty: Optional[Liability1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Lblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_invstr_prfl: list[ModificationScope46Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdInvstrPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    fscl_yr: Optional[FiscalYear1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "FsclYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InvestmentAccount76Acmt00300108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fnd_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "FndTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fnd_fmly_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FndFmlyNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    scty_dtls: Optional[FinancialInstrument55Acmt00300108] = field(
        default=None,
        metadata={
            "name": "SctyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_ownr: Optional[AccountOwner3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    intrmy: list[Intermediary47Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    acct_svcr: Optional[PartyIdentification125ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountParties18Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    prncpl_acct_pty: Optional[AccountParties13ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "PrncplAcctPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    scndry_ownr: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ScndryOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    bnfcry: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    pwr_of_attny: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "PwrOfAttny",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    lgl_guardn: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "LglGuardn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ctdn_for_mnr: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "CtdnForMnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    sucssr_on_dth: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "SucssrOnDth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    admstr: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Admstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    othr_pty: list[ExtendedParty15Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "OthrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    grntr: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Grntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    sttlr: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Sttlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    snr_mgg_offcl: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "SnrMggOffcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    prtctr: list[InvestmentAccountOwnershipInformation17Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Prtctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    regd_shrhldr_nm: Optional[RegisteredShareholderName1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "RegdShrhldrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class AccountSelection3ChoiceAcmt00300108:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_acct_selctn_data: Optional[InvestmentAccount76Acmt00300108] = field(
        default=None,
        metadata={
            "name": "OthrAcctSelctnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class InvestmentPlan16Acmt00300108:
    frqcy: Optional[Frequency20ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    qty: Optional[UnitsOrAmount1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    grss_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GrssAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    incm_pref: Optional[IncomePreference2Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    initl_amt: Optional[InitialAmount1ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "InitlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    ttl_nb_of_instlmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfInstlmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rndg_drctn: Optional[RoundingDirection1Code] = field(
        default=None,
        metadata={
            "name": "RndgDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    scty_dtls: list[Repartition6Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "SctyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_occurs": 1,
            "max_occurs": 50,
        },
    )
    modfd_csh_sttlm: list[CashSettlement4Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdCshSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 8,
        },
    )
    ctrct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_ctrct_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdCtrctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pdct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    slachrg_and_comssn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SLAChrgAndComssnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    insrnc_cover: Optional[InsuranceType2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "InsrncCover",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    plan_sts: Optional[PlanStatus2ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "PlanSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    instlmt_mgr_role: Optional[PartyRole4ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "InstlmtMgrRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class ModificationScope41Acmt00300108:
    mod_scp_indctn: Optional[DataModification1Code] = field(
        default=None,
        metadata={
            "name": "ModScpIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    invstmt_plan: Optional[InvestmentPlan16Acmt00300108] = field(
        default=None,
        metadata={
            "name": "InvstmtPlan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )


@dataclass
class AccountModificationInstructionV08Acmt00300108:
    msg_id: Optional[MessageIdentification1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    prvs_ref: Optional[AdditionalReference13Acmt00300108] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    instr_dtls: Optional[InvestmentAccountModification4Acmt00300108] = field(
        default=None,
        metadata={
            "name": "InstrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    invstmt_acct_selctn: Optional[AccountSelection3ChoiceAcmt00300108] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctSelctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "required": True,
        },
    )
    modfd_invstmt_acct: Optional[InvestmentAccount75Acmt00300108] = field(
        default=None,
        metadata={
            "name": "ModfdInvstmtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_acct_pties: list[AccountParties18Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdAcctPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_intrmies: list[ModificationScope40Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdIntrmies",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_plcmnt: Optional[ModificationScope43Acmt00300108] = field(
        default=None,
        metadata={
            "name": "ModfdPlcmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_isse_allcn: Optional[ModificationScope21Acmt00300108] = field(
        default=None,
        metadata={
            "name": "ModfdIsseAllcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    modfd_svgs_invstmt_plan: list[ModificationScope41Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdSvgsInvstmtPlan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 50,
        },
    )
    modfd_wdrwl_invstmt_plan: list[ModificationScope41Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdWdrwlInvstmtPlan",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 10,
        },
    )
    modfd_csh_sttlm: list[CashSettlement4Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdCshSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 8,
        },
    )
    modfd_svc_lvl_agrmt: list[ModificationScope44Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdSvcLvlAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
            "max_occurs": 30,
        },
    )
    modfd_addtl_inf: list[ModificationScope45Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "ModfdAddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    mkt_prctc_vrsn: Optional[MarketPracticeVersion1Acmt00300108] = field(
        default=None,
        metadata={
            "name": "MktPrctcVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )
    xtnsn: list[Extension1Acmt00300108] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
        },
    )


@dataclass
class Acmt00300108:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08"

    acct_mod_instr: Optional[AccountModificationInstructionV08Acmt00300108] = field(
        default=None,
        metadata={
            "name": "AcctModInstr",
            "type": "Element",
            "required": True,
        },
    )
