from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    ClearingChannel2Code,
    CreditDebitCode,
    DocumentType3Code,
    DocumentType6Code,
    Frequency6Code,
    InvestigationLocationMethod1Code,
    MandateClassification1Code,
    NamePrefix2Code,
    PaymentMethod4Code,
    PreferredContactMethod1Code,
    Priority2Code,
    SequenceType3Code,
    SettlementMethod1Code,
    TaxRecordPeriod1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01"


@dataclass
class AccountSchemeName1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountCamt11000101(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountCamt11000101(ISO20022MessageElement):
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
class CancellationReason33ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountType2ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CategoryPurpose1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification3ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceCamt11000101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Camt11000101(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod2Camt11000101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class DatePeriod5Camt11000101(ISO20022MessageElement):
    cur_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CurValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    reqd_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class DiscountAmountType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GarnishmentType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt11000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt11000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestigationActionReason1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestigationReason1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestigationReasonSubType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestigationRequestAction1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestigationServiceLevel1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestigationSubType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvestigationType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LocalInstrument2ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MandateSetupReason1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalGroupInformation29Camt11000101(ISO20022MessageElement):
    orgnl_msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrgnlCreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class OtherContact1Camt11000101(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Purpose2ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceLevel8ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SkipPayloadCamt11000101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt11000101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TaxAmountType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TaxAuthorisation1Camt11000101(ISO20022MessageElement):
    titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Titl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TaxParty1Camt11000101(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UnderlyingGroupInformation1Camt11000101(ISO20022MessageElement):
    orgnl_msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrgnlCreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_msg_dlvry_chanl: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgDlvryChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UnderlyingInvestigationInstrument1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AddressType3ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class AdjustmentRequest1Camt11000101(ISO20022MessageElement):
    prd: Optional[DatePeriod5Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt11000101(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact4Camt11000101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod1Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class CreditorReferenceType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[DocumentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DiscountAmountAndType1Camt11000101(ISO20022MessageElement):
    tp: Optional[DiscountAmountType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class DocumentAdjustment1Camt11000101(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DocumentFormat1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class DocumentLineType1Camt11000101(ISO20022MessageElement):
    cd_or_prtry: Optional[DocumentLineType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentType1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class EquivalentAmount2Camt11000101(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    ccy_of_trf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CcyOfTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class FrequencyAndMoment1Camt11000101(ISO20022MessageElement):
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    pt_in_tm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class FrequencyPeriod1Camt11000101(ISO20022MessageElement):
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    cnt_per_prd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CntPerPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class GarnishmentType1Camt11000101(ISO20022MessageElement):
    cd_or_prtry: Optional[GarnishmentType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericAccountIdentification1Camt11000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt11000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Camt11000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Camt11000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MandateClassification1ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[MandateClassification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentTypeInformation27Camt11000101(ISO20022MessageElement):
    instr_prty: Optional[Priority2Code] = field(
        default=None,
        metadata={
            "name": "InstrPrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    clr_chanl: Optional[ClearingChannel2Code] = field(
        default=None,
        metadata={
            "name": "ClrChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    svc_lvl: list[ServiceLevel8ChoiceCamt11000101] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    seq_tp: Optional[SequenceType3Code] = field(
        default=None,
        metadata={
            "name": "SeqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class ProxyAccountIdentification1Camt11000101(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class ReferredDocumentType3ChoiceCamt11000101(ISO20022MessageElement):
    cd: Optional[DocumentType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Camt11000101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class TaxAmountAndType1Camt11000101(ISO20022MessageElement):
    tp: Optional[TaxAmountType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class TaxParty2Camt11000101(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    authstn: Optional[TaxAuthorisation1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class TaxPeriod3Camt11000101(ISO20022MessageElement):
    yr: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Yr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    tp: Optional[TaxRecordPeriod1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    fr_to_dt: Optional[DatePeriod2Camt11000101] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt11000101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class AmountType4ChoiceCamt11000101(ISO20022MessageElement):
    instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    eqvt_amt: Optional[EquivalentAmount2Camt11000101] = field(
        default=None,
        metadata={
            "name": "EqvtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class CreditorReferenceType2Camt11000101(ISO20022MessageElement):
    cd_or_prtry: Optional[CreditorReferenceType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineIdentification1Camt11000101(ISO20022MessageElement):
    tp: Optional[DocumentLineType1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class FileData1Camt11000101(ISO20022MessageElement):
    tp: Optional[DocumentType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[DateAndDateTime2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    frmt: Optional[DocumentFormat1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    file_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ntwk_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtwkRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    file_lctn_elctrnc_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileLctnElctrncAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class Frequency36ChoiceCamt11000101(ISO20022MessageElement):
    tp: Optional[Frequency6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prd: Optional[FrequencyPeriod1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    pt_in_tm: Optional[FrequencyAndMoment1Camt11000101] = field(
        default=None,
        metadata={
            "name": "PtInTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class MandateTypeInformation2Camt11000101(ISO20022MessageElement):
    svc_lvl: Optional[ServiceLevel8ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    lcl_instrm: Optional[LocalInstrument2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ctgy_purp: Optional[CategoryPurpose1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "CtgyPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    clssfctn: Optional[MandateClassification1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Clssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class OrganisationIdentification29Camt11000101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class PersonIdentification13Camt11000101(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Camt11000101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class PostalAddress24Camt11000101(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ReferredDocumentType4Camt11000101(ISO20022MessageElement):
    cd_or_prtry: Optional[ReferredDocumentType3ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RemittanceAmount2Camt11000101(ISO20022MessageElement):
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    tax_amt: list[TaxAmountAndType1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class RemittanceAmount3Camt11000101(ISO20022MessageElement):
    due_pybl_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dscnt_apld_amt: list[DiscountAmountAndType1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "DscntApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdt_note_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "CdtNoteAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    tax_amt: list[TaxAmountAndType1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    adjstmnt_amt_and_rsn: list[DocumentAdjustment1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "AdjstmntAmtAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class TaxRecordDetails3Camt11000101(ISO20022MessageElement):
    prd: Optional[TaxPeriod3Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class BranchData3Camt11000101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Camt11000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class CashAccount40Camt11000101(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    tp: Optional[CashAccountType2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class CreditTransferMandateData1Camt11000101(ISO20022MessageElement):
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[MandateTypeInformation2Camt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dt_of_vrfctn: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtOfVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    elctrnc_sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ElctrncSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    fnl_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    frqcy: Optional[Frequency36ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rsn: Optional[MandateSetupReason1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class CreditorReferenceInformation2Camt11000101(ISO20022MessageElement):
    tp: Optional[CreditorReferenceType2Camt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentLineInformation1Camt11000101(ISO20022MessageElement):
    id: list[DocumentLineIdentification1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_occurs": 1,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    amt: Optional[RemittanceAmount3Camt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class FinancialInstitutionIdentification18Camt11000101(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt11000101] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Camt11000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class NameAndAddress16Camt11000101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    adr: Optional[PostalAddress24Camt11000101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class Party38ChoiceCamt11000101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification29Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification13Camt11000101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class TaxAmount3Camt11000101(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "TaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ttl_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dtls: list[TaxRecordDetails3Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification6Camt11000101(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification18Camt11000101] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData3Camt11000101] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class CompensationRequest1Camt11000101(ISO20022MessageElement):
    compstn_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "CompstnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    prd: Optional[DatePeriod2Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    xpctd_val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class DebitAuthorisation3Camt11000101(ISO20022MessageElement):
    cxl_rsn: Optional[CancellationReason33ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    amt_to_dbt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "AmtToDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    val_dt_to_dbt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDtToDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    addtl_cxl_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlCxlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class InvestigationLocationData1Camt11000101(ISO20022MessageElement):
    mtd: Optional[InvestigationLocationMethod1Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    elctrnc_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    pstl_adr: Optional[NameAndAddress16Camt11000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class PartyIdentification135Camt11000101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress24Camt11000101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    id: Optional[Party38ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact4Camt11000101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class ReferredDocumentInformation7Camt11000101(ISO20022MessageElement):
    tp: Optional[ReferredDocumentType4Camt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RltdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    line_dtls: list[DocumentLineInformation1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "LineDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class TaxRecord3Camt11000101(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctgy_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtgyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dbtr_sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frms_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prd: Optional[TaxPeriod3Camt11000101] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    tax_amt: Optional[TaxAmount3Camt11000101] = field(
        default=None,
        metadata={
            "name": "TaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class UnderlyingStatementEntry5Camt11000101(ISO20022MessageElement):
    orgnl_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_grp_inf: Optional[OriginalGroupInformation29Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlGrpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlStmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_ntry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlNtryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlUETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    orgnl_ntry_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlNtryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_ntry_val_dt: Optional[DateAndDateTime2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlNtryValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class AdditionalRequestData1ChoiceCamt11000101(ISO20022MessageElement):
    reqd_dbt_authstn: Optional[DebitAuthorisation3Camt11000101] = field(
        default=None,
        metadata={
            "name": "ReqdDbtAuthstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    reqd_compstn: Optional[CompensationRequest1Camt11000101] = field(
        default=None,
        metadata={
            "name": "ReqdCompstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    reqd_valtn: Optional[AdjustmentRequest1Camt11000101] = field(
        default=None,
        metadata={
            "name": "ReqdValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    req_nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class AmendmentInformationDetails14Camt11000101(ISO20022MessageElement):
    orgnl_mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlMndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cdtr_schme_id: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrSchmeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_cdtr_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Camt11000101
    ] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_cdtr_agt_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlCdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_dbtr: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_dbtr_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_dbtr_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Camt11000101
    ] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_dbtr_agt_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_fnl_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrgnlFnlColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_frqcy: Optional[Frequency36ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_rsn: Optional[MandateSetupReason1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_trckg_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlTrckgDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class Garnishment3Camt11000101(ISO20022MessageElement):
    tp: Optional[GarnishmentType1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    grnshee: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "Grnshee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    grnshmt_admstr: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "GrnshmtAdmstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rmtd_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "RmtdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    fmly_mdcl_insrnc_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FmlyMdclInsrncInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    mplyee_termntn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MplyeeTermntnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class InvestigationActionReason1Camt11000101(ISO20022MessageElement):
    orgtr: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rsn: Optional[InvestigationActionReason1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class Party40ChoiceCamt11000101(ISO20022MessageElement):
    pty: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification6Camt11000101] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class PartyAndSignature3Camt11000101(ISO20022MessageElement):
    pty: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    sgntr: Optional[SkipPayloadCamt11000101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )


@dataclass
class RelatedInvestigationData1Camt11000101(ISO20022MessageElement):
    invstgtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvstgtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn: list[InvestigationLocationData1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class SettlementInstruction11Camt11000101(ISO20022MessageElement):
    sttlm_mtd: Optional[SettlementMethod1Code] = field(
        default=None,
        metadata={
            "name": "SttlmMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    sttlm_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "SttlmAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    clr_sys: Optional[ClearingSystemIdentification3ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "ClrSys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    instg_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Camt11000101
    ] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    instg_rmbrsmnt_agt_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    instd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Camt11000101
    ] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    instd_rmbrsmnt_agt_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    thrd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification6Camt11000101
    ] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    thrd_rmbrsmnt_agt_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "ThrdRmbrsmntAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class TaxData1Camt11000101(ISO20022MessageElement):
    cdtr: Optional[TaxParty1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dbtr: Optional[TaxParty2Camt11000101] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ultmt_dbtr: Optional[TaxParty2Camt11000101] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    admstn_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdmstnZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_taxbl_base_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "TtlTaxblBaseAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ttl_tax_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "TtlTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcrd: list[TaxRecord3Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class Document12Camt11000101(ISO20022MessageElement):
    tp: Optional[DocumentType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[DateAndDateTime2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    lang_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LangCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    frmt: Optional[DocumentFormat1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    file_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature3Camt11000101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    nclsr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Nclsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 10485760,
            "format": "base64",
        },
    )


@dataclass
class InvestigationRequestAction1Camt11000101(ISO20022MessageElement):
    actn: Optional[InvestigationRequestAction1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Actn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    actn_rsn: Optional[InvestigationActionReason1Camt11000101] = field(
        default=None,
        metadata={
            "name": "ActnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class MandateRelatedInformation15Camt11000101(ISO20022MessageElement):
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_sgntr: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    amdmnt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AmdmntInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    amdmnt_inf_dtls: Optional[AmendmentInformationDetails14Camt11000101] = field(
        default=None,
        metadata={
            "name": "AmdmntInfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    elctrnc_sgntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 1025,
        },
    )
    frst_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    fnl_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FnlColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    frqcy: Optional[Frequency36ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rsn: Optional[MandateSetupReason1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    trckg_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrckgDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[0-9]{2}",
        },
    )


@dataclass
class StructuredRemittanceInformation17Camt11000101(ISO20022MessageElement):
    rfrd_doc_inf: list[ReferredDocumentInformation7Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "RfrdDocInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rfrd_doc_amt: Optional[RemittanceAmount2Camt11000101] = field(
        default=None,
        metadata={
            "name": "RfrdDocAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdtr_ref_inf: Optional[CreditorReferenceInformation2Camt11000101] = field(
        default=None,
        metadata={
            "name": "CdtrRefInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    invcr: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "Invcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    invcee: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "Invcee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    tax_rmt: Optional[TaxData1Camt11000101] = field(
        default=None,
        metadata={
            "name": "TaxRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    grnshmt_rmt: Optional[Garnishment3Camt11000101] = field(
        default=None,
        metadata={
            "name": "GrnshmtRmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    addtl_rmt_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class InvestigationReason2Camt11000101(ISO20022MessageElement):
    seq: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Seq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    rsn: Optional[InvestigationReason1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    rsn_sub_tp: Optional[InvestigationReasonSubType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "RsnSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    addtl_req_data: Optional[AdditionalRequestData1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "AddtlReqData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rltd_invstgtn_data: Optional[RelatedInvestigationData1Camt11000101] = field(
        default=None,
        metadata={
            "name": "RltdInvstgtnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    nclsd_file: list[Document12Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "NclsdFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rltd_file_data: list[FileData1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "RltdFileData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class MandateRelatedData2ChoiceCamt11000101(ISO20022MessageElement):
    drct_dbt_mndt: Optional[MandateRelatedInformation15Camt11000101] = field(
        default=None,
        metadata={
            "name": "DrctDbtMndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdt_trf_mndt: Optional[CreditTransferMandateData1Camt11000101] = field(
        default=None,
        metadata={
            "name": "CdtTrfMndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class RemittanceInformation21Camt11000101(ISO20022MessageElement):
    ustrd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: list[StructuredRemittanceInformation17Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class OriginalTransactionReference35Camt11000101(ISO20022MessageElement):
    intr_bk_sttlm_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    amt: Optional[AmountType4ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    reqd_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdtr_schme_id: Optional[PartyIdentification135Camt11000101] = field(
        default=None,
        metadata={
            "name": "CdtrSchmeId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    sttlm_inf: Optional[SettlementInstruction11Camt11000101] = field(
        default=None,
        metadata={
            "name": "SttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    pmt_tp_inf: Optional[PaymentTypeInformation27Camt11000101] = field(
        default=None,
        metadata={
            "name": "PmtTpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    pmt_mtd: Optional[PaymentMethod4Code] = field(
        default=None,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    mndt_rltd_inf: Optional[MandateRelatedData2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "MndtRltdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    rmt_inf: Optional[RemittanceInformation21Camt11000101] = field(
        default=None,
        metadata={
            "name": "RmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ultmt_dbtr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dbtr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dbtr_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Camt11000101] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification6Camt11000101] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdtr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    cdtr_acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    ultmt_cdtr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    purp: Optional[Purpose2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Purp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class UnderlyingPaymentInstruction8Camt11000101(ISO20022MessageElement):
    orgnl_grp_inf: Optional[UnderlyingGroupInformation1Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlGrpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_pmt_inf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlPmtInfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlEndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlUETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    orgnl_instd_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlInstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    reqd_colltn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdColltnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_tx_ref: Optional[OriginalTransactionReference35Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_svc_lvl: Optional[ServiceLevel8ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlSvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class UnderlyingPaymentTransaction7Camt11000101(ISO20022MessageElement):
    orgnl_grp_inf: Optional[UnderlyingGroupInformation1Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlGrpInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlEndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlUETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    orgnl_intr_bk_sttlm_amt: Optional[ActiveOrHistoricCurrencyAndAmountCamt11000101] = (
        field(
            default=None,
            metadata={
                "name": "OrgnlIntrBkSttlmAmt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            },
        )
    )
    orgnl_intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrgnlIntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_tx_ref: Optional[OriginalTransactionReference35Camt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    orgnl_svc_lvl: Optional[ServiceLevel8ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "OrgnlSvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class UnderlyingData2ChoiceCamt11000101(ISO20022MessageElement):
    initn: Optional[UnderlyingPaymentInstruction8Camt11000101] = field(
        default=None,
        metadata={
            "name": "Initn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    intr_bk: Optional[UnderlyingPaymentTransaction7Camt11000101] = field(
        default=None,
        metadata={
            "name": "IntrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    stmt_ntry: Optional[UnderlyingStatementEntry5Camt11000101] = field(
        default=None,
        metadata={
            "name": "StmtNtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    acct: Optional[CashAccount40Camt11000101] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    othr: Optional[GenericIdentification1Camt11000101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class InvestigationRequest2Camt11000101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rqstr_invstgtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RqstrInvstgtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspndr_invstgtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspndrInvstgtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    eir: Optional[str] = field(
        default=None,
        metadata={
            "name": "EIR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    req_actn: Optional[InvestigationRequestAction1Camt11000101] = field(
        default=None,
        metadata={
            "name": "ReqActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    invstgtn_tp: Optional[InvestigationType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "InvstgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    invstgtn_sub_tp: Optional[InvestigationSubType1ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "InvstgtnSubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    undrlyg_instrm: Optional[UnderlyingInvestigationInstrument1ChoiceCamt11000101] = (
        field(
            default=None,
            metadata={
                "name": "UndrlygInstrm",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            },
        )
    )
    undrlyg: Optional[UnderlyingData2ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Undrlyg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    rqstr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Rqstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    rspndr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "Rspndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    req_orgtr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "ReqOrgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    xpctd_rspndr: Optional[Party40ChoiceCamt11000101] = field(
        default=None,
        metadata={
            "name": "XpctdRspndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )
    svc_lvl: list[InvestigationServiceLevel1ChoiceCamt11000101] = field(
        default_factory=list,
        metadata={
            "name": "SvcLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class InvestigationRequestV01Camt11000101(ISO20022MessageElement):
    invstgtn_req: Optional[InvestigationRequest2Camt11000101] = field(
        default=None,
        metadata={
            "name": "InvstgtnReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "required": True,
        },
    )
    invstgtn_data: list[InvestigationReason2Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "InvstgtnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Camt11000101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01",
        },
    )


@dataclass
class Camt11000101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01"

    invstgtn_req: Optional[InvestigationRequestV01Camt11000101] = field(
        default=None,
        metadata={
            "name": "InvstgtnReq",
            "type": "Element",
            "required": True,
        },
    )
