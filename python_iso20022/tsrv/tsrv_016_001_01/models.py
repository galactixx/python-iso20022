from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, NamePrefix1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01"


@dataclass
class ActiveCurrencyAndAmountTsrv01600101(ISO20022MessageElement):
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
class DateAndPlaceOfBirthTsrv01600101(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Discrepancy1Tsrv01600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nrrtv: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceTsrv01600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceTsrv01600101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryData3Tsrv01600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )


@dataclass
class ContactDetails2Tsrv01600101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Demand2Tsrv01600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountTsrv01600101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class GenericOrganisationIdentification1Tsrv01600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceTsrv01600101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Tsrv01600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceTsrv01600101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress6Tsrv01600101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class OrganisationIdentification8Tsrv01600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Tsrv01600101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )


@dataclass
class PersonIdentification5Tsrv01600101(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsrv01600101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Tsrv01600101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )


@dataclass
class Party11ChoiceTsrv01600101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification8Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )


@dataclass
class PartyIdentification43Tsrv01600101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    id: Optional[Party11ChoiceTsrv01600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )


@dataclass
class PartyAndSignature2Tsrv01600101(ISO20022MessageElement):
    pty: Optional[PartyIdentification43Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )
    sgntr: Optional[ProprietaryData3Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )


@dataclass
class Undertaking9Tsrv01600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[PartyIdentification43Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )
    applcnt_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplcntRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DemandRefusal1Tsrv01600101(ISO20022MessageElement):
    udrtkg_id: Optional[Undertaking9Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "UdrtkgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )
    advsg_pty_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdvsgPtyRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scnd_advsg_pty_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndAdvsgPtyRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cnfrmr_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnfrmrRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dmnd_dtls: Optional[Demand2Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "DmndDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
        },
    )
    sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "required": True,
            "length": 7,
            "pattern": r"REFUSED",
        },
    )
    dscrpncy: list[Discrepancy1Tsrv01600101] = field(
        default_factory=list,
        metadata={
            "name": "Dscrpncy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    dspstn_of_docs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DspstnOfDocs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2000,
        },
    )


@dataclass
class DemandRefusalNotificationV01Tsrv01600101(ISO20022MessageElement):
    dmnd_rfsl_ntfctn_dtls: list[DemandRefusal1Tsrv01600101] = field(
        default_factory=list,
        metadata={
            "name": "DmndRfslNtfctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )
    dgtl_sgntr: Optional[PartyAndSignature2Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01",
        },
    )


@dataclass
class Tsrv01600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsrv.016.001.01"

    dmnd_rfsl_ntfctn: Optional[DemandRefusalNotificationV01Tsrv01600101] = field(
        default=None,
        metadata={
            "name": "DmndRfslNtfctn",
            "type": "Element",
            "required": True,
        },
    )
