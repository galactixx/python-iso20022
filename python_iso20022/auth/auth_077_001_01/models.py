from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.auth.enums import BenchmarkCurveName2Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01"


@dataclass
class GenericIdentification36Auth07700101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceAuth07700101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Period2Auth07700101(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )


@dataclass
class SupervisingAuthorityIdentification1ChoiceAuth07700101(ISO20022MessageElement):
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth07700101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BenchmarkDetail1Auth07700101(ISO20022MessageElement):
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    cmnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class OtherIdentification1Auth07700101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceAuth07700101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )


@dataclass
class Period4ChoiceAuth07700101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth07700101] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class PostalAddress1Auth07700101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupervisingAuthorityIdentification1Auth07700101(ISO20022MessageElement):
    id: Optional[SupervisingAuthorityIdentification1ChoiceAuth07700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SupplementaryData1Auth07700101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Auth07700101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class SecurityIdentification19Auth07700101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Auth07700101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class StatusDetail1Auth07700101(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    cmptnt_authrty: Optional[SupervisingAuthorityIdentification1Auth07700101] = field(
        default=None,
        metadata={
            "name": "CmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    sts: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 10,
        },
    )
    sts_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )
    actvty_prd: Optional[Period4ChoiceAuth07700101] = field(
        default=None,
        metadata={
            "name": "ActvtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    cmnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 20000,
        },
    )


@dataclass
class BenchmarkCancellation1Auth07700101(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[SecurityIdentification19Auth07700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth07700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceAuth07700101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Auth07700101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Auth07700101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class PartyIdentification136Auth07700101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceAuth07700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class BenchmarkCreate1Auth07700101(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[SecurityIdentification19Auth07700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    othr: Optional[BenchmarkDetail1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    admstr: Optional[PartyIdentification136Auth07700101] = field(
        default=None,
        metadata={
            "name": "Admstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    ndrsng_pty: Optional[PartyIdentification136Auth07700101] = field(
        default=None,
        metadata={
            "name": "NdrsngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    sts: Optional[StatusDetail1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    tech_vldty_prd: Optional[Period4ChoiceAuth07700101] = field(
        default=None,
        metadata={
            "name": "TechVldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth07700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class BenchmarkUpdate1Auth07700101(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[SecurityIdentification19Auth07700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    prvs_id: Optional[SecurityIdentification19Auth07700101] = field(
        default=None,
        metadata={
            "name": "PrvsId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    othr: Optional[BenchmarkDetail1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    admstr: Optional[PartyIdentification136Auth07700101] = field(
        default=None,
        metadata={
            "name": "Admstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "required": True,
        },
    )
    ndrsng_pty: Optional[PartyIdentification136Auth07700101] = field(
        default=None,
        metadata={
            "name": "NdrsngPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    sts: Optional[StatusDetail1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    tech_vldty_prd: Optional[Period4ChoiceAuth07700101] = field(
        default=None,
        metadata={
            "name": "TechVldtyPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Auth07700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class BenchmarkReport1ChoiceAuth07700101(ISO20022MessageElement):
    cret: Optional[BenchmarkCreate1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Cret",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    upd: Optional[BenchmarkUpdate1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Upd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )
    cxl: Optional[BenchmarkCancellation1Auth07700101] = field(
        default=None,
        metadata={
            "name": "Cxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class FinancialBenchmarkReportV01Auth07700101(ISO20022MessageElement):
    bchmk_data: list[BenchmarkReport1ChoiceAuth07700101] = field(
        default_factory=list,
        metadata={
            "name": "BchmkData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth07700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01",
        },
    )


@dataclass
class Auth07700101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01"

    fin_bchmk_rpt: Optional[FinancialBenchmarkReportV01Auth07700101] = field(
        default=None,
        metadata={
            "name": "FinBchmkRpt",
            "type": "Element",
            "required": True,
        },
    )
