from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    ChargeBearerType1Code,
    ClearingChannel2Code,
    CreditDebitCode,
    DocumentType3Code,
    DocumentType6Code,
    Instruction4Code,
    NamePrefix2Code,
    PreferredContactMethod1Code,
    Priority2Code,
    Priority3Code,
    RegulatoryReportingType1Code,
    RemittanceLocationMethod2Code,
    SettlementMethod1Code,
    TaxRecordPeriod1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04"


@dataclass
class AccountSchemeName1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountTrck00100104(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountTrck00100104(ISO20022MessageElement):
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
class CashAccountType2ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CategoryPurpose1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification3ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyExchange13Trck00100104(ISO20022MessageElement):
    src_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trgt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class CurrencyExchange15Trck00100104(ISO20022MessageElement):
    src_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    trgt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceTrck00100104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Trck00100104(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod2Trck00100104(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )


@dataclass
class DiscountAmountType1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineType1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GarnishmentType1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Trck00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstructionForCreditorAgent3Trck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class LocalInstrument2ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessInstruction4Trck00100104(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class OtherContact1Trck00100104(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PaymentIdentification10Trck00100104(ISO20022MessageElement):
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    clr_sys_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrSysRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentScenario1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Purpose2ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RegulatoryAuthority2Trck00100104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class RelatedTransactionData1Trck00100104(ISO20022MessageElement):
    mstr_uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrUETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    sub_uetr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SubUETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )


@dataclass
class ReturnReason5ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceLevel8ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SettlementDateTimeIndication1Trck00100104(ISO20022MessageElement):
    dbt_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DbtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdt_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CdtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class SettlementTimeRequest2Trck00100104(ISO20022MessageElement):
    clstm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "CLSTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    till_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "TillTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    fr_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "FrTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rjct_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "RjctTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class StatusReason6ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Trck00100104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TaxAmountType1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TaxAuthorisation1Trck00100104(ISO20022MessageElement):
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TaxParty1Trck00100104(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AddressType3ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Trck00100104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Trck00100104(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact4Trck00100104(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class CreditorReferenceType1ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[DocumentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DiscountAmountAndType1Trck00100104(ISO20022MessageElement):
    tp: Optional[DiscountAmountType1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )


@dataclass
class DocumentAdjustment1Trck00100104(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DocumentLineType1Trck00100104(ISO20022MessageElement):
    cd_or_prtry: Optional[DocumentLineType1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EquivalentAmount2Trck00100104(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    ccy_of_trf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOfTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class GarnishmentType1Trck00100104(ISO20022MessageElement):
    cd_or_prtry: Optional[GarnishmentType1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericAccountIdentification1Trck00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Trck00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Trck00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Trck00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstructionForNextAgent1Trck00100104(ISO20022MessageElement):
    cd: Optional[Instruction4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PaymentRejectReturnReason1Trck00100104(ISO20022MessageElement):
    rsn: Optional[ReturnReason5ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class PaymentStatusReason1Trck00100104(ISO20022MessageElement):
    rsn: Optional[StatusReason6ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class PaymentTypeInformation28Trck00100104(ISO20022MessageElement):
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    clr_chanl: Optional[ClearingChannel2Code] = field(
        default=None,
        metadata={
            "name": "ClrChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    svc_lvl: list[ServiceLevel8ChoiceTrck00100104] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class ProxyAccountIdentification1Trck00100104(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class ReferredDocumentType3ChoiceTrck00100104(ISO20022MessageElement):
    cd: Optional[DocumentType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class StructuredRegulatoryReporting3Trck00100104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Trck00100104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )


@dataclass
class TaxAmountAndType1Trck00100104(ISO20022MessageElement):
    tp: Optional[TaxAmountType1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )


@dataclass
class TaxParty2Trck00100104(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authstn: Optional[TaxAuthorisation1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TaxPeriod2Trck00100104(ISO20022MessageElement):
    yr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Yr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    tp: Optional[TaxRecordPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    fr_to_dt: Optional[DatePeriod2Trck00100104] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TrackerData8Trck00100104(ISO20022MessageElement):
    confd_dt: Optional[DateAndDateTime2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "ConfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    confd_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "ConfdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rtrd_confd_dt: Optional[DateAndDateTime2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "RtrdConfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rtrd_confd_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "RtrdConfdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rmng_to_be_confd_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "RmngToBeConfdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prevsly_confd_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "PrevslyConfdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prevsly_confd_dt: Optional[DateAndDateTime2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "PrevslyConfdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class AccountIdentification4ChoiceTrck00100104(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class CreditorReferenceType2Trck00100104(ISO20022MessageElement):
    cd_or_prtry: Optional[CreditorReferenceType1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineIdentification1Trck00100104(ISO20022MessageElement):
    tp: Optional[DocumentLineType1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class FinancialInstitutionIdentification21Trck00100104(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Trck00100104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[GenericFinancialIdentification1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class OrganisationIdentification29Trck00100104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class PersonIdentification13Trck00100104(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Trck00100104] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    othr: list[GenericPersonIdentification1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class PostalAddress24Trck00100104(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ReferredDocumentType4Trck00100104(ISO20022MessageElement):
    cd_or_prtry: Optional[ReferredDocumentType3ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RegulatoryReporting3Trck00100104(ISO20022MessageElement):
    dbt_cdt_rptg_ind: Optional[RegulatoryReportingType1Code] = field(
        default=None,
        metadata={
            "name": "DbtCdtRptgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    authrty: Optional[RegulatoryAuthority2Trck00100104] = field(
        default=None,
        metadata={
            "name": "Authrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dtls: list[StructuredRegulatoryReporting3Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class RemittanceAmount2Trck00100104(ISO20022MessageElement):
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    tax_amt: list[TaxAmountAndType1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class RemittanceAmount3Trck00100104(ISO20022MessageElement):
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    tax_amt: list[TaxAmountAndType1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TaxRecordDetails2Trck00100104(ISO20022MessageElement):
    prd: Optional[TaxPeriod2Trck00100104] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )


@dataclass
class TrackerStatus1Trck00100104(ISO20022MessageElement):
    sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    dt: Optional[DateAndDateTime2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    sts_rsn: list[PaymentStatusReason1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rjct_rtr_rsn: list[PaymentRejectReturnReason1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "RjctRtrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class BranchData3Trck00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Trck00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class CashAccount38Trck00100104(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class CreditorReferenceInformation2Trck00100104(ISO20022MessageElement):
    tp: Optional[CreditorReferenceType2Trck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineInformation1Trck00100104(ISO20022MessageElement):
    id: list[DocumentLineIdentification1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_occurs": 1,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    amt: Optional[RemittanceAmount3Trck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class FinancialInstitutionIdentification18Trck00100104(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Trck00100104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Trck00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    othr: Optional[GenericFinancialIdentification1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class NameAndAddress16Trck00100104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    adr: Optional[PostalAddress24Trck00100104] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )


@dataclass
class Party38ChoiceTrck00100104(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification29Trck00100104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvt_id: Optional[PersonIdentification13Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TaxAmount2Trck00100104(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "TaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dtls: list[TaxRecordDetails2Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TrackerParty2ChoiceTrck00100104(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification29Trck00100104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvt_id: Optional[PersonIdentification13Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    fin_instn_id: Optional[FinancialInstitutionIdentification21Trck00100104] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification6Trck00100104(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification18Trck00100104] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData3Trck00100104] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class PartyIdentification135Trck00100104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Trck00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    id: Optional[Party38ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact4Trck00100104] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class ReferredDocumentInformation7Trck00100104(ISO20022MessageElement):
    tp: Optional[ReferredDocumentType4Trck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    line_dtls: list[DocumentLineInformation1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "LineDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class RemittanceLocationData1Trck00100104(ISO20022MessageElement):
    mtd: Optional[RemittanceLocationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    elctrnc_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    pstl_adr: Optional[NameAndAddress16Trck00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TaxRecord2Trck00100104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtgyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[TaxPeriod2Trck00100104] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    tax_amt: Optional[TaxAmount2Trck00100104] = field(
        default=None,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TrackerPartyIdentification2Trck00100104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Trck00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    id: Optional[TrackerParty2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class Charges7Trck00100104(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )


@dataclass
class Garnishment3Trck00100104(ISO20022MessageElement):
    tp: Optional[GarnishmentType1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    grnshee: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "Grnshee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    grnshmt_admstr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "GrnshmtAdmstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    fmly_mdcl_insrnc_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FmlyMdclInsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    mplyee_termntn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MplyeeTermntnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class Party40ChoiceTrck00100104(ISO20022MessageElement):
    pty: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class RemittanceLocation7Trck00100104(ISO20022MessageElement):
    rmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmt_lctn_dtls: list[RemittanceLocationData1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "RmtLctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class SettlementInstruction9Trck00100104(ISO20022MessageElement):
    sttlm_mtd: Optional[SettlementMethod1Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    sttlm_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "SttlmAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    clr_sys: Optional[ClearingSystemIdentification3ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "ClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instg_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instg_rmbrsmnt_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instd_rmbrsmnt_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    thrd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    thrd_rmbrsmnt_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TaxInformation7Trck00100104(ISO20022MessageElement):
    cdtr: Optional[TaxParty1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr: Optional[TaxParty2Trck00100104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ultmt_dbtr: Optional[TaxParty2Trck00100104] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord2Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TaxInformation8Trck00100104(ISO20022MessageElement):
    cdtr: Optional[TaxParty1Trck00100104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr: Optional[TaxParty2Trck00100104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord2Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TrackerHeader6Trck00100104(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[0-9]{1,15}",
        },
    )
    trckr_infrmg_pty: Optional[TrackerPartyIdentification2Trck00100104] = field(
        default=None,
        metadata={
            "name": "TrckrInfrmgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    trckr_infrmd_pty: Optional[TrackerPartyIdentification2Trck00100104] = field(
        default=None,
        metadata={
            "name": "TrckrInfrmdPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    svc_lvl: Optional[ServiceLevel8ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TrackerRecord8Trck00100104(ISO20022MessageElement):
    pty_or_agt_id: Optional[TrackerPartyIdentification2Trck00100104] = field(
        default=None,
        metadata={
            "name": "PtyOrAgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intr_bk_sttlm_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    chrg_br: Optional[ChargeBearerType1Code] = field(
        default=None,
        metadata={
            "name": "ChrgBr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    chrgs_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "ChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    xchg_rate_data: Optional[CurrencyExchange13Trck00100104] = field(
        default=None,
        metadata={
            "name": "XchgRateData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prcg_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PrcgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class StructuredRemittanceInformation16Trck00100104(ISO20022MessageElement):
    rfrd_doc_inf: list[ReferredDocumentInformation7Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "RfrdDocInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rfrd_doc_amt: Optional[RemittanceAmount2Trck00100104] = field(
        default=None,
        metadata={
            "name": "RfrdDocAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr_ref_inf: Optional[CreditorReferenceInformation2Trck00100104] = field(
        default=None,
        metadata={
            "name": "CdtrRefInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    invcr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "Invcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    invcee: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "Invcee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    tax_rmt: Optional[TaxInformation7Trck00100104] = field(
        default=None,
        metadata={
            "name": "TaxRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    grnshmt_rmt: Optional[Garnishment3Trck00100104] = field(
        default=None,
        metadata={
            "name": "GrnshmtRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    addtl_rmt_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TransactionParties8Trck00100104(ISO20022MessageElement):
    ultmt_dbtr: Optional[Party40ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr: Optional[Party40ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    dbtr_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    initg_pty: Optional[Party40ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt1: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt1_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt2: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt2_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt3: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt3_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt1_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt2_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt3",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt3_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr: Optional[Party40ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    cdtr_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ultmt_cdtr: Optional[Party40ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class RemittanceInformation16Trck00100104(ISO20022MessageElement):
    ustrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: list[StructuredRemittanceInformation16Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class CreditTransferTransaction46Trck00100104(ISO20022MessageElement):
    ultmt_dbtr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    initg_pty: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt1: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt1_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt2: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt2_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt3: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt3_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt1_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt2_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt3",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt3_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ultmt_cdtr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instr_for_cdtr_agt: list[InstructionForCreditorAgent3Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "InstrForCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instr_for_nxt_agt: list[InstructionForNextAgent1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "InstrForNxtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    tax: Optional[TaxInformation8Trck00100104] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rmt_inf: Optional[RemittanceInformation16Trck00100104] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TrackerPaymentTransaction14Trck00100104(ISO20022MessageElement):
    trckd_msg_id: Optional[OriginalBusinessInstruction4Trck00100104] = field(
        default=None,
        metadata={
            "name": "TrckdMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    trckr_infrmg_pty: Optional[TrackerPartyIdentification2Trck00100104] = field(
        default=None,
        metadata={
            "name": "TrckrInfrmgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    trckr_infrmd_pty: Optional[TrackerPartyIdentification2Trck00100104] = field(
        default=None,
        metadata={
            "name": "TrckrInfrmdPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    tech_sndr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechSndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    tech_rcvr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    pmt_id: Optional[PaymentIdentification10Trck00100104] = field(
        default=None,
        metadata={
            "name": "PmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rltd_pmt_id: Optional[RelatedTransactionData1Trck00100104] = field(
        default=None,
        metadata={
            "name": "RltdPmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    orgnl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlEndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_tp_inf: Optional[PaymentTypeInformation28Trck00100104] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    pmt_scnro: Optional[PaymentScenario1ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "PmtScnro",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    sttlm_inf: Optional[SettlementInstruction9Trck00100104] = field(
        default=None,
        metadata={
            "name": "SttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intr_bk_sttlm_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rtrd_intr_bk_sttlm_amt: Optional[ActiveCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "RtrdIntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    sttlm_prty: Optional[Priority3Code] = field(
        default=None,
        metadata={
            "name": "SttlmPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    sttlm_tm_indctn: Optional[SettlementDateTimeIndication1Trck00100104] = field(
        default=None,
        metadata={
            "name": "SttlmTmIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    sttlm_tm_req: Optional[SettlementTimeRequest2Trck00100104] = field(
        default=None,
        metadata={
            "name": "SttlmTmReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    accptnc_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AccptncDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    poolg_adjstmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PoolgAdjstmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    eqvt_amt: Optional[EquivalentAmount2Trck00100104] = field(
        default=None,
        metadata={
            "name": "EqvtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rtrd_instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountTrck00100104] = field(
        default=None,
        metadata={
            "name": "RtrdInstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    xchg_rate_data: Optional[CurrencyExchange15Trck00100104] = field(
        default=None,
        metadata={
            "name": "XchgRateData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    chrg_br: Optional[ChargeBearerType1Code] = field(
        default=None,
        metadata={
            "name": "ChrgBr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    chrgs_inf: list[Charges7Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "ChrgsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    trckr_rcrd: list[TrackerRecord8Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "TrckrRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    trckr_data: Optional[TrackerData8Trck00100104] = field(
        default=None,
        metadata={
            "name": "TrckrData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbt_conf_urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtConfURLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    prvs_instg_agt1: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt1_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt2: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt2_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt3: Optional[
        BranchAndFinancialInstitutionIdentification6Trck00100104
    ] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    prvs_instg_agt3_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "PrvsInstgAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt1_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt1Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt2_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt2Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt3",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    intrmy_agt3_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt3Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ultmt_dbtr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    initg_pty: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr: Optional[Party40ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Trck00100104] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr: Optional[Party40ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    cdtr_acct: Optional[CashAccount38Trck00100104] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    ultmt_cdtr: Optional[PartyIdentification135Trck00100104] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instr_for_cdtr_agt: list[InstructionForCreditorAgent3Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "InstrForCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    instr_for_nxt_agt: list[InstructionForNextAgent1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "InstrForNxtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    purp: Optional[Purpose2ChoiceTrck00100104] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rgltry_rptg: list[RegulatoryReporting3Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "RgltryRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "max_occurs": 10,
        },
    )
    tax: Optional[TaxInformation8Trck00100104] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rltd_rmt_inf: list[RemittanceLocation7Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "RltdRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "max_occurs": 10,
        },
    )
    rmt_inf: Optional[RemittanceInformation16Trck00100104] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rjct_rtr_rsn: list[PaymentRejectReturnReason1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "RjctRtrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    rtr_chain: Optional[TransactionParties8Trck00100104] = field(
        default=None,
        metadata={
            "name": "RtrChain",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )
    undrlyg_cstmr_cdt_trf: Optional[CreditTransferTransaction46Trck00100104] = field(
        default=None,
        metadata={
            "name": "UndrlygCstmrCdtTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class TrackerStatusAndTransaction19Trck00100104(ISO20022MessageElement):
    tx_sts: Optional[TrackerStatus1Trck00100104] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    tx: list[TrackerPaymentTransaction14Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class PaymentStatusTrackerUpdateV04Trck00100104(ISO20022MessageElement):
    grp_hdr: Optional[TrackerHeader6Trck00100104] = field(
        default=None,
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "required": True,
        },
    )
    trckr_sts_and_tx: list[TrackerStatusAndTransaction19Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "TrckrStsAndTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Trck00100104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04",
        },
    )


@dataclass
class Trck00100104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:trck.001.001.04"

    pmt_sts_trckr_upd: Optional[PaymentStatusTrackerUpdateV04Trck00100104] = field(
        default=None,
        metadata={
            "name": "PmtStsTrckrUpd",
            "type": "Element",
            "required": True,
        },
    )
