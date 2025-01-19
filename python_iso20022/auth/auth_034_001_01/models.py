from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    DocumentType3Code,
    ExchangeRateType1Code,
    InformationType1Code,
    NamePrefix1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01"


@dataclass
class BinaryFile1Auth03400101(ISO20022MessageElement):
    mimetp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMETp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ncodg_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    incl_binry_objct: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InclBinryObjct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class CurrencyAndAmountAuth03400101(ISO20022MessageElement):
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
class DateAndPlaceOfBirthAuth03400101(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class LegalOrganisation1Auth03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class MessageIdentification1Auth03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceAuth03400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Period2Auth03400101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAuth03400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth03400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TaxParty1Auth03400101(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactDetails2Auth03400101(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CreditorReferenceType1ChoiceAuth03400101(ISO20022MessageElement):
    cd: Optional[DocumentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentGeneralInformation2Auth03400101(ISO20022MessageElement):
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sndr_rcvr_seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SndrRcvrSeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 256,
        },
    )
    attchd_binry_file: list[BinaryFile1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "AttchdBinryFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class EarlyPaymentsVat1Auth03400101(ISO20022MessageElement):
    class Meta:
        name = "EarlyPaymentsVAT1"

    tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DscntTaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    dscnt_tax_amt: Optional[CurrencyAndAmountAuth03400101] = field(
        default=None,
        metadata={
            "name": "DscntTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )


@dataclass
class ExchangeRateInformation1Auth03400101(ISO20022MessageElement):
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rate_tp: Optional[ExchangeRateType1Code] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    ctrct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification1Auth03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceAuth03400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification1Auth03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAuth03400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InformationType1ChoiceAuth03400101(ISO20022MessageElement):
    cd: Optional[InformationType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PostalAddress6Auth03400101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Auth03400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth03400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )


@dataclass
class AdditionalInformation1Auth03400101(ISO20022MessageElement):
    inf_tp: Optional[InformationType1ChoiceAuth03400101] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    inf_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class CreditorReferenceType2Auth03400101(ISO20022MessageElement):
    cd_or_prtry: Optional[CreditorReferenceType1ChoiceAuth03400101] = field(
        default=None,
        metadata={
            "name": "CdOrPrtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyReference3Auth03400101(ISO20022MessageElement):
    trgt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrgtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    src_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrcCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate_inf: list[ExchangeRateInformation1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "XchgRateInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class EarlyPayment1Auth03400101(ISO20022MessageElement):
    early_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlyPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    dscnt_pct: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DscntPct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_amt: Optional[CurrencyAndAmountAuth03400101] = field(
        default=None,
        metadata={
            "name": "DscntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    early_pmt_tax_spcfctn: list[EarlyPaymentsVat1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "EarlyPmtTaxSpcfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    early_pmt_tax_ttl: Optional[CurrencyAndAmountAuth03400101] = field(
        default=None,
        metadata={
            "name": "EarlyPmtTaxTtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    due_pybl_amt_wth_early_pmt: Optional[CurrencyAndAmountAuth03400101] = field(
        default=None,
        metadata={
            "name": "DuePyblAmtWthEarlyPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class OrganisationIdentification8Auth03400101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    othr: list[GenericOrganisationIdentification1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class PersonIdentification5Auth03400101(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthAuth03400101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    othr: list[GenericPersonIdentification1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class TaxOrganisationIdentification1Auth03400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Auth03400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    ctct_dtls: Optional[ContactDetails2Auth03400101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class CreditorReferenceInformation2Auth03400101(ISO20022MessageElement):
    tp: Optional[CreditorReferenceType2Auth03400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentification28Auth03400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Auth03400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    id: Optional[OrganisationIdentification8Auth03400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Auth03400101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )


@dataclass
class Party11ChoiceAuth03400101(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification8Auth03400101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    prvt_id: Optional[PersonIdentification5Auth03400101] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class SettlementSubTotalCalculatedTax2Auth03400101(ISO20022MessageElement):
    tp_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TpCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    clctd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ClctdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_amt: list[CurrencyAndAmountAuth03400101] = field(
        default_factory=list,
        metadata={
            "name": "BsisAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    clctd_amt: list[CurrencyAndAmountAuth03400101] = field(
        default_factory=list,
        metadata={
            "name": "ClctdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    xmptn_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmptnRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    xmptn_rsn_txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmptnRsnTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )
    tax_ccy_xchg: Optional[CurrencyReference3Auth03400101] = field(
        default=None,
        metadata={
            "name": "TaxCcyXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class TaxReportHeader1Auth03400101(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Auth03400101] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    nb_of_tax_rpts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfTaxRpts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tax_authrty: list[TaxOrganisationIdentification1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "TaxAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class PartyIdentification116Auth03400101(ISO20022MessageElement):
    pty_id: Optional[OrganisationIdentification28Auth03400101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    lgl_org: Optional[LegalOrganisation1Auth03400101] = field(
        default=None,
        metadata={
            "name": "LglOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    tax_pty: Optional[TaxParty1Auth03400101] = field(
        default=None,
        metadata={
            "name": "TaxPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class PartyIdentification43Auth03400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Auth03400101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    id: Optional[Party11ChoiceAuth03400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[ContactDetails2Auth03400101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class TradeSettlement2Auth03400101(ISO20022MessageElement):
    pmt_ref: Optional[CreditorReferenceInformation2Auth03400101] = field(
        default=None,
        metadata={
            "name": "PmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    due_pybl_amt: Optional[CurrencyAndAmountAuth03400101] = field(
        default=None,
        metadata={
            "name": "DuePyblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    invc_ccy_xchg: Optional[CurrencyReference3Auth03400101] = field(
        default=None,
        metadata={
            "name": "InvcCcyXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    dlvry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DlvryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    bllg_prd: Optional[Period2Auth03400101] = field(
        default=None,
        metadata={
            "name": "BllgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    tax_ttl_amt: Optional[CurrencyAndAmountAuth03400101] = field(
        default=None,
        metadata={
            "name": "TaxTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    xmptn_rsn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmptnRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    xmptn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )
    sub_ttl_clctd_tax: list[SettlementSubTotalCalculatedTax2Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "SubTtlClctdTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    early_pmts: list[EarlyPayment1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "EarlyPmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class GroupHeader69Auth03400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    rpt_ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    tax_rpt_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRptPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    orgnl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sellr_tax_rprtv: Optional[PartyIdentification116Auth03400101] = field(
        default=None,
        metadata={
            "name": "SellrTaxRprtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    buyr_tax_rprtv: Optional[PartyIdentification116Auth03400101] = field(
        default=None,
        metadata={
            "name": "BuyrTaxRprtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    lang_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "LangCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class PartyIdentification72Auth03400101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification43Auth03400101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    lgl_org: Optional[LegalOrganisation1Auth03400101] = field(
        default=None,
        metadata={
            "name": "LglOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    tax_pty: Optional[TaxParty1Auth03400101] = field(
        default=None,
        metadata={
            "name": "TaxPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class TaxReport1Auth03400101(ISO20022MessageElement):
    tax_rpt_hdr: Optional[GroupHeader69Auth03400101] = field(
        default=None,
        metadata={
            "name": "TaxRptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification72Auth03400101] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    buyr: Optional[PartyIdentification72Auth03400101] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    trad_sttlm: Optional[TradeSettlement2Auth03400101] = field(
        default=None,
        metadata={
            "name": "TradSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    othr_pty: list[PartyIdentification72Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "OthrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    addtl_inf: list[AdditionalInformation1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    addtl_ref: list[DocumentGeneralInformation2Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "AddtlRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class InvoiceTaxReportV01Auth03400101(ISO20022MessageElement):
    invc_tax_rpt_hdr: Optional[TaxReportHeader1Auth03400101] = field(
        default=None,
        metadata={
            "name": "InvcTaxRptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "required": True,
        },
    )
    tax_rpt: list[TaxReport1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "TaxRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth03400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01",
        },
    )


@dataclass
class Auth03400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01"

    invc_tax_rpt: Optional[InvoiceTaxReportV01Auth03400101] = field(
        default=None,
        metadata={
            "name": "InvcTaxRpt",
            "type": "Element",
            "required": True,
        },
    )
