from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    DistributionPolicy1Code,
    EventFrequency3Code,
    EventFrequency4Code,
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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11"


@dataclass
class DateAndDateTime2ChoiceSemt00300211(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class FinancialInstrumentQuantity36ChoiceSemt00300211(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    dgtl_tkn_unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DgtlTknUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification144Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 14,
        },
    )


@dataclass
class GenericIdentification18Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification39Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 8,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )


@dataclass
class GenericIdentification47Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification84Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 34,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification86Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource4ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "length": 2,
            "pattern": r"XX|TS",
        },
    )


@dataclass
class MarketIdentification2ChoiceSemt00300211(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class MarketIdentification4ChoiceSemt00300211(ISO20022MessageElement):
    mkt_idr_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdrCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class NameAndAddress12Semt00300211(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class Number3ChoiceSemt00300211(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[0-9]{5}",
        },
    )


@dataclass
class OriginalAndCurrentQuantities4Semt00300211(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
            "fraction_digits": 5,
        },
    )


@dataclass
class Pagination1Semt00300211(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class RestrictedFinactiveOrHistoricCurrencyAnd13DecimalAmountSemt00300211(
    ISO20022MessageElement
):
    class Meta:
        name = "RestrictedFINActiveOrHistoricCurrencyAnd13DecimalAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
class RestrictedFinactiveOrHistoricCurrencyAndAmountSemt00300211(
    ISO20022MessageElement
):
    class Meta:
        name = "RestrictedFINActiveOrHistoricCurrencyAndAmount"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 14,
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
class SimpleIdentificationInformation1Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt00300211(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification4Semt00300211(ISO20022MessageElement):
    prtry: Optional[SimpleIdentificationInformation1Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection14Semt00300211(ISO20022MessageElement):
    amt: Optional[RestrictedFinactiveOrHistoricCurrencyAndAmountSemt00300211] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class ClassificationType33ChoiceSemt00300211(ISO20022MessageElement):
    clssfctn_fin_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    altrn_clssfctn: Optional[GenericIdentification86Semt00300211] = field(
        default=None,
        metadata={
            "name": "AltrnClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class DerivativeBasicAttributes2Semt00300211(ISO20022MessageElement):
    ntnl_ccy_and_amt: Optional[
        RestrictedFinactiveOrHistoricCurrencyAndAmountSemt00300211
    ] = field(
        default=None,
        metadata={
            "name": "NtnlCcyAndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    intrst_incl_in_pric: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrstInclInPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class ExposureType24ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[ExposureType12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class FinancialInstrument22Semt00300211(ISO20022MessageElement):
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    pdct_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "PdctGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    umbrll_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UmbrllNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    reqd_navccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReqdNAVCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    dual_fnd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DualFndInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    ctry_of_dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfDmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    regd_dstrbtn_ctry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "RegdDstrbtnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FormOfSecurity7ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class Frequency26ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[EventFrequency4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class Frequency27ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[EventFrequency3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class GenericIdentification85Semt00300211(ISO20022MessageElement):
    tp: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class InterestComputationMethodFormat5ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class MarketType17ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[MarketType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class Number23ChoiceSemt00300211(ISO20022MessageElement):
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[GenericIdentification18Semt00300211] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class OptionStyle9ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[OptionStyle2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class OptionType7ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class OtherIdentification2Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 31,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,31}",
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource4ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification136ChoiceSemt00300211(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Semt00300211] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class PartyIdentification137ChoiceSemt00300211(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification84Semt00300211] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    nm_and_adr: Optional[NameAndAddress12Semt00300211] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class PledgeeTypeAndAnyBicidentifier2Semt00300211(ISO20022MessageElement):
    class Meta:
        name = "PledgeeTypeAndAnyBICIdentifier2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    pldgee_tp: Optional[PledgeeType1Code] = field(
        default=None,
        metadata={
            "name": "PldgeeTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class PledgeeTypeAndText2Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([^/]+/)+([^/]+)|([^/]*)",
        },
    )
    pldgee_tp: Optional[PledgeeType1Code] = field(
        default=None,
        metadata={
            "name": "PldgeeTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class PriceRateOrAmount1ChoiceSemt00300211(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[
        RestrictedFinactiveOrHistoricCurrencyAnd13DecimalAmountSemt00300211
    ] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class PriceRateOrAmountOrUnknown3ChoiceSemt00300211(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[
        RestrictedFinactiveOrHistoricCurrencyAnd13DecimalAmountSemt00300211
    ] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    uknwn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UknwnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class PurposeCode8ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[SecuritiesAccountPurposeType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class Quantity54ChoiceSemt00300211(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities4Semt00300211] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class QuantityAndAvailability4Semt00300211(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    avlbty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AvlbtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class Role7ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Semt00300211(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText15Semt00300211(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 30,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )


@dataclass
class SecuritiesPaymentStatus6ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[SecuritiesPaymentStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class StatementBasis9ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[StatementBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SubBalanceType13ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[SecuritiesBalanceType12Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SubBalanceType14ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[SecuritiesBalanceType7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SupplementaryData1Semt00300211(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt00300211] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class TypeOfPrice32ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[TypeOfPrice14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class TypeOfPrice33ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[TypeOfPrice11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class UpdateType16ChoiceSemt00300211(ISO20022MessageElement):
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification47Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class YieldedOrValueType1ChoiceSemt00300211(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class Account30Semt00300211(ISO20022MessageElement):
    id: Optional[AccountIdentification4Semt00300211] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification137ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class BalanceAmounts5Semt00300211(ISO20022MessageElement):
    hldg_val: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "HldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    prvs_hldg_val: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "PrvsHldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    book_val: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "BookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    urlsd_gn_loss: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "UrlsdGnLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    acrd_intrst_amt: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class BalanceAmounts6Semt00300211(ISO20022MessageElement):
    hldg_val: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "HldgVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    book_val: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "BookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    urlsd_gn_loss: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "UrlsdGnLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class BalanceQuantity15ChoiceSemt00300211(ISO20022MessageElement):
    qty: Optional[Quantity54ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification144Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class BlockChainAddressWallet10Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    tp: Optional[PurposeCode8ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 70,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,70}",
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )


@dataclass
class BlockChainAddressWallet9Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    tp: Optional[PurposeCode8ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 70,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,70}",
        },
    )


@dataclass
class ForeignExchangeTerms35Semt00300211(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    qtg_instn: Optional[PartyIdentification137ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class MarketIdentification91Semt00300211(ISO20022MessageElement):
    id: Optional[MarketIdentification2ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    tp: Optional[MarketType17ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class PartyIdentification156Semt00300211(ISO20022MessageElement):
    id: Optional[PartyIdentification136ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification157Semt00300211(ISO20022MessageElement):
    id: Optional[PartyIdentification137ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PledgeeFormat6ChoiceSemt00300211(ISO20022MessageElement):
    tp_and_id: Optional[PledgeeTypeAndAnyBicidentifier2Semt00300211] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    id: Optional[PledgeeTypeAndText2Semt00300211] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification85Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class Price3Semt00300211(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType1ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount1ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class SafekeepingPlaceFormat39ChoiceSemt00300211(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText15Semt00300211] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Semt00300211] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification85Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SecuritiesAccount34Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    tp: Optional[PurposeCode8ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SecuritiesAccount42Semt00300211(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )
    tp: Optional[PurposeCode8ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.,'\+ ]{1,35}",
        },
    )


@dataclass
class SecurityIdentification20Semt00300211(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification2Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class Statement76Semt00300211(ISO20022MessageElement):
    rpt_nb: Optional[Number3ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 16,
            "pattern": r"([0-9a-zA-Z\-\?:\(\)\.,'\+ ]([0-9a-zA-Z\-\?:\(\)\.,'\+ ]*(/[0-9a-zA-Z\-\?:\(\)\.,'\+ ])?)*)",
        },
    )
    stmt_dt_tm: Optional[DateAndDateTime2ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    frqcy: Optional[Frequency26ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    upd_tp: Optional[UpdateType16ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    stmt_bsis: Optional[StatementBasis9ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "StmtBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    audtd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudtdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    sub_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SubAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    tax_lot_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxLotInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    scty_intrst_or_set_off: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SctyIntrstOrSetOff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SubBalanceQuantity9ChoiceSemt00300211(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity36ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prtry: Optional[GenericIdentification144Semt00300211] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    qty_and_avlbty: Optional[QuantityAndAvailability4Semt00300211] = field(
        default=None,
        metadata={
            "name": "QtyAndAvlbty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class TotalValueInPageAndStatement4Semt00300211(ISO20022MessageElement):
    ttl_hldgs_val_of_pg: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "TtlHldgsValOfPg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    ttl_hldgs_val_of_stmt: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "TtlHldgsValOfStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    ttl_book_val_of_stmt: Optional[AmountAndDirection14Semt00300211] = field(
        default=None,
        metadata={
            "name": "TtlBookValOfStmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class AdditionalBalanceInformation23Semt00300211(ISO20022MessageElement):
    sub_bal_tp: Optional[SubBalanceType14ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "SubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    qty: Optional[SubBalanceQuantity9ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    sub_bal_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubBalAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )


@dataclass
class Balance22Semt00300211(ISO20022MessageElement):
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    qty: Optional[BalanceQuantity15ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class Balance23Semt00300211(ISO20022MessageElement):
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    qty: Optional[BalanceQuantity15ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )


@dataclass
class Intermediary45Semt00300211(ISO20022MessageElement):
    id: Optional[PartyIdentification157Semt00300211] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    role: Optional[Role7ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    acct: Optional[Account30Semt00300211] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class Pledgee4Semt00300211(ISO20022MessageElement):
    pldgee_tp_and_id: Optional[PledgeeFormat6ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "PldgeeTpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PriceInformation22Semt00300211(ISO20022MessageElement):
    tp: Optional[TypeOfPrice33ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmountOrUnknown3ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    val_tp: Optional[YieldedOrValueType1ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    src_of_pric: Optional[MarketIdentification91Semt00300211] = field(
        default=None,
        metadata={
            "name": "SrcOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    qtn_dt: Optional[DateAndDateTime2ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class PriceType5ChoiceSemt00300211(ISO20022MessageElement):
    mkt: Optional[Price3Semt00300211] = field(
        default=None,
        metadata={
            "name": "Mkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    indctv: Optional[Price3Semt00300211] = field(
        default=None,
        metadata={
            "name": "Indctv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SafeKeepingPlace4Semt00300211(ISO20022MessageElement):
    sfkpg_plc_frmt: Optional[SafekeepingPlaceFormat39ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class FinancialInstrumentAttributes122Semt00300211(ISO20022MessageElement):
    plc_of_listg: Optional[MarketIdentification4ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethodFormat5ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    regn_form: Optional[FormOfSecurity7ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "RegnForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    pmt_frqcy: Optional[Frequency27ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    pmt_sts: Optional[SecuritiesPaymentStatus6ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "PmtSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    varbl_rate_chng_frqcy: Optional[Frequency27ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "VarblRateChngFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    clssfctn_tp: Optional[ClassificationType33ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "ClssfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    optn_style: Optional[OptionStyle9ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    optn_tp: Optional[OptionType7ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    dnmtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "DnmtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cpn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CpnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    fltg_rate_fxg_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FltgRateFxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    nxt_cllbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NxtCllblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    putbl_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PutblDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    dtd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    frst_pmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    prvs_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PrvsFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cur_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    yld_to_mtrty_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YldToMtrtyRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    nxt_intrst_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NxtIntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    indx_rate_bsis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IndxRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cpn_attchd_nb: Optional[Number23ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "CpnAttchdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    pool_nb: Optional[GenericIdentification39Semt00300211] = field(
        default=None,
        metadata={
            "name": "PoolNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    varbl_rate_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VarblRateInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    cllbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CllblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    putbl_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PutblInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    mkt_or_indctv_pric: Optional[PriceType5ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "MktOrIndctvPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    exrc_pric: Optional[Price3Semt00300211] = field(
        default=None,
        metadata={
            "name": "ExrcPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    sbcpt_pric: Optional[Price3Semt00300211] = field(
        default=None,
        metadata={
            "name": "SbcptPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    convs_pric: Optional[Price3Semt00300211] = field(
        default=None,
        metadata={
            "name": "ConvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    strk_pric: Optional[Price3Semt00300211] = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    min_nmnl_qty: Optional[FinancialInstrumentQuantity36ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "MinNmnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    ctrct_sz: Optional[FinancialInstrumentQuantity36ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    undrlyg_fin_instrm_id: list[SecurityIdentification20Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    fin_instrm_attr_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class QuantityBreakdown70Semt00300211(ISO20022MessageElement):
    lot_nb: Optional[GenericIdentification39Semt00300211] = field(
        default=None,
        metadata={
            "name": "LotNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    lot_qty: Optional[Balance23Semt00300211] = field(
        default=None,
        metadata={
            "name": "LotQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    lot_dt_tm: Optional[DateAndDateTime2ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "LotDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    lot_pric: Optional[Price3Semt00300211] = field(
        default=None,
        metadata={
            "name": "LotPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    tp_of_pric: Optional[TypeOfPrice32ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "TpOfPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    acct_base_ccy_amts: Optional[BalanceAmounts6Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcctBaseCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    instrm_ccy_amts: Optional[BalanceAmounts6Semt00300211] = field(
        default=None,
        metadata={
            "name": "InstrmCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    altrn_rptg_ccy_amts: Optional[BalanceAmounts6Semt00300211] = field(
        default=None,
        metadata={
            "name": "AltrnRptgCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SubBalanceInformation23Semt00300211(ISO20022MessageElement):
    sub_bal_tp: Optional[SubBalanceType13ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "SubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    qty: Optional[SubBalanceQuantity9ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    sub_bal_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubBalAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 140,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,140}",
        },
    )
    addtl_bal_brkdwn_dtls: list[AdditionalBalanceInformation23Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class AggregateBalancePerSafekeepingPlace40Semt00300211(ISO20022MessageElement):
    sfkpg_plc: Optional[SafeKeepingPlace4Semt00300211] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    plc_of_listg: Optional[MarketIdentification4ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    pldgee: Optional[Pledgee4Semt00300211] = field(
        default=None,
        metadata={
            "name": "Pldgee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    aggt_bal: Optional[Balance22Semt00300211] = field(
        default=None,
        metadata={
            "name": "AggtBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    pric_dtls: list[PriceInformation22Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_occurs": 1,
        },
    )
    fxdtls: list[ForeignExchangeTerms35Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    acct_base_ccy_amts: Optional[BalanceAmounts5Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcctBaseCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    instrm_ccy_amts: Optional[BalanceAmounts5Semt00300211] = field(
        default=None,
        metadata={
            "name": "InstrmCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    altrn_rptg_ccy_amts: Optional[BalanceAmounts5Semt00300211] = field(
        default=None,
        metadata={
            "name": "AltrnRptgCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    qty_brkdwn: list[QuantityBreakdown70Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    xpsr_tp: Optional[ExposureType24ChoiceSemt00300211] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    bal_brkdwn: list[SubBalanceInformation23Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "BalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    addtl_bal_brkdwn: list[AdditionalBalanceInformation23Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    hldg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )


@dataclass
class AggregateBalanceInformation43Semt00300211(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification20Semt00300211] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    fin_instrm_attrbts: Optional[FinancialInstrumentAttributes122Semt00300211] = field(
        default=None,
        metadata={
            "name": "FinInstrmAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    invstmt_fnds_fin_instrm_attrbts: Optional[FinancialInstrument22Semt00300211] = (
        field(
            default=None,
            metadata={
                "name": "InvstmtFndsFinInstrmAttrbts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            },
        )
    )
    addtl_deriv_attrbts: Optional[DerivativeBasicAttributes2Semt00300211] = field(
        default=None,
        metadata={
            "name": "AddtlDerivAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    aggt_bal: Optional[Balance22Semt00300211] = field(
        default=None,
        metadata={
            "name": "AggtBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafeKeepingPlace4Semt00300211] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    corp_actn_optn_tp: Optional[CorporateActionOption5Code] = field(
        default=None,
        metadata={
            "name": "CorpActnOptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    pric_dtls: list[PriceInformation22Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_occurs": 1,
        },
    )
    fxdtls: list[ForeignExchangeTerms35Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    acct_base_ccy_amts: Optional[BalanceAmounts5Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcctBaseCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    instrm_ccy_amts: Optional[BalanceAmounts5Semt00300211] = field(
        default=None,
        metadata={
            "name": "InstrmCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    altrn_rptg_ccy_amts: Optional[BalanceAmounts5Semt00300211] = field(
        default=None,
        metadata={
            "name": "AltrnRptgCcyAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    qty_brkdwn: list[QuantityBreakdown70Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "QtyBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    bal_brkdwn: list[SubBalanceInformation23Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "BalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    addtl_bal_brkdwn: list[AdditionalBalanceInformation23Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "AddtlBalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    bal_at_sfkpg_plc: list[AggregateBalancePerSafekeepingPlace40Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "BalAtSfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    hldg_addtl_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "HldgAddtlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "min_length": 1,
            "max_length": 350,
            "pattern": r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,350}",
        },
    )
    splmtry_data: list[SupplementaryData1Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SubAccountIdentification68Semt00300211(ISO20022MessageElement):
    acct_ownr: Optional[PartyIdentification156Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount34Semt00300211] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet9Semt00300211] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    bal_for_sub_acct: list[AggregateBalanceInformation43Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "BalForSubAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )


@dataclass
class SecuritiesBalanceAccountingReport002V11Semt00300211(ISO20022MessageElement):
    pgntn: Optional[Pagination1Semt00300211] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement76Semt00300211] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification156Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    acct_svcr: Optional[PartyIdentification157Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount42Semt00300211] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet10Semt00300211] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    intrmy_inf: list[Intermediary45Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            "max_occurs": 10,
        },
    )
    bal_for_acct: list[AggregateBalanceInformation43Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "BalForAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    sub_acct_dtls: list[SubAccountIdentification68Semt00300211] = field(
        default_factory=list,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    acct_base_ccy_ttl_amts: Optional[TotalValueInPageAndStatement4Semt00300211] = field(
        default=None,
        metadata={
            "name": "AcctBaseCcyTtlAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
        },
    )
    altrn_rptg_ccy_ttl_amts: Optional[TotalValueInPageAndStatement4Semt00300211] = (
        field(
            default=None,
            metadata={
                "name": "AltrnRptgCcyTtlAmts",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11",
            },
        )
    )


@dataclass
class Semt00300211(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.003.002.11"

    scties_bal_acctg_rpt: Optional[
        SecuritiesBalanceAccountingReport002V11Semt00300211
    ] = field(
        default=None,
        metadata={
            "name": "SctiesBalAcctgRpt",
            "type": "Element",
            "required": True,
        },
    )
