from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    DateType1Code,
    DateType8Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    TypeOfIdentification1Code,
)
from python_iso20022.seev.enums import (
    CorporateActionEventType39Code,
    CorporateActionOption11Code,
    WithholdingTaxRateType1Code,
)
from python_iso20022.seev.seev_050_001_03.enums import (
    MarketClaimType1Code,
    TransferOfProceedsType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev05000103(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
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
class ActiveCurrencyAndAmountSeev05000103(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSeev05000103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class FinancialInstrumentQuantity18ChoiceSeev05000103(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceSeev05000103(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification30Seev05000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Seev05000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev05000103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev05000103(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class References25Seev05000103(ISO20022MessageElement):
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev05000103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BlockChainAddressWallet3Seev05000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Seev05000103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CorporateAction59Seev05000103(ISO20022MessageElement):
    rcrd_dt: Optional[DateAndDateTime2ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "RcrdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    ex_dvdd_dt: Optional[DateAndDateTime2ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "ExDvddDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class CorporateActionEventType111ChoiceSeev05000103(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType39Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class CorporateActionOption30ChoiceSeev05000103(ISO20022MessageElement):
    cd: Optional[CorporateActionOption11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class DateCode19ChoiceSeev05000103(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class DateFormat58ChoiceSeev05000103(ISO20022MessageElement):
    dt_or_dt_tm: Optional[DateAndDateTime2ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "DtOrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    dt_cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class GenericIdentification78Seev05000103(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Seev05000103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSeev05000103(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class OtherIdentification1Seev05000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSeev05000103(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev05000103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class PostalAddress1Seev05000103(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ProceedsQuantityBreakdown1Seev05000103(ISO20022MessageElement):
    trf_of_rcvd_prcds_qty: Optional[FinancialInstrumentQuantity18ChoiceSeev05000103] = (
        field(
            default=None,
            metadata={
                "name": "TrfOfRcvdPrcdsQty",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            },
        )
    )
    csh_compstn_qty: Optional[FinancialInstrumentQuantity18ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "CshCompstnQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class Quantity6ChoiceSeev05000103(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity1ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev05000103] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class RateType42ChoiceSeev05000103(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Seev05000103(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Seev05000103(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Seev05000103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev05000103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )


@dataclass
class AlternatePartyIdentification7Seev05000103(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSeev05000103(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Seev05000103] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class DateFormat43ChoiceSeev05000103(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class NameAndAddress5Seev05000103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev05000103] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class RateTypeAndPercentageRate12Seev05000103(ISO20022MessageElement):
    rate_tp: Optional[RateType42ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RelatedSettlementInstruction2Seev05000103(ISO20022MessageElement):
    rltd_sttlm_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RltdSttlmInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rltd_sttlm_qty: Optional[FinancialInstrumentQuantity18ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "RltdSttlmQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    trf_of_prcds_tp_ind: Optional[TransferOfProceedsType1Code] = field(
        default=None,
        metadata={
            "name": "TrfOfPrcdsTpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prcds_qty_brkdwn: Optional[ProceedsQuantityBreakdown1Seev05000103] = field(
        default=None,
        metadata={
            "name": "PrcdsQtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class SafekeepingPlaceFormat42ChoiceSeev05000103(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Seev05000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Seev05000103] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    prtry: Optional[GenericIdentification78Seev05000103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class SecurityIdentification19Seev05000103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev05000103] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AccountIdentification70Seev05000103(ISO20022MessageElement):
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_ownr: Optional[PartyIdentification127ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat42ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class CorporateActionGeneralInformation181Seev05000103(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType111ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev05000103] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class PartyIdentification120ChoiceSeev05000103(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Seev05000103] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev05000103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class PartyIdentification257ChoiceSeev05000103(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev05000103] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dgtl_ldgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DgtlLdgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "pattern": r"[1-9B-DF-HJ-NP-TV-XZ][0-9B-DF-HJ-NP-TV-XZ]{8,8}",
        },
    )


@dataclass
class RateAndAmountFormat55ChoiceSeev05000103(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev05000103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate12Seev05000103] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class SecuritiesOption76Seev05000103(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev05000103] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    entitld_qty: Optional[Quantity6ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "EntitldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    pmt_dt: Optional[DateFormat58ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )


@dataclass
class CashOption106Seev05000103(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    csh_acct_id: Optional[CashAccountIdentification9ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    grss_csh_amt: Optional[ActiveCurrencyAndAmountSeev05000103] = field(
        default=None,
        metadata={
            "name": "GrssCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    net_csh_amt: Optional[ActiveCurrencyAndAmountSeev05000103] = field(
        default=None,
        metadata={
            "name": "NetCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    entitld_amt: Optional[ActiveCurrencyAndAmountSeev05000103] = field(
        default=None,
        metadata={
            "name": "EntitldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat55ChoiceSeev05000103] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev05000103] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    earlst_pmt_dt: Optional[DateAndDateTime2ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    pmt_dt: Optional[DateFormat43ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )


@dataclass
class PartyIdentification316Seev05000103(ISO20022MessageElement):
    id: Optional[PartyIdentification257ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: list[AlternatePartyIdentification7Seev05000103] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class PartyIdentificationAndAccount163Seev05000103(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    sfkpg_acct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    altrn_id: list[AlternatePartyIdentification7Seev05000103] = field(
        default_factory=list,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class CorporateActionOption234Seev05000103(ISO20022MessageElement):
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption30ChoiceSeev05000103] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption76Seev05000103] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    csh_mvmnt_dtls: list[CashOption106Seev05000103] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class SettlementParties123Seev05000103(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification316Seev05000103] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount163Seev05000103] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount163Seev05000103] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount163Seev05000103] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class SettlementParties124Seev05000103(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification316Seev05000103] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    pty1: Optional[PartyIdentificationAndAccount163Seev05000103] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    pty2: Optional[PartyIdentificationAndAccount163Seev05000103] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount163Seev05000103] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class MarketClaimCreationV03Seev05000103(ISO20022MessageElement):
    tx_ref: Optional[References25Seev05000103] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation181Seev05000103] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
                "required": True,
            },
        )
    )
    rltd_sttlm_instr_dtls: Optional[RelatedSettlementInstruction2Seev05000103] = field(
        default=None,
        metadata={
            "name": "RltdSttlmInstrDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    acct_dtls: Optional[AccountIdentification70Seev05000103] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    corp_actn_dtls: Optional[CorporateAction59Seev05000103] = field(
        default=None,
        metadata={
            "name": "CorpActnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    mkt_clm_tp: Optional[MarketClaimType1Code] = field(
        default=None,
        metadata={
            "name": "MktClmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    mkt_clm_dtls: Optional[CorporateActionOption234Seev05000103] = field(
        default=None,
        metadata={
            "name": "MktClmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
            "required": True,
        },
    )
    dlvrg_sttlm_pties: Optional[SettlementParties123Seev05000103] = field(
        default=None,
        metadata={
            "name": "DlvrgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    rcvg_sttlm_pties: Optional[SettlementParties124Seev05000103] = field(
        default=None,
        metadata={
            "name": "RcvgSttlmPties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Seev05000103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03",
        },
    )


@dataclass
class Seev05000103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03"

    mkt_clm_cre: Optional[MarketClaimCreationV03Seev05000103] = field(
        default=None,
        metadata={
            "name": "MktClmCre",
            "type": "Element",
            "required": True,
        },
    )
