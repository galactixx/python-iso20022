from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    NoReasonCode,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    AcknowledgementReason7Code,
    CancelledStatusReason6Code,
    CorporateActionEventType40Code,
    CorporateActionOption17Code,
    OptionFeatures12Code,
    OptionNumber1Code,
    PendingReason27Code,
    ProtectInstructionStatus3Code,
    ProtectTransactionType2Code,
    RejectionReason85Code,
    ReturnedStatus1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15"


@dataclass
class ActiveCurrencyAndAmountSeev03400115(ISO20022MessageElement):
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
class CorporateActionNarrative10Seev03400115(ISO20022MessageElement):
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev03400115(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification9Seev03400115(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev03400115(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev03400115(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Seev03400115(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03400115(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev03400115(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class ProprietaryQuantity8Seev03400115(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03400115(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AcceptedReason10ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[AcknowledgementReason7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class BlockChainAddressWallet3Seev03400115(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CancelledReason8ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class CorporateActionEventType112ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType40Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class CorporateActionOption41ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[CorporateActionOption17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev03400115(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev03400115] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class GenericIdentification78Seev03400115(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NoSpecifiedReason1Seev03400115(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class OptionFeaturesFormat25ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[OptionFeatures12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class OptionNumber1ChoiceSeev03400115(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[0-9]{3}",
        },
    )
    cd: Optional[OptionNumber1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class OtherIdentification1Seev03400115(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev03400115(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03400115] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class PendingReason66ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[PendingReason27Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class ProprietaryReason4Seev03400115(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProtectInstruction2Seev03400115(ISO20022MessageElement):
    tx_tp: Optional[ProtectTransactionType2Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    prtct_tx_sts: Optional[ProtectInstructionStatus3Code] = field(
        default=None,
        metadata={
            "name": "PrtctTxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 15,
        },
    )
    prtct_sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtctSfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtct_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PrtctDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    ucvrd_prtct_qty: Optional[FinancialInstrumentQuantity18ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "UcvrdPrtctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class Quantity48ChoiceSeev03400115(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity8Seev03400115] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class Quantity51ChoiceSeev03400115(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev03400115] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class RejectedReason60ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[RejectionReason85Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class ReturnedReason2ChoiceSeev03400115(ISO20022MessageElement):
    cd: Optional[ReturnedStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev03400115(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev03400115(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Seev03400115(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03400115] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class AcceptedStatusReason9Seev03400115(ISO20022MessageElement):
    rsn_cd: Optional[AcceptedReason10ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CancelledStatusReason11Seev03400115(ISO20022MessageElement):
    rsn_cd: Optional[CancelledReason8ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSeev03400115(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Seev03400115] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionGeneralInformation182Seev03400115(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType112ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification33Seev03400115(ISO20022MessageElement):
    id: Optional[DocumentIdentification3ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class PendingStatusReason27Seev03400115(ISO20022MessageElement):
    rsn_cd: Optional[PendingReason66ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Seev03400115(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Seev03400115] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class RejectedStatusReason56Seev03400115(ISO20022MessageElement):
    rsn_cd: Optional[RejectedReason60ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ReturnedStatusReason2Seev03400115(ISO20022MessageElement):
    rsn_cd: Optional[ReturnedReason2ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev03400115(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev03400115] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev03400115] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry: Optional[GenericIdentification78Seev03400115] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class SecurityIdentification19Seev03400115(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat11Seev03400115(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity48ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class AcceptedStatus8ChoiceSeev03400115(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rsn: list[AcceptedStatusReason9Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class CancelledStatus12ChoiceSeev03400115(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rsn: list[CancelledStatusReason11Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class CorporateActionOption238Seev03400115(ISO20022MessageElement):
    optn_nb: Optional[OptionNumber1ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    optn_tp: Optional[CorporateActionOption41ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )
    optn_featrs: Optional[OptionFeaturesFormat25ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_length": 1,
            "max_length": 140,
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev03400115] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    ttl_elgbl_bal: Optional[SignedQuantityFormat11Seev03400115] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    instd_bal: Optional[SignedQuantityFormat11Seev03400115] = field(
        default=None,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    uinstd_bal: Optional[SignedQuantityFormat11Seev03400115] = field(
        default=None,
        metadata={
            "name": "UinstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtct_bal: Optional[SignedQuantityFormat11Seev03400115] = field(
        default=None,
        metadata={
            "name": "PrtctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    sts_qty: Optional[Quantity51ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "StsQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    sts_csh_amt: Optional[ActiveCurrencyAndAmountSeev03400115] = field(
        default=None,
        metadata={
            "name": "StsCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    slctn_dealr_fee_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SlctnDealrFeeInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class PendingStatus71ChoiceSeev03400115(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rsn: list[PendingStatusReason27Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class RejectedStatus56ChoiceSeev03400115(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rsn: list[RejectedStatusReason56Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class ReturnedStatus2ChoiceSeev03400115(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rsn: list[ReturnedStatusReason2Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class AcceptedStatus2Seev03400115(ISO20022MessageElement):
    accptd_qty: Optional[Quantity51ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "AccptdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    accptd_rsn: Optional[AcceptedStatus8ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "AccptdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class CancelledStatus5Seev03400115(ISO20022MessageElement):
    canc_qty: Optional[Quantity51ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "CancQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    cxl_rsn: Optional[CancelledStatus12ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class PendingStatus1Seev03400115(ISO20022MessageElement):
    pdg_qty: Optional[Quantity51ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "PdgQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    pdg_rsn: Optional[PendingStatus71ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "PdgRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class RejectedStatus11Seev03400115(ISO20022MessageElement):
    rjctd_qty: Optional[Quantity51ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "RjctdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rjctd_rsn: Optional[RejectedStatus56ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "RjctdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "required": True,
        },
    )


@dataclass
class InstructionProcessingStatus55ChoiceSeev03400115(ISO20022MessageElement):
    canc: Optional[CancelledStatus5Seev03400115] = field(
        default=None,
        metadata={
            "name": "Canc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    accptd_for_frthr_prcg: Optional[AcceptedStatus2Seev03400115] = field(
        default=None,
        metadata={
            "name": "AccptdForFrthrPrcg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    fwdd: Optional[NoSpecifiedReason1Seev03400115] = field(
        default=None,
        metadata={
            "name": "Fwdd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rjctd: Optional[RejectedStatus11Seev03400115] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    pdg: Optional[PendingStatus1Seev03400115] = field(
        default=None,
        metadata={
            "name": "Pdg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rtrd: Optional[ReturnedStatus2ChoiceSeev03400115] = field(
        default=None,
        metadata={
            "name": "Rtrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    dflt_actn: Optional[NoSpecifiedReason1Seev03400115] = field(
        default=None,
        metadata={
            "name": "DfltActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    stg_instr: Optional[NoSpecifiedReason1Seev03400115] = field(
        default=None,
        metadata={
            "name": "StgInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    rcvd_by_issr_or_offerr: Optional[NoSpecifiedReason1Seev03400115] = field(
        default=None,
        metadata={
            "name": "RcvdByIssrOrOfferr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Seev03400115] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class CorporateActionInstructionStatusAdviceV15Seev03400115(ISO20022MessageElement):
    instr_id: Optional[DocumentIdentification9Seev03400115] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    othr_doc_id: list[DocumentIdentification33Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation182Seev03400115] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
                "required": True,
            },
        )
    )
    instr_prcg_sts: list[InstructionProcessingStatus55ChoiceSeev03400115] = field(
        default_factory=list,
        metadata={
            "name": "InstrPrcgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
            "min_occurs": 1,
        },
    )
    corp_actn_instr: Optional[CorporateActionOption238Seev03400115] = field(
        default=None,
        metadata={
            "name": "CorpActnInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    prtct_instr: Optional[ProtectInstruction2Seev03400115] = field(
        default=None,
        metadata={
            "name": "PrtctInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative10Seev03400115] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03400115] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15",
        },
    )


@dataclass
class Seev03400115(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.034.001.15"

    corp_actn_instr_sts_advc: Optional[
        CorporateActionInstructionStatusAdviceV15Seev03400115
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnInstrStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
