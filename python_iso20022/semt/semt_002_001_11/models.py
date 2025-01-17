from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    AddressType2Code,
    DistributionPolicy1Code,
    EventFrequency3Code,
    EventFrequency7Code,
    ExposureType12Code,
    FormOfSecurity1Code,
    InterestComputationMethod2Code,
    InvestmentFundRole2Code,
    MarketType4Code,
    OptionStyle2Code,
    OptionType1Code,
    PriceValueType1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    SecuritiesAccountPurposeType1Code,
    SecuritiesPaymentStatus1Code,
    ShortLong1Code,
    StatementUpdateType1Code,
    TypeOfPrice14Code,
)
from python_iso20022.semt.enums import (
    CorporateActionOption5Code,
    PledgeeType1Code,
    SecuritiesBalanceType7Code,
    SecuritiesBalanceType12Code,
    StatementBasis1Code,
    TypeOfPrice11Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11"


@dataclass
class ActiveOrHistoricCurrencyAnd13DecimalAmountSemt00200111:
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
class ActiveOrHistoricCurrencyAndAmountSemt00200111:
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
class DateAndDateTime2ChoiceSemt00200111:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceSemt00200111:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification1Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification37Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification56Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt00200111:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification1ChoiceSemt00200111:
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketIdentification3ChoiceSemt00200111:
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Number3ChoiceSemt00200111:
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[0-9]{5}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Semt00200111:
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Semt00200111:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification15Semt00200111:
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SimpleIdentificationInformation4Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt00200111:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification26Semt00200111:
    prtry: Optional[SimpleIdentificationInformation4Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection6Semt00200111:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt00200111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class BalanceQuantity14ChoiceSemt00200111:
    qty: Optional[FinancialInstrumentQuantity33ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification56Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class BasicCollateralValuation1DetailsSemt00200111:
    valtn_hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ValtnHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    hrcut_src: Optional[PartyIdentification15Semt00200111] = field(
        default=None,
        metadata={
            "name": "HrcutSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class ClassificationType32ChoiceSemt00200111:
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification36Semt00200111] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class ExposureType22ChoiceSemt00200111:
    cd: Optional[ExposureType12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class FinancialInstrument21Semt00200111:
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    umbrll_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UmbrllNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dual_fnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DualFndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    ctry_of_dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfDmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regd_dstrbtn_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RegdDstrbtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FormOfSecurity6ChoiceSemt00200111:
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Frequency22ChoiceSemt00200111:
    cd: Optional[EventFrequency7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Frequency23ChoiceSemt00200111:
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class GenericIdentification78Semt00200111:
    tp: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification80Semt00200111:
    tp: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InterestComputationMethodFormat4ChoiceSemt00200111:
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class MarketType15ChoiceSemt00200111:
    cd: Optional[MarketType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Number22ChoiceSemt00200111:
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[GenericIdentification1Semt00200111] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class OptionStyle8ChoiceSemt00200111:
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class OptionType6ChoiceSemt00200111:
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class OtherIdentification1Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification127ChoiceSemt00200111:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt00200111] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class PledgeeTypeAndAnyBicidentifier2Semt00200111:
    class Meta:
        name = "PledgeeTypeAndAnyBICIdentifier2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    pldgee_tp: Optional[PledgeeType1Code] = field(
        default=None,
        metadata={
            "name": "PldgeeTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class PledgeeTypeAndText1Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pldgee_tp: Optional[PledgeeType1Code] = field(
        default=None,
        metadata={
            "name": "PldgeeTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Semt00200111:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceSemt00200111:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt00200111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class PriceRateOrAmountOrUnknown2ChoiceSemt00200111:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt00200111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    uknwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UknwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class PurposeCode7ChoiceSemt00200111:
    cd: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Quantity51ChoiceSemt00200111:
    qty: Optional[FinancialInstrumentQuantity33ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Semt00200111] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class QuantityAndAvailability3Semt00200111:
    qty: Optional[FinancialInstrumentQuantity33ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    avlbty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlbtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class Role6ChoiceSemt00200111:
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Semt00200111:
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Semt00200111:
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesPaymentStatus5ChoiceSemt00200111:
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class StatementBasis7ChoiceSemt00200111:
    cd: Optional[StatementBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SubBalanceType11ChoiceSemt00200111:
    cd: Optional[SecuritiesBalanceType12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SubBalanceType12ChoiceSemt00200111:
    cd: Optional[SecuritiesBalanceType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SupplementaryData1Semt00200111:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt00200111] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class TypeOfPrice28ChoiceSemt00200111:
    cd: Optional[TypeOfPrice11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class TypeOfPrice29ChoiceSemt00200111:
    cd: Optional[TypeOfPrice14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class UpdateType15ChoiceSemt00200111:
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSemt00200111:
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Balance18Semt00200111:
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qty: Optional[BalanceQuantity14ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class BalanceAmounts3Semt00200111:
    hldg_val: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "HldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prvs_hldg_val: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "PrvsHldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    book_val: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "BookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    elgbl_coll_val: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "ElgblCollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class BalanceQuantity13ChoiceSemt00200111:
    qty: Optional[Quantity51ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification56Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class BlockChainAddressWallet1Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[PurposeCode7ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class BlockChainAddressWallet2Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[PurposeCode7ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class MarketIdentification89Semt00200111:
    id: Optional[MarketIdentification1ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    tp: Optional[MarketType15ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Semt00200111:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt00200111] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class PartyIdentification144Semt00200111:
    id: Optional[PartyIdentification127ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PledgeeFormat5ChoiceSemt00200111:
    tp_and_id: Optional[PledgeeTypeAndAnyBicidentifier2Semt00200111] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    id: Optional[PledgeeTypeAndText1Semt00200111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification80Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Price7Semt00200111:
    tp: Optional[YieldedOrValueType1ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceFormat29ChoiceSemt00200111:
    id: Optional[SafekeepingPlaceTypeAndText8Semt00200111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Semt00200111] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification78Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SecuritiesAccount25Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PurposeCode7ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccount26Semt00200111:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PurposeCode7ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecurityIdentification19Semt00200111:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Statement73Semt00200111:
    rpt_nb: Optional[Number3ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_dt_tm: Optional[DateAndDateTime2ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    frqcy: Optional[Frequency22ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    upd_tp: Optional[UpdateType15ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    stmt_bsis: Optional[StatementBasis7ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "StmtBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    sub_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SubAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    scty_intrst_or_set_off: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctyIntrstOrSetOff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SubBalanceQuantity8ChoiceSemt00200111:
    qty: Optional[FinancialInstrumentQuantity33ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prtry: Optional[GenericIdentification56Semt00200111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qty_and_avlbty: Optional[QuantityAndAvailability3Semt00200111] = field(
        default=None,
        metadata={
            "name": "QtyAndAvlbty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class TotalValueInPageAndStatement1Semt00200111:
    ttl_hldgs_val_of_pg: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "TtlHldgsValOfPg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    ttl_hldgs_val_of_stmt: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "TtlHldgsValOfStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    ttl_book_val_of_stmt: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "TtlBookValOfStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    ttl_elgbl_coll_val: Optional[AmountAndDirection6Semt00200111] = field(
        default=None,
        metadata={
            "name": "TtlElgblCollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Balance16Semt00200111:
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qty: Optional[BalanceQuantity13ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class Balance17Semt00200111:
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    qty: Optional[BalanceQuantity13ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class Balance21Semt00200111:
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qty: Optional[SubBalanceQuantity8ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification120ChoiceSemt00200111:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt00200111] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt00200111] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Pledgee3Semt00200111:
    pldgee_tp_and_id: Optional[PledgeeFormat5ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "PldgeeTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PriceInformation20Semt00200111:
    tp: Optional[TypeOfPrice28ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmountOrUnknown2ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    val_tp: Optional[YieldedOrValueType1ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    src_of_pric: Optional[MarketIdentification89Semt00200111] = field(
        default=None,
        metadata={
            "name": "SrcOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qtn_dt: Optional[DateAndDateTime2ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class PriceType4ChoiceSemt00200111:
    mkt: Optional[Price7Semt00200111] = field(
        default=None,
        metadata={
            "name": "Mkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    indctv: Optional[Price7Semt00200111] = field(
        default=None,
        metadata={
            "name": "Indctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SafeKeepingPlace3Semt00200111:
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat29ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Account29Semt00200111:
    id: Optional[AccountIdentification26Semt00200111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification120ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class FinancialInstrumentAttributes111Semt00200111:
    plc_of_listg: Optional[MarketIdentification3ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat4ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    regn_form: Optional[FormOfSecurity6ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    pmt_frqcy: Optional[Frequency23ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus5ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency23ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    clssfctn_tp: Optional[ClassificationType32ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    optn_style: Optional[OptionStyle8ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    optn_tp: Optional[OptionType6ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld_to_mtrty_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YldToMtrtyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number22ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    pool_nb: Optional[GenericIdentification37Semt00200111] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    mkt_or_indctv_pric: Optional[PriceType4ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "MktOrIndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    exrc_pric: Optional[Price7Semt00200111] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    sbcpt_pric: Optional[Price7Semt00200111] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    convs_pric: Optional[Price7Semt00200111] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    strk_pric: Optional[Price7Semt00200111] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity33ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity33ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    undrlyg_fin_instrm_id: list[SecurityIdentification19Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class ForeignExchangeTerms34Semt00200111:
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qtg_instn: Optional[PartyIdentification120ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class PartyIdentification136Semt00200111:
    id: Optional[PartyIdentification120ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class QuantityBreakdown57Semt00200111:
    lot_nb: Optional[GenericIdentification37Semt00200111] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    lot_qty: Optional[Balance16Semt00200111] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    lot_dt_tm: Optional[DateAndDateTime2ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "LotDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    lot_pric: Optional[Price7Semt00200111] = field(
        default=None,
        metadata={
            "name": "LotPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    tp_of_pric: Optional[TypeOfPrice29ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class AdditionalBalanceInformation20Semt00200111:
    sub_bal_tp: Optional[SubBalanceType12ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "SubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    qty: Optional[Balance21Semt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    sub_bal_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubBalAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    qty_brkdwn: list[QuantityBreakdown57Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Intermediary44Semt00200111:
    id: Optional[PartyIdentification136Semt00200111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    role: Optional[Role6ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    acct: Optional[Account29Semt00200111] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SubBalanceInformation20Semt00200111:
    sub_bal_tp: Optional[SubBalanceType11ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "SubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    qty: Optional[Balance21Semt00200111] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    sub_bal_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubBalAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    qty_brkdwn: list[QuantityBreakdown57Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    addtl_bal_brkdwn_dtls: list[AdditionalBalanceInformation20Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class AggregateBalancePerSafekeepingPlace39Semt00200111:
    sfkpg_plc: Optional[SafeKeepingPlace3Semt00200111] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification3ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    pldgee: Optional[Pledgee3Semt00200111] = field(
        default=None,
        metadata={
            "name": "Pldgee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    aggt_bal: Optional[Balance17Semt00200111] = field(
        default=None,
        metadata={
            "name": "AggtBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    avlbl_bal: Optional[Balance18Semt00200111] = field(
        default=None,
        metadata={
            "name": "AvlblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    not_avlbl_bal: Optional[BalanceQuantity14ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "NotAvlblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    pric_dtls: list[PriceInformation20Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    fxdtls: list[ForeignExchangeTerms34Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    acct_base_ccy_amts: Optional[BalanceAmounts3Semt00200111] = field(
        default=None,
        metadata={
            "name": "AcctBaseCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    instrm_ccy_amts: Optional[BalanceAmounts3Semt00200111] = field(
        default=None,
        metadata={
            "name": "InstrmCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qty_brkdwn: list[QuantityBreakdown57Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    xpsr_tp: Optional[ExposureType22ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    bal_brkdwn: list[SubBalanceInformation20Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "BalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    addtl_bal_brkdwn: list[AdditionalBalanceInformation20Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    hldg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class AggregateBalanceInformation42Semt00200111:
    fin_instrm_id: Optional[SecurityIdentification19Semt00200111] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes111Semt00200111] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    invstmt_fnds_fin_instrm_attrbts: Optional[FinancialInstrument21Semt00200111] = (
        field(
            default=None,
            metadata={
                "name": "InvstmtFndsFinInstrmAttrbts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            },
        )
    )
    valtn_hrcut_dtls: Optional[BasicCollateralValuation1DetailsSemt00200111] = field(
        default=None,
        metadata={
            "name": "ValtnHrcutDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    aggt_bal: Optional[Balance17Semt00200111] = field(
        default=None,
        metadata={
            "name": "AggtBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    avlbl_bal: Optional[Balance18Semt00200111] = field(
        default=None,
        metadata={
            "name": "AvlblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    not_avlbl_bal: Optional[BalanceQuantity14ChoiceSemt00200111] = field(
        default=None,
        metadata={
            "name": "NotAvlblBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace3Semt00200111] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    corp_actn_optn_tp: Optional[CorporateActionOption5Code] = field(
        default=None,
        metadata={
            "name": "CorpActnOptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    pric_dtls: list[PriceInformation20Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    fxdtls: list[ForeignExchangeTerms34Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    acct_base_ccy_amts: Optional[BalanceAmounts3Semt00200111] = field(
        default=None,
        metadata={
            "name": "AcctBaseCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    instrm_ccy_amts: Optional[BalanceAmounts3Semt00200111] = field(
        default=None,
        metadata={
            "name": "InstrmCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    qty_brkdwn: list[QuantityBreakdown57Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    bal_brkdwn: list[SubBalanceInformation20Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "BalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    addtl_bal_brkdwn: list[AdditionalBalanceInformation20Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    bal_at_sfkpg_plc: list[AggregateBalancePerSafekeepingPlace39Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "BalAtSfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    hldg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    splmtry_data: list[SupplementaryData1Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SubAccountIdentification67Semt00200111:
    acct_ownr: Optional[PartyIdentification144Semt00200111] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount25Semt00200111] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet2Semt00200111] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    bal_for_sub_acct: list[AggregateBalanceInformation42Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "BalForSubAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class SecuritiesBalanceCustodyReportV11Semt00200111:
    pgntn: Optional[Pagination1Semt00200111] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement73Semt00200111] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification144Semt00200111] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    acct_svcr: Optional[PartyIdentification136Semt00200111] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount26Semt00200111] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet1Semt00200111] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    intrmy_inf: list[Intermediary44Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
            "max_occurs": 10,
        },
    )
    bal_for_acct: list[AggregateBalanceInformation42Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "BalForAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    sub_acct_dtls: list[SubAccountIdentification67Semt00200111] = field(
        default_factory=list,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )
    acct_base_ccy_ttl_amts: Optional[TotalValueInPageAndStatement1Semt00200111] = field(
        default=None,
        metadata={
            "name": "AcctBaseCcyTtlAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11",
        },
    )


@dataclass
class Semt00200111:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.002.001.11"

    scties_bal_ctdy_rpt: Optional[SecuritiesBalanceCustodyReportV11Semt00200111] = (
        field(
            default=None,
            metadata={
                "name": "SctiesBalCtdyRpt",
                "type": "Element",
                "required": True,
            },
        )
    )
