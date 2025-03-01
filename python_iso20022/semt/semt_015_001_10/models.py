from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    CreditDebitCode,
    EventFrequency3Code,
    FormOfSecurity1Code,
    InterestComputationMethod2Code,
    OptionStyle2Code,
    OptionType1Code,
    PartialSettlement2Code,
    PriceValueType1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SecuritiesPaymentStatus1Code,
)
from python_iso20022.semt.enums import (
    CorporateActionEventType38Code,
    SecuritiesBalanceType11Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10"


@dataclass
class ActiveCurrencyAndAmountSemt01500110(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSemt01500110(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSemt01500110(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSemt01500110(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSemt01500110(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification1Semt01500110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Semt01500110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt01500110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Semt01500110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Linkages75Semt01500110(ISO20022MessageElement):
    scties_sttlm_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSemt01500110(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt01500110(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AdditionalParameters33Semt01500110(ISO20022MessageElement):
    prtl_sttlm: Optional[PartialSettlement2Code] = field(
        default=None,
        metadata={
            "name": "PrtlSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prvs_prtl_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvsPrtlConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctr_pty_mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyMktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BlockChainAddressWallet3Semt01500110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ClassificationType32ChoiceSemt01500110(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Semt01500110] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class CorporateActionEventType110ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType38Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class ForeignExchangeTerms23Semt01500110(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountSemt01500110] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )


@dataclass
class FormOfSecurity6ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class Frequency23ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class GenericIdentification78Semt01500110(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class Number22ChoiceSemt01500110(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[GenericIdentification1Semt01500110] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class OptionStyle8ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class OptionType6ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class OtherIdentification1Semt01500110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt01500110(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt01500110] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSemt01500110(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt01500110] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class QuantityBreakdown60Semt01500110(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification37Semt01500110] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class QuantityBreakdown61Semt01500110(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification37Semt01500110] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    lot_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    scties_sub_bal_tp: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "SctiesSubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Semt01500110(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Semt01500110(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Semt01500110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesBalanceType6ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[SecuritiesBalanceType11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class SecuritiesPaymentStatus5ChoiceSemt01500110(ISO20022MessageElement):
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class SupplementaryData1Semt01500110(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt01500110] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSemt01500110(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class AmountAndDirection44Semt01500110(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt01500110] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    orgnl_ccy_and_ordrd_amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt01500110] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlCcyAndOrdrdAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            },
        )
    )
    fxdtls: Optional[ForeignExchangeTerms23Semt01500110] = field(
        default=None,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class Price7Semt01500110(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType1ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceFormat41ChoiceSemt01500110(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Semt01500110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Semt01500110] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prtry: Optional[GenericIdentification78Semt01500110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class SecuritiesSubBalanceTypeAndQuantityBreakdown5Semt01500110(ISO20022MessageElement):
    tp: Optional[SecuritiesBalanceType6ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    qty_brkdwn: list[QuantityBreakdown61Semt01500110] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class SecurityIdentification19Semt01500110(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt01500110] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class IntraPositionDetails65Semt01500110(ISO20022MessageElement):
    sttld_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "SttldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    scties_sub_bal_id: Optional[GenericIdentification37Semt01500110] = field(
        default=None,
        metadata={
            "name": "SctiesSubBalId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    coll_mntr_amt: Optional[AmountAndDirection44Semt01500110] = field(
        default=None,
        metadata={
            "name": "CollMntrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prevsly_sttld_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01500110] = (
        field(
            default=None,
            metadata={
                "name": "PrevslySttldQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            },
        )
    )
    rmng_to_be_sttld_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01500110] = (
        field(
            default=None,
            metadata={
                "name": "RmngToBeSttldQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            },
        )
    )
    sttlm_dt: Optional[DateAndDateTime2ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    avlbl_dt: Optional[DateAndDateTime2ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "AvlblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    corp_actn_evt_tp: Optional[CorporateActionEventType110ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    bal_fr: Optional[SecuritiesSubBalanceTypeAndQuantityBreakdown5Semt01500110] = field(
        default=None,
        metadata={
            "name": "BalFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    bal_to: Optional[SecuritiesSubBalanceTypeAndQuantityBreakdown5Semt01500110] = field(
        default=None,
        metadata={
            "name": "BalTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    instr_prcg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrPrcgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PriceType4ChoiceSemt01500110(ISO20022MessageElement):
    mkt: Optional[Price7Semt01500110] = field(
        default=None,
        metadata={
            "name": "Mkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    indctv: Optional[Price7Semt01500110] = field(
        default=None,
        metadata={
            "name": "Indctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class FinancialInstrumentAttributes112Semt01500110(ISO20022MessageElement):
    plc_of_listg: Optional[MarketIdentification3ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    regn_form: Optional[FormOfSecurity6ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    pmt_frqcy: Optional[Frequency23ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus5ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency23ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    optn_tp: Optional[OptionType6ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld_to_mtrty_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YldToMtrtyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number22ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    pool_nb: Optional[GenericIdentification37Semt01500110] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    qty_brkdwn: list[QuantityBreakdown60Semt01500110] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    mkt_or_indctv_pric: Optional[PriceType4ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "MktOrIndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    exrc_pric: Optional[Price7Semt01500110] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    sbcpt_pric: Optional[Price7Semt01500110] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    convs_pric: Optional[Price7Semt01500110] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    strk_pric: Optional[Price7Semt01500110] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    undrlyg_fin_instrm_id: list[SecurityIdentification19Semt01500110] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class IntraPositionMovementConfirmationV10Semt01500110(ISO20022MessageElement):
    addtl_params: Optional[AdditionalParameters33Semt01500110] = field(
        default=None,
        metadata={
            "name": "AddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    lkg: Optional[Linkages75Semt01500110] = field(
        default=None,
        metadata={
            "name": "Lkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Semt01500110] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt01500110] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat41ChoiceSemt01500110] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Semt01500110] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes112Semt01500110] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )
    intra_pos_dtls: Optional[IntraPositionDetails65Semt01500110] = field(
        default=None,
        metadata={
            "name": "IntraPosDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Semt01500110] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10",
        },
    )


@dataclass
class Semt01500110(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.015.001.10"

    intra_pos_mvmnt_conf: Optional[IntraPositionMovementConfirmationV10Semt01500110] = (
        field(
            default=None,
            metadata={
                "name": "IntraPosMvmntConf",
                "type": "Element",
                "required": True,
            },
        )
    )
