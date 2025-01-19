from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CommissionType6Code,
    DeliveryReceiptType2Code,
    DistributionPolicy1Code,
    EucapitalGain2Code,
    EudividendStatus1Code,
    FormOfSecurity1Code,
    InvestmentFundRole2Code,
    OrderOriginatorEligibility1Code,
    PriceMethod1Code,
    ResidentialStatus1Code,
    RoundingDirection2Code,
    TaxableIncomePerShareCalculated2Code,
    TaxationBasis2Code,
    TaxExemptReason1Code,
    TypeOfPrice10Code,
    WaivingInstruction1Code,
)
from python_iso20022.setr.enums import (
    BestExecution1Code,
    CancellationRight1Code,
    ChargeType11Code,
    FinancialAdvice1Code,
    FundCashAccount2Code,
    FundOrderType4Code,
    FundOrderType5Code,
    IncomePreference1Code,
    LateReport1Code,
    NegotiatedTrade1Code,
    PersonIdentificationType2Code,
    TaxationBasis4Code,
    TaxType11Code,
    TradingCapacity2Code,
    UktaxGroupUnitCode,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSetr05200101(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountSetr05200101(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSetr05200101(ISO20022MessageElement):
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
class AlternateSecurityIdentification1Setr05200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Bicidentification1Setr05200101(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class ClearingSystemMemberIdentificationChoiceSetr05200101(ISO20022MessageElement):
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )


@dataclass
class CurrencyAndAmountSetr05200101(ISO20022MessageElement):
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
class DateAndDateTimeChoiceSetr05200101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class Extension1Setr05200101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentQuantity1Setr05200101(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class GenericIdentification1Setr05200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Setr05200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class PlaceOfTradeIdentification1ChoiceSetr05200101(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xchg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Xchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    over_the_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OverTheCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformationSetr05200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification1Setr05200101(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformationSetr05200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class CashAccountIdentification1ChoiceSetr05200101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    dmst_acct: Optional[SimpleIdentificationInformationSetr05200101] = field(
        default=None,
        metadata={
            "name": "DmstAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class CommissionWaiver3Setr05200101(ISO20022MessageElement):
    instr_bsis: Optional[WaivingInstruction1Code] = field(
        default=None,
        metadata={
            "name": "InstrBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_instr_bsis: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedInstrBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    wvd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WvdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class CopyInformation2Setr05200101(ISO20022MessageElement):
    cpy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CpyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    orgnl_rcvr: Optional[Bicidentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "OrgnlRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class CountryAndResidentialStatusType1Setr05200101(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    resdtl_sts: Optional[ResidentialStatus1Code] = field(
        default=None,
        metadata={
            "name": "ResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class Equalisation1Setr05200101(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class FundOrderType3Setr05200101(ISO20022MessageElement):
    ordr_tp: Optional[FundOrderType4Code] = field(
        default=None,
        metadata={
            "name": "OrdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_ordr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedOrdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification11Setr05200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[PersonIdentificationType2Code] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_id_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedIdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestmentFundsOrderBreakdown1Setr05200101(ISO20022MessageElement):
    ordr_brkdwn_tp: Optional[FundOrderType5Code] = field(
        default=None,
        metadata={
            "name": "OrdrBrkdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_ordr_brkdwn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedOrdrBrkdwnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Setr05200101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Setr05200101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class ProfitAndLoss1ChoiceSetr05200101(ISO20022MessageElement):
    prft: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Prft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    loss: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Loss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class SecurityIdentification3ChoiceSetr05200101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class TaxCalculationInformation6Setr05200101(ISO20022MessageElement):
    bsis: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_bsis: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxbl_amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "TaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class AccountIdentificationAndName3Setr05200101(ISO20022MessageElement):
    id: Optional[CashAccountIdentification1ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrument10Setr05200101(ISO20022MessageElement):
    id: Optional[SecurityIdentification3ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class IndividualPerson12Setr05200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    ctry_and_resdtl_sts: Optional[CountryAndResidentialStatusType1Setr05200101] = field(
        default=None,
        metadata={
            "name": "CtryAndResdtlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    othr_id: list[GenericIdentification11Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class InvestmentAccount20Setr05200101(ISO20022MessageElement):
    acct_id: Optional[AccountIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    tp: Optional[FundCashAccount2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NameAndAddress4Setr05200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr05200101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Setr05200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Setr05200101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class SubAccount1Setr05200101(ISO20022MessageElement):
    id: Optional[AccountIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UnitPrice10Setr05200101(ISO20022MessageElement):
    tp: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    val: Optional[PriceValue1Setr05200101] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    taxbl_incm_per_shr: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_taxbl_incm_per_shr_clctd: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pric_diff_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricDiffRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DeliveryParameters3Setr05200101(ISO20022MessageElement):
    adr: Optional[NameAndAddress4Setr05200101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    issd_cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssdCertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstitutionIdentification3ChoiceSetr05200101(ISO20022MessageElement):
    nm_and_adr: Optional[NameAndAddress5Setr05200101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentificationChoiceSetr05200101] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            },
        )
    )
    prtry_id: Optional[SimpleIdentificationInformationSetr05200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSetr05200101(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Setr05200101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class Account7Setr05200101(ISO20022MessageElement):
    id: Optional[AccountIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class AdditionalReference3Setr05200101(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Charge18Setr05200101(ISO20022MessageElement):
    tp: Optional[ChargeType11Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    chrg_bsis: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "ChrgBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_chrg_bsis: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedChrgBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rcpt_id: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class Cheque3Setr05200101(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pyee_id: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "PyeeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    drwee_id: Optional[FinancialInstitutionIdentification3ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "DrweeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    drwr_id: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "DrwrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class Commission10Setr05200101(ISO20022MessageElement):
    tp: Optional[CommissionType6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    bsis: Optional[TaxationBasis4Code] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_bsis: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rcpt_id: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    wvg_dtls: Optional[CommissionWaiver3Setr05200101] = field(
        default=None,
        metadata={
            "name": "WvgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class CreditTransfer6Setr05200101(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dbtr_acct: Optional[AccountIdentificationAndName3Setr05200101] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dbtr_agt: Optional[FinancialInstitutionIdentification3ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "DbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dbtr_agt_acct: Optional[AccountIdentificationAndName3Setr05200101] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    intrmy_agt1: Optional[FinancialInstitutionIdentification3ChoiceSetr05200101] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            },
        )
    )
    intrmy_agt1_acct: Optional[AccountIdentificationAndName3Setr05200101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    intrmy_agt2: Optional[FinancialInstitutionIdentification3ChoiceSetr05200101] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            },
        )
    )
    intrmy_agt2_acct: Optional[AccountIdentificationAndName3Setr05200101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    cdtr_agt: Optional[FinancialInstitutionIdentification3ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    cdtr_agt_acct: Optional[AccountIdentificationAndName3Setr05200101] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    cdtr: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    cdtr_acct: Optional[AccountIdentificationAndName3Setr05200101] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class ForeignExchangeTerms7Setr05200101(ISO20022MessageElement):
    to_amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    fr_amt: Optional[ActiveCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    qtg_instn: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class InvestmentAccount21Setr05200101(ISO20022MessageElement):
    acct_id: Optional[AccountIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ownr_id: list[PartyIdentification2ChoiceSetr05200101] = field(
        default_factory=list,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    acct_svcr: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    sub_acct_dtls: Optional[SubAccount1Setr05200101] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class PartyIdentificationAndAccount3Setr05200101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    acct_id: Optional[AccountIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class Tax14Setr05200101(ISO20022MessageElement):
    tp: Optional[TaxType11Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rcpt_id: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xmptn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XmptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    xmptn_rsn: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "XmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_xmptn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedXmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation6Setr05200101] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class DeliveringPartiesAndAccount3Setr05200101(ISO20022MessageElement):
    dlvrrs_ctdn_dtls: Optional[PartyIdentificationAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "DlvrrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dlvrrs_intrmy_dtls: Optional[PartyIdentificationAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "DlvrrsIntrmyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    dlvrg_agt_dtls: Optional[PartyIdentificationAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "DlvrgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class Intermediary9Setr05200101(ISO20022MessageElement):
    id: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    acct: Optional[Account7Setr05200101] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    tradg_pty_cpcty: Optional[TradingCapacity2Code] = field(
        default=None,
        metadata={
            "name": "TradgPtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    role: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_role: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PaymentInstrument11ChoiceSetr05200101(ISO20022MessageElement):
    cdt_trf_dtls: Optional[CreditTransfer6Setr05200101] = field(
        default=None,
        metadata={
            "name": "CdtTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    chq_dtls: Optional[Cheque3Setr05200101] = field(
        default=None,
        metadata={
            "name": "ChqDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    bkrs_drft_dtls: Optional[Cheque3Setr05200101] = field(
        default=None,
        metadata={
            "name": "BkrsDrftDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    csh_acct_dtls: Optional[InvestmentAccount20Setr05200101] = field(
        default=None,
        metadata={
            "name": "CshAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class ReceivingPartiesAndAccount3Setr05200101(ISO20022MessageElement):
    rcvrs_ctdn_dtls: Optional[PartyIdentificationAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "RcvrsCtdnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    rcvrs_intrmy_dtls: Optional[PartyIdentificationAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "RcvrsIntrmyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    rcvg_agt_dtls: Optional[PartyIdentificationAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "RcvgAgtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )


@dataclass
class TotalCharges3Setr05200101(ISO20022MessageElement):
    ttl_amt_of_chrgs: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "TtlAmtOfChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    chrg_dtls: list[Charge18Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "ChrgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class TotalCommissions3Setr05200101(ISO20022MessageElement):
    ttl_amt_of_comssns: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "TtlAmtOfComssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    comssn_dtls: list[Commission10Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "ComssnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class TotalTaxes3Setr05200101(ISO20022MessageElement):
    ttl_amt_of_taxs: Optional[ActiveCurrencyAnd13DecimalAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "TtlAmtOfTaxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    taxbl_incm_per_dvdd: Optional[ActiveCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerDvdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    eucptl_gn: Optional[EucapitalGain2Code] = field(
        default=None,
        metadata={
            "name": "EUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_eucptl_gn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedEUCptlGn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    eudvdd_sts: Optional[EudividendStatus1Code] = field(
        default=None,
        metadata={
            "name": "EUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_eudvdd_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedEUDvddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pctg_of_debt_clm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PctgOfDebtClm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tax_dtls: list[Tax14Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "TaxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class FundSettlementParameters4Setr05200101(ISO20022MessageElement):
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    sttlm_plc: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "SttlmPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcvg_sd_dtls: Optional[ReceivingPartiesAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    dlvrg_sd_dtls: Optional[DeliveringPartiesAndAccount3Setr05200101] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class PaymentTransaction22Setr05200101(ISO20022MessageElement):
    pmt_instrm: Optional[PaymentInstrument11ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "PmtInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class RedemptionExecution6Setr05200101(ISO20022MessageElement):
    ordr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    deal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ordr_tp: list[FundOrderType3Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "OrdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "max_occurs": 10,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument10Setr05200101] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    sub_acct_for_hldg: Optional[SubAccount1Setr05200101] = field(
        default=None,
        metadata={
            "name": "SubAcctForHldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    units_nb: Optional[FinancialInstrumentQuantity1Setr05200101] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    rndg: Optional[RoundingDirection2Code] = field(
        default=None,
        metadata={
            "name": "Rndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    hldgs_red_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HldgsRedRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    grss_amt: Optional[ActiveCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "GrssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    trad_dt_tm: Optional[DateAndDateTimeChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "TradDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    sttlm_amt: Optional[ActiveCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    sttlm_mtd: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    prtly_exctd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlyExctdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    dealg_pric_dtls: Optional[UnitPrice10Setr05200101] = field(
        default=None,
        metadata={
            "name": "DealgPricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    inftv_pric_dtls: list[UnitPrice10Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "InftvPricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "max_occurs": 2,
        },
    )
    best_exctn: Optional[BestExecution1Code] = field(
        default=None,
        metadata={
            "name": "BestExctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    cum_dvdd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CumDvddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    intrm_prft_amt: Optional[ProfitAndLoss1ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "IntrmPrftAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    fxdtls: list[ForeignExchangeTerms7Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    incm_pref: Optional[IncomePreference1Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    grp1_or2_units: Optional[UktaxGroupUnitCode] = field(
        default=None,
        metadata={
            "name": "Grp1Or2Units",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    chrg_gnl_dtls: Optional[TotalCharges3Setr05200101] = field(
        default=None,
        metadata={
            "name": "ChrgGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    stff_clnt_brkdwn: list[InvestmentFundsOrderBreakdown1Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "StffClntBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "max_occurs": 4,
        },
    )
    comssn_gnl_dtls: Optional[TotalCommissions3Setr05200101] = field(
        default=None,
        metadata={
            "name": "ComssnGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    tax_gnl_dtls: Optional[TotalTaxes3Setr05200101] = field(
        default=None,
        metadata={
            "name": "TaxGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    sttlm_and_ctdy_dtls: Optional[FundSettlementParameters4Setr05200101] = field(
        default=None,
        metadata={
            "name": "SttlmAndCtdyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    phys_dlvry_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhysDlvryInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    phys_dlvry_dtls: Optional[DeliveryParameters3Setr05200101] = field(
        default=None,
        metadata={
            "name": "PhysDlvryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    reqd_sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    csh_sttlm_dtls: Optional[PaymentTransaction22Setr05200101] = field(
        default=None,
        metadata={
            "name": "CshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    non_std_sttlm_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    prtl_sttlm_of_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmOfUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    prtl_sttlm_of_csh: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrtlSttlmOfCsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    prtl_red_whldg_amt: Optional[CurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "PrtlRedWhldgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    fin_advc: Optional[FinancialAdvice1Code] = field(
        default=None,
        metadata={
            "name": "FinAdvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    ngtd_trad: Optional[NegotiatedTrade1Code] = field(
        default=None,
        metadata={
            "name": "NgtdTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    late_rpt: Optional[LateReport1Code] = field(
        default=None,
        metadata={
            "name": "LateRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    rltd_pty_dtls: list[Intermediary9Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "RltdPtyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "max_occurs": 10,
        },
    )
    equlstn: Optional[Equalisation1Setr05200101] = field(
        default=None,
        metadata={
            "name": "Equlstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class RedemptionMultipleExecution3Setr05200101(ISO20022MessageElement):
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bnfcry_dtls: Optional[IndividualPerson12Setr05200101] = field(
        default=None,
        metadata={
            "name": "BnfcryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    plc_of_trad: Optional[PlaceOfTradeIdentification1ChoiceSetr05200101] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    ordr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrdrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    reqd_futr_trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdFutrTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    cxl_rght: Optional[CancellationRight1Code] = field(
        default=None,
        metadata={
            "name": "CxlRght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnded_cxl_rght: Optional[str] = field(
        default=None,
        metadata={
            "name": "XtndedCxlRght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    invstmt_acct_dtls: Optional[InvestmentAccount21Setr05200101] = field(
        default=None,
        metadata={
            "name": "InvstmtAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    indv_exctn_dtls: list[RedemptionExecution6Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "IndvExctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "min_occurs": 1,
        },
    )
    ttl_sttlm_amt: Optional[ActiveCurrencyAndAmountSetr05200101] = field(
        default=None,
        metadata={
            "name": "TtlSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    csh_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CshSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    blk_csh_sttlm_dtls: Optional[PaymentTransaction22Setr05200101] = field(
        default=None,
        metadata={
            "name": "BlkCshSttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class RedemptionOrderConfirmationAmendmentV01Setr05200101(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Setr05200101] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference3Setr05200101] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    prvs_ref: list[AdditionalReference3Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    rltd_ref: Optional[AdditionalReference3Setr05200101] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    mltpl_exctn_dtls: Optional[RedemptionMultipleExecution3Setr05200101] = field(
        default=None,
        metadata={
            "name": "MltplExctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "required": True,
        },
    )
    rltd_pty_dtls: list[Intermediary9Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "RltdPtyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
            "max_occurs": 10,
        },
    )
    cpy_dtls: Optional[CopyInformation2Setr05200101] = field(
        default=None,
        metadata={
            "name": "CpyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )
    xtnsn: list[Extension1Setr05200101] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01",
        },
    )


@dataclass
class Setr05200101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.052.001.01"

    red_ordr_conf_amdmnt_v01: Optional[
        RedemptionOrderConfirmationAmendmentV01Setr05200101
    ] = field(
        default=None,
        metadata={
            "name": "RedOrdrConfAmdmntV01",
            "type": "Element",
            "required": True,
        },
    )
