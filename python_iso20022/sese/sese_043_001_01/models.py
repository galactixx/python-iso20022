from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    GenderCode,
    InvestmentFundFee1Code,
    InvestmentFundRole2Code,
    NamePrefix1Code,
    PriceMethod1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SettlementTransactionCondition11Code,
    TaxableIncomePerShareCalculated2Code,
    TaxationBasis2Code,
    TaxationBasis5Code,
    TaxType17Code,
    TradeTransactionCondition5Code,
    TypeOfIdentification1Code,
    TypeOfPrice10Code,
    UktaxGroupUnit1Code,
    WaivingInstruction1Code,
)
from python_iso20022.sese.enums import (
    AccountOwnershipType6Code,
    BusinessFlowType1Code,
    CashAssetType1Code,
    DrawdownStatus1Code,
    DrawdownType2Code,
    GeneralInvestmentAccountType2Code,
    HolderType1Code,
    LumpSumType1Code,
    OtherAmountType1Code,
    OtherAsset2Code,
    PensionOrderType1Code,
    PensionSchemeType3Code,
    PensionTransferScope1Code,
    PersonIdentificationType7Code,
    PortfolioWithdrawalReason1Code,
    TaxEfficientProductType2Code,
    TaxWrapperAmountType1Code,
    TransferType4Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01"


@dataclass
class AccountSchemeName1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAnd13DecimalAmountSese04300101(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountSese04300101(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSese04300101(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese04300101(ISO20022MessageElement):
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
class AllOtherCash1Sese04300101(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CashAll1Sese04300101(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2ChoiceSese04300101(ISO20022MessageElement):
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    inifsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "INIFSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"IN[a-zA-Z0-9]{11,11}",
        },
    )
    grhebic: Optional[str] = field(
        default=None,
        metadata={
            "name": "GRHEBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"GR[0-9]{7,7}",
        },
    )
    plknr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PLKNR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"PL[0-9]{8,8}",
        },
    )
    othr_clr_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClrCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification4ChoiceSese04300101(ISO20022MessageElement):
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSese04300101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class DateQuarter1ChoiceSese04300101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Extension1Sese04300101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceSese04300101(ISO20022MessageElement):
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketPracticeVersion1Sese04300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class MoneyPurchaseAnnualAllowance1Sese04300101(ISO20022MessageElement):
    trggrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Trggrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    trggrd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TrggrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PartyTextInformation1Sese04300101(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PreviousYear1ChoiceSese04300101(ISO20022MessageElement):
    all_prvs_yrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllPrvsYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"ALL",
        },
    )
    spcfc_prvs_yrs: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "name": "SpcfcPrvsYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class ResidualCash2Sese04300101(ISO20022MessageElement):
    ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SubAccount5Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalInformation15Sese04300101(ISO20022MessageElement):
    inf_tp: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AlternateSecurityIdentification7Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class CashAssetType1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[CashAssetType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class ChargeBasis2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TaxationBasis5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class ChargeType5ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[InvestmentFundFee1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class ClassificationType32ChoiceSese04300101(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class ContactIdentification2Sese04300101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateAndAmount2Sese04300101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class DrawdownStatus1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[DrawdownStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class DrawdownType2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[DrawdownType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class GeneralInvestmentAccountType2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[GeneralInvestmentAccountType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class GenericAccountIdentification1Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification78Sese04300101(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class InnovativeFinance1Sese04300101(ISO20022MessageElement):
    tp: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class LumpSumType1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[LumpSumType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class OtherAmount3Sese04300101(ISO20022MessageElement):
    tp: Optional[GenericIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class OtherAmountType1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[OtherAmountType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry_cd: Optional[GenericIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class OtherAsset2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[OtherAsset2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PartyIdentification126ChoiceSese04300101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PensionOrderType1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[PensionOrderType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PensionSchemeType3ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[PensionSchemeType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PensionTransferScope1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[PensionTransferScope1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PostalAddress1Sese04300101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress6Sese04300101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PreviousYear4Sese04300101(ISO20022MessageElement):
    prvs_yrs: Optional[PreviousYear1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "PrvsYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    csh_cmpnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CshCmpntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PriceValue1Sese04300101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class Quantity50Sese04300101(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pctg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    csh_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "CshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    othr_asst: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Role4ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese04300101(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Sese04300101(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SettlementTransactionCondition30ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class SubscriptionInformation2Sese04300101(ISO20022MessageElement):
    dt_of_frst_sbcpt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfFrstSbcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    eqty_cmpnt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "EqtyCmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    csh_cmpnt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "CshCmpnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ttl_amt_yr_to_dt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TtlAmtYrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class TaxBasis1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxEfficientProductType2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TaxEfficientProductType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxReferenceParty1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[HolderType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxReferenceType1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[PersonIdentificationType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxType3ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TaxType17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxableIncomePerShareCalculated2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TradeTransactionCondition8ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TradeTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TransferType2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TransferType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TypeOfAmount1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TaxWrapperAmountType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TypeOfPrice46ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class WaivingInstruction2ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[WaivingInstruction1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification47Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class WithdrawalReason1ChoiceSese04300101(ISO20022MessageElement):
    cd: Optional[PortfolioWithdrawalReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class AccountIdentificationAndName6Sese04300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class AlternatePartyIdentification7Sese04300101(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BonusWithdrawal2Sese04300101(ISO20022MessageElement):
    tp_of_amt: Optional[TypeOfAmount1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "TpOfAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    rsn: Optional[WithdrawalReason1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    uclmd_amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "UclmdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    outsdng: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Outsdng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class BranchData2Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Sese04300101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class CashAsset3Sese04300101(ISO20022MessageElement):
    csh_asst_tp: Optional[CashAssetType1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "CshAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    hldg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trf_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Sese04300101] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class ChargeOrCommissionDiscount1Sese04300101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis: Optional[WaivingInstruction2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Crystallisation2Sese04300101(ISO20022MessageElement):
    trch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    crstllsd_units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrstllsdUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ucrstllsd_units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UcrstllsdUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    crstllsd_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "CrstllsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ucrstllsd_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "UcrstllsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class GeneralInvestment2Sese04300101(ISO20022MessageElement):
    tp: Optional[GeneralInvestmentAccountType2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ownrsh_tp: Optional[AccountOwnershipType6Code] = field(
        default=None,
        metadata={
            "name": "OwnrshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cur_invstmt_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "CurInvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    estmtd_val: Optional[DateAndAmount2Sese04300101] = field(
        default=None,
        metadata={
            "name": "EstmtdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class IndividualPerson8Sese04300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    nm_sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmSfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    gndr: Optional[GenderCode] = field(
        default=None,
        metadata={
            "name": "Gndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_invstr_adr: Optional[PostalAddress1Sese04300101] = field(
        default=None,
        metadata={
            "name": "IndvInvstrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Sese04300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese04300101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class OtherAmount1Sese04300101(ISO20022MessageElement):
    tp: Optional[OtherAmountType1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class OtherAsset2Sese04300101(ISO20022MessageElement):
    othr_asst_tp: Optional[OtherAsset2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "OthrAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PartyIdentification140Sese04300101(ISO20022MessageElement):
    pty: Optional[PartyIdentification126ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyTextInformation6Sese04300101(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    regn_adr: Optional[PostalAddress1Sese04300101] = field(
        default=None,
        metadata={
            "name": "RegnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PensionOrder1Sese04300101(ISO20022MessageElement):
    tp: Optional[PensionOrderType1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PensionPolicy1Sese04300101(ISO20022MessageElement):
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[AdditionalInformation15Sese04300101] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class SafekeepingPlaceFormat28ChoiceSese04300101(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Sese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry: Optional[GenericIdentification78Sese04300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class SecurityIdentification25ChoiceSese04300101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Sese04300101] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Tax36Sese04300101(ISO20022MessageElement):
    dt_or_prd: Optional[DateQuarter1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "DtOrPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxCalculationInformation10Sese04300101(ISO20022MessageElement):
    bsis: Optional[TaxBasis1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    taxbl_amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class TaxReference1Sese04300101(ISO20022MessageElement):
    tax_tp: Optional[TaxReferenceType1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    hldr_tp: Optional[TaxReferenceParty1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "HldrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxReference2Sese04300101(ISO20022MessageElement):
    tp: Optional[TaxReferenceType1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UnitPrice23Sese04300101(ISO20022MessageElement):
    tp: Optional[TypeOfPrice46ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    val: Optional[PriceValue1Sese04300101] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    acrd_intrst_nav: Optional[ActiveOrHistoricCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    taxbl_incm_per_shr: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[
        TaxableIncomePerShareCalculated2ChoiceSese04300101
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class FinancialInstitutionIdentification16Sese04300101(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification4ChoiceSese04300101] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            },
        )
    )
    nm_and_adr: Optional[NameAndAddress5Sese04300101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch_id: Optional[BranchData2Sese04300101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class FinancialInstrumentIdentification2Sese04300101(ISO20022MessageElement):
    id: Optional[SecurityIdentification25ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class FinancialInstrumentIdentification5Sese04300101(ISO20022MessageElement):
    id: Optional[SecurityIdentification25ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Organisation36Sese04300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    id: Optional[PartyIdentification140Sese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    taxtn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_invstr_adr: Optional[PostalAddress1Sese04300101] = field(
        default=None,
        metadata={
            "name": "CorpInvstrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification122ChoiceSese04300101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese04300101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification123ChoiceSese04300101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese04300101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PartyIdentification125ChoiceSese04300101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese04300101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PartyIdentification132Sese04300101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2ChoiceSese04300101] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            },
        )
    )
    nm_and_adr: Optional[NameAndAddress5Sese04300101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification309Sese04300101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2ChoiceSese04300101] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            },
        )
    )
    nm_and_adr: Optional[NameAndAddress5Sese04300101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Pension5Sese04300101(ISO20022MessageElement):
    id: Optional[PensionPolicy1Sese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tp: Optional[PensionSchemeType3ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    trf_scp: Optional[PensionTransferScope1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "TrfScp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tax_ref: list[TaxReference1Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "TaxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    drwdwn_trch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrwdwnTrchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    drwdwn_sts: Optional[DrawdownStatus1ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "DrwdwnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    drwdwn_tp: Optional[DrawdownType2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "DrwdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    nb_of_drwdwn_trnchs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDrwdwnTrnchs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    estmtd_val: Optional[DateAndAmount2Sese04300101] = field(
        default=None,
        metadata={
            "name": "EstmtdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    blck_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BlckTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    blck_trf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckTrfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_free_csh_prtcn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxFreeCshPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tax_free_csh_amt: Optional[DateAndAmount2Sese04300101] = field(
        default=None,
        metadata={
            "name": "TaxFreeCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    val_of_pnsn_plcy_or_plan_or_schme: Optional[DateAndAmount2Sese04300101] = field(
        default=None,
        metadata={
            "name": "ValOfPnsnPlcyOrPlanOrSchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    rtrmnt_age_prtcn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RtrmntAgePrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    rtrmnt_age: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RtrmntAge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    shrg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Shrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    lump_sum_tp: list[LumpSumType1ChoiceSese04300101] = field(
        default_factory=list,
        metadata={
            "name": "LumpSumTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pnsn_ordr: list[PensionOrder1Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "PnsnOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ring_fncd_drwdwn_assts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RingFncdDrwdwnAssts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    mny_purchs_anl_allwnc: Optional[MoneyPurchaseAnnualAllowance1Sese04300101] = field(
        default=None,
        metadata={
            "name": "MnyPurchsAnlAllwnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    sfgrd_bnft: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SfgrdBnft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    non_sfgrdd_grnted_bnfts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonSfgrddGrntedBnfts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    lftm_allwnc_prtcn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LftmAllwncPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    clnt_lftm_allwnc_prtcn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClntLftmAllwncPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    bnft_crstllstn_evt_ocrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BnftCrstllstnEvtOcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    non_wrppr_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonWrpprTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TaxEfficientProduct7Sese04300101(ISO20022MessageElement):
    tax_effcnt_pdct_tp: Optional[TaxEfficientProductType2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "TaxEffcntPdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    cur_yr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CurYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    csh_cmpnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CshCmpntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prvs_yrs: Optional[PreviousYear4Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrvsYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prvs_yr_sbcpt_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "PrvsYrSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prvs_yrs_sbcpt_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "PrvsYrsSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dt_of_frst_sbcpt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfFrstSbcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cur_yr_sbcpt_dtls: Optional[SubscriptionInformation2Sese04300101] = field(
        default=None,
        metadata={
            "name": "CurYrSbcptDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    bns_or_wdrwl: list[BonusWithdrawal2Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "BnsOrWdrwl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    wdrwl_for_resdtl_purchs_prgrs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WdrwlForResdtlPurchsPrgrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trfr_altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfrAltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_sbcpt_amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TtlSbcptAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    othr_amt: list[OtherAmount3Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "OthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dt_frst_qlfyg_addtn: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtFrstQlfygAddtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    invstr_tax_ref: Optional[TaxReference2Sese04300101] = field(
        default=None,
        metadata={
            "name": "InvstrTaxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    invstmts_to_fllw_val: list[DateAndAmount2Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "InvstmtsToFllwVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    innvtv_finc: list[InnovativeFinance1Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "InnvtvFinc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    lwst_invstd_amt_cur_yr: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = (
        field(
            default=None,
            metadata={
                "name": "LwstInvstdAmtCurYr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            },
        )
    )
    tax_clctn_base: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TaxClctnBase",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    uusd_tax_ddctn: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "UusdTaxDdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cur_invstmt_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "CurInvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    estmtd_val: Optional[DateAndAmount2Sese04300101] = field(
        default=None,
        metadata={
            "name": "EstmtdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Account28Sese04300101(ISO20022MessageElement):
    ownr_id: Optional[PartyIdentification132Sese04300101] = field(
        default=None,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification132Sese04300101] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    sub_acct_dtls: Optional[SubAccount5Sese04300101] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Conversion3Sese04300101(ISO20022MessageElement):
    orgnl_scty: Optional[FinancialInstrumentIdentification5Sese04300101] = field(
        default=None,
        metadata={
            "name": "OrgnlScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class CreditTransfer11Sese04300101(ISO20022MessageElement):
    dbtr: Optional[PartyIdentification132Sese04300101] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dbtr_acct: Optional[AccountIdentificationAndName6Sese04300101] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification16Sese04300101] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dbtr_agt_acct: Optional[AccountIdentificationAndName6Sese04300101] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    intrmy_agt1: Optional[FinancialInstitutionIdentification16Sese04300101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    intrmy_agt1_acct: Optional[AccountIdentificationAndName6Sese04300101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    intrmy_agt2: Optional[FinancialInstitutionIdentification16Sese04300101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    intrmy_agt2_acct: Optional[AccountIdentificationAndName6Sese04300101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification16Sese04300101] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    cdtr_agt_acct: Optional[AccountIdentificationAndName6Sese04300101] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cdtr: Optional[PartyIdentification132Sese04300101] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cdtr_acct: Optional[AccountIdentificationAndName6Sese04300101] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class FinancialInstrument63ChoiceSese04300101(ISO20022MessageElement):
    scty: Optional[FinancialInstrumentIdentification2Sese04300101] = field(
        default=None,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    csh_asst: Optional[CashAsset3Sese04300101] = field(
        default=None,
        metadata={
            "name": "CshAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    othr_asst: Optional[OtherAsset2Sese04300101] = field(
        default=None,
        metadata={
            "name": "OthrAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class FundPortfolio7ChoiceSese04300101(ISO20022MessageElement):
    tax_effcnt_pdct: Optional[TaxEfficientProduct7Sese04300101] = field(
        default=None,
        metadata={
            "name": "TaxEffcntPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    gnl_invstmt: Optional[GeneralInvestment2Sese04300101] = field(
        default=None,
        metadata={
            "name": "GnlInvstmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pnsn: Optional[Pension5Sese04300101] = field(
        default=None,
        metadata={
            "name": "Pnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class InvestmentAccount69Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification132Sese04300101] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PartyIdentification139Sese04300101(ISO20022MessageElement):
    pty: Optional[PartyIdentification125ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification141Sese04300101(ISO20022MessageElement):
    id: Optional[PartyIdentification122ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese04300101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese04300101] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PartyIdentificationAndAccount194Sese04300101(ISO20022MessageElement):
    id: Optional[PartyIdentification123ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese04300101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese04300101] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation6Sese04300101] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Account27Sese04300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification139Sese04300101] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class AdditionalReference10Sese04300101(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese04300101] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference11Sese04300101(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese04300101] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Fee5Sese04300101(ISO20022MessageElement):
    tp: Optional[ChargeType5ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    bsis: Optional[ChargeBasis2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    std_amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "StdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    std_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_dtls: Optional[ChargeOrCommissionDiscount1Sese04300101] = field(
        default=None,
        metadata={
            "name": "DscntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    non_std_slaref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSLARef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese04300101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    inftv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InftvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )


@dataclass
class PaymentInstrument20Sese04300101(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_trf_dtls: Optional[CreditTransfer11Sese04300101] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class SettlementParties94Sese04300101(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification141Sese04300101] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount194Sese04300101] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount194Sese04300101] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount194Sese04300101] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount194Sese04300101] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount194Sese04300101] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Tax35Sese04300101(ISO20022MessageElement):
    tp: Optional[TaxType3ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese04300101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation10Sese04300101] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class FundSettlementParameters17Sese04300101(ISO20022MessageElement):
    sfkpg_plc: Optional[SafekeepingPlaceFormat28ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSese04300101] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSese04300101] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcvg_sd_dtls: Optional[SettlementParties94Sese04300101] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    dlvrg_sd_dtls: Optional[SettlementParties94Sese04300101] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Intermediary43Sese04300101(ISO20022MessageElement):
    id: Optional[PartyIdentification139Sese04300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    acct: Optional[Account27Sese04300101] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    role: Optional[Role4ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ctct_prsn: Optional[ContactIdentification2Sese04300101] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class TotalFeesAndTaxes41Sese04300101(ISO20022MessageElement):
    ttl_ovrhd_apld: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TtlOvrhdApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ttl_fees: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TtlFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ttl_taxs: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "TtlTaxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_fee: list[Fee5Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "IndvFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    indv_tax: list[Tax35Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Unit11Sese04300101(ISO20022MessageElement):
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    acqstn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AcqstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    cert_nb: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    grp1_or2_units: Optional[UktaxGroupUnit1Code] = field(
        default=None,
        metadata={
            "name": "Grp1Or2Units",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pric_dtls: Optional[UnitPrice23Sese04300101] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tx_ovrhd: Optional[TotalFeesAndTaxes41Sese04300101] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    othr_amt: list[OtherAmount1Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "OthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class FinancialInstrument105Sese04300101(ISO20022MessageElement):
    line_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instrm: Optional[FinancialInstrument63ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Instrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    qty: Optional[Quantity50Sese04300101] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtl_instd_qty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlInstdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    orgnl_pctg_instd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OrgnlPctgInstd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    trf_tp: Optional[TransferType2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "TrfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    addtl_asst: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AddtlAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    not_avlbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    convs: Optional[Conversion3Sese04300101] = field(
        default=None,
        metadata={
            "name": "Convs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    units_dtls: list[Unit11Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "UnitsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    clnt_ref: Optional[AdditionalReference10Sese04300101] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    ctr_pty_ref: Optional[AdditionalReference10Sese04300101] = field(
        default=None,
        metadata={
            "name": "CtrPtyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    biz_flow_tp: Optional[BusinessFlowType1Code] = field(
        default=None,
        metadata={
            "name": "BizFlowTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    avrg_acqstn_pric: Optional[ActiveCurrencyAndAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "AvrgAcqstnPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trf_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    ttl_book_val: Optional[DateAndAmount2Sese04300101] = field(
        default=None,
        metadata={
            "name": "TtlBookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    orgnl_cost: Optional[ActiveCurrencyAnd13DecimalAmountSese04300101] = field(
        default=None,
        metadata={
            "name": "OrgnlCost",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    latst_valtn: Optional[DateAndAmount2Sese04300101] = field(
        default=None,
        metadata={
            "name": "LatstValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trfee_acct: Optional[Account28Sese04300101] = field(
        default=None,
        metadata={
            "name": "TrfeeAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trfr: Optional[Account28Sese04300101] = field(
        default=None,
        metadata={
            "name": "Trfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    intrmy_inf: list[Intermediary43Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    reqd_trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    reqd_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    fctv_trf_dt: Optional[DateAndDateTime2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "FctvTrfDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    fctv_sttlm_dt: Optional[DateAndDateTime2ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "FctvSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pmt_dtls: Optional[PaymentInstrument20Sese04300101] = field(
        default=None,
        metadata={
            "name": "PmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    crstllstn_dtls: list[Crystallisation2Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "CrstllstnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tax_valtn_pt: Optional[Tax36Sese04300101] = field(
        default=None,
        metadata={
            "name": "TaxValtnPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    sttlm_pties_dtls: Optional[FundSettlementParameters17Sese04300101] = field(
        default=None,
        metadata={
            "name": "SttlmPtiesDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    assts_held_in_own_nm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsstsHeldInOwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trf_rslts_in_chng_of_bnfcl_ownr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrfRsltsInChngOfBnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PortfolioTransfer13Sese04300101(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trf_instr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfInstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    trf_cmpltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfCmpltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    actl_trf_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ActlTrfDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prtfl: Optional[FundPortfolio7ChoiceSese04300101] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    all_othr_csh: list[AllOtherCash1Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AllOthrCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    csh_all: list[CashAll1Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "CshAll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    rsdl_csh: list[ResidualCash2Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "RsdlCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    tax_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TaxDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pmt_dtls: Optional[PaymentInstrument20Sese04300101] = field(
        default=None,
        metadata={
            "name": "PmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    fin_instrm_asst_for_trf: list[FinancialInstrument105Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmAsstForTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class PortfolioTransferCompletionV01Sese04300101(ISO20022MessageElement):
    msg_ref: Optional[MessageIdentification1Sese04300101] = field(
        default=None,
        metadata={
            "name": "MsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference11Sese04300101] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    prvs_ref: Optional[AdditionalReference10Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    rltd_ref: Optional[AdditionalReference10Sese04300101] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pmry_indv_invstr: Optional[IndividualPerson8Sese04300101] = field(
        default=None,
        metadata={
            "name": "PmryIndvInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    regd_hldr: Optional[IndividualPerson8Sese04300101] = field(
        default=None,
        metadata={
            "name": "RegdHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    scndry_indv_invstr: Optional[IndividualPerson8Sese04300101] = field(
        default=None,
        metadata={
            "name": "ScndryIndvInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    othr_indv_invstr: list[IndividualPerson8Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "OthrIndvInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    pmry_corp_invstr: Optional[Organisation36Sese04300101] = field(
        default=None,
        metadata={
            "name": "PmryCorpInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    scndry_corp_invstr: Optional[Organisation36Sese04300101] = field(
        default=None,
        metadata={
            "name": "ScndryCorpInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    othr_corp_invstr: list[Organisation36Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "OthrCorpInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trfr_acct: Optional[InvestmentAccount69Sese04300101] = field(
        default=None,
        metadata={
            "name": "TrfrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    nmnee_acct: Optional[InvestmentAccount69Sese04300101] = field(
        default=None,
        metadata={
            "name": "NmneeAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    trfee: Optional[PartyIdentification309Sese04300101] = field(
        default=None,
        metadata={
            "name": "Trfee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "required": True,
        },
    )
    pdct_trf: list[PortfolioTransfer13Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "PdctTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
            "min_occurs": 1,
        },
    )
    mkt_prctc_vrsn: Optional[MarketPracticeVersion1Sese04300101] = field(
        default=None,
        metadata={
            "name": "MktPrctcVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )
    xtnsn: list[Extension1Sese04300101] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01",
        },
    )


@dataclass
class Sese04300101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.043.001.01"

    prtfl_trf_cmpltn: Optional[PortfolioTransferCompletionV01Sese04300101] = field(
        default=None,
        metadata={
            "name": "PrtflTrfCmpltn",
            "type": "Element",
            "required": True,
        },
    )
