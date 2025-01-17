from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.enums import (
    AssetClassDetailedSubProductType16Code,
    CollateralAccountType3Code,
    ProductType7Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01"


@dataclass
class ActiveCurrencyAnd24AmountAuth11200101:
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
class ActiveCurrencyAndAmountAuth11200101:
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
class FinancialInstrument104Auth11200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class GenericIdentification168Auth11200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Auth11200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth11200101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AssetClassDetailedSubProductType1ChoiceAuth11200101:
    cd: Optional[AssetClassDetailedSubProductType16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Auth11200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )


@dataclass
class GeneralCollateral4Auth11200101:
    fin_instrm_id: list[FinancialInstrument104Auth11200101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    mkt_val: Optional[ActiveCurrencyAnd24AmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class PartyIdentification118ChoiceAuth11200101:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    prtry: Optional[GenericIdentification168Auth11200101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )


@dataclass
class SecurityIdentificationAndAmount1Auth11200101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    mkt_val: Optional[ActiveCurrencyAnd24AmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    fin_instrm_tp: Optional[ProductType7Code] = field(
        default=None,
        metadata={
            "name": "FinInstrmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class SpecificCollateral3Auth11200101:
    fin_instrm_id: Optional[FinancialInstrument104Auth11200101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    mkt_val: Optional[ActiveCurrencyAnd24AmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth11200101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth11200101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class CollateralType22ChoiceAuth11200101:
    gnl_coll: Optional[GeneralCollateral4Auth11200101] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    spcfc_coll: Optional[SpecificCollateral3Auth11200101] = field(
        default=None,
        metadata={
            "name": "SpcfcColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )


@dataclass
class Commodity2Auth11200101:
    mkt_val: Optional[ActiveCurrencyAnd24AmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    cmmdty_tp: Optional[AssetClassDetailedSubProductType1ChoiceAuth11200101] = field(
        default=None,
        metadata={
            "name": "CmmdtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class Guarantee1Auth11200101:
    prvdr: Optional[PartyIdentification118ChoiceAuth11200101] = field(
        default=None,
        metadata={
            "name": "Prvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class TripartyCollateralAndAmount1Auth11200101:
    trpty: Optional[ActiveCurrencyAndAmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "Trpty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    coll_tp: Optional[CollateralType22ChoiceAuth11200101] = field(
        default=None,
        metadata={
            "name": "CollTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class AssetHolding3ChoiceAuth11200101:
    gold: Optional[ActiveCurrencyAndAmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "Gold",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    trpty: Optional[TripartyCollateralAndAmount1Auth11200101] = field(
        default=None,
        metadata={
            "name": "Trpty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    csh: Optional[ActiveCurrencyAndAmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "Csh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    scty: Optional[SecurityIdentificationAndAmount1Auth11200101] = field(
        default=None,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    grnt: Optional[Guarantee1Auth11200101] = field(
        default=None,
        metadata={
            "name": "Grnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )
    cmmdty: Optional[Commodity2Auth11200101] = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )


@dataclass
class AssetHolding3Auth11200101:
    pst_hrcut_val: Optional[ActiveCurrencyAnd24AmountAuth11200101] = field(
        default=None,
        metadata={
            "name": "PstHrcutVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    asst_tp: Optional[AssetHolding3ChoiceAuth11200101] = field(
        default=None,
        metadata={
            "name": "AsstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    coll_rqrmnt: Optional[CollateralAccountType3Code] = field(
        default=None,
        metadata={
            "name": "CollRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )


@dataclass
class InteroperabilityCcp1Auth11200101:
    class Meta:
        name = "InteroperabilityCCP1"

    id: Optional[GenericIdentification168Auth11200101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "required": True,
        },
    )
    ttl_initl_mrgn: list[ActiveCurrencyAndAmountAuth11200101] = field(
        default_factory=list,
        metadata={
            "name": "TtlInitlMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_occurs": 1,
        },
    )
    trds_clrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrdsClrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    grss_ntnl_amt: list[ActiveCurrencyAnd24AmountAuth11200101] = field(
        default_factory=list,
        metadata={
            "name": "GrssNtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_occurs": 1,
        },
    )
    asst_hldg: list[AssetHolding3Auth11200101] = field(
        default_factory=list,
        metadata={
            "name": "AsstHldg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class CcpinteroperabilityReportV01Auth11200101:
    class Meta:
        name = "CCPInteroperabilityReportV01"

    intrprblty_ccp: list[InteroperabilityCcp1Auth11200101] = field(
        default_factory=list,
        metadata={
            "name": "IntrprbltyCCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth11200101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
        },
    )


@dataclass
class Auth11200101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01"

    ccpintrprblty_rpt: Optional[CcpinteroperabilityReportV01Auth11200101] = field(
        default=None,
        metadata={
            "name": "CCPIntrprbltyRpt",
            "type": "Element",
            "required": True,
        },
    )
