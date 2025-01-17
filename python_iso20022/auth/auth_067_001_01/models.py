from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.enums import (
    AssetClassDetailedSubProductType16Code,
    CollateralAccountType3Code,
    ProductType7Code,
    SchemeIdentificationType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01"


@dataclass
class ActiveCurrencyAnd24AmountAuth06700101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 24,
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
class ActiveCurrencyAndAmountAuth06700101:
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
class GenericIdentification168Auth06700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Auth06700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth06700101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AssetClassDetailedSubProductType1ChoiceAuth06700101:
    cd: Optional[AssetClassDetailedSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Auth06700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )


@dataclass
class GenericIdentification165Auth06700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )


@dataclass
class PartyIdentification118ChoiceAuth06700101:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prtry: Optional[GenericIdentification168Auth06700101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )


@dataclass
class SecurityIdentificationAndAmount1Auth06700101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    mkt_val: Optional[ActiveCurrencyAnd24AmountAuth06700101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )
    fin_instrm_tp: Optional[ProductType7Code] = field(
        default=None,
        metadata={
            "name": "FinInstrmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth06700101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06700101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )


@dataclass
class Commodity2Auth06700101:
    mkt_val: Optional[ActiveCurrencyAnd24AmountAuth06700101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )
    cmmdty_tp: Optional[AssetClassDetailedSubProductType1ChoiceAuth06700101] = field(
        default=None,
        metadata={
            "name": "CmmdtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )


@dataclass
class Guarantee1Auth06700101:
    prvdr: Optional[PartyIdentification118ChoiceAuth06700101] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth06700101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )


@dataclass
class AssetHolding1ChoiceAuth06700101:
    gold: Optional[ActiveCurrencyAndAmountAuth06700101] = field(
        default=None,
        metadata={
            "name": "Gold",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )
    trpty: Optional[ActiveCurrencyAndAmountAuth06700101] = field(
        default=None,
        metadata={
            "name": "Trpty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )
    csh: Optional[ActiveCurrencyAndAmountAuth06700101] = field(
        default=None,
        metadata={
            "name": "Csh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )
    scty: Optional[SecurityIdentificationAndAmount1Auth06700101] = field(
        default=None,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )
    grnt: Optional[Guarantee1Auth06700101] = field(
        default=None,
        metadata={
            "name": "Grnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )
    cmmdty: Optional[Commodity2Auth06700101] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )


@dataclass
class AssetHolding1Auth06700101:
    pst_hrcut_val: Optional[ActiveCurrencyAnd24AmountAuth06700101] = field(
        default=None,
        metadata={
            "name": "PstHrcutVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )
    asst_tp: Optional[AssetHolding1ChoiceAuth06700101] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )
    coll_rqrmnt: Optional[CollateralAccountType3Code] = field(
        default=None,
        metadata={
            "name": "CollRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )


@dataclass
class CollateralAccount4Auth06700101:
    id: Optional[GenericIdentification165Auth06700101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "required": True,
        },
    )
    asst_hldg: list[AssetHolding1Auth06700101] = field(
        default_factory=list,
        metadata={
            "name": "AsstHldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class CcpcollateralReportV01Auth06700101:
    class Meta:
        name = "CCPCollateralReportV01"

    coll_acct_ownr: list[CollateralAccount4Auth06700101] = field(
        default_factory=list,
        metadata={
            "name": "CollAcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06700101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01",
        },
    )


@dataclass
class Auth06700101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.067.001.01"

    ccpcoll_rpt: Optional[CcpcollateralReportV01Auth06700101] = field(
        default=None,
        metadata={
            "name": "CCPCollRpt",
            "type": "Element",
            "required": True,
        },
    )
