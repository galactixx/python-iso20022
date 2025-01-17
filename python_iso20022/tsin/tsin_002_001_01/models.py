from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    CashAccountType4Code,
    FinancingStatusReason1Code,
    RequestStatus1Code,
    TechnicalValidationStatus1Code,
)
from python_iso20022.tsin.tsin_002_001_01.enums import CancellationStatus4Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01"


@dataclass
class ActiveCurrencyAndAmountTsin00200101:
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
class ClearingSystemMemberIdentification2ChoiceTsin00200101:
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    inifsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "INIFSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"IN[a-zA-Z0-9]{11,11}",
        },
    )
    grhebic: Optional[str] = field(
        default=None,
        metadata={
            "name": "GRHEBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"GR[0-9]{7,7}",
        },
    )
    plknr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PLKNR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"PL[0-9]{8,8}",
        },
    )
    othr_clr_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClrCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirthTsin00200101:
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancingDateDetails1Tsin00200101:
    book_dt: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "BookDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    cdt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CdtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    dbt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DbtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class GenericIdentification3Tsin00200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Tsin00200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Tsin00200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformation2Tsin00200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class AccountIdentification3ChoiceTsin00200101:
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Tsin00200101] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class CashAccountType2Tsin00200101:
    cd: Optional[CashAccountType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstitutionIdentification6Tsin00200101:
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2ChoiceTsin00200101] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            },
        )
    )
    prtry_id: Optional[GenericIdentification4Tsin00200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class FinancingRateOrAmountChoiceTsin00200101:
    amt: Optional[ActiveCurrencyAndAmountTsin00200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class OrganisationIdentification2Tsin00200101:
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    ibei: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[A-Z]{2,2}[B-DF-HJ-NP-TV-XZ0-9]{7,7}[0-9]{1,1}",
        },
    )
    bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    eangln: Optional[str] = field(
        default=None,
        metadata={
            "name": "EANGLN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[0-9]{13,13}",
        },
    )
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    duns: Optional[str] = field(
        default=None,
        metadata={
            "name": "DUNS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[0-9]{9,9}",
        },
    )
    bk_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BkPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry_id: Optional[GenericIdentification3Tsin00200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class OriginalInvoiceInformation1Tsin00200101:
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_invc_amt: Optional[ActiveCurrencyAndAmountTsin00200101] = field(
        default=None,
        metadata={
            "name": "TtlInvcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification25Tsin00200101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsin00200101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class PersonIdentification3Tsin00200101:
    drvrs_lic_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvrsLicNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scl_scty_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SclSctyNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    aln_regn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlnRegnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pspt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PsptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    idnty_card_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdntyCardNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mplyr_id_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MplyrIdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirthTsin00200101] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    othr_id: Optional[GenericIdentification4Tsin00200101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress1Tsin00200101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class StatusReason4ChoiceTsin00200101:
    cd: Optional[FinancingStatusReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CancellationStatusInformation1Tsin00200101:
    sts: Optional[CancellationStatus4Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsin00200101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class CashAccount7Tsin00200101:
    id: Optional[AccountIdentification3ChoiceTsin00200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2Tsin00200101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class FinancingResult1Tsin00200101:
    fincg_req_sts: Optional[RequestStatus1Code] = field(
        default=None,
        metadata={
            "name": "FincgReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsin00200101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )
    fincd_amt: Optional[FinancingRateOrAmountChoiceTsin00200101] = field(
        default=None,
        metadata={
            "name": "FincdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class Party2ChoiceTsin00200101:
    org_id: Optional[OrganisationIdentification2Tsin00200101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    prvt_id: list[PersonIdentification3Tsin00200101] = field(
        default_factory=list,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "max_occurs": 4,
        },
    )


@dataclass
class ValidationStatusInformation1Tsin00200101:
    sts: Optional[TechnicalValidationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    sts_rsn: Optional[StatusReason4ChoiceTsin00200101] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    addtl_sts_rsn_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlStsRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class FinancingAllowedSummary1Tsin00200101:
    fincd_itm_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FincdItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttl_accptd_itms_amt: Optional[ActiveCurrencyAndAmountTsin00200101] = field(
        default=None,
        metadata={
            "name": "TtlAccptdItmsAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    apld_pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ttl_fincd_amt: Optional[ActiveCurrencyAndAmountTsin00200101] = field(
        default=None,
        metadata={
            "name": "TtlFincdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    fincg_dt_dtls: Optional[FinancingDateDetails1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "FincgDtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    cdt_acct: Optional[CashAccount7Tsin00200101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    fincg_acct: Optional[CashAccount7Tsin00200101] = field(
        default=None,
        metadata={
            "name": "FincgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class InstalmentFinancingInformation1Tsin00200101:
    instlmt_seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstlmtSeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    instlmt_ttl_amt: Optional[ActiveCurrencyAndAmountTsin00200101] = field(
        default=None,
        metadata={
            "name": "InstlmtTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    instlmt_fincg_rslt: Optional[FinancingResult1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "InstlmtFincgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification8Tsin00200101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pstl_adr: Optional[PostalAddress1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    id: Optional[Party2ChoiceTsin00200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentificationAndAccount6Tsin00200101:
    pty_id: Optional[PartyIdentification25Tsin00200101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    cdt_acct: Optional[CashAccount7Tsin00200101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    fincg_acct: Optional[CashAccount7Tsin00200101] = field(
        default=None,
        metadata={
            "name": "FincgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class InvoiceFinancingDetails1Tsin00200101:
    orgnl_invc_inf: Optional[OriginalInvoiceInformation1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "OrgnlInvcInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    spplr: Optional[PartyIdentification8Tsin00200101] = field(
        default=None,
        metadata={
            "name": "Spplr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    invc_fincg_rslt: Optional[FinancingResult1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "InvcFincgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    instlmt_fincg_inf: list[InstalmentFinancingInformation1Tsin00200101] = field(
        default_factory=list,
        metadata={
            "name": "InstlmtFincgInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class OriginalRequestInformation1Tsin00200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    fincg_rqstr: Optional[PartyIdentificationAndAccount6Tsin00200101] = field(
        default=None,
        metadata={
            "name": "FincgRqstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    intrmy_agt: Optional[FinancialInstitutionIdentification6Tsin00200101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    frst_agt: Optional[FinancialInstitutionIdentification6Tsin00200101] = field(
        default=None,
        metadata={
            "name": "FrstAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )
    vldtn_sts_inf: Optional[ValidationStatusInformation1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "VldtnStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    cxl_sts_inf: Optional[CancellationStatusInformation1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "CxlStsInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class FinancingInformationAndStatus1Tsin00200101:
    fincg_allwd_summry: Optional[FinancingAllowedSummary1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "FincgAllwdSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    invc_fincg_dtls: list[InvoiceFinancingDetails1Tsin00200101] = field(
        default_factory=list,
        metadata={
            "name": "InvcFincgDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class InvoiceFinancingRequestStatusV01Tsin00200101:
    sts_id: Optional[MessageIdentification1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "StsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    orgnl_req_inf_and_sts: Optional[OriginalRequestInformation1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "OrgnlReqInfAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
            "required": True,
        },
    )
    fincg_inf_and_sts: Optional[FinancingInformationAndStatus1Tsin00200101] = field(
        default=None,
        metadata={
            "name": "FincgInfAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01",
        },
    )


@dataclass
class Tsin00200101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01"

    invc_fincg_req_sts: Optional[InvoiceFinancingRequestStatusV01Tsin00200101] = field(
        default=None,
        metadata={
            "name": "InvcFincgReqSts",
            "type": "Element",
            "required": True,
        },
    )
