from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04"


@dataclass
class ActiveCurrencyAndAmountAuth02500104(ISO20022MessageElement):
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
class BinaryFile1Auth02500104(ISO20022MessageElement):
    mimetp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMETp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ncodg_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    incl_binry_objct: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InclBinryObjct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceAuth02500104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Auth02500104(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DocumentAmendment1Auth02500104(ISO20022MessageElement):
    crrctn_id: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrrctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgnl_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification22Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class DocumentIdentification28Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification35Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceAuth02500104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceAuth02500104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Auth02500104(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAuth02500104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ShipmentCondition1ChoiceAuth02500104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignatureEnvelopeReferenceAuth02500104(ISO20022MessageElement):
    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth02500104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceAuth02500104(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Auth02500104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Auth02500104(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Auth02500104(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class ContractRegistrationReference2ChoiceAuth02500104(ISO20022MessageElement):
    regd_ctrct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegdCtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctrct: Optional[DocumentIdentification35Auth02500104] = field(
        default=None,
        metadata={
            "name": "Ctrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class DocumentEntryAmendment1Auth02500104(ISO20022MessageElement):
    crrctg_ntry_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrrctgNtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgnl_doc: Optional[DocumentIdentification28Auth02500104] = field(
        default=None,
        metadata={
            "name": "OrgnlDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )


@dataclass
class DocumentGeneralInformation5Auth02500104(ISO20022MessageElement):
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    doc_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    sndr_rcvr_seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SndrRcvrSeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lk_file_hash: Optional[SignatureEnvelopeReferenceAuth02500104] = field(
        default=None,
        metadata={
            "name": "LkFileHash",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    attchd_binry_file: Optional[BinaryFile1Auth02500104] = field(
        default=None,
        metadata={
            "name": "AttchdBinryFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )


@dataclass
class GenericFinancialIdentification1Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ShipmentAttribute2Auth02500104(ISO20022MessageElement):
    conds: Optional[ShipmentCondition1ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "Conds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    xpctd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    ctry_of_cntr_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfCntrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Auth02500104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth02500104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentification39Auth02500104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class PersonIdentification18Auth02500104(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Auth02500104] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    othr: list[GenericPersonIdentification2Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class PostalAddress27Auth02500104(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupportingDocumentEntry2Auth02500104(ISO20022MessageElement):
    ntry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_doc: Optional[DocumentIdentification22Auth02500104] = field(
        default=None,
        metadata={
            "name": "OrgnlDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{1}[a-zA-Z0-9_]{3}",
        },
    )
    ttl_amt: Optional[ActiveCurrencyAndAmountAuth02500104] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    ttl_amt_aftr_shipmnt: Optional[ActiveCurrencyAndAmountAuth02500104] = field(
        default=None,
        metadata={
            "name": "TtlAmtAftrShipmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    ttl_amt_in_ctrct_ccy: Optional[ActiveCurrencyAndAmountAuth02500104] = field(
        default=None,
        metadata={
            "name": "TtlAmtInCtrctCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    ttl_amt_aftr_shipmnt_in_ctrct_ccy: Optional[ActiveCurrencyAndAmountAuth02500104] = (
        field(
            default=None,
            metadata={
                "name": "TtlAmtAftrShipmntInCtrctCcy",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            },
        )
    )
    shipmnt_attrbts: Optional[ShipmentAttribute2Auth02500104] = field(
        default=None,
        metadata={
            "name": "ShipmntAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    ntry_amdmnt_id: Optional[DocumentEntryAmendment1Auth02500104] = field(
        default=None,
        metadata={
            "name": "NtryAmdmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    mtrty_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtrtyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )
    attchmnt: list[DocumentGeneralInformation5Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "Attchmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class BranchData5Auth02500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Auth02500104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Auth02500104(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Auth02500104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Auth02500104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    othr: Optional[GenericFinancialIdentification1Auth02500104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class Party52ChoiceAuth02500104(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Auth02500104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    prvt_id: Optional[PersonIdentification18Auth02500104] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Auth02500104(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Auth02500104] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Auth02500104] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class PartyIdentification272Auth02500104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Auth02500104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    id: Optional[Party52ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Auth02500104] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class Party50ChoiceAuth02500104(ISO20022MessageElement):
    pty: Optional[PartyIdentification272Auth02500104] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification8Auth02500104] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class SupportingDocument4Auth02500104(ISO20022MessageElement):
    spprtg_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpprtgDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert: Optional[DocumentIdentification28Auth02500104] = field(
        default=None,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification272Auth02500104] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    acct_svcr: Optional[BranchAndFinancialInstitutionIdentification8Auth02500104] = (
        field(
            default=None,
            metadata={
                "name": "AcctSvcr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
                "required": True,
            },
        )
    )
    amdmnt: Optional[DocumentAmendment1Auth02500104] = field(
        default=None,
        metadata={
            "name": "Amdmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )
    ctrct_ref: Optional[ContractRegistrationReference2ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "CtrctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    ntry: list[SupportingDocumentEntry2Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "Ntry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class CurrencyControlHeader9Auth02500104(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    nb_of_itms: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfItms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    initg_pty: Optional[Party50ChoiceAuth02500104] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    fwdg_agt: Optional[BranchAndFinancialInstitutionIdentification8Auth02500104] = (
        field(
            default=None,
            metadata={
                "name": "FwdgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            },
        )
    )


@dataclass
class CurrencyControlSupportingDocumentDeliveryV04Auth02500104(ISO20022MessageElement):
    grp_hdr: Optional[CurrencyControlHeader9Auth02500104] = field(
        default=None,
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "required": True,
        },
    )
    spprtg_doc: list[SupportingDocument4Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "SpprtgDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth02500104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04",
        },
    )


@dataclass
class Auth02500104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.025.001.04"

    ccy_ctrl_spprtg_doc_dlvry: Optional[
        CurrencyControlSupportingDocumentDeliveryV04Auth02500104
    ] = field(
        default=None,
        metadata={
            "name": "CcyCtrlSpprtgDocDlvry",
            "type": "Element",
            "required": True,
        },
    )
