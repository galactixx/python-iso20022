from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.colr.enums import (
    CollateralTransactionType1Code,
    ExposureType14Code,
)
from python_iso20022.enums import (
    AddressType2Code,
    CollateralRole1Code,
    CreditDebit3Code,
    CreditDebitCode,
    DateType2Code,
    ReceiveDelivery1Code,
    TradingCapacity7Code,
    TypeOfIdentification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01"


@dataclass
class ActiveCurrencyAndAmountColr02300101:
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
class ActiveOrHistoricCurrencyAndAmountColr02300101:
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
class CashAccountIdentification5ChoiceColr02300101:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class DateAndDateTime2ChoiceColr02300101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceColr02300101:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Colr02300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Colr02300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceColr02300101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Colr02300101:
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Colr02300101:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Colr02300101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentifications46Colr02300101:
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class BlockChainAddressWallet3Colr02300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CollateralDate2Colr02300101:
    trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class CollateralTransactionType1ChoiceColr02300101:
    cd: Optional[CollateralTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class Date3ChoiceColr02300101:
    cd: Optional[DateType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class ExposureType23ChoiceColr02300101:
    cd: Optional[ExposureType14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class ForeignExchangeTerms23Colr02300101:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountColr02300101] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )


@dataclass
class IdentificationType42ChoiceColr02300101:
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class OtherIdentification1Colr02300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Colr02300101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProprietaryReason4Colr02300101:
    rsn: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Quantity51ChoiceColr02300101:
    qty: Optional[FinancialInstrumentQuantity33ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Colr02300101] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class SecuritiesAccount19Colr02300101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Colr02300101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Colr02300101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )


@dataclass
class TradingPartyCapacity5ChoiceColr02300101:
    cd: Optional[TradingCapacity7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class AlternatePartyIdentification7Colr02300101:
    id_tp: Optional[IdentificationType42ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountAndDirection44Colr02300101:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountColr02300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountColr02300101] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Colr02300101] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class AmountAndDirection49Colr02300101:
    amt: Optional[ActiveCurrencyAndAmountColr02300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountColr02300101] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Colr02300101] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class ClosingDate4ChoiceColr02300101:
    dt: Optional[DateAndDateTime2ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    cd: Optional[Date3ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class NameAndAddress5Colr02300101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Colr02300101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class ProprietaryStatusAndReason6Colr02300101:
    prtry_sts: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class SecuritiesMovementStatus1ChoiceColr02300101:
    amt: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    csh: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Csh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    ccy: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    excld: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Excld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    futr: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Futr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    pdg: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    mnly_accptd: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "MnlyAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    elgblty: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Elgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    tax: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    wait: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "Wait",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class SecurityIdentification19Colr02300101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AllocationStatus1ChoiceColr02300101:
    fully_allctd: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "FullyAllctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtly_allctd: Optional[ProprietaryReason4Colr02300101] = field(
        default=None,
        metadata={
            "name": "PrtlyAllctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class CashMovement7Colr02300101:
    csh_mvmnt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CshMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    csh_amt: Optional[ActiveCurrencyAndAmountColr02300101] = field(
        default=None,
        metadata={
            "name": "CshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    mvmnt_sts: Optional[ProprietaryStatusAndReason6Colr02300101] = field(
        default=None,
        metadata={
            "name": "MvmntSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    coll_mvmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    csh_mvmnt_apprvd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CshMvmntApprvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    pos_tp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PosTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    clnt_csh_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCshMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_csh_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCshMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CollateralAmount14Colr02300101:
    tx: Optional[AmountAndDirection49Colr02300101] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    termntn: Optional[AmountAndDirection49Colr02300101] = field(
        default=None,
        metadata={
            "name": "Termntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    acrd: Optional[AmountAndDirection49Colr02300101] = field(
        default=None,
        metadata={
            "name": "Acrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    val_sght: Optional[AmountAndDirection49Colr02300101] = field(
        default=None,
        metadata={
            "name": "ValSght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    udsptd_tx: Optional[AmountAndDirection49Colr02300101] = field(
        default=None,
        metadata={
            "name": "UdsptdTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class CollateralAmount5Colr02300101:
    reqrd_mrgn: Optional[AmountAndDirection44Colr02300101] = field(
        default=None,
        metadata={
            "name": "ReqrdMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    collsd: Optional[AmountAndDirection44Colr02300101] = field(
        default=None,
        metadata={
            "name": "Collsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    rmng_collsd: Optional[AmountAndDirection44Colr02300101] = field(
        default=None,
        metadata={
            "name": "RmngCollsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sttld: Optional[AmountAndDirection44Colr02300101] = field(
        default=None,
        metadata={
            "name": "Sttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    rmng_sttlm: Optional[AmountAndDirection44Colr02300101] = field(
        default=None,
        metadata={
            "name": "RmngSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class CollateralStatus3ChoiceColr02300101:
    pdg: list[ProprietaryReason4Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: list[ProprietaryStatusAndReason6Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceColr02300101:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr02300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Colr02300101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class SecuritiesMovement8Colr02300101:
    scties_mvmnt_tp: Optional[ReceiveDelivery1Code] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Colr02300101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    scties_qty: Optional[Quantity51ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "SctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    mvmnt_sts: Optional[SecuritiesMovementStatus1ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "MvmntSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    coll_mvmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    scties_mvmnts_apprvd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctiesMvmntsApprvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    pos_tp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PosTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr02300101] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr02300101] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    clnt_scties_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntSctiesMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_scties_mvmnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrSctiesMvmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrgnd_val: Optional[AmountAndDirection44Colr02300101] = field(
        default=None,
        metadata={
            "name": "MrgndVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class SettlementStatus27ChoiceColr02300101:
    prtl_sttlm: list[ProprietaryReason4Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "PrtlSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sttld: list[ProprietaryReason4Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "Sttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    usttld: list[ProprietaryReason4Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "Usttld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class CollateralParameters13Colr02300101:
    coll_instr_tp: Optional[CollateralTransactionType1ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "CollInstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    xpsr_tp: Optional[ExposureType23ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    coll_sd: Optional[CollateralRole1Code] = field(
        default=None,
        metadata={
            "name": "CollSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    prty: Optional[GenericIdentification30Colr02300101] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    automtc_allcn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomtcAllcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    coll_apprvd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollApprvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sttlm_apprvd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SttlmApprvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    coll_amt: Optional[CollateralAmount5Colr02300101] = field(
        default=None,
        metadata={
            "name": "CollAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class DealTransactionDetails7Colr02300101:
    clsg_dt: Optional[ClosingDate4ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    deal_dtls_amt: Optional[CollateralAmount14Colr02300101] = field(
        default=None,
        metadata={
            "name": "DealDtlsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class PartyIdentification136Colr02300101:
    id: Optional[PartyIdentification120ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentificationAndAccount193Colr02300101:
    id: Optional[PartyIdentification120ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Colr02300101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class PartyIdentificationAndAccount203Colr02300101:
    id: Optional[PartyIdentification120ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Colr02300101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr02300101] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr02300101] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity5ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class PartyIdentificationAndAccount202Colr02300101:
    id: Optional[PartyIdentification120ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Colr02300101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr02300101] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr02300101] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    acct_ownr: Optional[PartyIdentification136Colr02300101] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity5ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class CollateralParties8Colr02300101:
    pty_a: Optional[PartyIdentificationAndAccount202Colr02300101] = field(
        default=None,
        metadata={
            "name": "PtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    clnt_pty_a: Optional[PartyIdentificationAndAccount193Colr02300101] = field(
        default=None,
        metadata={
            "name": "ClntPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    pty_b: Optional[PartyIdentificationAndAccount203Colr02300101] = field(
        default=None,
        metadata={
            "name": "PtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    clnt_pty_b: Optional[PartyIdentificationAndAccount193Colr02300101] = field(
        default=None,
        metadata={
            "name": "ClntPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    trpty_agt: Optional[PartyIdentification136Colr02300101] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class TripartyCollateralStatusAdviceV01Colr02300101:
    tx_instr_id: Optional[TransactionIdentifications46Colr02300101] = field(
        default=None,
        metadata={
            "name": "TxInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    pgntn: Optional[Pagination1Colr02300101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    allcn_sts: Optional[AllocationStatus1ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "AllcnSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    sttlm_sts: Optional[SettlementStatus27ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    coll_sts: Optional[CollateralStatus3ChoiceColr02300101] = field(
        default=None,
        metadata={
            "name": "CollSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    gnl_params: Optional[CollateralParameters13Colr02300101] = field(
        default=None,
        metadata={
            "name": "GnlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    coll_pties: Optional[CollateralParties8Colr02300101] = field(
        default=None,
        metadata={
            "name": "CollPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    deal_tx_dtls: Optional[DealTransactionDetails7Colr02300101] = field(
        default=None,
        metadata={
            "name": "DealTxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    deal_tx_dt: Optional[CollateralDate2Colr02300101] = field(
        default=None,
        metadata={
            "name": "DealTxDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
            "required": True,
        },
    )
    scties_mvmnt: list[SecuritiesMovement8Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    csh_mvmnt: list[CashMovement7Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Colr02300101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01",
        },
    )


@dataclass
class Colr02300101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01"

    trpty_coll_sts_advc: Optional[TripartyCollateralStatusAdviceV01Colr02300101] = (
        field(
            default=None,
            metadata={
                "name": "TrptyCollStsAdvc",
                "type": "Element",
                "required": True,
            },
        )
    )
