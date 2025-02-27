from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03"


@dataclass
class AccountSchemeName1ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountCamt10600103(ISO20022MessageElement):
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
class CashAccountType2ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTime2ChoiceCamt10600103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Camt10600103(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification3Camt10600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt10600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstructionForInstructedAgent1Camt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    instr_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Camt10600103(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryReference1Camt10600103(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt10600103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Camt10600103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class ChargeType3ChoiceCamt10600103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification3Camt10600103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt10600103(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Camt10600103(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class GenericAccountIdentification1Camt10600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt10600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Camt10600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Camt10600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountIdentification1Camt10600103(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class SupplementaryData1Camt10600103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt10600103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )


@dataclass
class TotalCharges7Camt10600103(ISO20022MessageElement):
    nb_of_chrgs_rcrds: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfChrgsRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_chrgs_amt: Optional[ActiveCurrencyAndAmountCamt10600103] = field(
        default=None,
        metadata={
            "name": "TtlChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class TotalCharges8Camt10600103(ISO20022MessageElement):
    nb_of_chrgs_brkdwn_itms: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfChrgsBrkdwnItms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ctrl_sum: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CtrlSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_chrgs_amt: Optional[ActiveCurrencyAndAmountCamt10600103] = field(
        default=None,
        metadata={
            "name": "TtlChrgsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class TransactionReferences7Camt10600103(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_inf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtInfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mndt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MndtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clr_sys_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClrSysRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: list[ProprietaryReference1Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt10600103(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt10600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class ChargesBreakdown1Camt10600103(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountCamt10600103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    tp: Optional[ChargeType3ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class OrganisationIdentification39Camt10600103(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class PersonIdentification18Camt10600103(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Camt10600103] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    othr: list[GenericPersonIdentification2Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class PostalAddress27Camt10600103(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BranchData5Camt10600103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt10600103] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class CashAccount40Camt10600103(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    tp: Optional[CashAccountType2ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Camt10600103] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Camt10600103(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt10600103] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt10600103] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt10600103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class Party52ChoiceCamt10600103(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Camt10600103] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    prvt_id: Optional[PersonIdentification18Camt10600103] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Camt10600103(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Camt10600103] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Camt10600103] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class PartyIdentification272Camt10600103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt10600103] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    id: Optional[Party52ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Camt10600103] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class SettlementInstruction19Camt10600103(ISO20022MessageElement):
    reqd_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
                "required": True,
            },
        )
    )
    cdtr_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "CdtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    cdtr: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    cdtr_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class ChargesPerTransactionRecord6Camt10600103(ISO20022MessageElement):
    rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrgs_rqstr: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "ChrgsRqstr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            },
        )
    )
    sttlm_instr: Optional[SettlementInstruction19Camt10600103] = field(
        default=None,
        metadata={
            "name": "SttlmInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    undrlyg_tx: Optional[TransactionReferences7Camt10600103] = field(
        default=None,
        metadata={
            "name": "UndrlygTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    ttl_chrgs_per_rcrd: Optional[TotalCharges8Camt10600103] = field(
        default=None,
        metadata={
            "name": "TtlChrgsPerRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_brkdwn: list[ChargesBreakdown1Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "ChrgsBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_occurs": 1,
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr: Optional[PartyIdentification272Camt10600103] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt10600103
    ] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    instr_for_instd_agt: Optional[InstructionForInstructedAgent1Camt10600103] = field(
        default=None,
        metadata={
            "name": "InstrForInstdAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ChargesPerTypeRecord6Camt10600103(ISO20022MessageElement):
    rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrgs_rqstr: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "ChrgsRqstr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            },
        )
    )
    sttlm_instr: Optional[SettlementInstruction19Camt10600103] = field(
        default=None,
        metadata={
            "name": "SttlmInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    undrlyg_tx: Optional[TransactionReferences7Camt10600103] = field(
        default=None,
        metadata={
            "name": "UndrlygTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountCamt10600103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr: Optional[PartyIdentification272Camt10600103] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt10600103
    ] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    instr_for_instd_agt: Optional[InstructionForInstructedAgent1Camt10600103] = field(
        default=None,
        metadata={
            "name": "InstrForInstdAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ChargesRecord12Camt10600103(ISO20022MessageElement):
    chrgs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChrgsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrgs_rqstr: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "ChrgsRqstr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            },
        )
    )
    sttlm_instr: Optional[SettlementInstruction19Camt10600103] = field(
        default=None,
        metadata={
            "name": "SttlmInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    undrlyg_tx: Optional[TransactionReferences7Camt10600103] = field(
        default=None,
        metadata={
            "name": "UndrlygTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountCamt10600103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    val_dt: Optional[DateAndDateTime2ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr: Optional[PartyIdentification272Camt10600103] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "DbtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            },
        )
    )
    dbtr_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "DbtrAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt10600103
    ] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    tp: Optional[ChargeType3ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    instr_for_instd_agt: Optional[InstructionForInstructedAgent1Camt10600103] = field(
        default=None,
        metadata={
            "name": "InstrForInstdAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GroupHeader130Camt10600103(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    chrgs_rqstr: Optional[BranchAndFinancialInstitutionIdentification8Camt10600103] = (
        field(
            default=None,
            metadata={
                "name": "ChrgsRqstr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            },
        )
    )
    sttlm_instr: Optional[SettlementInstruction19Camt10600103] = field(
        default=None,
        metadata={
            "name": "SttlmInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    ttl_chrgs: Optional[TotalCharges7Camt10600103] = field(
        default=None,
        metadata={
            "name": "TtlChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt10600103
    ] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class ChargesPerTransaction6Camt10600103(ISO20022MessageElement):
    chrgs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChrgsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_chrgs_per_tx: Optional[TotalCharges7Camt10600103] = field(
        default=None,
        metadata={
            "name": "TtlChrgsPerTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt10600103
    ] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    rcrd: list[ChargesPerTransactionRecord6Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ChargesPerType6Camt10600103(ISO20022MessageElement):
    chrgs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChrgsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_chrgs_per_chrg_tp: Optional[TotalCharges7Camt10600103] = field(
        default=None,
        metadata={
            "name": "TtlChrgsPerChrgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt10600103
    ] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    chrgs_acct_agt_acct: Optional[CashAccount40Camt10600103] = field(
        default=None,
        metadata={
            "name": "ChrgsAcctAgtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    tp: Optional[ChargeType3ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    rcrd: list[ChargesPerTypeRecord6Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "Rcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_occurs": 1,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Charges6ChoiceCamt10600103(ISO20022MessageElement):
    sngl: Optional[ChargesRecord12Camt10600103] = field(
        default=None,
        metadata={
            "name": "Sngl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    per_tx: Optional[ChargesPerTransaction6Camt10600103] = field(
        default=None,
        metadata={
            "name": "PerTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )
    per_tp: list[ChargesPerType6Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "PerTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class ChargesPaymentRequestV03Camt10600103(ISO20022MessageElement):
    grp_hdr: Optional[GroupHeader130Camt10600103] = field(
        default=None,
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    chrgs: Optional[Charges6ChoiceCamt10600103] = field(
        default=None,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Camt10600103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03",
        },
    )


@dataclass
class Camt10600103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03"

    chrgs_pmt_req: Optional[ChargesPaymentRequestV03Camt10600103] = field(
        default=None,
        metadata={
            "name": "ChrgsPmtReq",
            "type": "Element",
            "required": True,
        },
    )
