from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType1Code,
    AddressType2Code,
    Appearance1Code,
    CalculationType1Code,
    DistributionPolicy1Code,
    FormOfSecurity1Code,
    Operation1Code,
    Operator1Code,
    OptionParty1Code,
    OptionType1Code,
    RateType12Code,
    SecuritiesPaymentStatus1Code,
    SettlementType1Code,
    Standardisation1Code,
    TimeUnit1Code,
    TradeTransactionCondition2Code,
)
from python_iso20022.reda.enums import (
    AssignmentMethod1Code,
    BenchmarkCurveName1Code,
    CallType1Code,
    Frequency5Code,
    GlobalNote1Code,
    InitialPhysicalForm1Code,
    InitialPhysicalForm2Code,
    InstrumentSubStructureType1Code,
    InterestType3Code,
    InvestorRestrictionType1Code,
    InvestorType1Code,
    LegalRestrictions1Code,
    LegalRestrictions2Code,
    MaturityRedemptionType1Code,
    OptionStyle1Code,
    PreferenceToIncome1Code,
    PriceValueType3Code,
    PutType1Code,
    RestrictionType1Code,
    SecuritiesTransactionType11Code,
    SecurityStatus2Code,
    SettlementUnitType1Code,
    SettleStyle1Code,
    Tefrarules1Code,
    TypeOfPrice1Code,
    UnitOfMeasure9Code,
    WarrantStyle1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01"


@dataclass
class ActiveCurrencyAnd13DecimalAmountReda01200101(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountReda01200101(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountReda01200101(ISO20022MessageElement):
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
class CommunicationAddress3Reda01200101(ISO20022MessageElement):
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )
    phne: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phne",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mob",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    tlx_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TlxAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateAndDateTime2ChoiceReda01200101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class DateTimePeriod1Reda01200101(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class DateTimePeriod2Reda01200101(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class ErrorHandling3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceReda01200101(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification1Reda01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Reda01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Jurisdiction1Reda01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OriginalBusinessInstruction1Reda01200101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Pagination1Reda01200101(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class RateOrAbsoluteValue1ChoiceReda01200101(ISO20022MessageElement):
    rate_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    abs_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AbsVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda01200101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Appearance3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[Appearance1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class AssignmentMethod2ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[AssignmentMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class BenchmarkCurveName7ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[BenchmarkCurveName1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class CalculationType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[CalculationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class CallType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[CallType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class ClassificationType2Reda01200101(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    fin_instrm_pdct_tp_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmPdctTpCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    altrn_clssfctn: list[GenericIdentification36Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class DateTimePeriod1ChoiceReda01200101(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    dt_tm_rg: Optional[DateTimePeriod1Reda01200101] = field(
        default=None,
        metadata={
            "name": "DtTmRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class DistributionPolicy2ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class ErrorHandling5Reda01200101(ISO20022MessageElement):
    err: Optional[ErrorHandling3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class FinancialInstrumentName2Reda01200101(ISO20022MessageElement):
    isoshrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    isolng_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOLngNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    vld_fr: Optional[DateAndDateTime2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class FormOfSecurity8ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Frequency35ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[Frequency5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class GlobalNote2ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[GlobalNote1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class InitialPhysicalForm3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[InitialPhysicalForm2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class InitialPhysicalForm4ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[InitialPhysicalForm1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class InstrumentSubStructureType2ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[InstrumentSubStructureType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class InvestorRestrictionType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[InvestorRestrictionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class InvestorType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[InvestorType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class LegalRestrictions4ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[LegalRestrictions1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class LegalRestrictions5ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[LegalRestrictions2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class MaturityRedemptionType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[MaturityRedemptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class MessageHeader12Reda01200101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Reda01200101] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class OptionParty3ChoiceReda01200101(ISO20022MessageElement):
    cd: list[OptionParty1Code] = field(
        default_factory=list,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class OptionStyle1ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[OptionStyle1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class OptionType8ChoiceReda01200101(ISO20022MessageElement):
    cd: list[OptionType1Code] = field(
        default_factory=list,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class OtherIdentification1Reda01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification177ChoiceReda01200101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Reda01200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class PostalAddress1Reda01200101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PreferenceToIncome5ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[PreferenceToIncome1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceReda01200101(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class PriceValue1Reda01200101(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class PutType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[PutType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class RateType12FormatChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[RateType12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecuritiesAccount19Reda01200101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesPaymentStatus5ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecuritiesTransactionType31ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[SecuritiesTransactionType11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityRestrictionType2ChoiceReda01200101(ISO20022MessageElement):
    rstrctn_tp: Optional[RestrictionType1Code] = field(
        default=None,
        metadata={
            "name": "RstrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry_rstrctn: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "PrtryRstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityStatus3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[SecurityStatus2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SettleStyle2ChoiceReda01200101(ISO20022MessageElement):
    cd: list[SettleStyle1Code] = field(
        default_factory=list,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SettlementType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[SettlementType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SettlementUnitType3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[SettlementUnitType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Standardisation3ChoiceReda01200101(ISO20022MessageElement):
    cd: list[Standardisation1Code] = field(
        default_factory=list,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SupplementaryData1Reda01200101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda01200101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class Tefrarules3ChoiceReda01200101(ISO20022MessageElement):
    class Meta:
        name = "TEFRARules3Choice"

    cd: Optional[Tefrarules1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Term1Reda01200101(ISO20022MessageElement):
    oprtr: Optional[Operator1Code] = field(
        default=None,
        metadata={
            "name": "Oprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    val: Optional[RateOrAbsoluteValue1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class TimeUnit3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class TradeTransactionCondition7ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[TradeTransactionCondition2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class UnitOfMeasure7ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[UnitOfMeasure9Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class UnitOrFaceAmount1ChoiceReda01200101(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class WarrantStyle3ChoiceReda01200101(ISO20022MessageElement):
    cd: Optional[WarrantStyle1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Reda01200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class AmountOrPercentageRange1Reda01200101(ISO20022MessageElement):
    opr: Optional[Operation1Code] = field(
        default=None,
        metadata={
            "name": "Opr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    term: list[Term1Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "max_occurs": 10,
        },
    )


@dataclass
class Equity3Reda01200101(ISO20022MessageElement):
    pref_to_incm: Optional[PreferenceToIncome5ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "PrefToIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    mtrty_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    non_pd_amt: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "NonPdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    par_val: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "ParVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    vtng_rghts_per_shr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VtngRghtsPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class FinancialInstrumentForm2Reda01200101(ISO20022MessageElement):
    bookg_apprnc: Optional[Appearance3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "BookgApprnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    lgl_form: Optional[FormOfSecurity8ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "LglForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class IssuanceAccount2Reda01200101(ISO20022MessageElement):
    issnc_acct: Optional[SecuritiesAccount19Reda01200101] = field(
        default=None,
        metadata={
            "name": "IssncAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    pmry_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmryAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress4Reda01200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda01200101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Reda01200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda01200101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Price8Reda01200101(ISO20022MessageElement):
    val_tp: Optional[PriceValueType3Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    pric_tp: Optional[TypeOfPrice1Code] = field(
        default=None,
        metadata={
            "name": "PricTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class RateAndAmountFormat1ChoiceReda01200101(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    not_spcfd_rate: Optional[RateType12FormatChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "NotSpcfdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityIdentification39Reda01200101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SecurityRestriction3Reda01200101(ISO20022MessageElement):
    fctv_prd: Optional[DateTimePeriod2Reda01200101] = field(
        default=None,
        metadata={
            "name": "FctvPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    rstrctn_tp: Optional[SecurityRestrictionType2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "RstrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    lgl_rstrctn_tp: Optional[LegalRestrictions5ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "LglRstrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    invstr_rstrctn_tp: list[InvestorRestrictionType3ChoiceReda01200101] = field(
        default_factory=list,
        metadata={
            "name": "InvstrRstrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    invstr_tp: list[InvestorType3ChoiceReda01200101] = field(
        default_factory=list,
        metadata={
            "name": "InvstrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SettlementInformation17Reda01200101(ISO20022MessageElement):
    scties_qty_tp: Optional[SettlementUnitType3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "SctiesQtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    ctrct_sttlm_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "CtrctSttlmMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    min_dnmtn: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "MinDnmtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    min_mltpl_qty: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "MinMltplQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    devtg_sttlm_unit: list[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default_factory=list,
        metadata={
            "name": "DevtgSttlmUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class TradingParameters2Reda01200101(ISO20022MessageElement):
    mkt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    rnd_lot: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "RndLot",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    trad_lot_sz: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "TradLotSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    scndry_plc_of_listg: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ScndryPlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "max_occurs": 5,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    min_tradd_nmnl_qty: Optional[UnitOrFaceAmount1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "MinTraddNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    max_tradd_nmnl_qty: Optional[UnitOrFaceAmount1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "MaxTraddNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    min_tradg_pricg_incrmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinTradgPricgIncrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    pmry_plc_of_listg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmryPlcOfListgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )


@dataclass
class BenchmarkCurve6Reda01200101(ISO20022MessageElement):
    sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    bchmk_id: Optional[SecurityIdentification39Reda01200101] = field(
        default=None,
        metadata={
            "name": "BchmkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    bchmk_pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "BchmkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    bchmk_crv_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BchmkCrvCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    bchmk_crv_nm: Optional[BenchmarkCurveName7ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "BchmkCrvNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    bchmk_crv_pt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BchmkCrvPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class BusinessError4Reda01200101(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification39Reda01200101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    biz_err: list[ErrorHandling5Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class FinancialInstrumentIdentificationValidity3Reda01200101(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification39Reda01200101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    isinvld_fr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ISINVldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceReda01200101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda01200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda01200101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class PostalAddress3Reda01200101(ISO20022MessageElement):
    adr_tp: Optional[AddressType1Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    mlng_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MlngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    regn_adr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RegnAdrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    nm_and_adr: Optional[NameAndAddress4Reda01200101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class SecurityWithHoldingTax1Reda01200101(ISO20022MessageElement):
    whldg_tax_val: Optional[RateAndAmountFormat1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "WhldgTaxVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class UnderlyingAttributes4Reda01200101(ISO20022MessageElement):
    allcn_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AllcnPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qty: Optional[UnitOrFaceAmount1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    sttlm_tp: Optional[SettlementType3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "SttlmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    csh_amt: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "CshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    csh_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    drty_pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "DrtyPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    end_pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "EndPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    start_val: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "StartVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cur_val: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "CurVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    end_val: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "EndVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    adjstd_qty: Optional[UnitOrFaceAmount1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "AdjstdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cap_val: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "CapVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class YieldCalculation6Reda01200101(ISO20022MessageElement):
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    clctn_tp: Optional[CalculationType3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "ClctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    red_pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "RedPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    val_prd: Optional[DateTimePeriod1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "ValPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    clctn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )


@dataclass
class Debt5Reda01200101(ISO20022MessageElement):
    pmt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pmt_frqcy: Optional[Frequency35ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    intrst_fxg_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IntrstFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    dtd_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    frst_pmt_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    mtrty_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    nxt_cpn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "NxtCpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    putbl_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    nxt_cllbl_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    nxt_fctr_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "NxtFctrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    xprtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pmt_drctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtDrctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    odd_cpn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OddCpnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cpprgm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CPPrgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cpregn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPRegnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    intrst_acrl_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "IntrstAcrlDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pre_fndd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreFnddInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    escrwd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EscrwdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    perptl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PerptlInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    subrdntd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SubrdntdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    xtndbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XtndblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    xtndbl_prd: Optional[DateTimePeriod1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "XtndblPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    over_alltmt_amt: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "OverAlltmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    over_alltmt_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OverAlltmtRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amtsbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmtsblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    intrst_clctn_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstClctnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    cptlsd_intrst: Optional[DistributionPolicy2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "CptlsdIntrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    actl_dnmtn_amt: list[ActiveCurrencyAndAmountReda01200101] = field(
        default_factory=list,
        metadata={
            "name": "ActlDnmtnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pcs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pls_max: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlsMax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pls_per_mln: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlsPerMln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pls_per_lot: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlsPerLot",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    pls_per_trad: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlsPerTrad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    cst_pre_pmt_pnlty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CstPrePmtPnltyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    lot_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LotId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cst_pre_pmt_yld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CstPrePmtYld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    wghtd_avrg_cpn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WghtdAvrgCpn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    wghtd_avrg_life: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WghtdAvrgLife",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    wghtd_avrg_ln: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WghtdAvrgLn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    wghtd_avrg_mtrty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WghtdAvrgMtrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    insrd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InsrdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    bk_qlfd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BkQlfdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    yld_clctn: list[YieldCalculation6Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "YldClctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    intrst_tp: Optional[InterestType3Code] = field(
        default=None,
        metadata={
            "name": "IntrstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    instrm_str_tp: Optional[InstrumentSubStructureType2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "InstrmStrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    gbl_tp: Optional[GlobalNote2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "GblTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    potntl_euro_sys_elgblty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PotntlEuroSysElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    geogcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "Geogcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    yld_rg: Optional[AmountOrPercentageRange1Reda01200101] = field(
        default=None,
        metadata={
            "name": "YldRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cpn_rg: Optional[AmountOrPercentageRange1Reda01200101] = field(
        default=None,
        metadata={
            "name": "CpnRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )
    altrntv_min_tax_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AltrntvMinTaxInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    auto_rinvstmt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AutoRinvstmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tx_conds: Optional[TradeTransactionCondition7ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "TxConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    look_bck: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LookBck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_sbstitn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSbstitn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    min_incrmt: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "MinIncrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    min_qty: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "MinQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pdctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rstrctd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RstrctdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pric_frqcy: Optional[Frequency35ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "PricFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sbstitn_frqcy: Optional[Frequency35ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "SbstitnFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    sbstitn_lft: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SbstitnLft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    whl_pool_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WhlPoolInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pric_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pric_rg: Optional[AmountOrPercentageRange1Reda01200101] = field(
        default=None,
        metadata={
            "name": "PricRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Future4Reda01200101(ISO20022MessageElement):
    ctrct_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    exrc_pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    futr_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FutrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    min_sz: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "MinSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    unit_of_measr: Optional[UnitOfMeasure7ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tm_unit: Optional[TimeUnit3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "TmUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    addtl_undrlyg_attrbts: list[UnderlyingAttributes4Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlUndrlygAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Option15Reda01200101(ISO20022MessageElement):
    optn_sttlm_style: Optional[SettleStyle2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "OptnSttlmStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    convs_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ConvsDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    strk_pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    min_exrcbl_qty: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "MinExrcblQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    convs_prd: Optional[DateTimePeriod1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "ConvsPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    optn_style: Optional[OptionStyle1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    optn_tp: Optional[OptionType8ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    strk_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StrkVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    strk_mltplr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StrkMltplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    instrm_assgnmt_mtd: Optional[AssignmentMethod2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "InstrmAssgnmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    vrsn_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VrsnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    xpry_lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    stdstn: Optional[Standardisation3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Stdstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tradg_pty_role: Optional[OptionParty3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "TradgPtyRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    ctrct_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    addtl_undrlyg_attrbts: list[UnderlyingAttributes4Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlUndrlygAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Organisation38Reda01200101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    id: Optional[PartyIdentification177ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    taxtn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ntl_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstl_adr: list[PostalAddress3Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
    pmry_com_adr: Optional[CommunicationAddress3Reda01200101] = field(
        default=None,
        metadata={
            "name": "PmryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    scndry_com_adr: Optional[CommunicationAddress3Reda01200101] = field(
        default=None,
        metadata={
            "name": "ScndryComAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class PartyIdentification136Reda01200101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Derivative4Reda01200101(ISO20022MessageElement):
    futr: Optional[Future4Reda01200101] = field(
        default=None,
        metadata={
            "name": "Futr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    optn: Optional[Option15Reda01200101] = field(
        default=None,
        metadata={
            "name": "Optn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Issuance6Reda01200101(ISO20022MessageElement):
    isse_plc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssePlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ctry_of_isse: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    anncmnt_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AnncmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    issr_org: Optional[Organisation38Reda01200101] = field(
        default=None,
        metadata={
            "name": "IssrOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    isse_nmnl_amt: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "IsseNmnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    full_issd_amt: Optional[ActiveCurrencyAndAmountReda01200101] = field(
        default=None,
        metadata={
            "name": "FullIssdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    isse_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IsseSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    isse_pric: Optional[PriceValue1Reda01200101] = field(
        default=None,
        metadata={
            "name": "IssePric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    issnc_dstrbtn: Optional[SecuritiesTransactionType31ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "IssncDstrbtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    govng_law: list[Jurisdiction1Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "GovngLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SystemPartyIdentification8Reda01200101(ISO20022MessageElement):
    id: Optional[PartyIdentification136Reda01200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda01200101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Warrant4Reda01200101(ISO20022MessageElement):
    mltplr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Mltplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    sbcpt_pric: Optional[Price8Reda01200101] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tp: Optional[WarrantStyle3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    warrt_agt: list[Organisation38Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "WarrtAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class FinancialInstrument97Reda01200101(ISO20022MessageElement):
    eqty: Optional[Equity3Reda01200101] = field(
        default=None,
        metadata={
            "name": "Eqty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    warrt: Optional[Warrant4Reda01200101] = field(
        default=None,
        metadata={
            "name": "Warrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    debt: Optional[Debt5Reda01200101] = field(
        default=None,
        metadata={
            "name": "Debt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    deriv: Optional[Derivative4Reda01200101] = field(
        default=None,
        metadata={
            "name": "Deriv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SystemPartyIdentification2ChoiceReda01200101(ISO20022MessageElement):
    org_id: Optional[PartyIdentification136Reda01200101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cmbnd_id: Optional[SystemPartyIdentification8Reda01200101] = field(
        default=None,
        metadata={
            "name": "CmbndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityCsdlink7Reda01200101(ISO20022MessageElement):
    class Meta:
        name = "SecurityCSDLink7"

    vld_fr: Optional[DateAndDateTime2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    vld_to: Optional[DateAndDateTime2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "VldTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    scty_mntnc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctyMntnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    issr_csd: Optional[SystemPartyIdentification2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "IssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    invstr_csd: Optional[SystemPartyIdentification2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "InvstrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tech_issr_csd: Optional[SystemPartyIdentification2ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "TechIssrCSD",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    issnc_acct: list[IssuanceAccount2Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "IssncAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class CommonFinancialInstrumentAttributes11Reda01200101(ISO20022MessageElement):
    scty_sts: Optional[SecurityStatus3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "SctySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    fin_instrm_nm: list[FinancialInstrumentName2Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cert_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctrct_vrsn_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrctVrsnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cpn_attchd_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[0-9]{1,3}",
        },
    )
    tax_lot_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxLotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    pool_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    cvrd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CvrdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    lgl_rstrctns: Optional[LegalRestrictions4ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "LglRstrctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pos_lmt: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "PosLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    near_term_pos_lmt: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "NearTermPosLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    listg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ListgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    rcrd_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )
    clssfctn_tp: Optional[ClassificationType2Reda01200101] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    issnc: Optional[Issuance6Reda01200101] = field(
        default=None,
        metadata={
            "name": "Issnc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tradg_mkt: list[TradingParameters2Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "TradgMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    sprd_and_bchmk_crv: list[BenchmarkCurve6Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "SprdAndBchmkCrv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    put_tp: Optional[PutType3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "PutTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    call_tp: Optional[CallType3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "CallTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    fngb_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FngbInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cnfdtl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cnfdtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prvt_plcmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrvtPlcmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    convtbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConvtblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    convs_prd: Optional[DateTimePeriod1Reda01200101] = field(
        default=None,
        metadata={
            "name": "ConvsPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    convs_ratio_nmrtr: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "ConvsRatioNmrtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    convs_ratio_dnmtr: Optional[FinancialInstrumentQuantity1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "ConvsRatioDnmtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pmry_plc_of_dpst: Optional[PartyIdentification136Reda01200101] = field(
        default=None,
        metadata={
            "name": "PmryPlcOfDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tradg_mtd: Optional[UnitOrFaceAmount1ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "TradgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    tefrarule: Optional[Tefrarules3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "TEFRARule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    sr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "Clss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    whldg_tax_rgm: list[SecurityWithHoldingTax1Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus5ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    initl_phys_form: Optional[InitialPhysicalForm4ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "InitlPhysForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    aftr_xchg_phys_form: Optional[InitialPhysicalForm3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "AftrXchgPhysForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    cmon_sfkpr: Optional[PartyIdentification177ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "CmonSfkpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    red_tp: Optional[MaturityRedemptionType3ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "RedTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    red_pmt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RedPmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    rstrctn: list[SecurityRestriction3Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "Rstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    fin_instrm_id_vldty: list[
        FinancialInstrumentIdentificationValidity3Reda01200101
    ] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmIdVldty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    sttlm_inf: list[SettlementInformation17Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "SttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    fin_instrm_form: Optional[FinancialInstrumentForm2Reda01200101] = field(
        default=None,
        metadata={
            "name": "FinInstrmForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    ctct_nm: Optional[Organisation38Reda01200101] = field(
        default=None,
        metadata={
            "name": "CtctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    lead_mgr: Optional[Organisation38Reda01200101] = field(
        default=None,
        metadata={
            "name": "LeadMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    prncpl_png_agt: Optional[Organisation38Reda01200101] = field(
        default=None,
        metadata={
            "name": "PrncplPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    png_agt: Optional[Organisation38Reda01200101] = field(
        default=None,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    dpstry: Optional[Organisation38Reda01200101] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    undrlyg_rsk: Optional[Organisation38Reda01200101] = field(
        default=None,
        metadata={
            "name": "UndrlygRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    scty_csdlk: list[SecurityCsdlink7Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "SctyCSDLk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityAttributes11Reda01200101(ISO20022MessageElement):
    fin_instrm_id: list[SecurityIdentification39Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    fin_instrm_tp: Optional[FinancialInstrument97Reda01200101] = field(
        default=None,
        metadata={
            "name": "FinInstrmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    fin_instrm_attrbts: list[CommonFinancialInstrumentAttributes11Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityOrBusinessError4ChoiceReda01200101(ISO20022MessageElement):
    scty_rpt: list[SecurityAttributes11Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "SctyRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    biz_err: list[BusinessError4Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityOrOperationalError4ChoiceReda01200101(ISO20022MessageElement):
    scty_rpt_or_biz_err: Optional[SecurityOrBusinessError4ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "SctyRptOrBizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    oprl_err: list[ErrorHandling5Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class SecurityReportV01Reda01200101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader12Reda01200101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )
    pgntn: Optional[Pagination1Reda01200101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    scty_rpt_or_err: Optional[SecurityOrOperationalError4ChoiceReda01200101] = field(
        default=None,
        metadata={
            "name": "SctyRptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda01200101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01",
        },
    )


@dataclass
class Reda01200101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01"

    scty_rpt: Optional[SecurityReportV01Reda01200101] = field(
        default=None,
        metadata={
            "name": "SctyRpt",
            "type": "Element",
            "required": True,
        },
    )
