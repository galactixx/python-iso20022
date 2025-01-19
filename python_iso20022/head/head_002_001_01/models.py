from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:head.002.001.01"


@dataclass
class LaxPayloadHead00200101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ManifestData2Head00200101(ISO20022MessageElement):
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nb_of_docs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDocs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class PayloadData2Head00200101(ISO20022MessageElement):
    pyld_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PyldIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
        },
    )
    pssbl_dplct_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PssblDplctFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
        },
    )


@dataclass
class SignatureEnvelopeHead00200101(ISO20022MessageElement):
    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class ApplicationSpecifics1Head00200101(ISO20022MessageElement):
    sys_usr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysUsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    sgntr: Optional[SignatureEnvelopeHead00200101] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
        },
    )
    ttl_nb_of_docs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfDocs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class PayloadDescription2Head00200101(ISO20022MessageElement):
    pyld_data: Optional[PayloadData2Head00200101] = field(
        default=None,
        metadata={
            "name": "PyldData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
        },
    )
    appl_spcfcs: Optional[ApplicationSpecifics1Head00200101] = field(
        default=None,
        metadata={
            "name": "ApplSpcfcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
        },
    )
    pyld_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PyldTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    mnfst_data: list[ManifestData2Head00200101] = field(
        default_factory=list,
        metadata={
            "name": "MnfstData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
        },
    )


@dataclass
class BusinessFileHeaderV01Head00200101(ISO20022MessageElement):
    pyld_desc: Optional[PayloadDescription2Head00200101] = field(
        default=None,
        metadata={
            "name": "PyldDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
            "required": True,
        },
    )
    pyld: list[LaxPayloadHead00200101] = field(
        default_factory=list,
        metadata={
            "name": "Pyld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.002.001.01",
        },
    )


@dataclass
class XchgHead00200101(BusinessFileHeaderV01, ISO20022MessageElement):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:head.002.001.01"
