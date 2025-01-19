from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02"


@dataclass
class Count1Tsmt00500102(ISO20022MessageElement):
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class MessageIdentification1Tsmt00500102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt00500102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmendmentAcceptanceV02Tsmt00500102(ISO20022MessageElement):
    accptnc_id: Optional[MessageIdentification1Tsmt00500102] = field(
        default=None,
        metadata={
            "name": "AccptncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt00500102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt00500102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
        },
    )
    dlta_rpt_ref: Optional[MessageIdentification1Tsmt00500102] = field(
        default=None,
        metadata={
            "name": "DltaRptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
            "required": True,
        },
    )
    accptd_amdmnt_nb: Optional[Count1Tsmt00500102] = field(
        default=None,
        metadata={
            "name": "AccptdAmdmntNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt00500102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02"

    amdmnt_accptnc: Optional[AmendmentAcceptanceV02Tsmt00500102] = field(
        default=None,
        metadata={
            "name": "AmdmntAccptnc",
            "type": "Element",
            "required": True,
        },
    )
