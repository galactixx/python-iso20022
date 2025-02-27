from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    CorporateActionNarrative1Code,
    SafekeepingAccountIdentification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09"


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev03800109(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Seev03800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev03800109(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryQuantity8Seev03800109(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    qty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03800109(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification10Seev03800109(ISO20022MessageElement):
    id_cd: Optional[SafekeepingAccountIdentification1Code] = field(
        default=None,
        metadata={
            "name": "IdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )


@dataclass
class CorporateActionNarrative3ChoiceSeev03800109(ISO20022MessageElement):
    cd: Optional[CorporateActionNarrative1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Seev03800109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class GenericIdentification78Seev03800109(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev03800109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherIdentification1Seev03800109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev03800109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03800109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class Quantity48ChoiceSeev03800109(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity8Seev03800109] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03800109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev03800109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignedQuantityFormat10Seev03800109(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03800109(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03800109] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )


@dataclass
class CorporateActionGeneralInformation92Seev03800109(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nrrtv_tp: Optional[CorporateActionNarrative3ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "NrrtvTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev03800109(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev03800109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03800109] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    prtry: Optional[GenericIdentification78Seev03800109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class SecurityIdentification19Seev03800109(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev03800109] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat11Seev03800109(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity48ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )


@dataclass
class BalanceFormat11ChoiceSeev03800109(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat11Seev03800109] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03800109] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03800109] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class AccountIdentification71Seev03800109(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    confd_bal: Optional[BalanceFormat11ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "ConfdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "required": True,
        },
    )


@dataclass
class AccountIdentification72ChoiceSeev03800109(ISO20022MessageElement):
    for_all_accts: Optional[AccountIdentification10Seev03800109] = field(
        default=None,
        metadata={
            "name": "ForAllAccts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    accts_list_and_bal_dtls: list[AccountIdentification71Seev03800109] = field(
        default_factory=list,
        metadata={
            "name": "AcctsListAndBalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class CorporateActionNarrativeV09Seev03800109(ISO20022MessageElement):
    acct_dtls: Optional[AccountIdentification72ChoiceSeev03800109] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    undrlyg_scty: Optional[SecurityIdentification19Seev03800109] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation92Seev03800109] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
                "required": True,
            },
        )
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 8000,
        },
    )
    splmtry_data: list[SupplementaryData1Seev03800109] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09",
        },
    )


@dataclass
class Seev03800109(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09"

    corp_actn_nrrtv: Optional[CorporateActionNarrativeV09Seev03800109] = field(
        default=None,
        metadata={
            "name": "CorpActnNrrtv",
            "type": "Element",
            "required": True,
        },
    )
