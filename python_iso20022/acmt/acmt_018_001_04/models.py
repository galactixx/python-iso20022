from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.acmt.enums import CommunicationMethod3Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    Modification1Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04"


@dataclass
class AccountContract2Acmt01800104(ISO20022MessageElement):
    trgt_go_live_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TrgtGoLiveDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    trgt_clsg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TrgtClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    urgcy_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UrgcyFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class AccountSchemeName1ChoiceAcmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountAcmt01800104(ISO20022MessageElement):
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
class BankTransactionCodeStructure6Acmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceAcmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContractDocument1Acmt01800104(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 6,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Acmt01800104(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceAcmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Acmt01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Acmt01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceAcmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Acmt01800104(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAcmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryBankTransactionCodeStructure1Acmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SkipPayloadAcmt01800104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Acmt01800104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceAcmt01800104(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class BankTransactionCodeStructure5Acmt01800104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    fmly: Optional[BankTransactionCodeStructure6Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Fmly",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )


@dataclass
class Channel2ChoiceAcmt01800104(ISO20022MessageElement):
    cd: Optional[CommunicationMethod3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Acmt01800104(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Acmt01800104(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class FixedAmountOrUnlimited1ChoiceAcmt01800104(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountAcmt01800104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    not_ltd: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotLtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "length": 9,
            "pattern": r"UNLIMITED",
        },
    )


@dataclass
class GenericAccountIdentification1Acmt01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Acmt01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Acmt01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Acmt01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MaximumAmountByPeriod1Acmt01800104(ISO20022MessageElement):
    max_amt: Optional[ActiveCurrencyAndAmountAcmt01800104] = field(
        default=None,
        metadata={
            "name": "MaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    nb_of_days: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )


@dataclass
class References4Acmt01800104(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    prc_id: Optional[MessageIdentification1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "PrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    attchd_doc_nm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AttchdDocNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Acmt01800104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceAcmt01800104(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class Authorisation2Acmt01800104(ISO20022MessageElement):
    max_amt_by_tx: Optional[FixedAmountOrUnlimited1ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "MaxAmtByTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    max_amt_by_prd: list[MaximumAmountByPeriod1Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "MaxAmtByPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    max_amt_by_blk_submissn: Optional[FixedAmountOrUnlimited1ChoiceAcmt01800104] = (
        field(
            default=None,
            metadata={
                "name": "MaxAmtByBlkSubmissn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            },
        )
    )


@dataclass
class BankTransactionCodeStructure4Acmt01800104(ISO20022MessageElement):
    domn: Optional[BankTransactionCodeStructure5Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Domn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    prtry: Optional[ProprietaryBankTransactionCodeStructure1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class OrganisationIdentification39Acmt01800104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class PersonIdentification18Acmt01800104(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    othr: list[GenericPersonIdentification2Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class PostalAddress27Acmt01800104(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class AccountForAction1Acmt01800104(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class BranchData5Acmt01800104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt01800104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Acmt01800104(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Acmt01800104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt01800104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    othr: Optional[GenericFinancialIdentification1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class Party52ChoiceAcmt01800104(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Acmt01800104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    prvt_id: Optional[PersonIdentification18Acmt01800104] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Acmt01800104(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Acmt01800104] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Acmt01800104] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class PartyIdentification272Acmt01800104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Acmt01800104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    id: Optional[Party52ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Acmt01800104] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class PartyAndCertificate6Acmt01800104(ISO20022MessageElement):
    pty: Optional[PartyIdentification272Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    cert: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )


@dataclass
class PartyAndCertificate7Acmt01800104(ISO20022MessageElement):
    mod_cd: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "ModCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    pty: Optional[PartyIdentification272Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    cert: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )


@dataclass
class PartyAndSignature4Acmt01800104(ISO20022MessageElement):
    pty: Optional[PartyIdentification272Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    sgntr: Optional[SkipPayloadAcmt01800104] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )


@dataclass
class Group5Acmt01800104(ISO20022MessageElement):
    mod_cd: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "ModCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    pty: list[PartyAndCertificate7Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class PartyOrGroup3ChoiceAcmt01800104(ISO20022MessageElement):
    grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "GrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    pty: Optional[PartyAndCertificate6Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class PartyAndAuthorisation6Acmt01800104(ISO20022MessageElement):
    mod_cd: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "ModCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    pty_or_grp: Optional[PartyOrGroup3ChoiceAcmt01800104] = field(
        default=None,
        metadata={
            "name": "PtyOrGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    sgntr_ordr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SgntrOrdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "pattern": r"[\+]{0,1}[0-9]{1,15}",
        },
    )
    authstn: Optional[Authorisation2Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Authstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )


@dataclass
class OperationMandate6Acmt01800104(ISO20022MessageElement):
    mod_cd: Optional[Modification1Code] = field(
        default=None,
        metadata={
            "name": "ModCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    aplbl_chanl: list[Channel2ChoiceAcmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "AplblChanl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_occurs": 1,
        },
    )
    reqrd_sgntr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqrdSgntrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
            "pattern": r"[\+]{0,1}[0-9]{1,15}",
        },
    )
    sgntr_ordr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SgntrOrdrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    mndt_hldr: list[PartyAndAuthorisation6Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "MndtHldr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    bk_opr: list[BankTransactionCodeStructure4Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "BkOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_occurs": 1,
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    end_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class AccountMandateMaintenanceAmendmentRequestV04Acmt01800104(ISO20022MessageElement):
    refs: Optional[References4Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    fr: Optional[OrganisationIdentification39Acmt01800104] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    ctrct_dts: Optional[AccountContract2Acmt01800104] = field(
        default=None,
        metadata={
            "name": "CtrctDts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    undrlyg_mstr_agrmt: Optional[ContractDocument1Acmt01800104] = field(
        default=None,
        metadata={
            "name": "UndrlygMstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    acct_id: list[AccountForAction1Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "min_occurs": 1,
        },
    )
    acct_svcr_id: Optional[BranchAndFinancialInstitutionIdentification8Acmt01800104] = (
        field(
            default=None,
            metadata={
                "name": "AcctSvcrId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
                "required": True,
            },
        )
    )
    org_id: Optional[OrganisationIdentification39Acmt01800104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
            "required": True,
        },
    )
    mndt: list[OperationMandate6Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "Mndt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    grp: list[Group5Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "Grp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    dgtl_sgntr: list[PartyAndSignature4Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Acmt01800104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04",
        },
    )


@dataclass
class Acmt01800104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04"

    acct_mndt_mntnc_amdmnt_req: Optional[
        AccountMandateMaintenanceAmendmentRequestV04Acmt01800104
    ] = field(
        default=None,
        metadata={
            "name": "AcctMndtMntncAmdmntReq",
            "type": "Element",
            "required": True,
        },
    )
