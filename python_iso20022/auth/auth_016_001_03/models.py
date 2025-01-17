from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_016_001_03.enums import (
    CancelledStatusReason15Code,
    InternalPartyRole1Code,
    ReportingWaiverType1Code,
    ReportingWaiverType3Code,
    Side5Code,
)
from python_iso20022.auth.enums import (
    BenchmarkCurveName2Code,
    OptionStyle7Code,
    OptionType2Code,
    PhysicalTransferType4Code,
    PriceStatus1Code,
    RateBasis1Code,
    RegulatoryTradingCapacity1Code,
)
from python_iso20022.enums import NoReasonCode, VariationType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03"


@dataclass
class ActiveCurrencyAnd13DecimalAmountAuth01600103:
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
class ActiveOrHistoricCurrencyAndAmountAuth01600103:
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
class DebtInstrument4Auth01600103:
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class DerivativeForeignExchange2Auth01600103:
    othr_ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DerivativeInterest2Auth01600103:
    othr_ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrNtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DigitalTokenAmount2Auth01600103:
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[1-9B-DF-HJ-NP-XZ][0-9B-DF-HJ-NP-XZ]{8,8}",
        },
    )
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "max_length": 30,
        },
    )


@dataclass
class IdentificationSource3ChoiceAuth01600103:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAuth01600103:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RecordTechnicalData5Auth01600103:
    rct_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    xchg_rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "XchgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class SecuritiesTransactionTransmission2Auth01600103:
    trnsmssn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrnsmssnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    trnsmttg_buyr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrnsmttgBuyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    trnsmttg_sellr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrnsmttgSellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth01600103:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection53Auth01600103:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth01600103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class AmountAndDirection61Auth01600103:
    amt: Optional[ActiveCurrencyAnd13DecimalAmountAuth01600103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class AssetClassAttributes1Auth01600103:
    intrst: Optional[DerivativeInterest2Auth01600103] = field(
        default=None,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    fx: Optional[DerivativeForeignExchange2Auth01600103] = field(
        default=None,
        metadata={
            "name": "FX",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class BenchmarkCurveName5ChoiceAuth01600103:
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class FinancialInstrumentQuantity25ChoiceAuth01600103:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    nmnl_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth01600103] = field(
        default=None,
        metadata={
            "name": "NmnlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    mntry_val: Optional[ActiveOrHistoricCurrencyAndAmountAuth01600103] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class GenericPersonIdentification1Auth01600103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InterestRateContractTerm2Auth01600103:
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass
class OtherIdentification1Auth01600103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class RecordTechnicalData2Auth01600103:
    rct_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RctDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    cxl_rsn: Optional[CancelledStatusReason15Code] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class SecuritiesTransactionIndicator2Auth01600103:
    wvr_ind: list[ReportingWaiverType1Code] = field(
        default_factory=list,
        metadata={
            "name": "WvrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    shrt_sellg_ind: Optional[Side5Code] = field(
        default=None,
        metadata={
            "name": "ShrtSellgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    otcpst_trad_ind: list[ReportingWaiverType3Code] = field(
        default_factory=list,
        metadata={
            "name": "OTCPstTradInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    rsk_rdcg_tx: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RskRdcgTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    scties_fincg_tx_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTxInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class SecuritiesTransactionPrice1Auth01600103:
    pdg: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SecuritiesTransactionPrice6Auth01600103:
    pdg: Optional[PriceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dgtl_tkn: list[DigitalTokenAmount2Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "DgtlTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class SupplementaryData1Auth01600103:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth01600103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class AssetClassAttributes1ChoiceAuth01600103:
    intrst: Optional[DerivativeInterest2Auth01600103] = field(
        default=None,
        metadata={
            "name": "Intrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    fx: Optional[DerivativeForeignExchange2Auth01600103] = field(
        default=None,
        metadata={
            "name": "FX",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    both: Optional[AssetClassAttributes1Auth01600103] = field(
        default=None,
        metadata={
            "name": "Both",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class FloatingInterestRate8Auth01600103:
    ref_rate: Optional[BenchmarkCurveName5ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    term: Optional[InterestRateContractTerm2Auth01600103] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class PersonIdentification10Auth01600103:
    frst_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrstNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    othr: Optional[GenericPersonIdentification1Auth01600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class PersonIdentification12Auth01600103:
    ctry_of_brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[GenericPersonIdentification1Auth01600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class SecuritiesTransactionPrice2ChoiceAuth01600103:
    mntry_val: Optional[AmountAndDirection61Auth01600103] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Yld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class SecuritiesTransactionPrice7Auth01600103:
    mntry_val: Optional[AmountAndDirection61Auth01600103] = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    dgtl_tkn_qty: Optional[DigitalTokenAmount2Auth01600103] = field(
        default=None,
        metadata={
            "name": "DgtlTknQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class SecuritiesTransactionReport2Auth01600103:
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    exctg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExctgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    submitg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubmitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    tech_attrbts: Optional[RecordTechnicalData2Auth01600103] = field(
        default=None,
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class SecurityIdentification19Auth01600103:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SecurityInstrumentDescription23Auth01600103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    clssfctn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z]{6,6}",
        },
    )
    ntnl_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtnlCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class ExecutingParty1ChoiceAuth01600103:
    prsn: Optional[PersonIdentification12Auth01600103] = field(
        default=None,
        metadata={
            "name": "Prsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )
    clnt: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "Clnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class FinancialInstrument58Auth01600103:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[FloatingInterestRate8Auth01600103] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class InvestmentParty1ChoiceAuth01600103:
    prsn: Optional[PersonIdentification12Auth01600103] = field(
        default=None,
        metadata={
            "name": "Prsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class PersonOrOrganisation1ChoiceAuth01600103:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    mic: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    prsn: Optional[PersonIdentification10Auth01600103] = field(
        default=None,
        metadata={
            "name": "Prsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    intl: Optional[InternalPartyRole1Code] = field(
        default=None,
        metadata={
            "name": "Intl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class PersonOrOrganisation2ChoiceAuth01600103:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prsn: Optional[PersonIdentification10Auth01600103] = field(
        default=None,
        metadata={
            "name": "Prsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class SecuritiesTransactionPrice22ChoiceAuth01600103:
    pric: Optional[SecuritiesTransactionPrice2ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    dgtl_tkn_pric: Optional[SecuritiesTransactionPrice7Auth01600103] = field(
        default=None,
        metadata={
            "name": "DgtlTknPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    no_pric: Optional[SecuritiesTransactionPrice6Auth01600103] = field(
        default=None,
        metadata={
            "name": "NoPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class SecuritiesTransactionPrice4ChoiceAuth01600103:
    pric: Optional[SecuritiesTransactionPrice2ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    no_pric: Optional[SecuritiesTransactionPrice1Auth01600103] = field(
        default=None,
        metadata={
            "name": "NoPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class BasketDescription3Auth01600103:
    isin: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    indx: list[FinancialInstrument58Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class FinancialInstrumentIdentification6ChoiceAuth01600103:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    indx: Optional[FinancialInstrument58Auth01600103] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class PartyIdentification76Auth01600103:
    id: Optional[PersonOrOrganisation1ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    ctry_of_brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecuritiesTransaction3Auth01600103:
    trad_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    tradg_cpcty: Optional[RegulatoryTradingCapacity1Code] = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity25ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    dgtl_tkn_qty: list[DigitalTokenAmount2Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "DgtlTknQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    deriv_ntnl_chng: Optional[VariationType1Code] = field(
        default=None,
        metadata={
            "name": "DerivNtnlChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    pric: Optional[SecuritiesTransactionPrice22ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    net_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    trad_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ctry_of_brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBrnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    up_frnt_pmt: Optional[AmountAndDirection53Auth01600103] = field(
        default=None,
        metadata={
            "name": "UpFrntPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    trad_plc_mtchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradPlcMtchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 52,
        },
    )
    cmplx_trad_cmpnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmplxTradCmpntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentIdentification7ChoiceAuth01600103:
    sngl: Optional[FinancialInstrumentIdentification6ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Sngl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    bskt: Optional[BasketDescription3Auth01600103] = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class PartyIdentification79Auth01600103:
    acct_ownr: list[PartyIdentification76Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_occurs": 1,
        },
    )
    dcsn_makr: list[PersonOrOrganisation2ChoiceAuth01600103] = field(
        default_factory=list,
        metadata={
            "name": "DcsnMakr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class SwapLegIdentification2Auth01600103:
    swp_in: Optional[FinancialInstrumentIdentification7ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "SwpIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    swp_out: Optional[FinancialInstrumentIdentification7ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "SwpOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class UnderlyingIdentification2ChoiceAuth01600103:
    swp: Optional[SwapLegIdentification2Auth01600103] = field(
        default=None,
        metadata={
            "name": "Swp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    othr: Optional[FinancialInstrumentIdentification7ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class DerivativeInstrument6Auth01600103:
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    pric_mltplr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PricMltplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    undrlyg_instrm: Optional[UnderlyingIdentification2ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "UndrlygInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    optn_tp: Optional[OptionType2Code] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    strk_pric: Optional[SecuritiesTransactionPrice4ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    optn_exrc_style: Optional[OptionStyle7Code] = field(
        default=None,
        metadata={
            "name": "OptnExrcStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    dlvry_tp: Optional[PhysicalTransferType4Code] = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    asst_clss_spcfc_attrbts: Optional[AssetClassAttributes1ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "AsstClssSpcfcAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class SecurityInstrumentDescription22Auth01600103:
    fin_instrm_gnl_attrbts: Optional[SecurityInstrumentDescription23Auth01600103] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmGnlAttrbts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
                "required": True,
            },
        )
    )
    debt_instrm_attrbts: Optional[DebtInstrument4Auth01600103] = field(
        default=None,
        metadata={
            "name": "DebtInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    deriv_instrm_attrbts: Optional[DerivativeInstrument6Auth01600103] = field(
        default=None,
        metadata={
            "name": "DerivInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )


@dataclass
class FinancialInstrumentAttributes5ChoiceAuth01600103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrn_id: Optional[SecurityIdentification19Auth01600103] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    othr: Optional[SecurityInstrumentDescription22Auth01600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class SecuritiesTransactionReport7Auth01600103:
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    exctg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExctgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    invstmt_pty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InvstmtPtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    submitg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubmitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    buyr: Optional[PartyIdentification79Auth01600103] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification79Auth01600103] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    ordr_trnsmssn: Optional[SecuritiesTransactionTransmission2Auth01600103] = field(
        default=None,
        metadata={
            "name": "OrdrTrnsmssn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    tx: Optional[SecuritiesTransaction3Auth01600103] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    fin_instrm: Optional[FinancialInstrumentAttributes5ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "FinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    invstmt_dcsn_prsn: Optional[InvestmentParty1ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "InvstmtDcsnPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    exctg_prsn: Optional[ExecutingParty1ChoiceAuth01600103] = field(
        default=None,
        metadata={
            "name": "ExctgPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    addtl_attrbts: Optional[SecuritiesTransactionIndicator2Auth01600103] = field(
        default=None,
        metadata={
            "name": "AddtlAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "required": True,
        },
    )
    tech_attrbts: Optional[RecordTechnicalData5Auth01600103] = field(
        default=None,
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class ReportingTransactionType3ChoiceAuth01600103:
    new: Optional[SecuritiesTransactionReport7Auth01600103] = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    cxl: Optional[SecuritiesTransactionReport2Auth01600103] = field(
        default=None,
        metadata={
            "name": "Cxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class FinancialInstrumentReportingTransactionReportV03Auth01600103:
    tx: list[ReportingTransactionType3ChoiceAuth01600103] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth01600103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03",
        },
    )


@dataclass
class Auth01600103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03"

    fin_instrm_rptg_tx_rpt: Optional[
        FinancialInstrumentReportingTransactionReportV03Auth01600103
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgTxRpt",
            "type": "Element",
            "required": True,
        },
    )
