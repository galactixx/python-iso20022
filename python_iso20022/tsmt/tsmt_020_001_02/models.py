from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02"


@dataclass
class MessageIdentification1Tsmt02000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt02000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MisMatchAcceptanceV02Tsmt02000102(ISO20022MessageElement):
    accptnc_id: Optional[MessageIdentification1Tsmt02000102] = field(
        default=None,
        metadata={
            "name": "AccptncId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt02000102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt02000102] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02",
        },
    )
    data_set_mtch_rpt_ref: Optional[MessageIdentification1Tsmt02000102] = field(
        default=None,
        metadata={
            "name": "DataSetMtchRptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02",
            "required": True,
        },
    )


@dataclass
class Tsmt02000102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02"

    mis_mtch_accptnc: Optional[MisMatchAcceptanceV02Tsmt02000102] = field(
        default=None,
        metadata={
            "name": "MisMtchAccptnc",
            "type": "Element",
            "required": True,
        },
    )
