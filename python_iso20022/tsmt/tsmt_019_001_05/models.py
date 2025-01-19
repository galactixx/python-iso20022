from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AdjustmentDirection1Code, NamePrefix1Code
from python_iso20022.tsmt.enums import (
    AdjustmentType2Code,
    AssuredType1Code,
    BankRole1Code,
    ChargeType8Code,
    FreightCharges1Code,
    InsuranceClauses1Code,
    PaymentTime3Code,
    PaymentTime4Code,
    ProductCategory1Code,
    ProductCharacteristics1Code,
    ProductIdentifier2Code,
    TaxType9Code,
    TradeCertificateType1Code,
    TradeFinanceService2Code,
    UnitOfMeasure4Code,
)
from python_iso20022.tsmt.tsmt_019_001_05.enums import InstructionType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05"


@dataclass
class AccountSchemeName1ChoiceTsmt01900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountTsmt01900105(ISO20022MessageElement):
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
class AirportDescription1Tsmt01900105(ISO20022MessageElement):
    twn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Twn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    airprt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirprtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Bicidentification1Tsmt01900105(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class BpoapplicableRules1ChoiceTsmt01900105(ISO20022MessageElement):
    class Meta:
        name = "BPOApplicableRules1Choice"

    urbpovrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "URBPOVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    othr_rules_and_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRulesAndVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashAccountType2ChoiceTsmt01900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyAndAmountTsmt01900105(ISO20022MessageElement):
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
class DocumentIdentification7Tsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class GenericIdentification1Tsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Tsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Tsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Tsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class MultimodalTransport3Tsmt01900105(ISO20022MessageElement):
    takng_in_chrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "TakngInChrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_fnl_dstn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfFnlDstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PercentageTolerance1Tsmt01900105(ISO20022MessageElement):
    plus_pct: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlusPct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class PostalAddress2Tsmt01900105(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress5Tsmt01900105(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ShipmentDateRange1Tsmt01900105(ISO20022MessageElement):
    earlst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    latst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class ShipmentDateRange2Tsmt01900105(ISO20022MessageElement):
    sub_qty_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SubQtyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    earlst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    latst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransportByRail5Tsmt01900105(ISO20022MessageElement):
    plc_of_rct: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PlcOfRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_dlvry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PlcOfDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rail_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rail_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class TransportByRoad5Tsmt01900105(ISO20022MessageElement):
    plc_of_rct: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PlcOfRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_dlvry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PlcOfDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 35,
        },
    )
    road_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    road_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class TransportBySea6Tsmt01900105(ISO20022MessageElement):
    port_of_loadng: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PortOfLoadng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    port_of_dschrge: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PortOfDschrge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vssl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "VsslNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sea_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeaCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sea_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeaCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class UserDefinedInformation1Tsmt01900105(ISO20022MessageElement):
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AdjustmentType1ChoiceTsmt01900105(ISO20022MessageElement):
    tp: Optional[AdjustmentType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_adjstmnt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAdjstmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AirportName1ChoiceTsmt01900105(ISO20022MessageElement):
    airprt_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirprtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 6,
        },
    )
    othr_airprt_desc: Optional[AirportDescription1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "OthrAirprtDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class AmountOrPercentage2ChoiceTsmt01900105(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class Charges5Tsmt01900105(ISO20022MessageElement):
    chrgs_pyer: Optional[BankRole1Code] = field(
        default=None,
        metadata={
            "name": "ChrgsPyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    chrgs_pyee: Optional[BankRole1Code] = field(
        default=None,
        metadata={
            "name": "ChrgsPyee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    amt: Optional[CurrencyAndAmountTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ChargesType1ChoiceTsmt01900105(ISO20022MessageElement):
    tp: Optional[ChargeType8Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_chrgs_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrChrgsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContactIdentification1Tsmt01900105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class ContactIdentification3Tsmt01900105(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class CountrySubdivision1ChoiceTsmt01900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[GenericIdentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class DocumentIdentification1Tsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    submitr: Optional[Bicidentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class GenericAccountIdentification1Tsmt01900105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Incoterms4ChoiceTsmt01900105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification13Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class InstructionType1Tsmt01900105(ISO20022MessageElement):
    tp: Optional[InstructionType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class NameAndAddress6Tsmt01900105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class PartyIdentification26Tsmt01900105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pstl_adr: Optional[PostalAddress5Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class PartyIdentification27Tsmt01900105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PaymentPeriod3Tsmt01900105(ISO20022MessageElement):
    cd: Optional[PaymentTime3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class PaymentPeriod4Tsmt01900105(ISO20022MessageElement):
    cd: Optional[PaymentTime4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class ProductCategory1Tsmt01900105(ISO20022MessageElement):
    tp: Optional[ProductCategory1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductCharacteristics1Tsmt01900105(ISO20022MessageElement):
    tp: Optional[ProductCharacteristics1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    chrtcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductIdentifier2Tsmt01900105(ISO20022MessageElement):
    tp: Optional[ProductIdentifier2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RequiredSubmission2Tsmt01900105(ISO20022MessageElement):
    submitr: list[Bicidentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
        },
    )


@dataclass
class RequiredSubmission6Tsmt01900105(ISO20022MessageElement):
    submitr: list[Bicidentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
        },
    )
    cert_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    cert_tp_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertTpDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ShipmentSchedule2ChoiceTsmt01900105(ISO20022MessageElement):
    shipmnt_dt_rg: Optional[ShipmentDateRange1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "ShipmntDtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    shipmnt_sub_schdl: list[ShipmentDateRange2Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "ShipmntSubSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class TaxType2ChoiceTsmt01900105(ISO20022MessageElement):
    tp: Optional[TaxType9Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UnitOfMeasure3ChoiceTsmt01900105(ISO20022MessageElement):
    unit_of_measr_cd: Optional[UnitOfMeasure4Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification4ChoiceTsmt01900105(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class Adjustment7Tsmt01900105(ISO20022MessageElement):
    tp: Optional[AdjustmentType1ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    amt_or_pctg: Optional[AmountOrPercentage2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "AmtOrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    drctn: Optional[AdjustmentDirection1Code] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class BankContactPerson1ChoiceTsmt01900105(ISO20022MessageElement):
    buyr_bk_ctct_prsn: list[ContactIdentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "BuyrBkCtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    sellr_bk_ctct_prsn: list[ContactIdentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "SellrBkCtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class ChargesDetails3Tsmt01900105(ISO20022MessageElement):
    tp: Optional[ChargesType1ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    amt_or_pctg: Optional[AmountOrPercentage2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "AmtOrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class FinancialInstitutionIdentification4ChoiceTsmt01900105(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class Incoterms4Tsmt01900105(ISO20022MessageElement):
    incotrms_cd: Optional[Incoterms4ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "IncotrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Location2Tsmt01900105(ISO20022MessageElement):
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: Optional[CountrySubdivision1ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCodeOrOther1ChoiceTsmt01900105(ISO20022MessageElement):
    pmt_cd: Optional[PaymentPeriod3Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PmtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_pmt_terms: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class PaymentCodeOrOther2ChoiceTsmt01900105(ISO20022MessageElement):
    pmt_cd: Optional[PaymentPeriod4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PmtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_pmt_terms: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ProductCategory1ChoiceTsmt01900105(ISO20022MessageElement):
    strd_pdct_ctgy: Optional[ProductCategory1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "StrdPdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_pdct_ctgy: Optional[GenericIdentification4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "OthrPdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class ProductCharacteristics1ChoiceTsmt01900105(ISO20022MessageElement):
    strd_pdct_chrtcs: Optional[ProductCharacteristics1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "StrdPdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_pdct_chrtcs: Optional[GenericIdentification4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "OthrPdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class ProductIdentifier2ChoiceTsmt01900105(ISO20022MessageElement):
    strd_pdct_idr: Optional[ProductIdentifier2Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "StrdPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_pdct_idr: Optional[GenericIdentification4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "OthrPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class Quantity9Tsmt01900105(ISO20022MessageElement):
    unit_of_measr: Optional[UnitOfMeasure3ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[0-9]{1,15}",
        },
    )


@dataclass
class RequiredSubmission3Tsmt01900105(ISO20022MessageElement):
    submitr: list[Bicidentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
        },
    )
    mtch_issr: Optional[PartyIdentification27Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "MtchIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    mtch_isse_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtchIsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    mtch_trnsprt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtchTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    mtch_amt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtchAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    clauses_reqrd: list[InsuranceClauses1Code] = field(
        default_factory=list,
        metadata={
            "name": "ClausesReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    mtch_assrd_pty: Optional[AssuredType1Code] = field(
        default=None,
        metadata={
            "name": "MtchAssrdPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class RequiredSubmission4Tsmt01900105(ISO20022MessageElement):
    submitr: list[Bicidentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
        },
    )
    cert_tp: Optional[TradeCertificateType1Code] = field(
        default=None,
        metadata={
            "name": "CertTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    mtch_issr: Optional[PartyIdentification27Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "MtchIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    mtch_isse_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtchIsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    mtch_inspctn_dt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtchInspctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    authrsd_inspctr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AuthrsdInspctrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    mtch_consgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MtchConsgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    mtch_manfctr: Optional[PartyIdentification27Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "MtchManfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    line_itm_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LineItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Tax23Tsmt01900105(ISO20022MessageElement):
    tp: Optional[TaxType2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    amt_or_pctg: Optional[AmountOrPercentage2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "AmtOrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class TransportByAir5Tsmt01900105(ISO20022MessageElement):
    dprture_airprt: list[AirportName1ChoiceTsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "DprtureAirprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    dstn_airprt: list[AirportName1ChoiceTsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "DstnAirprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
        },
    )
    air_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    air_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class UnitPrice18Tsmt01900105(ISO20022MessageElement):
    unit_pric: Optional[UnitOfMeasure3ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    amt: Optional[CurrencyAndAmountTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    fctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[0-9]{1,15}",
        },
    )


@dataclass
class CashAccount24Tsmt01900105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Charge24Tsmt01900105(ISO20022MessageElement):
    tp: Optional[FreightCharges1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    chrgs: list[ChargesDetails3Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class PaymentTerms4Tsmt01900105(ISO20022MessageElement):
    pmt_terms: Optional[PaymentCodeOrOther1ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "PmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    amt_or_pctg: Optional[AmountOrPercentage2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "AmtOrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class PaymentTerms5Tsmt01900105(ISO20022MessageElement):
    pmt_terms: Optional[PaymentCodeOrOther2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "PmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    amt_or_pctg: Optional[AmountOrPercentage2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "AmtOrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class SingleTransport7Tsmt01900105(ISO20022MessageElement):
    trnsprt_by_air: list[TransportByAir5Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtByAir",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    trnsprt_by_sea: list[TransportBySea6Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtBySea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    trnsprt_by_road: list[TransportByRoad5Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtByRoad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    trnsprt_by_rail: list[TransportByRail5Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtByRail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class SettlementTerms3Tsmt01900105(ISO20022MessageElement):
    cdtr_agt: Optional[FinancialInstitutionIdentification4ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    cdtr_acct: Optional[CashAccount24Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class TransportMeans5Tsmt01900105(ISO20022MessageElement):
    indv_trnsprt: Optional[SingleTransport7Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "IndvTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    mltmdl_trnsprt: Optional[MultimodalTransport3Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "MltmdlTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class LineItemDetails13Tsmt01900105(ISO20022MessageElement):
    line_itm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    qty: Optional[Quantity9Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    qty_tlrnce: Optional[PercentageTolerance1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "QtyTlrnce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    unit_pric: Optional[UnitPrice18Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pric_tlrnce: Optional[PercentageTolerance1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PricTlrnce",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pdct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_idr: list[ProductIdentifier2ChoiceTsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "PdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pdct_chrtcs: list[ProductCharacteristics1ChoiceTsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "PdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pdct_ctgy: list[ProductCategory1ChoiceTsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "PdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pdct_orgn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PdctOrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    shipmnt_schdl: Optional[ShipmentSchedule2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "ShipmntSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    rtg_summry: Optional[TransportMeans5Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "RtgSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    adjstmnt: list[Adjustment7Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    frght_chrgs: Optional[Charge24Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "FrghtChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    tax: list[Tax23Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    ttl_amt: Optional[CurrencyAndAmountTsmt01900105] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    incotrms: Optional[Incoterms4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Incotrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class PaymentObligation2Tsmt01900105(ISO20022MessageElement):
    oblgr_bk: Optional[Bicidentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "OblgrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    rcpt_bk: Optional[Bicidentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "RcptBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    pmt_oblgtn_amt: Optional[AmountOrPercentage2ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "PmtOblgtnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    chrgs: list[Charges5Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    aplbl_rules: Optional[BpoapplicableRules1ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "AplblRules",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    aplbl_law: Optional[str] = field(
        default=None,
        metadata={
            "name": "AplblLaw",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    plc_of_jursdctn: Optional[Location2Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PlcOfJursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pmt_terms: list[PaymentTerms4Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "PmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    sttlm_terms: Optional[SettlementTerms3Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "SttlmTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class LineItem13Tsmt01900105(ISO20022MessageElement):
    goods_and_or_svcs_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsAndOrSvcsDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtl_shipmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtlShipmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    trns_shipmnt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrnsShipmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    shipmnt_dt_rg: Optional[ShipmentDateRange1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "ShipmntDtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    line_itm_dtls: list[LineItemDetails13Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "LineItmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
        },
    )
    line_itms_ttl_amt: Optional[CurrencyAndAmountTsmt01900105] = field(
        default=None,
        metadata={
            "name": "LineItmsTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    rtg_summry: Optional[TransportMeans5Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "RtgSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    incotrms: Optional[Incoterms4Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Incotrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    adjstmnt: list[Adjustment7Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    frght_chrgs: Optional[Charge24Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "FrghtChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    tax: list[Tax23Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    ttl_net_amt: Optional[CurrencyAndAmountTsmt01900105] = field(
        default=None,
        metadata={
            "name": "TtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    buyr_dfnd_inf: list[UserDefinedInformation1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "BuyrDfndInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    sellr_dfnd_inf: list[UserDefinedInformation1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "SellrDfndInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class Baseline5Tsmt01900105(ISO20022MessageElement):
    submitr_baseln_id: Optional[DocumentIdentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "SubmitrBaselnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    svc_cd: Optional[TradeFinanceService2Code] = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    buyr: Optional[PartyIdentification26Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification26Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    buyr_bk: Optional[Bicidentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "BuyrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    sellr_bk: Optional[Bicidentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "SellrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    buyr_sd_submitg_bk: list[Bicidentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "BuyrSdSubmitgBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    sellr_sd_submitg_bk: list[Bicidentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "SellrSdSubmitgBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    bll_to: Optional[PartyIdentification26Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "BllTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    ship_to: Optional[PartyIdentification26Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "ShipTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    consgn: Optional[PartyIdentification26Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Consgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    goods: Optional[LineItem13Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Goods",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    pmt_terms: list[PaymentTerms5Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "PmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "min_occurs": 1,
        },
    )
    sttlm_terms: Optional[SettlementTerms3Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "SttlmTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    pmt_oblgtn: list[PaymentObligation2Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "PmtOblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    latst_mtch_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatstMtchDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    comrcl_data_set_reqrd: Optional[RequiredSubmission2Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "ComrclDataSetReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    trnsprt_data_set_reqrd: Optional[RequiredSubmission2Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "TrnsprtDataSetReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    insrnc_data_set_reqrd: Optional[RequiredSubmission3Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "InsrncDataSetReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    cert_data_set_reqrd: list[RequiredSubmission4Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "CertDataSetReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    othr_cert_data_set_reqrd: list[RequiredSubmission6Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "OthrCertDataSetReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    intt_to_pay_xpctd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InttToPayXpctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )


@dataclass
class InitialBaselineSubmissionV05Tsmt01900105(ISO20022MessageElement):
    submissn_id: Optional[MessageIdentification1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "SubmissnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[SimpleIdentificationInformationTsmt01900105] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    instr: Optional[InstructionType1Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Instr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    baseln: Optional[Baseline5Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "Baseln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    buyr_ctct_prsn: list[ContactIdentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "BuyrCtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    sellr_ctct_prsn: list[ContactIdentification1Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "SellrCtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )
    bk_ctct_prsn: Optional[BankContactPerson1ChoiceTsmt01900105] = field(
        default=None,
        metadata={
            "name": "BkCtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
            "required": True,
        },
    )
    othr_bk_ctct_prsn: list[ContactIdentification3Tsmt01900105] = field(
        default_factory=list,
        metadata={
            "name": "OthrBkCtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05",
        },
    )


@dataclass
class Tsmt01900105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.019.001.05"

    initl_baseln_submissn: Optional[InitialBaselineSubmissionV05Tsmt01900105] = field(
        default=None,
        metadata={
            "name": "InitlBaselnSubmissn",
            "type": "Element",
            "required": True,
        },
    )
