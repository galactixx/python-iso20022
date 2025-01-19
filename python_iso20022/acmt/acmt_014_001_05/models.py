from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.acmt.enums import (
    AccountStatus3Code,
    CommunicationMethod2Code,
    CommunicationMethod3Code,
    Frequency7Code,
    UseCases1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05"


@dataclass
class AccountContract3Acmt01400105(ISO20022MessageElement):
    trgt_go_live_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TrgtGoLiveDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    trgt_clsg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TrgtClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    go_live_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "GoLiveDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    clsg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    urgcy_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UrgcyFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    rmvl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RmvlInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class AccountSchemeName1ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountAcmt01400105(ISO20022MessageElement):
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
class BankTransactionCodeStructure6Acmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    sub_fmly_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubFmlyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class CashAccountType2ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CommunicationFormat1ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContractDocument1Acmt01400105(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sgn_off_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SgnOffDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 6,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Acmt01400105(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Acmt01400105(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryBankTransactionCodeStructure1Acmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SkipPayloadAcmt01400105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Acmt01400105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class BankTransactionCodeStructure5Acmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    fmly: Optional[BankTransactionCodeStructure6Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Fmly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class Channel2ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[CommunicationMethod3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Acmt01400105(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CodeOrProprietary1ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification13Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class CommunicationMethod2ChoiceAcmt01400105(ISO20022MessageElement):
    cd: Optional[CommunicationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Acmt01400105(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class FixedAmountOrUnlimited1ChoiceAcmt01400105(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    not_ltd: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotLtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "length": 9,
            "pattern": r"UNLIMITED",
        },
    )


@dataclass
class GenericAccountIdentification1Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MaximumAmountByPeriod1Acmt01400105(ISO20022MessageElement):
    max_amt: Optional[ActiveCurrencyAndAmountAcmt01400105] = field(
        default=None,
        metadata={
            "name": "MaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    nb_of_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )


@dataclass
class ProxyAccountIdentification1Acmt01400105(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class References5Acmt01400105(ISO20022MessageElement):
    req_tp: Optional[UseCases1Code] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    msg_id: Optional[MessageIdentification1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    prc_id: Optional[MessageIdentification1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "PrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    ackd_msg_id: list[MessageIdentification1Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "AckdMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    attchd_doc_nm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AttchdDocNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Acmt01400105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceAcmt01400105(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class Authorisation2Acmt01400105(ISO20022MessageElement):
    max_amt_by_tx: Optional[FixedAmountOrUnlimited1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "MaxAmtByTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    max_amt_by_prd: list[MaximumAmountByPeriod1Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "MaxAmtByPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    max_amt_by_blk_submissn: Optional[FixedAmountOrUnlimited1ChoiceAcmt01400105] = (
        field(
            default=None,
            metadata={
                "name": "MaxAmtByBlkSubmissn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            },
        )
    )


@dataclass
class BankTransactionCodeStructure4Acmt01400105(ISO20022MessageElement):
    domn: Optional[BankTransactionCodeStructure5Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Domn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    prtry: Optional[ProprietaryBankTransactionCodeStructure1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class OrganisationIdentification39Acmt01400105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class PersonIdentification18Acmt01400105(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    othr: list[GenericPersonIdentification2Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class PostalAddress27Acmt01400105(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Restriction1Acmt01400105(ISO20022MessageElement):
    rstrctn_tp: Optional[CodeOrProprietary1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "RstrctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    vld_fr: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    vld_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VldUntil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class StatementFrequencyAndForm1Acmt01400105(ISO20022MessageElement):
    frqcy: Optional[Frequency7Code] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    com_mtd: Optional[CommunicationMethod2ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "ComMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    dlvry_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlvryAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    frmt: Optional[CommunicationFormat1ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Frmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class AccountForAction1Acmt01400105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class BranchData5Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class CashAccount40Acmt01400105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    tp: Optional[CashAccountType2ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class CustomerAccount5Acmt01400105(ISO20022MessageElement):
    id: list[AccountIdentification4ChoiceAcmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_occurs": 1,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sts: Optional[AccountStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    tp: Optional[CashAccountType2ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    mnthly_pmt_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MnthlyPmtVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    mnthly_rcvd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MnthlyRcvdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    mnthly_tx_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MnthlyTxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[0-9]{1,5}",
        },
    )
    avrg_bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AvrgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    acct_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr_ntfctn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FlrNtfctnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    clng_ntfctn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ClngNtfctnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    stmt_frqcy_and_frmt: list[StatementFrequencyAndForm1Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "StmtFrqcyAndFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    clsg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    rstrctn: list[Restriction1Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Rstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Acmt01400105(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Acmt01400105] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    othr: Optional[GenericFinancialIdentification1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class Party52ChoiceAcmt01400105(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Acmt01400105] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    prvt_id: Optional[PersonIdentification18Acmt01400105] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class PartyIdentification274Acmt01400105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    id: Optional[PersonIdentification18Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Acmt01400105] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Acmt01400105(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Acmt01400105] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Acmt01400105] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class Organisation42Acmt01400105(ISO20022MessageElement):
    full_lgl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullLglNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    tradg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    ctry_of_opr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    oprl_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "OprlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    biz_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "BizAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    lgl_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "LglAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    bllg_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "BllgAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    org_id: Optional[OrganisationIdentification39Acmt01400105] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    rprtv_offcr: list[PartyIdentification274Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "RprtvOffcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    trsr_mgr: Optional[PartyIdentification274Acmt01400105] = field(
        default=None,
        metadata={
            "name": "TrsrMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    main_mndt_hldr: list[PartyIdentification274Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "MainMndtHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    sndr: list[PartyIdentification274Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    lgl_rprtv: list[PartyIdentification274Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "LglRprtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class PartyIdentification272Acmt01400105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt01400105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    id: Optional[Party52ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Acmt01400105] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class PartyAndCertificate6Acmt01400105(ISO20022MessageElement):
    pty: Optional[PartyIdentification272Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    cert: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )


@dataclass
class PartyAndSignature4Acmt01400105(ISO20022MessageElement):
    pty: Optional[PartyIdentification272Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    sgntr: Optional[SkipPayloadAcmt01400105] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class Group6Acmt01400105(ISO20022MessageElement):
    grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    pty: list[PartyAndCertificate6Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_occurs": 1,
        },
    )


@dataclass
class PartyOrGroup3ChoiceAcmt01400105(ISO20022MessageElement):
    grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    pty: Optional[PartyAndCertificate6Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class PartyAndAuthorisation7Acmt01400105(ISO20022MessageElement):
    pty_or_grp: Optional[PartyOrGroup3ChoiceAcmt01400105] = field(
        default=None,
        metadata={
            "name": "PtyOrGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    sgntr_ordr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SgntrOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "pattern": r"[\+]{0,1}[0-9]{1,15}",
        },
    )
    authstn: Optional[Authorisation2Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class OperationMandate7Acmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    aplbl_chanl: list[Channel2ChoiceAcmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "AplblChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_occurs": 1,
        },
    )
    reqrd_sgntr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqrdSgntrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
            "pattern": r"[\+]{0,1}[0-9]{1,15}",
        },
    )
    sgntr_ordr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SgntrOrdrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    mndt_hldr: list[PartyAndAuthorisation7Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "MndtHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    bk_opr: list[BankTransactionCodeStructure4Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "BkOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "min_occurs": 1,
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class AccountReport36Acmt01400105(ISO20022MessageElement):
    acct: Optional[CustomerAccount5Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    undrlyg_mstr_agrmt: Optional[ContractDocument1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "UndrlygMstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    ctrct_dts: Optional[AccountContract3Acmt01400105] = field(
        default=None,
        metadata={
            "name": "CtrctDts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    mndt: list[OperationMandate7Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Mndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    grp: list[Group6Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Grp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    ref_acct: Optional[CashAccount40Acmt01400105] = field(
        default=None,
        metadata={
            "name": "RefAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    bal_trf_acct: Optional[AccountForAction1Acmt01400105] = field(
        default=None,
        metadata={
            "name": "BalTrfAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    trf_acct_svcr_id: Optional[
        BranchAndFinancialInstitutionIdentification8Acmt01400105
    ] = field(
        default=None,
        metadata={
            "name": "TrfAcctSvcrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class AccountReportV05Acmt01400105(ISO20022MessageElement):
    refs: Optional[References5Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    fr: Optional[OrganisationIdentification39Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    acct_svcr_id: Optional[BranchAndFinancialInstitutionIdentification8Acmt01400105] = (
        field(
            default=None,
            metadata={
                "name": "AcctSvcrId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
                "required": True,
            },
        )
    )
    org: Optional[Organisation42Acmt01400105] = field(
        default=None,
        metadata={
            "name": "Org",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
            "required": True,
        },
    )
    rpt: list[AccountReport36Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    dgtl_sgntr: list[PartyAndSignature4Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )
    splmtry_data: list[SupplementaryData1Acmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05",
        },
    )


@dataclass
class Acmt01400105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05"

    acct_rpt: Optional[AccountReportV05Acmt01400105] = field(
        default=None,
        metadata={
            "name": "AcctRpt",
            "type": "Element",
            "required": True,
        },
    )
