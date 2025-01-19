from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AdjustmentDirection1Code
from python_iso20022.tsmt.enums import (
    AdjustmentType2Code,
    ChargeType8Code,
    FreightCharges1Code,
    InstructionType3Code,
    InsuranceClauses1Code,
    PaymentTime3Code,
    ProductCategory1Code,
    ProductCharacteristics1Code,
    ProductIdentifier2Code,
    TaxType9Code,
    TradeCertificateType1Code,
    UnitOfMeasure4Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05"


@dataclass
class AccountSchemeName1ChoiceTsmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountTsmt01400105(ISO20022MessageElement):
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
class AirportDescription1Tsmt01400105(ISO20022MessageElement):
    twn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Twn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Bicidentification1Tsmt01400105(ISO20022MessageElement):
    class Meta:
        name = "BICIdentification1"

    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class CashAccountType2ChoiceTsmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CurrencyAndAmountTsmt01400105(ISO20022MessageElement):
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
class DatePeriodDetailsTsmt01400105(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification7Tsmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class GenericIdentification13Tsmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification4Tsmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InvoiceIdentification1Tsmt01400105(ISO20022MessageElement):
    invc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvcNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class MessageIdentification1Tsmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class MultimodalTransport3Tsmt01400105(ISO20022MessageElement):
    takng_in_chrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "TakngInChrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress2Tsmt01400105(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PostalAddress5Tsmt01400105(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ShipmentDate1ChoiceTsmt01400105(ISO20022MessageElement):
    propsd_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PropsdShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    actl_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ActlShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class SimpleIdentificationInformationTsmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransportByRail2Tsmt01400105(ISO20022MessageElement):
    plc_of_rct: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_dlvry: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rail_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransportByRail4Tsmt01400105(ISO20022MessageElement):
    plc_of_rct: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_dlvry: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rail_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    rail_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RailCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class TransportByRoad2Tsmt01400105(ISO20022MessageElement):
    plc_of_rct: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_dlvry: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    road_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransportByRoad4Tsmt01400105(ISO20022MessageElement):
    plc_of_rct: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfRct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    plc_of_dlvry: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfDlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    road_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    road_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class TransportBySea4Tsmt01400105(ISO20022MessageElement):
    port_of_loadng: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortOfLoadng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    port_of_dschrge: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortOfDschrge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vssl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "VsslNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sea_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeaCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransportBySea5Tsmt01400105(ISO20022MessageElement):
    port_of_loadng: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortOfLoadng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    port_of_dschrge: Optional[str] = field(
        default=None,
        metadata={
            "name": "PortOfDschrge",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vssl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "VsslNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sea_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeaCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sea_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeaCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    mstr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    chrtrr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChrtrrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    ownr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    imonb: Optional[str] = field(
        default=None,
        metadata={
            "name": "IMONb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[0-9]{7}",
        },
    )
    vyg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "VygNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class UserDefinedInformation1Tsmt01400105(ISO20022MessageElement):
    labl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Labl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AdjustmentType1ChoiceTsmt01400105(ISO20022MessageElement):
    tp: Optional[AdjustmentType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_adjstmnt_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAdjstmntTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AirportName1ChoiceTsmt01400105(ISO20022MessageElement):
    airprt_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirprtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 6,
        },
    )
    othr_airprt_desc: Optional[AirportDescription1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "OthrAirprtDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class AmountOrPercentage2ChoiceTsmt01400105(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    pctg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Pctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class ChargesType1ChoiceTsmt01400105(ISO20022MessageElement):
    tp: Optional[ChargeType8Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_chrgs_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrChrgsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DataSetSubmissionReferences3Tsmt01400105(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    submitr_tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubmitrTxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    forcd_mtch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForcdMtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification1Tsmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    submitr: Optional[Bicidentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Submitr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class GenericAccountIdentification1Tsmt01400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Incoterms4ChoiceTsmt01400105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification13Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class InstructionType3Tsmt01400105(ISO20022MessageElement):
    tp: Optional[InstructionType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class LineItemAndPoidentification1Tsmt01400105(ISO20022MessageElement):
    class Meta:
        name = "LineItemAndPOIdentification1"

    line_itm_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LineItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 70,
        },
    )
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class NameAndAddress6Tsmt01400105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class PartyIdentification26Tsmt01400105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    prtry_id: Optional[GenericIdentification4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    pstl_adr: Optional[PostalAddress5Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class PaymentPeriod3Tsmt01400105(ISO20022MessageElement):
    cd: Optional[PaymentTime3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    nb_of_days: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDays",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class ProductCategory1Tsmt01400105(ISO20022MessageElement):
    tp: Optional[ProductCategory1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    ctgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductCharacteristics1Tsmt01400105(ISO20022MessageElement):
    tp: Optional[ProductCharacteristics1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    chrtcs: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductIdentifier2Tsmt01400105(ISO20022MessageElement):
    tp: Optional[ProductIdentifier2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TaxType2ChoiceTsmt01400105(ISO20022MessageElement):
    tp: Optional[TaxType9Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransportedGoods1Tsmt01400105(ISO20022MessageElement):
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    goods_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    buyr_dfnd_inf: list[UserDefinedInformation1Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "BuyrDfndInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    sellr_dfnd_inf: list[UserDefinedInformation1Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "SellrDfndInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class UnitOfMeasure3ChoiceTsmt01400105(ISO20022MessageElement):
    unit_of_measr_cd: Optional[UnitOfMeasure4Code] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_unit_of_measr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrUnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AccountIdentification4ChoiceTsmt01400105(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class Adjustment6Tsmt01400105(ISO20022MessageElement):
    tp: Optional[AdjustmentType1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    drctn: Optional[AdjustmentDirection1Code] = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class ChargesDetails4Tsmt01400105(ISO20022MessageElement):
    chrgs_tp: Optional[ChargesType1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "ChrgsTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class FinancialInstitutionIdentification4ChoiceTsmt01400105(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class Incoterms4Tsmt01400105(ISO20022MessageElement):
    incotrms_cd: Optional[Incoterms4ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "IncotrmsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    lctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class OtherCertificateDataSet2Tsmt01400105(ISO20022MessageElement):
    data_set_id: Optional[DocumentIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    issr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    cert_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CertInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PartyIdentification29ChoiceTsmt01400105(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class PaymentCodeOrOther1ChoiceTsmt01400105(ISO20022MessageElement):
    pmt_cd: Optional[PaymentPeriod3Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PmtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    pmt_due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PmtDueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_pmt_terms: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrPmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ProductCategory1ChoiceTsmt01400105(ISO20022MessageElement):
    strd_pdct_ctgy: Optional[ProductCategory1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "StrdPdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_pdct_ctgy: Optional[GenericIdentification4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "OthrPdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class ProductCharacteristics1ChoiceTsmt01400105(ISO20022MessageElement):
    strd_pdct_chrtcs: Optional[ProductCharacteristics1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "StrdPdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_pdct_chrtcs: Optional[GenericIdentification4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "OthrPdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class ProductIdentifier2ChoiceTsmt01400105(ISO20022MessageElement):
    strd_pdct_idr: Optional[ProductIdentifier2Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "StrdPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_pdct_idr: Optional[GenericIdentification4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "OthrPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class Quantity10Tsmt01400105(ISO20022MessageElement):
    unit_of_measr: Optional[UnitOfMeasure3ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class Quantity9Tsmt01400105(ISO20022MessageElement):
    unit_of_measr: Optional[UnitOfMeasure3ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[0-9]{1,15}",
        },
    )


@dataclass
class Tax22Tsmt01400105(ISO20022MessageElement):
    tp: Optional[TaxType2ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class TransportByAir2Tsmt01400105(ISO20022MessageElement):
    dprture_airprt: Optional[AirportName1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "DprtureAirprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    dstn_airprt: Optional[AirportName1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "DstnAirprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    air_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransportByAir4Tsmt01400105(ISO20022MessageElement):
    dprture_airprt: Optional[AirportName1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "DprtureAirprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    dstn_airprt: Optional[AirportName1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "DstnAirprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    flght_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlghtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    air_crrier_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirCrrierNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    air_crrier_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "AirCrrierCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    crrier_agt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    crrier_agt_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrrierAgtCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class UnitPrice18Tsmt01400105(ISO20022MessageElement):
    unit_pric: Optional[UnitOfMeasure3ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    fctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[0-9]{1,15}",
        },
    )


@dataclass
class CashAccount24Tsmt01400105(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    tp: Optional[CashAccountType2ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CertifiedCharacteristics2ChoiceTsmt01400105(ISO20022MessageElement):
    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    qlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Qlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    anlys: Optional[str] = field(
        default=None,
        metadata={
            "name": "Anlys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    wght: Optional[Quantity9Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Wght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    qty: Optional[Quantity9Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    hlth_indctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HlthIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    phytosntry_indctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PhytosntryIndctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class Charge25Tsmt01400105(ISO20022MessageElement):
    tp: Optional[FreightCharges1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    chrgs: list[ChargesDetails4Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Chrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class Consignment3Tsmt01400105(ISO20022MessageElement):
    ttl_qty: Optional[Quantity10Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TtlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    ttl_vol: Optional[Quantity10Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TtlVol",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    ttl_wght: Optional[Quantity10Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TtlWght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class PaymentTerms4Tsmt01400105(ISO20022MessageElement):
    pmt_terms: Optional[PaymentCodeOrOther1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "PmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    amt_or_pctg: Optional[AmountOrPercentage2ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "AmtOrPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class SingleTransport3Tsmt01400105(ISO20022MessageElement):
    trnsprt_by_air: Optional[TransportByAir2Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TrnsprtByAir",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_by_sea: Optional[TransportBySea4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TrnsprtBySea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_by_road: Optional[TransportByRoad2Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TrnsprtByRoad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_by_rail: Optional[TransportByRail2Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TrnsprtByRail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class SingleTransport8Tsmt01400105(ISO20022MessageElement):
    trnsprt_by_air: list[TransportByAir4Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtByAir",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_by_sea: list[TransportBySea5Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtBySea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_by_road: list[TransportByRoad4Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtByRoad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_by_rail: list[TransportByRail4Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtByRail",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class CertificateDataSet2Tsmt01400105(ISO20022MessageElement):
    data_set_id: Optional[DocumentIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    cert_tp: Optional[TradeCertificateType1Code] = field(
        default=None,
        metadata={
            "name": "CertTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    line_itm: list[LineItemAndPoidentification1Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "LineItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    certfd_chrtcs: Optional[CertifiedCharacteristics2ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "CertfdChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    plc_of_isse: Optional[PostalAddress5Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PlcOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    issr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    inspctn_dt: Optional[DatePeriodDetailsTsmt01400105] = field(
        default=None,
        metadata={
            "name": "InspctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    authrsd_inspctr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AuthrsdInspctrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    cert_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    trnsprt: Optional[SingleTransport3Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Trnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    goods_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "GoodsDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    consgnr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Consgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    consgn: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Consgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    manfctr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class InsuranceDataSet1Tsmt01400105(ISO20022MessageElement):
    data_set_id: Optional[DocumentIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    issr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    fctv_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    plc_of_isse: Optional[PostalAddress5Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PlcOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    insrnc_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InsrncDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    trnsprt: Optional[SingleTransport3Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Trnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    insrd_amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "InsrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    insrd_goods_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "InsrdGoodsDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    insrnc_conds: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InsrncConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    insrnc_clauses: list[InsuranceClauses1Code] = field(
        default_factory=list,
        metadata={
            "name": "InsrncClauses",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    assrd: Optional[PartyIdentification29ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "Assrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    clms_pybl_at: Optional[PostalAddress5Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "ClmsPyblAt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    clms_pybl_in: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClmsPyblIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class LineItemDetails14Tsmt01400105(ISO20022MessageElement):
    line_itm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    qty: Optional[Quantity9Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    unit_pric: Optional[UnitPrice18Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "UnitPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    pdct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pdct_idr: list[ProductIdentifier2ChoiceTsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "PdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    pdct_chrtcs: list[ProductCharacteristics1ChoiceTsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "PdctChrtcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    pdct_ctgy: list[ProductCategory1ChoiceTsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "PdctCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    pdct_orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctOrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adjstmnt: list[Adjustment6Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    frght_chrgs: Optional[Charge25Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "FrghtChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    tax: list[Tax22Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    ttl_amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class SettlementTerms3Tsmt01400105(ISO20022MessageElement):
    cdtr_agt: Optional[FinancialInstitutionIdentification4ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "CdtrAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    cdtr_acct: Optional[CashAccount24Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "CdtrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class TransportMeans6Tsmt01400105(ISO20022MessageElement):
    indv_trnsprt: Optional[SingleTransport8Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "IndvTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    mltmdl_trnsprt: Optional[MultimodalTransport3Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "MltmdlTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class LineItem15Tsmt01400105(ISO20022MessageElement):
    purchs_ordr_ref: Optional[DocumentIdentification7Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "PurchsOrdrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    fnl_submissn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FnlSubmissn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    comrcl_line_itms: list[LineItemDetails14Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "ComrclLineItms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_occurs": 1,
        },
    )
    line_itms_ttl_amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "LineItmsTtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    adjstmnt: list[Adjustment6Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Adjstmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    frght_chrgs: Optional[Charge25Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "FrghtChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    tax: list[Tax22Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    ttl_net_amt: Optional[CurrencyAndAmountTsmt01400105] = field(
        default=None,
        metadata={
            "name": "TtlNetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    buyr_dfnd_inf: list[UserDefinedInformation1Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "BuyrDfndInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    sellr_dfnd_inf: list[UserDefinedInformation1Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "SellrDfndInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    incotrms: Optional[Incoterms4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Incotrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class TransportDetails4Tsmt01400105(ISO20022MessageElement):
    trnsprt_doc_ref: list[DocumentIdentification7Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtDocRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_occurs": 1,
        },
    )
    trnsprtd_goods: list[TransportedGoods1Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "TrnsprtdGoods",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_occurs": 1,
        },
    )
    consgnmt: Optional[Consignment3Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Consgnmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    rtg_summry: Optional[TransportMeans6Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "RtgSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    shipmnt_dt: Optional[ShipmentDate1ChoiceTsmt01400105] = field(
        default=None,
        metadata={
            "name": "ShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    frght_chrgs: Optional[Charge25Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "FrghtChrgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    incotrms: Optional[Incoterms4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Incotrms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class CommercialDataSet5Tsmt01400105(ISO20022MessageElement):
    data_set_id: Optional[DocumentIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    comrcl_doc_ref: Optional[InvoiceIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "ComrclDocRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    buyr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    sellr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    bll_to: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "BllTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    goods: list[LineItem15Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "Goods",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_occurs": 1,
        },
    )
    pmt_terms: list[PaymentTerms4Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "PmtTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_occurs": 1,
        },
    )
    sttlm_terms: Optional[SettlementTerms3Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "SttlmTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class TransportDataSet5Tsmt01400105(ISO20022MessageElement):
    data_set_id: Optional[DocumentIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "DataSetId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    buyr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    sellr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    consgnr: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Consgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    consgn: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Consgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    ship_to: Optional[PartyIdentification26Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "ShipTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_inf: Optional[TransportDetails4Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TrnsprtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )


@dataclass
class DataSetSubmissionV05Tsmt01400105(ISO20022MessageElement):
    submissn_id: Optional[MessageIdentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "SubmissnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    rltd_tx_refs: list[DataSetSubmissionReferences3Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "RltdTxRefs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "min_occurs": 1,
        },
    )
    cmon_submissn_ref: Optional[SimpleIdentificationInformationTsmt01400105] = field(
        default=None,
        metadata={
            "name": "CmonSubmissnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    instr: Optional[InstructionType3Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "Instr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    buyr_bk: Optional[Bicidentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "BuyrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    sellr_bk: Optional[Bicidentification1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "SellrBk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
            "required": True,
        },
    )
    comrcl_data_set: Optional[CommercialDataSet5Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "ComrclDataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    trnsprt_data_set: Optional[TransportDataSet5Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "TrnsprtDataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    insrnc_data_set: Optional[InsuranceDataSet1Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "InsrncDataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    cert_data_set: list[CertificateDataSet2Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "CertDataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )
    othr_cert_data_set: list[OtherCertificateDataSet2Tsmt01400105] = field(
        default_factory=list,
        metadata={
            "name": "OthrCertDataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05",
        },
    )


@dataclass
class Tsmt01400105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05"

    data_set_submissn: Optional[DataSetSubmissionV05Tsmt01400105] = field(
        default=None,
        metadata={
            "name": "DataSetSubmissn",
            "type": "Element",
            "required": True,
        },
    )
