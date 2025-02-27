from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    DateType8Code,
    ProcessingPosition3Code,
    ShortLong1Code,
)
from python_iso20022.seev.enums import (
    AdditionalBusinessProcess7Code,
    CorporateActionEventStage4Code,
    CorporateActionEventType37Code,
    CorporateActionOption12Code,
    CorporateActionReversalReason3Code,
    IntermediateSecurityDistributionType5Code,
    LotteryType1Code,
    OptionNumber1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16"


@dataclass
class ActiveCurrencyAndAmountSeev03700116(ISO20022MessageElement):
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
class CashAccountIdentification5ChoiceSeev03700116(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionEventReference3ChoiceSeev03700116(ISO20022MessageElement):
    lkd_offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdOffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkd_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LkdCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionNarrative31Seev03700116(ISO20022MessageElement):
    addtl_txt: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    nrrtv_vrsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NrrtvVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_nrrtv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PtyCtctNrrtv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    taxtn_conds: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TaxtnConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class DateAndDateTime2ChoiceSeev03700116(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class DocumentIdentification3ChoiceSeev03700116(ISO20022MessageElement):
    acct_svcr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctOwnrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSeev03700116(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Seev03700116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev03700116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev03700116(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class ProprietaryQuantity8Seev03700116(ISO20022MessageElement):
    qty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev03700116(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TransactionIdentification15Seev03700116(ISO20022MessageElement):
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalBusinessProcessFormat11ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[AdditionalBusinessProcess7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class BlockChainAddressWallet3Seev03700116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CorporateActionEventStageFormat14ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[CorporateActionEventStage4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionEventType109ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType37Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionOption33ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[CorporateActionOption12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionReversalReason10ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[CorporateActionReversalReason3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class DateCode19ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class DocumentNumber5ChoiceSeev03700116(ISO20022MessageElement):
    shrt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "pattern": r"[0-9]{3}",
        },
    )
    lng_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "LngNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "pattern": r"[a-z]{4}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}",
        },
    )
    prtry_nb: Optional[GenericIdentification36Seev03700116] = field(
        default=None,
        metadata={
            "name": "PrtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03700116(
    ISO20022MessageElement
):
    cd: Optional[IntermediateSecurityDistributionType5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class LotteryTypeFormat4ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[LotteryType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class OptionNumber1ChoiceSeev03700116(ISO20022MessageElement):
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "pattern": r"[0-9]{3}",
        },
    )
    cd: Optional[OptionNumber1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class OtherIdentification1Seev03700116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Seev03700116(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProcessingPosition7ChoiceSeev03700116(ISO20022MessageElement):
    cd: Optional[ProcessingPosition3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[GenericIdentification30Seev03700116] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class Quantity48ChoiceSeev03700116(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry_qty: Optional[ProprietaryQuantity8Seev03700116] = field(
        default=None,
        metadata={
            "name": "PrtryQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class Quantity51ChoiceSeev03700116(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev03700116] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class SignedQuantityFormat10Seev03700116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Seev03700116(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev03700116] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSeev03700116(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Seev03700116] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class CorporateActionEventReference3Seev03700116(ISO20022MessageElement):
    evt_id: Optional[CorporateActionEventReference3ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "EvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionReversalReason8Seev03700116(ISO20022MessageElement):
    rsn: Optional[CorporateActionReversalReason10ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateFormat30ChoiceSeev03700116(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class DocumentIdentification31Seev03700116(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class DocumentIdentification32Seev03700116(ISO20022MessageElement):
    id: Optional[DocumentIdentification3ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    doc_nb: Optional[DocumentNumber5ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    lkg_tp: Optional[ProcessingPosition7ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "LkgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class NameAndAddress5Seev03700116(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev03700116] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class SecurityIdentification19Seev03700116(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev03700116] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SignedQuantityFormat11Seev03700116(ISO20022MessageElement):
    shrt_lng_pos: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    qty_chc: Optional[Quantity48ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "QtyChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )


@dataclass
class Account10ChoiceSeev03700116(ISO20022MessageElement):
    csh_acct: Optional[CashAccountIdentification9ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "CshAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    chrgs_acct: Optional[CashAccountIdentification5ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "ChrgsAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    tax_acct: Optional[CashAccountIdentification5ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "TaxAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class BalanceFormat11ChoiceSeev03700116(ISO20022MessageElement):
    bal: Optional[SignedQuantityFormat11Seev03700116] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    elgbl_bal: Optional[SignedQuantityFormat10Seev03700116] = field(
        default=None,
        metadata={
            "name": "ElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    not_elgbl_bal: Optional[SignedQuantityFormat10Seev03700116] = field(
        default=None,
        metadata={
            "name": "NotElgblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionDate86Seev03700116(ISO20022MessageElement):
    rcrd_dt: Optional[DateFormat30ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    ex_dvdd_dt: Optional[DateFormat30ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionGeneralInformation179Seev03700116(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_actn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssActnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType109ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev03700116] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    frctnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "FrctnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class PartyIdentification120ChoiceSeev03700116(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev03700116] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev03700116] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class SecuritiesOption80Seev03700116(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev03700116] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    pstng_qty: Optional[Quantity51ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    orgnl_pstng_dt: Optional[DateAndDateTime2ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "OrgnlPstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class AccountAndBalance50Seev03700116(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blck_chain_adr_or_wllt: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "min_length": 1,
            "max_length": 140,
        },
    )
    confd_bal: Optional[BalanceFormat11ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "ConfdBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )


@dataclass
class CashOption109Seev03700116(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    acct: Optional[Account10ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    pstng_dt: Optional[DateAndDateTime2ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "PstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    orgnl_pstng_dt: Optional[DateAndDateTime2ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "OrgnlPstngDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    pstng_amt: Optional[ActiveCurrencyAndAmountSeev03700116] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )


@dataclass
class CorporateAction70Seev03700116(ISO20022MessageElement):
    dt_dtls: Optional[CorporateActionDate86Seev03700116] = field(
        default=None,
        metadata={
            "name": "DtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    evt_stag: Optional[CorporateActionEventStageFormat14ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "EvtStag",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    addtl_biz_prc_ind: Optional[AdditionalBusinessProcessFormat11ChoiceSeev03700116] = (
        field(
            default=None,
            metadata={
                "name": "AddtlBizPrcInd",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            },
        )
    )
    intrmdt_scties_dstrbtn_tp: Optional[
        IntermediateSecuritiesDistributionTypeFormat15ChoiceSeev03700116
    ] = field(
        default=None,
        metadata={
            "name": "IntrmdtSctiesDstrbtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    ltry_tp: Optional[LotteryTypeFormat4ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "LtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionOption240Seev03700116(ISO20022MessageElement):
    optn_nb: Optional[OptionNumber1ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    optn_tp: Optional[CorporateActionOption33ChoiceSeev03700116] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption80Seev03700116] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    csh_mvmnt_dtls: list[CashOption109Seev03700116] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class CorporateActionMovementReversalAdviceV16Seev03700116(ISO20022MessageElement):
    mvmnt_conf_id: Optional[DocumentIdentification31Seev03700116] = field(
        default=None,
        metadata={
            "name": "MvmntConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    othr_doc_id: list[DocumentIdentification32Seev03700116] = field(
        default_factory=list,
        metadata={
            "name": "OthrDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    evts_lkg: list[CorporateActionEventReference3Seev03700116] = field(
        default_factory=list,
        metadata={
            "name": "EvtsLkg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    rvsl_rsn: Optional[CorporateActionReversalReason8Seev03700116] = field(
        default=None,
        metadata={
            "name": "RvslRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    tx_id: Optional[TransactionIdentification15Seev03700116] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation179Seev03700116] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
                "required": True,
            },
        )
    )
    acct_dtls: Optional[AccountAndBalance50Seev03700116] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction70Seev03700116] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    corp_actn_conf_dtls: Optional[CorporateActionOption240Seev03700116] = field(
        default=None,
        metadata={
            "name": "CorpActnConfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
            "required": True,
        },
    )
    addtl_inf: Optional[CorporateActionNarrative31Seev03700116] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    issr_agt: list[PartyIdentification120ChoiceSeev03700116] = field(
        default_factory=list,
        metadata={
            "name": "IssrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    png_agt: list[PartyIdentification120ChoiceSeev03700116] = field(
        default_factory=list,
        metadata={
            "name": "PngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    sub_png_agt: list[PartyIdentification120ChoiceSeev03700116] = field(
        default_factory=list,
        metadata={
            "name": "SubPngAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )
    splmtry_data: list[SupplementaryData1Seev03700116] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16",
        },
    )


@dataclass
class Seev03700116(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.037.001.16"

    corp_actn_mvmnt_rvsl_advc: Optional[
        CorporateActionMovementReversalAdviceV16Seev03700116
    ] = field(
        default=None,
        metadata={
            "name": "CorpActnMvmntRvslAdvc",
            "type": "Element",
            "required": True,
        },
    )
