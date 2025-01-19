from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import CashAccountType4Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01"


@dataclass
class ActiveCurrencyAndAmountTsin00300101(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2ChoiceTsin00300101(ISO20022MessageElement):
    uschu: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCHU",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"CH[0-9]{6,6}",
        },
    )
    nzncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "NZNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"NZ[0-9]{6,6}",
        },
    )
    iensc: Optional[str] = field(
        default=None,
        metadata={
            "name": "IENSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"IE[0-9]{6,6}",
        },
    )
    gbsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GBSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"SC[0-9]{6,6}",
        },
    )
    usch: Optional[str] = field(
        default=None,
        metadata={
            "name": "USCH",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"CP[0-9]{4,4}",
        },
    )
    chbc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHBC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"SW[0-9]{3,5}",
        },
    )
    usfw: Optional[str] = field(
        default=None,
        metadata={
            "name": "USFW",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"FW[0-9]{9,9}",
        },
    )
    ptncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PTNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"PT[0-9]{8,8}",
        },
    )
    rucb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RUCB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"RU[0-9]{9,9}",
        },
    )
    itncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ITNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"IT[0-9]{10,10}",
        },
    )
    atblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"AT[0-9]{5,5}",
        },
    )
    cacpa: Optional[str] = field(
        default=None,
        metadata={
            "name": "CACPA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"CA[0-9]{9,9}",
        },
    )
    chsic: Optional[str] = field(
        default=None,
        metadata={
            "name": "CHSIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"SW[0-9]{6,6}",
        },
    )
    deblz: Optional[str] = field(
        default=None,
        metadata={
            "name": "DEBLZ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"BL[0-9]{8,8}",
        },
    )
    esncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ESNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"ES[0-9]{8,9}",
        },
    )
    zancc: Optional[str] = field(
        default=None,
        metadata={
            "name": "ZANCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"ZA[0-9]{6,6}",
        },
    )
    hkncc: Optional[str] = field(
        default=None,
        metadata={
            "name": "HKNCC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"HK[0-9]{3,3}",
        },
    )
    aubsbx: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    aubsbs: Optional[str] = field(
        default=None,
        metadata={
            "name": "AUBSBs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"AU[0-9]{6,6}",
        },
    )
    inifsc: Optional[str] = field(
        default=None,
        metadata={
            "name": "INIFSC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"IN[a-zA-Z0-9]{11,11}",
        },
    )
    grhebic: Optional[str] = field(
        default=None,
        metadata={
            "name": "GRHEBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"GR[0-9]{7,7}",
        },
    )
    plknr: Optional[str] = field(
        default=None,
        metadata={
            "name": "PLKNR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"PL[0-9]{8,8}",
        },
    )
    othr_clr_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClrCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Tsin00300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Tsin00300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
        },
    )


@dataclass
class SimpleIdentificationInformation2Tsin00300101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class AccountIdentification3ChoiceTsin00300101(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"[a-zA-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    bban: Optional[str] = field(
        default=None,
        metadata={
            "name": "BBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"[a-zA-Z0-9]{1,30}",
        },
    )
    upic: Optional[str] = field(
        default=None,
        metadata={
            "name": "UPIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"[0-9]{8,17}",
        },
    )
    prtry_acct: Optional[SimpleIdentificationInformation2Tsin00300101] = field(
        default=None,
        metadata={
            "name": "PrtryAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )


@dataclass
class CashAccountType2Tsin00300101(ISO20022MessageElement):
    cd: Optional[CashAccountType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstitutionIdentification6Tsin00300101(ISO20022MessageElement):
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2ChoiceTsin00300101] = (
        field(
            default=None,
            metadata={
                "name": "ClrSysMmbId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            },
        )
    )
    prtry_id: Optional[GenericIdentification4Tsin00300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class PartyIdentification25Tsin00300101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsin00300101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class CashAccount7Tsin00300101(ISO20022MessageElement):
    id: Optional[AccountIdentification3ChoiceTsin00300101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2Tsin00300101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PartyIdentificationAndAccount6Tsin00300101(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification25Tsin00300101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
        },
    )
    cdt_acct: Optional[CashAccount7Tsin00300101] = field(
        default=None,
        metadata={
            "name": "CdtAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    fincg_acct: Optional[CashAccount7Tsin00300101] = field(
        default=None,
        metadata={
            "name": "FincgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )


@dataclass
class CancellationRequestInformation1Tsin00300101(ISO20022MessageElement):
    orgnl_grp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlGrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OrgnlCreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
        },
    )
    nb_of_invc_reqs: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfInvcReqs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "pattern": r"[0-9]{1,15}",
        },
    )
    ttl_blk_invc_amt: Optional[ActiveCurrencyAndAmountTsin00300101] = field(
        default=None,
        metadata={
            "name": "TtlBlkInvcAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    cxl_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 105,
        },
    )
    fincg_rqstr: Optional[PartyIdentificationAndAccount6Tsin00300101] = field(
        default=None,
        metadata={
            "name": "FincgRqstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    intrmy_agt: Optional[FinancialInstitutionIdentification6Tsin00300101] = field(
        default=None,
        metadata={
            "name": "IntrmyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )
    frst_agt: Optional[FinancialInstitutionIdentification6Tsin00300101] = field(
        default=None,
        metadata={
            "name": "FrstAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
        },
    )


@dataclass
class InvoiceFinancingCancellationRequestV01Tsin00300101(ISO20022MessageElement):
    cxl_req_id: Optional[MessageIdentification1Tsin00300101] = field(
        default=None,
        metadata={
            "name": "CxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
        },
    )
    cxl_req_inf: Optional[CancellationRequestInformation1Tsin00300101] = field(
        default=None,
        metadata={
            "name": "CxlReqInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
            "required": True,
        },
    )


@dataclass
class Tsin00300101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01"

    invc_fincg_cxl_req: Optional[InvoiceFinancingCancellationRequestV01Tsin00300101] = (
        field(
            default=None,
            metadata={
                "name": "InvcFincgCxlReq",
                "type": "Element",
                "required": True,
            },
        )
    )
