from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_114_001_01.enums import (
    LanguageVersion1Code,
    TransactionOperationType13Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01"


@dataclass
class ClassificationType4Auth11400101(ISO20022MessageElement):
    lgl_frmwk: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LglFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 6,
        },
    )
    inf_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
            "length": 6,
        },
    )


@dataclass
class GenericIdentification175Auth11400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 72,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification185Auth11400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 100,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification190Auth11400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IndustrySector3ChoiceAuth11400101(ISO20022MessageElement):
    rgltry_txnmy_sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RgltryTxnmySctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    nacetxnmy_sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "NACETxnmySctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[A-V]{1,1}",
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceAuth11400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyName5Auth11400101(ISO20022MessageElement):
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[a-z]{2,2}",
        },
    )
    intrnl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Intrnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )


@dataclass
class Period2Auth11400101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth11400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Document26Auth11400101(ISO20022MessageElement):
    lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[a-z]{2,2}",
        },
    )
    orgnl_or_trnsltd: Optional[LanguageVersion1Code] = field(
        default=None,
        metadata={
            "name": "OrgnlOrTrnsltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )
    elctrnc_seal_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElctrncSealRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class GenericOrganisationIdentification3Auth11400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceAuth11400101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NaturalPersonIdentification5Auth11400101(ISO20022MessageElement):
    prsn_nm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PrsnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )
    npi: Optional[str] = field(
        default=None,
        metadata={
            "name": "NPI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    altrn_id: Optional[GenericIdentification175Auth11400101] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    ntty_sz: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttySz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    sctr: list[IndustrySector3ChoiceAuth11400101] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class Period4ChoiceAuth11400101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth11400101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth11400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth11400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "required": True,
        },
    )


@dataclass
class UniqueProductIdentifier2ChoiceAuth11400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: Optional[GenericIdentification185Auth11400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )


@dataclass
class OrganisationIdentification49Auth11400101(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    org_nm: list[PartyName5Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "OrgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    altrn_org_id: list[GenericOrganisationIdentification3Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "AltrnOrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    regd_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegdCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ntty_sz: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttySz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    sctr: list[IndustrySector3ChoiceAuth11400101] = field(
        default_factory=list,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    prsn_nm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PrsnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 500,
        },
    )
    npi: Optional[str] = field(
        default=None,
        metadata={
            "name": "NPI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class SecurityIdentification49Auth11400101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    unq_pdct_idr: Optional[UniqueProductIdentifier2ChoiceAuth11400101] = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    altrntv_instrm_id: Optional[GenericIdentification175Auth11400101] = field(
        default=None,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    pdct_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class PartyIdentification260ChoiceAuth11400101(ISO20022MessageElement):
    lgl_prsn: Optional[OrganisationIdentification49Auth11400101] = field(
        default=None,
        metadata={
            "name": "LglPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    ntrl_prsn: Optional[NaturalPersonIdentification5Auth11400101] = field(
        default=None,
        metadata={
            "name": "NtrlPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )


@dataclass
class Document28Auth11400101(ISO20022MessageElement):
    tech_rcrd_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    submissn_tp: Optional[TransactionOperationType13Code] = field(
        default=None,
        metadata={
            "name": "SubmissnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rltd_ntty: list[PartyIdentification260ChoiceAuth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rgltry_data_tp: list[ClassificationType4Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RgltryDataTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    vlntry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Vlntry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    hstrcl_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HstrclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rltd_prd: Optional[Period4ChoiceAuth11400101] = field(
        default=None,
        metadata={
            "name": "RltdPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    prsnl_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrsnlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    pblctn_prd: Optional[Period4ChoiceAuth11400101] = field(
        default=None,
        metadata={
            "name": "PblctnPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    home_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HomeCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    hst_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "HstCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rltd_pdct_idr: list[SecurityIdentification49Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    doc_ref: list[Document26Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "DocRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rltd_rgltry_data: list[GenericIdentification190Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdRgltryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    data_rcrd: Optional[SupplementaryDataEnvelope1Auth11400101] = field(
        default=None,
        metadata={
            "name": "DataRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )


@dataclass
class MetadataReport5Auth11400101(ISO20022MessageElement):
    submitg_ntty: Optional[PartyIdentification260ChoiceAuth11400101] = field(
        default=None,
        metadata={
            "name": "SubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    colltn_body: Optional[GenericIdentification175Auth11400101] = field(
        default=None,
        metadata={
            "name": "ColltnBody",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rltd_ntty: list[PartyIdentification260ChoiceAuth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rltd_pdct_idr: list[SecurityIdentification49Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RltdPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rgltry_data_tp: list[ClassificationType4Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RgltryDataTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )
    rgltry_data: list[Document28Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "RgltryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class RegulatoryMetadataReportV01Auth11400101(ISO20022MessageElement):
    metadata_rpt: list[MetadataReport5Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "MetadataRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth11400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01",
        },
    )


@dataclass
class Auth11400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.114.001.01"

    rgltry_metadata_rpt: Optional[RegulatoryMetadataReportV01Auth11400101] = field(
        default=None,
        metadata={
            "name": "RgltryMetadataRpt",
            "type": "Element",
            "required": True,
        },
    )
