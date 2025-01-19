from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01"


@dataclass
class IdentificationSource3ChoiceReda00900101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Reda00900101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
        },
    )


@dataclass
class Pagination1Reda00900101(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda00900101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class OtherIdentification1Reda00900101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceReda00900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Reda00900101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda00900101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )


@dataclass
class SecurityIdentification39Reda00900101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Reda00900101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SecuritiesReferenceDataChange3Reda00900101(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification39Reda00900101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )
    fld_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FldNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    od_fld_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "OdFldVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    new_fld_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewFldVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    opr_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OprTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )


@dataclass
class SecurityStatement3Reda00900101(ISO20022MessageElement):
    sys_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SysDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )
    chng: list[SecuritiesReferenceDataChange3Reda00900101] = field(
        default_factory=list,
        metadata={
            "name": "Chng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
        },
    )


@dataclass
class SecurityActivityAdviceV01Reda00900101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Reda00900101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
        },
    )
    pgntn: Optional[Pagination1Reda00900101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )
    scty_actvty: Optional[SecurityStatement3Reda00900101] = field(
        default=None,
        metadata={
            "name": "SctyActvty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda00900101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01",
        },
    )


@dataclass
class Reda00900101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01"

    scty_actvty_advc: Optional[SecurityActivityAdviceV01Reda00900101] = field(
        default=None,
        metadata={
            "name": "SctyActvtyAdvc",
            "type": "Element",
            "required": True,
        },
    )
