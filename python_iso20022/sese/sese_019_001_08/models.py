from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    GenderCode,
    NamePrefix1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SettlementTransactionCondition11Code,
    TradeTransactionCondition5Code,
    TypeOfIdentification1Code,
)
from python_iso20022.sese.enums import (
    AccountOwnershipType6Code,
    CashAssetType1Code,
    GeneralInvestmentAccountType2Code,
    HolderType1Code,
    OtherAsset2Code,
    PensionSchemeType3Code,
    PensionTransferScope1Code,
    PersonIdentificationType7Code,
    TaxEfficientProductType2Code,
)
from python_iso20022.sese.sese_019_001_08.enums import BusinessFlowDirectionType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSese01900108(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese01900108(ISO20022MessageElement):
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
class ClearingSystemMemberIdentification2ChoiceSese01900108(ISO20022MessageElement):
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    inifsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "INIFSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"IN[a-zA-Z0-9]{11,11}",
        },
    )
    grhebic: Optional[str] = field(
        default=None,
        metadata={
            "name": "GRHEBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"GR[0-9]{7,7}",
        },
    )
    plknr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PLKNR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"PL[0-9]{8,8}",
        },
    )
    othr_clr_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClrCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceSese01900108(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class Extension1Sese01900108(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource1ChoiceSese01900108(ISO20022MessageElement):
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketPracticeVersion1Sese01900108(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation1Sese01900108(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PreviousYear2ChoiceSese01900108(ISO20022MessageElement):
    all_prvs_yrs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllPrvsYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"ALL",
        },
    )
    spcfc_prvs_yrs: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "name": "SpcfcPrvsYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class SubAccount5Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalInformation15Sese01900108(ISO20022MessageElement):
    inf_tp: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AlternateSecurityIdentification7Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )


@dataclass
class CashAssetType1ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[CashAssetType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class ClassificationType32ChoiceSese01900108(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class DateAndAmount2Sese01900108(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSese01900108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )


@dataclass
class GeneralInvestmentAccountType2ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[GeneralInvestmentAccountType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class GenericIdentification78Sese01900108(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese01900108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class OtherAsset2ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[OtherAsset2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PartyIdentification126ChoiceSese01900108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese01900108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PensionSchemeType3ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[PensionSchemeType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PensionTransferScope1ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[PensionTransferScope1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PostalAddress1Sese01900108(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese01900108(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Sese01900108(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese01900108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SettlementTransactionCondition30ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class TaxEfficientProductType2ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[TaxEfficientProductType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class TaxReferenceParty1ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[HolderType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class TaxReferenceType1ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[PersonIdentificationType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class TradeTransactionCondition8ChoiceSese01900108(ISO20022MessageElement):
    cd: Optional[TradeTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class AlternatePartyIdentification7Sese01900108(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAsset2Sese01900108(ISO20022MessageElement):
    csh_asst_tp: Optional[CashAssetType1ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "CshAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    hldg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    addtl_inf: Optional[AdditionalInformation15Sese01900108] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class GeneralInvestment2Sese01900108(ISO20022MessageElement):
    tp: Optional[GeneralInvestmentAccountType2ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    ownrsh_tp: Optional[AccountOwnershipType6Code] = field(
        default=None,
        metadata={
            "name": "OwnrshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    cur_invstmt_amt: Optional[ActiveCurrencyAnd13DecimalAmountSese01900108] = field(
        default=None,
        metadata={
            "name": "CurInvstmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    estmtd_val: Optional[DateAndAmount2Sese01900108] = field(
        default=None,
        metadata={
            "name": "EstmtdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class IndividualPerson8Sese01900108(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    nm_sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "NmSfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    gndr: Optional[GenderCode] = field(
        default=None,
        metadata={
            "name": "Gndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_invstr_adr: Optional[PostalAddress1Sese01900108] = field(
        default=None,
        metadata={
            "name": "IndvInvstrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Sese01900108(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese01900108] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class OtherAsset2Sese01900108(ISO20022MessageElement):
    othr_asst_tp: Optional[OtherAsset2ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "OthrAsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    othr_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PartyIdentification140Sese01900108(ISO20022MessageElement):
    pty: Optional[PartyIdentification126ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyTextInformation6Sese01900108(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    regn_adr: Optional[PostalAddress1Sese01900108] = field(
        default=None,
        metadata={
            "name": "RegnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PensionPolicy1Sese01900108(ISO20022MessageElement):
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[AdditionalInformation15Sese01900108] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class SafekeepingPlaceFormat28ChoiceSese01900108(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Sese01900108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese01900108] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry: Optional[GenericIdentification78Sese01900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class SecurityIdentification25ChoiceSese01900108(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Sese01900108] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class TaxEfficientProduct4Sese01900108(ISO20022MessageElement):
    tax_effcnt_pdct_tp: Optional[TaxEfficientProductType2ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "TaxEffcntPdctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    cur_yr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CurYr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prvs_yrs: Optional[PreviousYear2ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "PrvsYrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class TaxReference1Sese01900108(ISO20022MessageElement):
    tax_tp: Optional[TaxReferenceType1ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    hldr_tp: Optional[TaxReferenceParty1ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "HldrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class FinancialInstrumentIdentification2Sese01900108(ISO20022MessageElement):
    id: Optional[SecurityIdentification25ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class Organisation36Sese01900108(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    id: Optional[PartyIdentification140Sese01900108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    taxtn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_invstr_adr: Optional[PostalAddress1Sese01900108] = field(
        default=None,
        metadata={
            "name": "CorpInvstrAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )


@dataclass
class PartyIdentification122ChoiceSese01900108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese01900108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification123ChoiceSese01900108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese01900108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese01900108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PartyIdentification125ChoiceSese01900108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese01900108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese01900108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PartyIdentification132Sese01900108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2ChoiceSese01900108] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            },
        )
    )
    nm_and_adr: Optional[NameAndAddress5Sese01900108] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese01900108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Pension6Sese01900108(ISO20022MessageElement):
    id: Optional[PensionPolicy1Sese01900108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    tp: Optional[PensionSchemeType3ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    trf_scp: Optional[PensionTransferScope1ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "TrfScp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    tax_ref: list[TaxReference1Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "TaxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    drwdwn_trch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrwdwnTrchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    non_wrppr_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NonWrpprTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class Account28Sese01900108(ISO20022MessageElement):
    ownr_id: Optional[PartyIdentification132Sese01900108] = field(
        default=None,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification132Sese01900108] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    sub_acct_dtls: Optional[SubAccount5Sese01900108] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class FinancialInstrument61ChoiceSese01900108(ISO20022MessageElement):
    scty: Optional[FinancialInstrumentIdentification2Sese01900108] = field(
        default=None,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    csh_asst: Optional[CashAsset2Sese01900108] = field(
        default=None,
        metadata={
            "name": "CshAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    othr_asst: Optional[OtherAsset2Sese01900108] = field(
        default=None,
        metadata={
            "name": "OthrAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class FundPortfolio9ChoiceSese01900108(ISO20022MessageElement):
    tax_effcnt_pdct: Optional[TaxEfficientProduct4Sese01900108] = field(
        default=None,
        metadata={
            "name": "TaxEffcntPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    gnl_invstmt: Optional[GeneralInvestment2Sese01900108] = field(
        default=None,
        metadata={
            "name": "GnlInvstmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pnsn: Optional[Pension6Sese01900108] = field(
        default=None,
        metadata={
            "name": "Pnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class InvestmentAccount69Sese01900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification132Sese01900108] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PartyIdentification139Sese01900108(ISO20022MessageElement):
    pty: Optional[PartyIdentification125ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification141Sese01900108(ISO20022MessageElement):
    id: Optional[PartyIdentification122ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese01900108] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese01900108] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PartyIdentificationAndAccount194Sese01900108(ISO20022MessageElement):
    id: Optional[PartyIdentification123ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese01900108] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese01900108] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation6Sese01900108] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class AdditionalReference10Sese01900108(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese01900108] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference11Sese01900108(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese01900108] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementParties94Sese01900108(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification141Sese01900108] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount194Sese01900108] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount194Sese01900108] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount194Sese01900108] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount194Sese01900108] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount194Sese01900108] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class FundSettlementParameters18Sese01900108(ISO20022MessageElement):
    sfkpg_plc: Optional[SafekeepingPlaceFormat28ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSese01900108] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSese01900108] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcvg_sd_dtls: Optional[SettlementParties94Sese01900108] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class FinancialInstrument101Sese01900108(ISO20022MessageElement):
    line_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instrm: Optional[FinancialInstrument61ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Instrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    clnt_ref: Optional[AdditionalReference10Sese01900108] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    ctr_pty_ref: Optional[AdditionalReference10Sese01900108] = field(
        default=None,
        metadata={
            "name": "CtrPtyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    trfee_acct: Optional[Account28Sese01900108] = field(
        default=None,
        metadata={
            "name": "TrfeeAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    trfr: Optional[Account28Sese01900108] = field(
        default=None,
        metadata={
            "name": "Trfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    sttlm_pties_dtls: Optional[FundSettlementParameters18Sese01900108] = field(
        default=None,
        metadata={
            "name": "SttlmPtiesDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    assts_held_in_own_nm: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsstsHeldInOwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    trf_rslts_in_chng_of_bnfcl_ownr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrfRsltsInChngOfBnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class PortfolioTransfer12Sese01900108(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtfl: Optional[FundPortfolio9ChoiceSese01900108] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    fin_instrm_asst_for_trf: list[FinancialInstrument101Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmAsstForTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    addtl_inf: list[AdditionalInformation15Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class AccountHoldingInformationRequestV08Sese01900108(ISO20022MessageElement):
    msg_ref: Optional[MessageIdentification1Sese01900108] = field(
        default=None,
        metadata={
            "name": "MsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference11Sese01900108] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    prvs_ref: Optional[AdditionalReference10Sese01900108] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    rltd_ref: Optional[AdditionalReference10Sese01900108] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    biz_flow_drctn_tp: Optional[BusinessFlowDirectionType1Code] = field(
        default=None,
        metadata={
            "name": "BizFlowDrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pmry_indv_invstr: Optional[IndividualPerson8Sese01900108] = field(
        default=None,
        metadata={
            "name": "PmryIndvInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    scndry_indv_invstr: Optional[IndividualPerson8Sese01900108] = field(
        default=None,
        metadata={
            "name": "ScndryIndvInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    othr_indv_invstr: list[IndividualPerson8Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "OthrIndvInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    pmry_corp_invstr: Optional[Organisation36Sese01900108] = field(
        default=None,
        metadata={
            "name": "PmryCorpInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    scndry_corp_invstr: Optional[Organisation36Sese01900108] = field(
        default=None,
        metadata={
            "name": "ScndryCorpInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    othr_corp_invstr: list[Organisation36Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "OthrCorpInvstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    trfr_acct: Optional[InvestmentAccount69Sese01900108] = field(
        default=None,
        metadata={
            "name": "TrfrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    nmnee_acct: Optional[InvestmentAccount69Sese01900108] = field(
        default=None,
        metadata={
            "name": "NmneeAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    trfee: Optional[PartyIdentification132Sese01900108] = field(
        default=None,
        metadata={
            "name": "Trfee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "required": True,
        },
    )
    pdct_trf: list[PortfolioTransfer12Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "PdctTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
            "min_occurs": 1,
        },
    )
    mkt_prctc_vrsn: Optional[MarketPracticeVersion1Sese01900108] = field(
        default=None,
        metadata={
            "name": "MktPrctcVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )
    xtnsn: list[Extension1Sese01900108] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08",
        },
    )


@dataclass
class Sese01900108(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08"

    acct_hldg_inf_req: Optional[AccountHoldingInformationRequestV08Sese01900108] = (
        field(
            default=None,
            metadata={
                "name": "AcctHldgInfReq",
                "type": "Element",
                "required": True,
            },
        )
    )
