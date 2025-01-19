from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.tsmt.enums import (
    Action2Code,
    BaselineStatus3Code,
    ProductCategory1Code,
    ProductCharacteristics1Code,
    ProductIdentifier2Code,
    UnitOfMeasure4Code,
)
from python_iso20022.tsmt.tsmt_011_001_04.enums import ReportType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04"


@dataclass
class Bicidentification1Tsmt01100104(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class CurrencyAndAmountTsmt01100104(ISO20022MessageElement):
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
class DocumentIdentification6Tsmt01100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    amdmnt_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmdmntSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )


@dataclass
class GenericIdentification4Tsmt01100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Tsmt01100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )


@dataclass
class PercentageTolerance1Tsmt01100104(ISO20022MessageElement):
    plus_pct: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlusPct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    mns_pct: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MnsPct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class PostalAddress5Tsmt01100104(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt01100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification5Tsmt01100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_issr: Optional[Bicidentification1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "IdIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )


@dataclass
class PartyIdentification26Tsmt01100104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    pstl_adr: Optional[PostalAddress5Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )


@dataclass
class PendingActivity2Tsmt01100104(ISO20022MessageElement):
    tp: Optional[Action2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ProductCategory1Tsmt01100104(ISO20022MessageElement):
    tp: Optional[ProductCategory1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductCharacteristics1Tsmt01100104(ISO20022MessageElement):
    tp: Optional[ProductCharacteristics1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    chrtcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductIdentifier2Tsmt01100104(ISO20022MessageElement):
    tp: Optional[ProductIdentifier2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ReportType2Tsmt01100104(ISO20022MessageElement):
    tp: Optional[ReportType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )


@dataclass
class TransactionStatus4Tsmt01100104(ISO20022MessageElement):
    sts: Optional[BaselineStatus3Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )


@dataclass
class UnitOfMeasure3ChoiceTsmt01100104(ISO20022MessageElement):
    unit_of_measr_cd: Optional[UnitOfMeasure4Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductCategory1ChoiceTsmt01100104(ISO20022MessageElement):
    strd_pdct_ctgy: Optional[ProductCategory1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "StrdPdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    othr_pdct_ctgy: Optional[GenericIdentification4Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "OthrPdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )


@dataclass
class ProductCharacteristics1ChoiceTsmt01100104(ISO20022MessageElement):
    strd_pdct_chrtcs: Optional[ProductCharacteristics1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "StrdPdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    othr_pdct_chrtcs: Optional[GenericIdentification4Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "OthrPdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )


@dataclass
class ProductIdentifier2ChoiceTsmt01100104(ISO20022MessageElement):
    strd_pdct_idr: Optional[ProductIdentifier2Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "StrdPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    othr_pdct_idr: Optional[GenericIdentification4Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "OthrPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )


@dataclass
class Quantity9Tsmt01100104(ISO20022MessageElement):
    unit_of_measr: Optional[UnitOfMeasure3ChoiceTsmt01100104] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    fctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "pattern": r"[0-9]{1,15}",
        },
    )


@dataclass
class LineItemDetails12Tsmt01100104(ISO20022MessageElement):
    line_itm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_idr: list[ProductIdentifier2ChoiceTsmt01100104] = field(
        default_factory=list,
        metadata={
            "name": "PdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    pdct_chrtcs: list[ProductCharacteristics1ChoiceTsmt01100104] = field(
        default_factory=list,
        metadata={
            "name": "PdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    pdct_ctgy: list[ProductCategory1ChoiceTsmt01100104] = field(
        default_factory=list,
        metadata={
            "name": "PdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    ordrd_qty: Optional[Quantity9Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "OrdrdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    accptd_qty: Optional[Quantity9Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "AccptdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    outsdng_qty: Optional[Quantity9Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "OutsdngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    pdg_qty: Optional[Quantity9Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "PdgQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    qty_tlrnce: Optional[PercentageTolerance1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "QtyTlrnce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    ordrd_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "OrdrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    accptd_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "AccptdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    outsdng_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "OutsdngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    pdg_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "PdgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    pric_tlrnce: Optional[PercentageTolerance1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "PricTlrnce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )


@dataclass
class LineItem14Tsmt01100104(ISO20022MessageElement):
    line_itm_dtls: list[LineItemDetails12Tsmt01100104] = field(
        default_factory=list,
        metadata={
            "name": "LineItmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "min_occurs": 1,
        },
    )
    ordrd_line_itms_ttl_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "OrdrdLineItmsTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    accptd_line_itms_ttl_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "AccptdLineItmsTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    outsdng_line_itms_ttl_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "OutsdngLineItmsTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    pdg_line_itms_ttl_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "PdgLineItmsTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    ordrd_ttl_net_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "OrdrdTtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    accptd_ttl_net_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "AccptdTtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    outsdng_ttl_net_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "OutsdngTtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    pdg_ttl_net_amt: Optional[CurrencyAndAmountTsmt01100104] = field(
        default=None,
        metadata={
            "name": "PdgTtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )


@dataclass
class BaselineReportV04Tsmt01100104(ISO20022MessageElement):
    rpt_id: Optional[MessageIdentification1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    rltd_msg_ref: Optional[MessageIdentification1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "RltdMsgRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )
    rpt_tp: Optional[ReportType2Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "RptTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    tx_id: Optional[SimpleIdentificationInformationTsmt01100104] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    estblishd_baseln_id: Optional[DocumentIdentification6Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "EstblishdBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    tx_sts: Optional[TransactionStatus4Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "TxSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    usr_tx_ref: list[DocumentIdentification5Tsmt01100104] = field(
        default_factory=list,
        metadata={
            "name": "UsrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "max_occurs": 2,
        },
    )
    buyr: Optional[PartyIdentification26Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification26Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    buyr_bk: Optional[Bicidentification1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "BuyrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    sellr_bk: Optional[Bicidentification1Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "SellrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    rptd_line_itm: Optional[LineItem14Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "RptdLineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
            "required": True,
        },
    )
    req_for_actn: Optional[PendingActivity2Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "ReqForActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04",
        },
    )


@dataclass
class Tsmt01100104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.011.001.04"

    baseln_rpt: Optional[BaselineReportV04Tsmt01100104] = field(
        default=None,
        metadata={
            "name": "BaselnRpt",
            "type": "Element",
            "required": True,
        },
    )
