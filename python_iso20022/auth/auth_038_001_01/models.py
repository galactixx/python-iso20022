from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.auth.auth_038_001_01.enums import (
    TaxReportingStatus1Code,
    TaxReportingStatus2Code,
)
from python_iso20022.enums import AddressType2Code, NamePrefix1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01"


@dataclass
class MessageIdentification1Auth03800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth03800101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ValidationRuleSchemeName1ChoiceAuth03800101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactDetails2Auth03800101:
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    othr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericValidationRuleIdentification1Auth03800101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    schme_nm: Optional[ValidationRuleSchemeName1ChoiceAuth03800101] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress6Auth03800101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Auth03800101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth03800101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
        },
    )


@dataclass
class InvoiceTaxReportTransactionStatus1Auth03800101:
    tax_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sts: Optional[TaxReportingStatus2Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
        },
    )
    vldtn_rule: list[GenericValidationRuleIdentification1Auth03800101] = field(
        default_factory=list,
        metadata={
            "name": "VldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth03800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )


@dataclass
class TaxOrganisationIdentification1Auth03800101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress6Auth03800101] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )
    ctct_dtls: Optional[ContactDetails2Auth03800101] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )


@dataclass
class InvoiceTaxStatusReportHeader1Auth03800101:
    tax_authrty: Optional[TaxOrganisationIdentification1Auth03800101] = field(
        default=None,
        metadata={
            "name": "TaxAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )
    msg_id: Optional[MessageIdentification1Auth03800101] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
        },
    )
    orgnl_msg_id: Optional[MessageIdentification1Auth03800101] = field(
        default=None,
        metadata={
            "name": "OrgnlMsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
        },
    )
    rpt_sts: Optional[TaxReportingStatus1Code] = field(
        default=None,
        metadata={
            "name": "RptSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
        },
    )
    vldtn_rule: list[GenericValidationRuleIdentification1Auth03800101] = field(
        default_factory=list,
        metadata={
            "name": "VldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )


@dataclass
class InvoiceTaxReportStatusAdviceV01Auth03800101:
    sts_rpt_hdr: Optional[InvoiceTaxStatusReportHeader1Auth03800101] = field(
        default=None,
        metadata={
            "name": "StsRptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
            "required": True,
        },
    )
    tx_sts: list[InvoiceTaxReportTransactionStatus1Auth03800101] = field(
        default_factory=list,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth03800101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01",
        },
    )


@dataclass
class Auth03800101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01"

    invc_tax_rpt_sts_advc: Optional[InvoiceTaxReportStatusAdviceV01Auth03800101] = (
        field(
            default=None,
            metadata={
                "name": "InvcTaxRptStsAdvc",
                "type": "Element",
                "required": True,
            },
        )
    )
