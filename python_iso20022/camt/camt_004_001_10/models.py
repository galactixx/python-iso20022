from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.camt_004_001_10.enums import (
    BalanceStatus1Code,
    ProcessingType1Code,
    SystemBalanceType2Code,
)
from python_iso20022.camt.enums import Frequency2Code, StandingOrderType1Code
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10"


@dataclass
class AccountSchemeName1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountCamt00400110(ISO20022MessageElement):
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
class BalanceType11ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountType2ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceCamt00400110(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Camt00400110(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod3Camt00400110(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class ErrorHandling3ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EventType1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt00400110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt00400110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessQuery1Camt00400110(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class OtherContact1Camt00400110(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt00400110(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Camt00400110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class Amount2ChoiceCamt00400110(ISO20022MessageElement):
    amt_wtht_ccy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtWthtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amt_wth_ccy: Optional[ActiveCurrencyAndAmountCamt00400110] = field(
        default=None,
        metadata={
            "name": "AmtWthCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class BalanceType9ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[SystemBalanceType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt00400110(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Camt00400110(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class ErrorHandling5Camt00400110(ISO20022MessageElement):
    err: Optional[ErrorHandling3ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ExecutionType1ChoiceCamt00400110(ISO20022MessageElement):
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    evt: Optional[EventType1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Evt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class GenericAccountIdentification1Camt00400110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt00400110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Camt00400110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Camt00400110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProcessingType1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[ProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountIdentification1Camt00400110(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class RequestType4ChoiceCamt00400110(ISO20022MessageElement):
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class StandingOrderType1ChoiceCamt00400110(ISO20022MessageElement):
    cd: Optional[StandingOrderType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    prtry: Optional[GenericIdentification1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class SupplementaryData1Camt00400110(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )


@dataclass
class TotalAmountAndCurrency1Camt00400110(ISO20022MessageElement):
    ttl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt00400110(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class BalanceRestrictionType1Camt00400110(ISO20022MessageElement):
    tp: Optional[GenericIdentification1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    prcg_tp: Optional[ProcessingType1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "PrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class CashBalance11Camt00400110(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    tp: Optional[BalanceType9ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    sts: Optional[BalanceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    nb_of_pmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfPmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Limit5Camt00400110(ISO20022MessageElement):
    amt: Optional[Amount2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )


@dataclass
class MessageHeader7Camt00400110(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    orgnl_biz_qry: Optional[OriginalBusinessQuery1Camt00400110] = field(
        default=None,
        metadata={
            "name": "OrgnlBizQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentification39Camt00400110(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class PersonIdentification18Camt00400110(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Camt00400110] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    othr: list[GenericPersonIdentification2Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class PostalAddress27Camt00400110(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class StandingOrderTotalAmount1Camt00400110(ISO20022MessageElement):
    set_prdfnd_ordr: Optional[TotalAmountAndCurrency1Camt00400110] = field(
        default=None,
        metadata={
            "name": "SetPrdfndOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    pdg_prdfnd_ordr: Optional[TotalAmountAndCurrency1Camt00400110] = field(
        default=None,
        metadata={
            "name": "PdgPrdfndOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    set_stg_ordr: Optional[TotalAmountAndCurrency1Camt00400110] = field(
        default=None,
        metadata={
            "name": "SetStgOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    pdg_stg_ordr: Optional[TotalAmountAndCurrency1Camt00400110] = field(
        default=None,
        metadata={
            "name": "PdgStgOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )


@dataclass
class BranchData5Camt00400110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00400110] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class CashAccount40Camt00400110(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    tp: Optional[CashAccountType2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class CashBalance13Camt00400110(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    tp: Optional[BalanceType11ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    sts: Optional[BalanceStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    nb_of_pmts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfPmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rstrctn_tp: Optional[BalanceRestrictionType1Camt00400110] = field(
        default=None,
        metadata={
            "name": "RstrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Camt00400110(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt00400110] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00400110] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class Party52ChoiceCamt00400110(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Camt00400110] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    prvt_id: Optional[PersonIdentification18Camt00400110] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Camt00400110(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Camt00400110] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Camt00400110] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class PartyIdentification272Camt00400110(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00400110] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    id: Optional[Party52ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Camt00400110] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class BilateralLimit4Camt00400110(ISO20022MessageElement):
    ctr_pty_id: Optional[BranchAndFinancialInstitutionIdentification8Camt00400110] = (
        field(
            default=None,
            metadata={
                "name": "CtrPtyId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
                "required": True,
            },
        )
    )
    lmt_amt: Optional[Amount2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "LmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    bil_bal: list[CashBalance11Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "BilBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class StandingOrder11Camt00400110(ISO20022MessageElement):
    amt: Optional[Amount2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    tp: Optional[StandingOrderType1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    assoctd_pool_acct: Optional[AccountIdentification4ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "AssoctdPoolAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frqcy: Optional[Frequency2Code] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    vldty_prd: Optional[DatePeriod3Camt00400110] = field(
        default=None,
        metadata={
            "name": "VldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    sys_mmb: Optional[BranchAndFinancialInstitutionIdentification8Camt00400110] = field(
        default=None,
        metadata={
            "name": "SysMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    rspnsbl_pty: Optional[BranchAndFinancialInstitutionIdentification8Camt00400110] = (
        field(
            default=None,
            metadata={
                "name": "RspnsblPty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            },
        )
    )
    lk_set_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lk_set_ordr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkSetOrdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lk_set_ordr_seq: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LkSetOrdrSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    exctn_tp: Optional[ExecutionType1ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "ExctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    cdtr: Optional[BranchAndFinancialInstitutionIdentification8Camt00400110] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    cdtr_acct: Optional[CashAccount40Camt00400110] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    dbtr: Optional[BranchAndFinancialInstitutionIdentification8Camt00400110] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    dbtr_acct: Optional[CashAccount40Camt00400110] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    ttls_per_stg_ordr: Optional[StandingOrderTotalAmount1Camt00400110] = field(
        default=None,
        metadata={
            "name": "TtlsPerStgOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    zero_sweep_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZeroSweepInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class CashAccountData1Camt00400110(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    tp: Optional[CashAccountType2ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    prxy: Optional[ProxyAccountIdentification1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    cur_mul_lmt: Optional[Limit5Camt00400110] = field(
        default=None,
        metadata={
            "name": "CurMulLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    ownr: Optional[PartyIdentification272Camt00400110] = field(
        default=None,
        metadata={
            "name": "Ownr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    svcr: Optional[BranchAndFinancialInstitutionIdentification8Camt00400110] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    mul_bal: list[CashBalance13Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "MulBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    cur_bil_lmt: list[BilateralLimit4Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "CurBilLmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    stg_ordr: list[StandingOrder11Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "StgOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class AccountOrBusinessError6ChoiceCamt00400110(ISO20022MessageElement):
    acct: Optional[CashAccountData1Camt00400110] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    biz_err: list[ErrorHandling5Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "BizErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class AccountReport35Camt00400110(ISO20022MessageElement):
    acct_id: Optional[AccountIdentification4ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    acct_or_err: Optional[AccountOrBusinessError6ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "AcctOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )


@dataclass
class AccountOrOperationalError6ChoiceCamt00400110(ISO20022MessageElement):
    acct_rpt: list[AccountReport35Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "AcctRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )
    oprl_err: list[ErrorHandling5Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "OprlErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class ReturnAccountV10Camt00400110(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader7Camt00400110] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    rpt_or_err: Optional[AccountOrOperationalError6ChoiceCamt00400110] = field(
        default=None,
        metadata={
            "name": "RptOrErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt00400110] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10",
        },
    )


@dataclass
class Camt00400110(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10"

    rtr_acct: Optional[ReturnAccountV10Camt00400110] = field(
        default=None,
        metadata={
            "name": "RtrAcct",
            "type": "Element",
            "required": True,
        },
    )
