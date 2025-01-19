from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.colr.colr_019_001_01.enums import ResponseStatus2Code
from python_iso20022.colr.enums import (
    BenchmarkCurveName7Code,
    CalculationMethod1Code,
    CollateralEntryType1Code,
    CollateralTransactionType1Code,
    EventFrequency12Code,
    ExposureType14Code,
    FrequencyRateFixing1Code,
    InterestRateIndexTenor2Code,
    RepoTerminationOption1Code,
)
from python_iso20022.enums import (
    AddressType2Code,
    CollateralRole1Code,
    CreditDebitCode,
    DateType2Code,
    DeliveryReceiptType2Code,
    InterestComputationMethod2Code,
    MarketType2Code,
    OptionType1Code,
    TradingCapacity7Code,
    TypeOfIdentification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01"


@dataclass
class ActiveCurrencyAndAmountColr01900101(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountColr01900101(ISO20022MessageElement):
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
class AdditionalInformation24Colr01900101(ISO20022MessageElement):
    coll_instr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CashAccountIdentification5ChoiceColr01900101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CrystallisationDay1Colr01900101(ISO20022MessageElement):
    day: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[0-9]{1,3}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceColr01900101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceColr01900101(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification1Colr01900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification178Colr01900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Colr01900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Colr01900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceColr01900101(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Colr01900101(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )


@dataclass
class Period2Colr01900101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )


@dataclass
class References70ChoiceColr01900101(ISO20022MessageElement):
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Colr01900101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentifications45Colr01900101(ISO20022MessageElement):
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class BasketIdentificationAndEligibilitySetProfile1Colr01900101(ISO20022MessageElement):
    prfrntl_bskt_id_nb: Optional[GenericIdentification1Colr01900101] = field(
        default=None,
        metadata={
            "name": "PrfrntlBsktIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    fllbck_startg_bskt_id: Optional[GenericIdentification1Colr01900101] = field(
        default=None,
        metadata={
            "name": "FllbckStartgBsktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    exclsn_bskt_id: Optional[GenericIdentification1Colr01900101] = field(
        default=None,
        metadata={
            "name": "ExclsnBsktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    elgblty_set_prfl: Optional[GenericIdentification1Colr01900101] = field(
        default=None,
        metadata={
            "name": "ElgbltySetPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class BenchmarkCurveName13ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[BenchmarkCurveName7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification1Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class BlockChainAddressWallet3Colr01900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CashMovement8Colr01900101(ISO20022MessageElement):
    csh_mvmnt: Optional[CollateralEntryType1Code] = field(
        default=None,
        metadata={
            "name": "CshMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    csh_amt: Optional[ActiveCurrencyAndAmountColr01900101] = field(
        default=None,
        metadata={
            "name": "CshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    coll_mvmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    clnt_csh_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCshMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_csh_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCshMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CollateralDate2Colr01900101(ISO20022MessageElement):
    trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class CollateralTransactionType1ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[CollateralTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class Date3ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[DateType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class DocumentNumber5ChoiceColr01900101(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Colr01900101] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class ExposureType23ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[ExposureType14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class ForeignExchangeTerms23Colr01900101(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountColr01900101] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )


@dataclass
class Frequency38ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[EventFrequency12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class FrequencyRateFixing1ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[FrequencyRateFixing1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    nb_of_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[0-9]{1,3}",
        },
    )


@dataclass
class IdentificationType42ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class MarketType8ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[MarketType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class OptionType6ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class OtherIdentification1Colr01900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )


@dataclass
class Period4ChoiceColr01900101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Colr01900101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class PostalAddress1Colr01900101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RateOrType1ChoiceColr01900101(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tp: Optional[GenericIdentification1Colr01900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class ResponseStatus9ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[ResponseStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class SecuritiesAccount19Colr01900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Colr01900101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Colr01900101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )


@dataclass
class TradingPartyCapacity5ChoiceColr01900101(ISO20022MessageElement):
    cd: Optional[TradingCapacity7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class AlternatePartyIdentification7Colr01900101(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection49Colr01900101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountColr01900101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountColr01900101] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Colr01900101] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class ClosingDate4ChoiceColr01900101(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    cd: Optional[Date3ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class CollateralParameters10Colr01900101(ISO20022MessageElement):
    coll_instr_tp: Optional[CollateralTransactionType1ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "CollInstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    xpsr_tp: Optional[ExposureType23ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    coll_sd: Optional[CollateralRole1Code] = field(
        default=None,
        metadata={
            "name": "CollSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    val_sght_mrgn_rate: Optional[RateOrType1ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "ValSghtMrgnRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    trf_titl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrfTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    sttlm_prc: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "SttlmPrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prty: Optional[GenericIdentification30Colr01900101] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    automtc_allcn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomtcAllcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    faild_sttlm_slvtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FaildSttlmSlvtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    main_tradg_acct_collstn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MainTradgAcctCollstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    bskt_id_and_elgblty_set_prfl: Optional[
        BasketIdentificationAndEligibilitySetProfile1Colr01900101
    ] = field(
        default=None,
        metadata={
            "name": "BsktIdAndElgbltySetPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    rspn_sts: Optional[ResponseStatus9ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "RspnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    addtl_inf: Optional[AdditionalInformation24Colr01900101] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class CollateralTransactionAmountBreakdown2Colr01900101(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification178Colr01900101] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    tx_amt: Optional[ActiveOrHistoricCurrencyAndAmountColr01900101] = field(
        default=None,
        metadata={
            "name": "TxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    prd: Optional[Period4ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class Linkages58Colr01900101(ISO20022MessageElement):
    msg_nb: Optional[DocumentNumber5ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    refs: Optional[References70ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )


@dataclass
class MarketIdentification84Colr01900101(ISO20022MessageElement):
    id: Optional[MarketIdentification1ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    tp: Optional[MarketType8ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Colr01900101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Colr01900101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class RateTypeAndLookback2Colr01900101(ISO20022MessageElement):
    tp: Optional[BenchmarkCurveName13ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    look_bck_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "LookBckDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[0-9]{1,3}",
        },
    )
    crstllstn_dt: Optional[CrystallisationDay1Colr01900101] = field(
        default=None,
        metadata={
            "name": "CrstllstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    tnr: Optional[InterestRateIndexTenor2Code] = field(
        default=None,
        metadata={
            "name": "Tnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SecurityIdentification19Colr01900101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Colr01900101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CollateralAmount18Colr01900101(ISO20022MessageElement):
    tx: Optional[AmountAndDirection49Colr01900101] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    termntn: Optional[AmountAndDirection49Colr01900101] = field(
        default=None,
        metadata={
            "name": "Termntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    acrd: Optional[AmountAndDirection49Colr01900101] = field(
        default=None,
        metadata={
            "name": "Acrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    cmpnd_smpl_acrl_clctn: Optional[CalculationMethod1Code] = field(
        default=None,
        metadata={
            "name": "CmpndSmplAcrlClctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    pmt_frqcy: Optional[Frequency38ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    intrst_pmt_dely: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstPmtDely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[0-9]{1,3}",
        },
    )
    tx_amt_brkdwn: list[CollateralTransactionAmountBreakdown2Colr01900101] = field(
        default_factory=list,
        metadata={
            "name": "TxAmtBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    val_sght: Optional[AmountAndDirection49Colr01900101] = field(
        default=None,
        metadata={
            "name": "ValSght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceColr01900101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr01900101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Colr01900101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class PartyIdentification134ChoiceColr01900101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr01900101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Colr01900101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PlaceOfTradeIdentification1Colr01900101(ISO20022MessageElement):
    mkt_tp_and_id: Optional[MarketIdentification84Colr01900101] = field(
        default=None,
        metadata={
            "name": "MktTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class RateOrName4ChoiceColr01900101(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rate_indx_dtls: Optional[RateTypeAndLookback2Colr01900101] = field(
        default=None,
        metadata={
            "name": "RateIndxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class SecuritiesMovement9Colr01900101(ISO20022MessageElement):
    scties_mvmnt_tp: Optional[CollateralEntryType1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Colr01900101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr01900101] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr01900101] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    coll_mvmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    clnt_scties_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntSctiesMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_scties_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrSctiesMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DealTransactionDetails5Colr01900101(ISO20022MessageElement):
    plc_of_trad: Optional[PlaceOfTradeIdentification1Colr01900101] = field(
        default=None,
        metadata={
            "name": "PlcOfTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    cncntrtn_lmt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CncntrtnLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    min_ntce_prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinNtcePrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    clsg_dt: Optional[ClosingDate4ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    deal_dtls_amt: Optional[CollateralAmount18Colr01900101] = field(
        default=None,
        metadata={
            "name": "DealDtlsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    pricg_rate_and_indx: Optional[RateOrName4ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "PricgRateAndIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    ovrnght_frqcy_rate_fxg: Optional[FrequencyRateFixing1ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "OvrnghtFrqcyRateFxg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    pmt: Optional[DeliveryReceiptType2Code] = field(
        default=None,
        metadata={
            "name": "Pmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    optn_tp: Optional[OptionType6ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    termntn_optn: Optional[RepoTerminationOption1Code] = field(
        default=None,
        metadata={
            "name": "TermntnOptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class PartyIdentification136Colr01900101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification149Colr01900101(ISO20022MessageElement):
    id: Optional[PartyIdentification134ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentificationAndAccount203Colr01900101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Colr01900101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr01900101] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr01900101] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity5ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class OtherParties38Colr01900101(ISO20022MessageElement):
    issr: Optional[PartyIdentification136Colr01900101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    invstr: list[PartyIdentification149Colr01900101] = field(
        default_factory=list,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class PartyIdentificationAndAccount202Colr01900101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Colr01900101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr01900101] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr01900101] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    acct_ownr: Optional[PartyIdentification136Colr01900101] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity5ChoiceColr01900101] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class CollateralParties10Colr01900101(ISO20022MessageElement):
    pty_a: Optional[PartyIdentificationAndAccount202Colr01900101] = field(
        default=None,
        metadata={
            "name": "PtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    clnt_pty_a: Optional[PartyIdentificationAndAccount202Colr01900101] = field(
        default=None,
        metadata={
            "name": "ClntPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    pty_b: Optional[PartyIdentificationAndAccount203Colr01900101] = field(
        default=None,
        metadata={
            "name": "PtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    clnt_pty_b: Optional[PartyIdentificationAndAccount203Colr01900101] = field(
        default=None,
        metadata={
            "name": "ClntPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    trpty_agt: Optional[PartyIdentification136Colr01900101] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    coll_acct: Optional[SecuritiesAccount19Colr01900101] = field(
        default=None,
        metadata={
            "name": "CollAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class TripartyCollateralTransactionInstructionV01Colr01900101(ISO20022MessageElement):
    tx_instr_id: Optional[TransactionIdentifications45Colr01900101] = field(
        default=None,
        metadata={
            "name": "TxInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    lnkgs: list[Linkages58Colr01900101] = field(
        default_factory=list,
        metadata={
            "name": "Lnkgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    pgntn: Optional[Pagination1Colr01900101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    gnl_params: Optional[CollateralParameters10Colr01900101] = field(
        default=None,
        metadata={
            "name": "GnlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    coll_pties: Optional[CollateralParties10Colr01900101] = field(
        default=None,
        metadata={
            "name": "CollPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    deal_tx_dtls: Optional[DealTransactionDetails5Colr01900101] = field(
        default=None,
        metadata={
            "name": "DealTxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    deal_tx_dt: Optional[CollateralDate2Colr01900101] = field(
        default=None,
        metadata={
            "name": "DealTxDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
            "required": True,
        },
    )
    scties_mvmnt: list[SecuritiesMovement9Colr01900101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    csh_mvmnt: list[CashMovement8Colr01900101] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    othr_pties: Optional[OtherParties38Colr01900101] = field(
        default=None,
        metadata={
            "name": "OthrPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Colr01900101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01",
        },
    )


@dataclass
class Colr01900101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01"

    trpty_coll_tx_instr: Optional[
        TripartyCollateralTransactionInstructionV01Colr01900101
    ] = field(
        default=None,
        metadata={
            "name": "TrptyCollTxInstr",
            "type": "Element",
            "required": True,
        },
    )
