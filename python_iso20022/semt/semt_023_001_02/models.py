from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    Eligibility1Code,
    EventFrequency4Code,
    SecuritiesAccountPurposeType1Code,
    StatementUpdateType1Code,
    TradingCapacity4Code,
    TradingCapacity6Code,
    TypeOfIdentification2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02"


@dataclass
class CashAccountIdentification5ChoiceSemt02300102(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class DateAndDateTime1ChoiceSemt02300102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class GenericIdentification30Semt02300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt02300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification7Semt02300102(ISO20022MessageElement):
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Semt02300102(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation1Semt02300102(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyTextInformation5Semt02300102(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class QueryReference2Semt02300102(ISO20022MessageElement):
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation2Semt02300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt02300102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification55ChoiceSemt02300102(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Semt02300102] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class Frequency25ChoiceSemt02300102(ISO20022MessageElement):
    cd: Optional[EventFrequency4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt02300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class IdentificationType43ChoiceSemt02300102(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prtry: Optional[GenericIdentification36Semt02300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class InvestorCapacity4ChoiceSemt02300102(ISO20022MessageElement):
    cd: Optional[Eligibility1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt02300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class PostalAddress8Semt02300102(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PurposeCode9ChoiceSemt02300102(ISO20022MessageElement):
    cd: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt02300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class StatementUpdateTypeCodeAndDsscode1ChoiceSemt02300102(ISO20022MessageElement):
    class Meta:
        name = "StatementUpdateTypeCodeAndDSSCode1Choice"

    stmt_upd_tp_as_cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "StmtUpdTpAsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    stmt_upd_tp_as_dss: Optional[GenericIdentification7Semt02300102] = field(
        default=None,
        metadata={
            "name": "StmtUpdTpAsDSS",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class SupplementaryData1Semt02300102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt02300102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )


@dataclass
class TradingPartyCapacity3ChoiceSemt02300102(ISO20022MessageElement):
    cd: Optional[TradingCapacity6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prtry: Optional[GenericIdentification36Semt02300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class TradingPartyCapacity4ChoiceSemt02300102(ISO20022MessageElement):
    cd: Optional[TradingCapacity4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt02300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class AlternatePartyIdentification8Semt02300102(ISO20022MessageElement):
    id_tp: Optional[IdentificationType43ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress13Semt02300102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress8Semt02300102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class Report6Semt02300102(ISO20022MessageElement):
    rpt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "pattern": r"[0-9]{1,5}",
        },
    )
    qry_ref: Optional[QueryReference2Semt02300102] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt_dt_tm: Optional[DateAndDateTime1ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "RptDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )
    frqcy: Optional[Frequency25ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    upd_tp: Optional[StatementUpdateTypeCodeAndDsscode1ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    ntce_tp: Optional[GenericIdentification30Semt02300102] = field(
        default=None,
        metadata={
            "name": "NtceTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class SecuritiesAccount35Semt02300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PurposeCode9ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PartyIdentification240ChoiceSemt02300102(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt02300102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress13Semt02300102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class ConfirmationPartyDetails11Semt02300102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Semt02300102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Semt02300102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class ConfirmationPartyDetails12Semt02300102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Semt02300102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Semt02300102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    invstr_cpcty: Optional[InvestorCapacity4ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "InvstrCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    tradg_pty_cpcty: Optional[TradingPartyCapacity4ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "TradgPtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class ConfirmationPartyDetails13Semt02300102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Semt02300102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Semt02300102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    invstr_prtcn_assoctn_mmbsh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InvstrPrtcnAssoctnMmbsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class ConfirmationPartyDetails14Semt02300102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount35Semt02300102] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    csh_dtls: Optional[AccountIdentification55ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "CshDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Semt02300102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation5Semt02300102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    pty_cpcty: Optional[TradingPartyCapacity3ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "PtyCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class PartyIdentificationAndAccount220Semt02300102(ISO20022MessageElement):
    id: Optional[PartyIdentification240ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_acct: Optional[CashAccountIdentification5ChoiceSemt02300102] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Semt02300102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification8Semt02300102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class ConfirmationParties7Semt02300102(ISO20022MessageElement):
    buyr: Optional[ConfirmationPartyDetails12Semt02300102] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    brrwr: Optional[ConfirmationPartyDetails12Semt02300102] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    sellr: Optional[ConfirmationPartyDetails12Semt02300102] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    lndr: Optional[ConfirmationPartyDetails12Semt02300102] = field(
        default=None,
        metadata={
            "name": "Lndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    brkr_of_cdt: Optional[ConfirmationPartyDetails11Semt02300102] = field(
        default=None,
        metadata={
            "name": "BrkrOfCdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    intrdcg_firm: Optional[ConfirmationPartyDetails11Semt02300102] = field(
        default=None,
        metadata={
            "name": "IntrdcgFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    step_in_firm: Optional[ConfirmationPartyDetails11Semt02300102] = field(
        default=None,
        metadata={
            "name": "StepInFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    step_out_firm: Optional[ConfirmationPartyDetails11Semt02300102] = field(
        default=None,
        metadata={
            "name": "StepOutFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    clr_firm: Optional[ConfirmationPartyDetails13Semt02300102] = field(
        default=None,
        metadata={
            "name": "ClrFirm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    exctg_brkr: Optional[ConfirmationPartyDetails13Semt02300102] = field(
        default=None,
        metadata={
            "name": "ExctgBrkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    cmupty: Optional[ConfirmationPartyDetails11Semt02300102] = field(
        default=None,
        metadata={
            "name": "CMUPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    cmuctr_pty: Optional[ConfirmationPartyDetails11Semt02300102] = field(
        default=None,
        metadata={
            "name": "CMUCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    affrmg_pty: Optional[ConfirmationPartyDetails11Semt02300102] = field(
        default=None,
        metadata={
            "name": "AffrmgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    trad_bnfcry_pty: Optional[ConfirmationPartyDetails14Semt02300102] = field(
        default=None,
        metadata={
            "name": "TradBnfcryPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class SecuritiesEndOfProcessReportV02Semt02300102(ISO20022MessageElement):
    pgntn: list[Pagination1Semt02300102] = field(
        default_factory=list,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    rpt_gnl_dtls: Optional[Report6Semt02300102] = field(
        default=None,
        metadata={
            "name": "RptGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
            "required": True,
        },
    )
    conf_pties: list[ConfirmationParties7Semt02300102] = field(
        default_factory=list,
        metadata={
            "name": "ConfPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    invstr: list[PartyIdentificationAndAccount220Semt02300102] = field(
        default_factory=list,
        metadata={
            "name": "Invstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt02300102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02",
        },
    )


@dataclass
class Semt02300102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02"

    scties_end_of_prc_rpt: Optional[SecuritiesEndOfProcessReportV02Semt02300102] = (
        field(
            default=None,
            metadata={
                "name": "SctiesEndOfPrcRpt",
                "type": "Element",
                "required": True,
            },
        )
    )
