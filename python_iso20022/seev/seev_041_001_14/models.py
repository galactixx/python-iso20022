from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    CancelledStatusReason5Code,
    NoReasonCode,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    CorporateActionEventType40Code,
    CorporateActionOption17Code,
    OptionFeatures12Code,
    OptionNumber1Code,
    PendingCancellationReason5Code,
    ProtectInstructionStatus4Code,
    ProtectTransactionType3Code,
    RejectionReason79Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14"


@dataclass
class ActiveCurrencyAndAmountSeev04100114(ISO20022MessageElement):
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
class CorporateActionNarrative10Seev04100114(ISO20022MessageElement):
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev04100114(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification9Seev04100114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev04100114(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev04100114(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Seev04100114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev04100114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev04100114(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev04100114(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class ProprietaryQuantity8Seev04100114(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev04100114(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BlockChainAddressWallet3Seev04100114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CancelledReason9ChoiceSeev04100114(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class CorporateActionEventType112ChoiceSeev04100114(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType40Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class CorporateActionOption41ChoiceSeev04100114(ISO20022MessageElement):
    cd: Optional[CorporateActionOption17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev04100114(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev04100114] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class GenericIdentification78Seev04100114(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NoSpecifiedReason1Seev04100114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )


@dataclass
class OptionFeaturesFormat25ChoiceSeev04100114(ISO20022MessageElement):
    cd: Optional[OptionFeatures12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class OptionNumber1ChoiceSeev04100114(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[0-9]{3}",
        },
    )
    cd: Optional[OptionNumber1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class OtherIdentification1Seev04100114(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev04100114(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev04100114] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class PendingCancellationReason5ChoiceSeev04100114(ISO20022MessageElement):
    cd: Optional[PendingCancellationReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class ProprietaryReason4Seev04100114(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProtectInstruction4Seev04100114(ISO20022MessageElement):
    tx_tp: Optional[ProtectTransactionType3Code] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    prtct_tx_sts: Optional[ProtectInstructionStatus4Code] = field(
        default=None,
        metadata={
            "name": "PrtctTxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 15,
        },
    )
    prtct_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PrtctDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    ucvrd_prtct_qty: Optional[FinancialInstrumentQuantity18ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "UcvrdPrtctQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class Quantity48ChoiceSeev04100114(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity8Seev04100114] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class Quantity51ChoiceSeev04100114(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev04100114] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class RejectedReason55ChoiceSeev04100114(ISO20022MessageElement):
    cd: Optional[RejectionReason79Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev04100114(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev04100114(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Seev04100114(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev04100114] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )


@dataclass
class CancelledStatusReason12Seev04100114(ISO20022MessageElement):
    rsn_cd: Optional[CancelledReason9ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSeev04100114(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Seev04100114] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionGeneralInformation182Seev04100114(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType112ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification33Seev04100114(ISO20022MessageElement):
    id: Optional[DocumentIdentification3ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class PendingCancellationStatusReason7Seev04100114(ISO20022MessageElement):
    rsn_cd: Optional[PendingCancellationReason5ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Seev04100114(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Seev04100114] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Seev04100114] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class RejectedStatusReason52Seev04100114(ISO20022MessageElement):
    rsn_cd: Optional[RejectedReason55ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev04100114(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev04100114] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev04100114] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry: Optional[GenericIdentification78Seev04100114] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class SecurityIdentification19Seev04100114(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev04100114] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat11Seev04100114(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity48ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )


@dataclass
class CancelledStatus11ChoiceSeev04100114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    rsn: list[CancelledStatusReason12Seev04100114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class CorporateActionOption239Seev04100114(ISO20022MessageElement):
    optn_nb: Optional[OptionNumber1ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    optn_tp: Optional[CorporateActionOption41ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "required": True,
        },
    )
    optn_featrs: Optional[OptionFeaturesFormat25ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "OptnFeatrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_length": 1,
            "max_length": 140,
        },
    )
    csh_acct: Optional[CashAccountIdentification9ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev04100114] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    ttl_elgbl_bal: Optional[SignedQuantityFormat11Seev04100114] = field(
        default=None,
        metadata={
            "name": "TtlElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    instd_bal: Optional[SignedQuantityFormat11Seev04100114] = field(
        default=None,
        metadata={
            "name": "InstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    uinstd_bal: Optional[SignedQuantityFormat11Seev04100114] = field(
        default=None,
        metadata={
            "name": "UinstdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtct_bal: Optional[SignedQuantityFormat11Seev04100114] = field(
        default=None,
        metadata={
            "name": "PrtctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    sts_qty: Optional[Quantity51ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "StsQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    sts_csh_amt: Optional[ActiveCurrencyAndAmountSeev04100114] = field(
        default=None,
        metadata={
            "name": "StsCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class PendingCancellationStatus13ChoiceSeev04100114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    rsn: list[PendingCancellationStatusReason7Seev04100114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class RejectedStatus53ChoiceSeev04100114(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    rsn: list[RejectedStatusReason52Seev04100114] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class InstructionCancellationRequestStatus17ChoiceSeev04100114(ISO20022MessageElement):
    cxl_cmpltd: Optional[CancelledStatus11ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "CxlCmpltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    accptd: Optional[NoSpecifiedReason1Seev04100114] = field(
        default=None,
        metadata={
            "name": "Accptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    rjctd: Optional[RejectedStatus53ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    pdg_cxl: Optional[PendingCancellationStatus13ChoiceSeev04100114] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Seev04100114] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class CorporateActionInstructionCancellationRequestStatusAdviceV14Seev04100114(
    ISO20022MessageElement
):
    instr_cxl_req_id: Optional[DocumentIdentification9Seev04100114] = field(
        default=None,
        metadata={
            "name": "InstrCxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    othr_doc_id: list[DocumentIdentification33Seev04100114] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation182Seev04100114] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
                "required": True,
            },
        )
    )
    instr_cxl_req_sts: list[
        InstructionCancellationRequestStatus17ChoiceSeev04100114
    ] = field(
        default_factory=list,
        metadata={
            "name": "InstrCxlReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
            "min_occurs": 1,
        },
    )
    corp_actn_instr: Optional[CorporateActionOption239Seev04100114] = field(
        default=None,
        metadata={
            "name": "CorpActnInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    prtct_instr: Optional[ProtectInstruction4Seev04100114] = field(
        default=None,
        metadata={
            "name": "PrtctInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    addtl_inf: Optional[CorporateActionNarrative10Seev04100114] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )
    splmtry_data: list[SupplementaryData1Seev04100114] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
        },
    )


@dataclass
class Seev04100114(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14"

    corp_actn_instr_cxl_req_sts_advc: Optional[
        CorporateActionInstructionCancellationRequestStatusAdviceV14Seev04100114
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnInstrCxlReqStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
