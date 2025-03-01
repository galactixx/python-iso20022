from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AcknowledgementReason5Code,
    CancelledStatusReason16Code,
    FailingReason3Code,
    NoReasonCode,
    PendingReason10Code,
)
from python_iso20022.semt.enums import (
    RejectionReason69Code,
    SecuritiesBalanceType13Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08"


@dataclass
class DateAndDateTime2ChoiceSemt01400108(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSemt01400108(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Semt01400108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt01400108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Semt01400108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt01400108(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Linkages75Semt01400108(ISO20022MessageElement):
    scties_sttlm_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt01400108(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentifications29Semt01400108(ISO20022MessageElement):
    acct_ownr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AcknowledgementReason12ChoiceSemt01400108(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class BlockChainAddressWallet3Semt01400108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CancellationReason36ChoiceSemt01400108(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class FailingReason7ChoiceSemt01400108(ISO20022MessageElement):
    cd: Optional[FailingReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class OtherIdentification1Semt01400108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt01400108(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt01400108] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class PendingReason26ChoiceSemt01400108(ISO20022MessageElement):
    cd: Optional[PendingReason10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class ProprietaryReason4Semt01400108(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class RejectionAndRepairReason36ChoiceSemt01400108(ISO20022MessageElement):
    cd: Optional[RejectionReason69Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class SecuritiesAccount19Semt01400108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesBalanceType7ChoiceSemt01400108(ISO20022MessageElement):
    cd: Optional[SecuritiesBalanceType13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class SupplementaryData1Semt01400108(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt01400108] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )


@dataclass
class AcknowledgementReason9Semt01400108(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason12ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CancellationReason22Semt01400108(ISO20022MessageElement):
    cd: Optional[CancellationReason36ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class FailingReason7Semt01400108(ISO20022MessageElement):
    cd: Optional[FailingReason7ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class PendingReason14Semt01400108(ISO20022MessageElement):
    cd: Optional[PendingReason26ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Semt01400108(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Semt01400108] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class RejectionOrRepairReason36Semt01400108(ISO20022MessageElement):
    cd: list[RejectionAndRepairReason36ChoiceSemt01400108] = field(
        default_factory=list,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SecurityIdentification19Semt01400108(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AcknowledgedAcceptedStatus21ChoiceSemt01400108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    rsn: list[AcknowledgementReason9Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class CancellationStatus24ChoiceSemt01400108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    rsn: list[CancellationReason22Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class FailingStatus9ChoiceSemt01400108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    rsn: list[FailingReason7Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class IntraPositionDetails60Semt01400108(ISO20022MessageElement):
    pool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Semt01400108] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Semt01400108] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Semt01400108] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    sttlm_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "SttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    lot_nb: Optional[GenericIdentification37Semt01400108] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    sttlm_dt: Optional[DateAndDateTime2ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    ackd_sts_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AckdStsTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    bal_fr: Optional[SecuritiesBalanceType7ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "BalFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    bal_to: Optional[SecuritiesBalanceType7ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "BalTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class PendingStatus36ChoiceSemt01400108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    rsn: list[PendingReason14Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class RejectionOrRepairStatus41ChoiceSemt01400108(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    rsn: list[RejectionOrRepairReason36Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class IntraPositionProcessingStatus9ChoiceSemt01400108(ISO20022MessageElement):
    rjctd: Optional[RejectionOrRepairStatus41ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    rpr: Optional[RejectionOrRepairStatus41ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Rpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    canc: Optional[CancellationStatus24ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    ackd_accptd: Optional[AcknowledgedAcceptedStatus21ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "AckdAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class SettlementStatus16ChoiceSemt01400108(ISO20022MessageElement):
    pdg: Optional[PendingStatus36ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    flng: Optional[FailingStatus9ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "Flng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prtry: Optional[ProprietaryStatusAndReason6Semt01400108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class IntraPositionMovementStatusAdviceV08Semt01400108(ISO20022MessageElement):
    tx_id: Optional[TransactionIdentifications29Semt01400108] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
            "required": True,
        },
    )
    lkg: Optional[Linkages75Semt01400108] = field(
        default=None,
        metadata={
            "name": "Lkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    prcg_sts: Optional[IntraPositionProcessingStatus9ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "PrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    sttlm_sts: Optional[SettlementStatus16ChoiceSemt01400108] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    tx_dtls: Optional[IntraPositionDetails60Semt01400108] = field(
        default=None,
        metadata={
            "name": "TxDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )
    splmtry_data: list[SupplementaryData1Semt01400108] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08",
        },
    )


@dataclass
class Semt01400108(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.014.001.08"

    intra_pos_mvmnt_sts_advc: Optional[
        IntraPositionMovementStatusAdviceV08Semt01400108
    ] = field(
        default=None,
        metadata={
            "name": "IntraPosMvmntStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
