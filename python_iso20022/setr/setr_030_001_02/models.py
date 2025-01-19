from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    AffirmationStatus1Code,
    ClearingAccountType1Code,
    Eligibility1Code,
    SecuritiesAccountPurposeType1Code,
    TradingCapacity4Code,
    TradingCapacity6Code,
    TypeOfIdentification2Code,
)
from python_iso20022.setr.enums import ClearingSide1Code, UnaffirmedReason1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02"


@dataclass
class GenericIdentification30Setr03000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Setr03000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationReference8ChoiceSetr03000102(ISO20022MessageElement):
    instg_pty_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstgPtyTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    exctg_pty_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExctgPtyTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ordr_lk_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntOrdrLkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndvAllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scndry_allcn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScndryAllcnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmplc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmplcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PartyTextInformation1Setr03000102(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyTextInformation5Setr03000102(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SimpleIdentificationInformation2Setr03000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Setr03000102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactiontIdentification4Setr03000102(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification55ChoiceSetr03000102(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Setr03000102] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class AffirmationStatus10ChoiceSetr03000102(ISO20022MessageElement):
    cd: Optional[AffirmationStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Setr03000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class DocumentNumber17ChoiceSetr03000102(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification30Setr03000102] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class IdentificationType43ChoiceSetr03000102(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prtry: Optional[GenericIdentification36Setr03000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class InvestorCapacity4ChoiceSetr03000102(ISO20022MessageElement):
    cd: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Setr03000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class PartyIdentification243ChoiceSetr03000102(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification30Setr03000102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class PostalAddress8Setr03000102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PurposeCode9ChoiceSetr03000102(ISO20022MessageElement):
    cd: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Setr03000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class SecuritiesAccount20Setr03000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[ClearingAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Setr03000102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Setr03000102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )


@dataclass
class TradingPartyCapacity3ChoiceSetr03000102(ISO20022MessageElement):
    cd: Optional[TradingCapacity6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prtry: Optional[GenericIdentification36Setr03000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class TradingPartyCapacity4ChoiceSetr03000102(ISO20022MessageElement):
    cd: Optional[TradingCapacity4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Setr03000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class UnaffirmedReason3ChoiceSetr03000102(ISO20022MessageElement):
    cd: Optional[UnaffirmedReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Setr03000102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class AlternatePartyIdentification8Setr03000102(ISO20022MessageElement):
    id_tp: Optional[IdentificationType43ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Linkages52Setr03000102(ISO20022MessageElement):
    msg_nb: Optional[DocumentNumber17ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "MsgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    ref: Optional[IdentificationReference8ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )


@dataclass
class NameAndAddress13Setr03000102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress8Setr03000102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class SecuritiesAccount35Setr03000102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PurposeCode9ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class StatusAndReason46Setr03000102(ISO20022MessageElement):
    affirm_sts: Optional[AffirmationStatus10ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "AffirmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    uaffrmd_rsn: Optional[UnaffirmedReason3ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "UaffrmdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PartyIdentification240ChoiceSetr03000102(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Setr03000102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress13Setr03000102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class ConfirmationPartyDetails12Setr03000102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr03000102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr03000102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    invstr_cpcty: Optional[InvestorCapacity4ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "InvstrCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    tradg_pty_cpcty: Optional[TradingPartyCapacity4ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "TradgPtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class ConfirmationPartyDetails14Setr03000102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount35Setr03000102] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    csh_dtls: Optional[AccountIdentification55ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "CshDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr03000102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr03000102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity3ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class ConfirmationPartyDetails15Setr03000102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount35Setr03000102] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    csh_dtls: Optional[AccountIdentification55ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "CshDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr03000102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Setr03000102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class PartyIdentificationAndAccount219Setr03000102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Setr03000102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    sd: Optional[ClearingSide1Code] = field(
        default=None,
        metadata={
            "name": "Sd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    clr_acct: Optional[SecuritiesAccount20Setr03000102] = field(
        default=None,
        metadata={
            "name": "ClrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Setr03000102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class Clearing6Setr03000102(ISO20022MessageElement):
    clr_mmb: list[PartyIdentificationAndAccount219Setr03000102] = field(
        default_factory=list,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_occurs": 1,
        },
    )
    clr_sgmt: Optional[PartyIdentification243ChoiceSetr03000102] = field(
        default=None,
        metadata={
            "name": "ClrSgmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class ConfirmationParties8Setr03000102(ISO20022MessageElement):
    affrmg_pty: Optional[ConfirmationPartyDetails15Setr03000102] = field(
        default=None,
        metadata={
            "name": "AffrmgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    buyr: Optional[ConfirmationPartyDetails12Setr03000102] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    brrwr: Optional[ConfirmationPartyDetails12Setr03000102] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    sellr: Optional[ConfirmationPartyDetails12Setr03000102] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    lndr: Optional[ConfirmationPartyDetails12Setr03000102] = field(
        default=None,
        metadata={
            "name": "Lndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    trad_bnfcry_pty: Optional[ConfirmationPartyDetails14Setr03000102] = field(
        default=None,
        metadata={
            "name": "TradBnfcryPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class SecuritiesTradeConfirmationResponseV02Setr03000102(ISO20022MessageElement):
    id: Optional[TransactiontIdentification4Setr03000102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    refs: list[Linkages52Setr03000102] = field(
        default_factory=list,
        metadata={
            "name": "Refs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "min_occurs": 1,
        },
    )
    sts: Optional[StatusAndReason46Setr03000102] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
            "required": True,
        },
    )
    clr_dtls: Optional[Clearing6Setr03000102] = field(
        default=None,
        metadata={
            "name": "ClrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    conf_pties: list[ConfirmationParties8Setr03000102] = field(
        default_factory=list,
        metadata={
            "name": "ConfPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Setr03000102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02",
        },
    )


@dataclass
class Setr03000102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:setr.030.001.02"

    scties_trad_conf_rspn: Optional[
        SecuritiesTradeConfirmationResponseV02Setr03000102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesTradConfRspn",
            "type": "Element",
            "required": True,
        },
    )
