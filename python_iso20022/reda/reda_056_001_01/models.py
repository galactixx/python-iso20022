from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01"


@dataclass
class EffectiveDate1Reda05600101(ISO20022MessageElement):
    fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    fctv_dt_param: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDtParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class GenericIdentification1Reda05600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda05600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Reda05600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification49Reda05600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentification44Reda05600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Reda05600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda05600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification26Reda05600101(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformation4Reda05600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )


@dataclass
class ClassificationType1ChoiceReda05600101(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification1Reda05600101] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class PostalAddress1Reda05600101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Purpose3ChoiceReda05600101(ISO20022MessageElement):
    scties_purp_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesPurpCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda05600101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class SecuritiesAccount22Reda05600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Reda05600101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Reda05600101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda05600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )


@dataclass
class MarketIdentification87Reda05600101(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    clssfctn_tp: Optional[ClassificationType1ChoiceReda05600101] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    sttlm_purp: Optional[Purpose3ChoiceReda05600101] = field(
        default=None,
        metadata={
            "name": "SttlmPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class NameAndAddress5Reda05600101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda05600101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class NameAndAddress8Reda05600101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda05600101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    altrntv_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentificationOrCashPurpose1ChoiceReda05600101(ISO20022MessageElement):
    sttlm_instr_mkt_id: Optional[MarketIdentification87Reda05600101] = field(
        default=None,
        metadata={
            "name": "SttlmInstrMktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    csh_ssipurp: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CshSSIPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class PartyIdentification62Reda05600101(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Reda05600101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda05600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class PartyIdentification64Reda05600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Reda05600101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda05600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class PartyIdentification71ChoiceReda05600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda05600101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda05600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class PartyIdentification75ChoiceReda05600101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda05600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification99ChoiceReda05600101(ISO20022MessageElement):
    nm_and_adr: Optional[NameAndAddress8Reda05600101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    any_bic: Optional[PartyIdentification44Reda05600101] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class PartyIdentification63Reda05600101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification75ChoiceReda05600101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentificationAndAccount95Reda05600101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification71ChoiceReda05600101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    acct_id: Optional[SecuritiesAccount22Reda05600101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyIdentificationAndAccount96Reda05600101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification64Reda05600101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    acct_id: Optional[AccountIdentification26Reda05600101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentificationAndAccount97Reda05600101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification62Reda05600101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    acct_id: Optional[AccountIdentification26Reda05600101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class CashParties24Reda05600101(ISO20022MessageElement):
    cdtr: Optional[PartyIdentificationAndAccount96Reda05600101] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    cdtr_agt: Optional[PartyIdentificationAndAccount97Reda05600101] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    intrmy: Optional[PartyIdentificationAndAccount97Reda05600101] = field(
        default=None,
        metadata={
            "name": "Intrmy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    intrmy2: Optional[PartyIdentificationAndAccount97Reda05600101] = field(
        default=None,
        metadata={
            "name": "Intrmy2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class SettlementParties32Reda05600101(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification63Reda05600101] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount95Reda05600101] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount95Reda05600101] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount95Reda05600101] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount95Reda05600101] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount95Reda05600101] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class SettlementParties35Reda05600101(ISO20022MessageElement):
    stg_sttlm_pties: Optional[SettlementParties32Reda05600101] = field(
        default=None,
        metadata={
            "name": "StgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    lcl_mkt_id: list[GenericIdentification49Reda05600101] = field(
        default_factory=list,
        metadata={
            "name": "LclMktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    regn_dtls: Optional[PartyIdentification99ChoiceReda05600101] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class SecuritiesOrCash1ChoiceReda05600101(ISO20022MessageElement):
    scties_dtls: Optional[SettlementParties35Reda05600101] = field(
        default=None,
        metadata={
            "name": "SctiesDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    csh_pties_dtls: Optional[CashParties24Reda05600101] = field(
        default=None,
        metadata={
            "name": "CshPtiesDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class StandingSettlementInstructionV01Reda05600101(ISO20022MessageElement):
    msg_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgRefId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    fctv_dt_dtls: Optional[EffectiveDate1Reda05600101] = field(
        default=None,
        metadata={
            "name": "FctvDtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )
    acct_id: list[AccountIdentification26Reda05600101] = field(
        default_factory=list,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "min_occurs": 1,
        },
    )
    mkt_id: Optional[MarketIdentificationOrCashPurpose1ChoiceReda05600101] = field(
        default=None,
        metadata={
            "name": "MktId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    sttlm_dtls: Optional[SecuritiesOrCash1ChoiceReda05600101] = field(
        default=None,
        metadata={
            "name": "SttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda05600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01",
        },
    )


@dataclass
class Reda05600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01"

    stg_sttlm_instr: Optional[StandingSettlementInstructionV01Reda05600101] = field(
        default=None,
        metadata={
            "name": "StgSttlmInstr",
            "type": "Element",
            "required": True,
        },
    )
