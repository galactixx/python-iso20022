from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.enums import (
    AddressType2Code,
    InvestmentFundFee1Code,
    NamePrefix1Code,
    NoReasonCode,
    PriceMethod1Code,
    TaxableIncomePerShareCalculated2Code,
    TaxationBasis2Code,
    TaxationBasis5Code,
    TaxType17Code,
    TypeOfPrice10Code,
    UktaxGroupUnit1Code,
    WaivingInstruction1Code,
)
from python_iso20022.sese.enums import (
    CashAssetType1Code,
    DrawdownType2Code,
    InvestmentFundRole8Code,
    OtherAmountType1Code,
    OtherAsset2Code,
    PersonIdentificationType7Code,
)
from python_iso20022.sese.sese_011_001_09.enums import (
    ApplicableRules1Code,
    BeneficiaryType1Code,
    CancelledStatusReason3Code,
    PendingSettlementStatusReason2Code,
    RejectedStatusReason13Code,
    TransferStatus6Code,
    TransferStatusType2Code,
    TransferUnmatchedReason3Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09"


@dataclass
class AccountSchemeName1ChoiceSese01100109:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountSese01100109:
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
class ActiveCurrencyAndAmountSese01100109:
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSese01100109:
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
class ActiveOrHistoricCurrencyAndAmountSese01100109:
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
class ClearingSystemMemberIdentification2ChoiceSese01100109:
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    inifsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "INIFSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"IN[a-zA-Z0-9]{11,11}",
        },
    )
    grhebic: Optional[str] = field(
        default=None,
        metadata={
            "name": "GRHEBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"GR[0-9]{7,7}",
        },
    )
    plknr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PLKNR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"PL[0-9]{8,8}",
        },
    )
    othr_clr_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClrCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification4ChoiceSese01100109:
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"AU[0-9]{6,6}",
        },
    )


@dataclass
class DateFormat42ChoiceSese01100109:
    yr_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YrMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    yr_mnth_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "YrMnthDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Extension1Sese01100109:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceSese01100109:
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketPracticeVersion1Sese01100109:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )


@dataclass
class SubAccount5Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalInformation15Sese01100109:
    inf_tp: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AlternateSecurityIdentification7Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )


@dataclass
class ApplicableRules1ChoiceSese01100109:
    cd: Optional[ApplicableRules1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class BeneficiaryType1ChoiceSese01100109:
    cd: Optional[BeneficiaryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class CancellationPendingStatus7ChoiceSese01100109:
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    data_src_schme: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DataSrcSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class CancelledStatus13ChoiceSese01100109:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    rsn: Optional[CancelledStatusReason3Code] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    xtnded_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    data_src_schme: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DataSrcSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class CashAssetType1ChoiceSese01100109:
    cd: Optional[CashAssetType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class ChargeBasis2ChoiceSese01100109:
    cd: Optional[TaxationBasis5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class ChargeType5ChoiceSese01100109:
    cd: Optional[InvestmentFundFee1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class ClassificationType32ChoiceSese01100109:
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class ContactIdentification2Sese01100109:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DrawdownType2ChoiceSese01100109:
    cd: Optional[DrawdownType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class FailedSettlementStatus2ChoiceSese01100109:
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    data_src_schme: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DataSrcSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class GenericAccountIdentification1Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InRepairStatus4ChoiceSese01100109:
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    data_src_schme: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DataSrcSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class OtherAmountType1ChoiceSese01100109:
    cd: Optional[OtherAmountType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry_cd: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "PrtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class OtherAsset2ChoiceSese01100109:
    cd: Optional[OtherAsset2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class PendingSettlementStatus3ChoiceSese01100109:
    rsn: Optional[PendingSettlementStatusReason2Code] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    xtnded_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    data_src_schme: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DataSrcSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class PostalAddress1Sese01100109:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress6Sese01100109:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PriceValue1Sese01100109:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )


@dataclass
class RejectedReason45ChoiceSese01100109:
    cd: Optional[RejectedStatusReason13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class ReversedStatus2ChoiceSese01100109:
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    data_src_schme: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DataSrcSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Role8ChoiceSese01100109:
    cd: Optional[InvestmentFundRole8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TaxBasis1ChoiceSese01100109:
    cd: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TaxReferenceType1ChoiceSese01100109:
    cd: Optional[PersonIdentificationType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TaxType3ChoiceSese01100109:
    cd: Optional[TaxType17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TaxableIncomePerShareCalculated2ChoiceSese01100109:
    cd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TransferInstructionStatus5Sese01100109:
    sts: Optional[TransferStatus6Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class TransferStatusType3ChoiceSese01100109:
    cd: Optional[TransferStatusType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TransferUnmatchedStatus4ChoiceSese01100109:
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    rsn: Optional[TransferUnmatchedReason3Code] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    xtnded_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    data_src_schme: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DataSrcSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TypeOfPrice46ChoiceSese01100109:
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Unit13Sese01100109:
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ordr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrdrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    acqstn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AcqstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cert_nb: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    grp1_or2_units: Optional[UktaxGroupUnit1Code] = field(
        default=None,
        metadata={
            "name": "Grp1Or2Units",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class WaivingInstruction2ChoiceSese01100109:
    cd: Optional[WaivingInstruction1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese01100109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class AccountIdentificationAndName6Sese01100109:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class BeneficiaryDrawdown1Sese01100109:
    bnfcry_tp: Optional[BeneficiaryType1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "BnfcryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    dth_udr_lmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DthUdrLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class BenefitCrystallisationEvent2Sese01100109:
    evt_tp_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtTpNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "EvtTpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EvtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    crstllstn_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "CrstllstnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    pctg_of_allwnc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    lftm_allwnc_prtcn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LftmAllwncPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class BranchData2Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Sese01100109] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Capped1Sese01100109:
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    incm_lmt_cur_prd: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "IncmLmtCurPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    incm_cur_prd: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "IncmCurPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    incm_lmt_nxt_prd: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "IncmLmtNxtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class CashAsset3Sese01100109:
    csh_asst_tp: Optional[CashAssetType1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "CshAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    hldg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trf_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Sese01100109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class ChargeOrCommissionDiscount1Sese01100109:
    amt: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis: Optional[WaivingInstruction2ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class EmploymentDetails1Sese01100109:
    tax_cd: Optional[GenericIdentification36Sese01100109] = field(
        default=None,
        metadata={
            "name": "TaxCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    othr_tax_cd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OthrTaxCdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cmltv_tax_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmltvTaxInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prvs_pay: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "PrvsPay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prvs_tax: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "PrvsTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    start_dt: Optional[DateFormat42ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    end_dt: Optional[DateFormat42ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class NameAndAddress5Sese01100109:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese01100109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class OtherAmount1Sese01100109:
    tp: Optional[OtherAmountType1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )


@dataclass
class OtherAsset2Sese01100109:
    othr_asst_tp: Optional[OtherAsset2ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "OthrAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class RejectionReason56Sese01100109:
    rsn: Optional[RejectedReason45ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SecurityIdentification25ChoiceSese01100109:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Sese01100109] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TaxCalculationInformation10Sese01100109:
    bsis: Optional[TaxBasis1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    taxbl_amt: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "TaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )


@dataclass
class TaxReference2Sese01100109:
    tp: Optional[TaxReferenceType1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UnitPrice23Sese01100109:
    tp: Optional[TypeOfPrice46ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    val: Optional[PriceValue1Sese01100109] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    acrd_intrst_nav: Optional[ActiveOrHistoricCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    taxbl_incm_per_shr: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[
        TaxableIncomePerShareCalculated2ChoiceSese01100109
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Drawdown2Sese01100109:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    trch_tp: Optional[DrawdownType2ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "TrchTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    aplbl_rules: Optional[ApplicableRules1ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "AplblRules",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    invstr_tax_ref: Optional[TaxReference2Sese01100109] = field(
        default=None,
        metadata={
            "name": "InvstrTaxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    pctg_of_ttl_trf_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfTtlTrfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ttl_amt_net_drwdwn: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "TtlAmtNetDrwdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_fnds_dsgntd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AddtlFndsDsgntd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    pnsn_cmcmnt_lump_sum_rmng: Optional[
        ActiveCurrencyAnd13DecimalAmountSese01100109
    ] = field(
        default=None,
        metadata={
            "name": "PnsnCmcmntLumpSumRmng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    pnsn_cmcmnt_lump_sum_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PnsnCmcmntLumpSumDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    mltpl_pnsn_cmcmnt_lump_sums: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MltplPnsnCmcmntLumpSums",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    lftm_allwnc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LftmAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rcpt_of_drwdwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RcptOfDrwdwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    bnfcry_dtls: Optional[BeneficiaryDrawdown1Sese01100109] = field(
        default=None,
        metadata={
            "name": "BnfcryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    capd_lmts: Optional[Capped1Sese01100109] = field(
        default=None,
        metadata={
            "name": "CapdLmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    flxbl_drwdwn_trggrd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FlxblDrwdwnTrggrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Drawdown3Sese01100109:
    mplymnt_dtls: Optional[EmploymentDetails1Sese01100109] = field(
        default=None,
        metadata={
            "name": "MplymntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class FinancialInstitutionIdentification10ChoiceSese01100109:
    nm_and_adr: Optional[NameAndAddress5Sese01100109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2ChoiceSese01100109] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            },
        )
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstitutionIdentification16Sese01100109:
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification4ChoiceSese01100109] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            },
        )
    )
    nm_and_adr: Optional[NameAndAddress5Sese01100109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch_id: Optional[BranchData2Sese01100109] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class FinancialInstrumentIdentification1Sese01100109:
    id: Optional[SecurityIdentification25ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentIdentification2Sese01100109:
    id: Optional[SecurityIdentification25ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class PartyIdentification125ChoiceSese01100109:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese01100109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class PartyIdentification132Sese01100109:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2ChoiceSese01100109] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            },
        )
    )
    nm_and_adr: Optional[NameAndAddress5Sese01100109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class TransferStatus5ChoiceSese01100109:
    sts: Optional[TransferInstructionStatus5Sese01100109] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    pdg_sttlm: Optional[PendingSettlementStatus3ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "PdgSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    umtchd: Optional[TransferUnmatchedStatus4ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Umtchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    in_rpr: Optional[InRepairStatus4ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "InRpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    rjctd: list[RejectionReason56Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "max_occurs": 10,
        },
    )
    faild_sttlm: Optional[FailedSettlementStatus2ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "FaildSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    canc: Optional[CancelledStatus13ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    rvsd: Optional[ReversedStatus2ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Rvsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cxl_pdg: Optional[CancellationPendingStatus7ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "CxlPdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Account33Sese01100109:
    ownr_id: Optional[PartyIdentification132Sese01100109] = field(
        default=None,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese01100109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    svcr: Optional[PartyIdentification132Sese01100109] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    sub_acct_dtls: Optional[SubAccount5Sese01100109] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Account34Sese01100109:
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification132Sese01100109] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    regn_adr: Optional[PostalAddress1Sese01100109] = field(
        default=None,
        metadata={
            "name": "RegnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Conversion2Sese01100109:
    src_scty: Optional[FinancialInstrumentIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "SrcScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    ttl_units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    units_dtls: list[Unit13Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "UnitsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class CreditTransfer9Sese01100109:
    dbtr: Optional[PartyIdentification132Sese01100109] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    dbtr_acct: Optional[AccountIdentificationAndName6Sese01100109] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification16Sese01100109] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    dbtr_agt_acct: Optional[AccountIdentificationAndName6Sese01100109] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    intrmy_agt1: Optional[FinancialInstitutionIdentification16Sese01100109] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    intrmy_agt1_acct: Optional[AccountIdentificationAndName6Sese01100109] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    intrmy_agt2: Optional[FinancialInstitutionIdentification16Sese01100109] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    intrmy_agt2_acct: Optional[AccountIdentificationAndName6Sese01100109] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification16Sese01100109] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    cdtr_agt_acct: Optional[AccountIdentificationAndName6Sese01100109] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cdtr: Optional[PartyIdentification132Sese01100109] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cdtr_acct: Optional[AccountIdentificationAndName6Sese01100109] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )


@dataclass
class FinancialInstitutionIdentification17Sese01100109:
    pty: Optional[FinancialInstitutionIdentification10ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class FinancialInstrument63ChoiceSese01100109:
    scty: Optional[FinancialInstrumentIdentification2Sese01100109] = field(
        default=None,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    csh_asst: Optional[CashAsset3Sese01100109] = field(
        default=None,
        metadata={
            "name": "CshAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    othr_asst: Optional[OtherAsset2Sese01100109] = field(
        default=None,
        metadata={
            "name": "OthrAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class PartyIdentification139Sese01100109:
    pty: Optional[PartyIdentification125ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class AdditionalReference10Sese01100109:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Cheque12Sese01100109:
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pyee_id: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "PyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    drwee_id: Optional[FinancialInstitutionIdentification17Sese01100109] = field(
        default=None,
        metadata={
            "name": "DrweeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    drwr_id: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "DrwrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Fee5Sese01100109:
    tp: Optional[ChargeType5ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    bsis: Optional[ChargeBasis2ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    std_amt: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "StdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    std_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_dtls: Optional[ChargeOrCommissionDiscount1Sese01100109] = field(
        default=None,
        metadata={
            "name": "DscntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    non_std_slaref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSLARef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    inftv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InftvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )


@dataclass
class Intermediary48Sese01100109:
    id: Optional[PartyIdentification132Sese01100109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    acct: Optional[Account34Sese01100109] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    role: Optional[Role8ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ctct_prsn: Optional[ContactIdentification2Sese01100109] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Tax35Sese01100109:
    tp: Optional[TaxType3ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation10Sese01100109] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class PaymentInstrument25ChoiceSese01100109:
    cdt_trf_dtls: Optional[CreditTransfer9Sese01100109] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    chq_dtls: Optional[Cheque12Sese01100109] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class References64ChoiceSese01100109:
    rltd_ref: list[AdditionalReference10Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "max_occurs": 2,
        },
    )
    othr_ref: list[AdditionalReference10Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "OthrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "max_occurs": 2,
        },
    )


@dataclass
class TotalFeesAndTaxes41Sese01100109:
    ttl_ovrhd_apld: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "TtlOvrhdApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ttl_fees: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "TtlFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ttl_taxs: Optional[ActiveCurrencyAndAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "TtlTaxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_fee: list[Fee5Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "IndvFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    indv_tax: list[Tax35Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class PaymentInstrument18Sese01100109:
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    csh_sttlm_dtls: Optional[PaymentInstrument25ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "CshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Unit11Sese01100109:
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ordr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrdrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    acqstn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AcqstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cert_nb: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    grp1_or2_units: Optional[UktaxGroupUnit1Code] = field(
        default=None,
        metadata={
            "name": "Grp1Or2Units",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pric_dtls: Optional[UnitPrice23Sese01100109] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    tx_ovrhd: Optional[TotalFeesAndTaxes41Sese01100109] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    othr_amt: list[OtherAmount1Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "OthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TransferStatusAndReason8Sese01100109:
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[AdditionalReference10Sese01100109] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    cxl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trf_evt_tp: list[TransferStatusType3ChoiceSese01100109] = field(
        default_factory=list,
        metadata={
            "name": "TrfEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    trf_sts: Optional[TransferStatus5ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "TrfSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    instrm: Optional[FinancialInstrument63ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Instrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    invstmt_acct_dtls: Optional[Account33Sese01100109] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    intrmy_inf: list[Intermediary48Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    snd_out_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SndOutDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ttl_units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    avrg_pric: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "AvrgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    units_dtls: list[Unit11Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "UnitsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    convs: Optional[Conversion2Sese01100109] = field(
        default=None,
        metadata={
            "name": "Convs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ttl_trf_val: Optional[ActiveCurrencyAnd13DecimalAmountSese01100109] = field(
        default=None,
        metadata={
            "name": "TtlTrfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    pmt_dtls: list[PaymentInstrument18Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "PmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    bnft_crstllstn_evt: list[BenefitCrystallisationEvent2Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "BnftCrstllstnEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    drwdwn_trch: list[Drawdown2Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "DrwdwnTrch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    othr_drwdwn_inf: Optional[Drawdown3Sese01100109] = field(
        default=None,
        metadata={
            "name": "OthrDrwdwnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    qry_rspn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "QryRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    sts_initr: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "StsInitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    sts_issr: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "StsIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    sts_rcpt: Optional[PartyIdentification139Sese01100109] = field(
        default=None,
        metadata={
            "name": "StsRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class TransferInstructionStatusReportV09Sese01100109:
    msg_id: Optional[MessageIdentification1Sese01100109] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    ctr_pty_ref: Optional[AdditionalReference10Sese01100109] = field(
        default=None,
        metadata={
            "name": "CtrPtyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    ref: Optional[References64ChoiceSese01100109] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    sts_rpt: Optional[TransferStatusAndReason8Sese01100109] = field(
        default=None,
        metadata={
            "name": "StsRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
            "required": True,
        },
    )
    mkt_prctc_vrsn: Optional[MarketPracticeVersion1Sese01100109] = field(
        default=None,
        metadata={
            "name": "MktPrctcVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )
    xtnsn: list[Extension1Sese01100109] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09",
        },
    )


@dataclass
class Sese01100109:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.011.001.09"

    trf_instr_sts_rpt: Optional[TransferInstructionStatusReportV09Sese01100109] = field(
        default=None,
        metadata={
            "name": "TrfInstrStsRpt",
            "type": "Element",
            "required": True,
        },
    )
