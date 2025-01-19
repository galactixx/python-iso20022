from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.enums import SchemeIdentificationType1Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01"


@dataclass
class ActiveCurrencyAndAmountAuth06600101(ISO20022MessageElement):
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
class SupplementaryDataEnvelope1Auth06600101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class GenericIdentification165Auth06600101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth06600101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "required": True,
        },
    )


@dataclass
class MonthlyResult1Auth06600101(ISO20022MessageElement):
    nb_of_obsrvtns: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfObsrvtns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    nb_of_xcptns: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfXcptns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cvrg: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Cvrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    lrgst_xcptn: Optional[ActiveCurrencyAndAmountAuth06600101] = field(
        default=None,
        metadata={
            "name": "LrgstXcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "required": True,
        },
    )
    avrg_xcptn: Optional[ActiveCurrencyAndAmountAuth06600101] = field(
        default=None,
        metadata={
            "name": "AvrgXcptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "required": True,
        },
    )
    lrgst_xcptn_id: Optional[GenericIdentification165Auth06600101] = field(
        default=None,
        metadata={
            "name": "LrgstXcptnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
        },
    )


@dataclass
class CcpbackTestingResultReportV01Auth06600101(ISO20022MessageElement):
    class Meta:
        name = "CCPBackTestingResultReportV01"

    mnthly_rslt: list[MonthlyResult1Auth06600101] = field(
        default_factory=list,
        metadata={
            "name": "MnthlyRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01",
        },
    )


@dataclass
class Auth06600101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.066.001.01"

    ccpbck_tstg_rslt_rpt: Optional[CcpbackTestingResultReportV01Auth06600101] = field(
        default=None,
        metadata={
            "name": "CCPBckTstgRsltRpt",
            "type": "Element",
            "required": True,
        },
    )
