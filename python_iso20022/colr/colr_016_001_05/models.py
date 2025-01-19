from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.colr.colr_016_001_05.enums import (
    CcpmemberType1Code,
    CollateralAppliedExcess1Code,
    CollateralDirection1Code,
    CollateralType8Code,
    ExposureType13Code,
    ReturnExcessCash1Code,
    SettlementStatus3Code,
)
from python_iso20022.colr.enums import (
    AgreementFramework1Code,
    CollateralAccountType1Code,
    ExposureType11Code,
    ThresholdType1Code,
)
from python_iso20022.enums import (
    DateType2Code,
    DepositType1Code,
    EventFrequency6Code,
    InterestComputationMethod2Code,
    PriceValueType1Code,
    SafekeepingPlace1Code,
    SafekeepingPlace3Code,
    ShortLong1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05"


@dataclass
class ActiveCurrencyAndAmountColr01600105(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountColr01600105(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceColr01600105(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class FinancialInstrumentQuantity33ChoiceColr01600105(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 30,
            "fraction_digits": 29,
        },
    )


@dataclass
class GenericIdentification30Colr01600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Colr01600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceColr01600105(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Pagination1Colr01600105(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )


@dataclass
class PostalAddress2Colr01600105(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Colr01600105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AgreementFramework1ChoiceColr01600105(ISO20022MessageElement):
    agrmt_frmwk: Optional[AgreementFramework1Code] = field(
        default=None,
        metadata={
            "name": "AgrmtFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    prtry_id: Optional[GenericIdentification30Colr01600105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class BlockChainAddressWallet3Colr01600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Colr01600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CashCollateral4Colr01600105(ISO20022MessageElement):
    asst_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AsstNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dpst_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "DpstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    dpst_tp: Optional[DepositType1Code] = field(
        default=None,
        metadata={
            "name": "DpstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    blckd_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "BlckdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    coll_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "CollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class CollateralAccountIdentificationType3ChoiceColr01600105(ISO20022MessageElement):
    tp: Optional[CollateralAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    prtry: Optional[GenericIdentification36Colr01600105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class CollateralAmount1Colr01600105(ISO20022MessageElement):
    coll_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "CollAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    rptd_ccy_and_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "RptdCcyAndAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    mkt_val_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "MktValAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    acrd_intrst_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    fees_and_comssns: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "FeesAndComssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class DateCode9ChoiceColr01600105(ISO20022MessageElement):
    cd: Optional[DateType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Colr01600105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class GenericIdentification78Colr01600105(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Colr01600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class NameAndAddress6Colr01600105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Colr01600105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )


@dataclass
class OtherIdentification1Colr01600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )


@dataclass
class OtherTypeOfCollateral3Colr01600105(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class PriceRateOrAmount3ChoiceColr01600105(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class ReportParameters6Colr01600105(ISO20022MessageElement):
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt_dt_and_tm: Optional[DateAndDateTime2ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "RptDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    frqcy: Optional[EventFrequency6Code] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    rpt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    clctn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class ReturnExcessCash1ChoiceColr01600105(ISO20022MessageElement):
    cd: Optional[ReturnExcessCash1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Colr01600105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Colr01600105(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText8Colr01600105(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace3Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Colr01600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Colr01600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Colr01600105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Colr01600105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )


@dataclass
class YieldedOrValueType1ChoiceColr01600105(ISO20022MessageElement):
    yldd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Yldd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    val_tp: Optional[PriceValueType1Code] = field(
        default=None,
        metadata={
            "name": "ValTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class Agreement4Colr01600105(ISO20022MessageElement):
    agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    agrmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    agrmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AgrmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    agrmt_frmwk: Optional[AgreementFramework1ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "AgrmtFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class BlockChainAddressWallet5Colr01600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CollateralAccount3Colr01600105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class DateFormat14ChoiceColr01600105(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    dt_cd: Optional[DateCode9ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class PartyIdentification178ChoiceColr01600105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr01600105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Colr01600105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class Price7Colr01600105(ISO20022MessageElement):
    tp: Optional[YieldedOrValueType1ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    val: Optional[PriceRateOrAmount3ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )


@dataclass
class ReturnExcessCash1Colr01600105(ISO20022MessageElement):
    rtr_xcss_csh_tp: Optional[ReturnExcessCash1ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "RtrXcssCshTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    csh_coll_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshCollCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SafekeepingPlaceFormat29ChoiceColr01600105(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText8Colr01600105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Colr01600105] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    prtry: Optional[GenericIdentification78Colr01600105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class SecurityIdentification19Colr01600105(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Colr01600105] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CollateralOwnership3Colr01600105(ISO20022MessageElement):
    prtry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    clnt_nm: Optional[PartyIdentification178ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "ClntNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class PartyIdentification242Colr01600105(ISO20022MessageElement):
    id: Optional[PartyIdentification178ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    ccpmmb_tp: Optional[CcpmemberType1Code] = field(
        default=None,
        metadata={
            "name": "CCPMmbTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class SummaryAmounts2Colr01600105(ISO20022MessageElement):
    thrshld_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "ThrshldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    thrshld_tp: Optional[ThresholdType1Code] = field(
        default=None,
        metadata={
            "name": "ThrshldTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    pre_hrcut_coll_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "PreHrcutCollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    adjstd_xpsr: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "AdjstdXpsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    coll_reqrd: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "CollReqrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    rtr_xcss_csh_and_coll_ccy: list[ReturnExcessCash1Colr01600105] = field(
        default_factory=list,
        metadata={
            "name": "RtrXcssCshAndCollCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    min_trf_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "MinTrfAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    rndg_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "RndgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    prvs_xpsr_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "PrvsXpsrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    prvs_coll_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "PrvsCollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    ttl_pdg_incmg_coll: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "TtlPdgIncmgColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    ttl_pdg_outgng_coll: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "TtlPdgOutgngColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    ttl_acrd_intrst_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "TtlAcrdIntrstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    ttl_fees: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "TtlFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class Obligation11Colr01600105(ISO20022MessageElement):
    pty_a: Optional[PartyIdentification242Colr01600105] = field(
        default=None,
        metadata={
            "name": "PtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    svcg_pty_a: Optional[PartyIdentification178ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    pty_b: Optional[PartyIdentification242Colr01600105] = field(
        default=None,
        metadata={
            "name": "PtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    svcg_pty_b: Optional[PartyIdentification178ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    coll_acct_id: Optional[CollateralAccount3Colr01600105] = field(
        default=None,
        metadata={
            "name": "CollAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet5Colr01600105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    xpsr_tp: Optional[ExposureType11Code] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    valtn_dt: Optional[DateAndDateTime2ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "ValtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )


@dataclass
class OtherCollateral10Colr01600105(ISO20022MessageElement):
    asst_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AsstNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lttr_of_cdt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LttrOfCdtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lttr_of_cdt_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "LttrOfCdtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    grnt_amt: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "GrntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    othr_tp_of_coll: Optional[OtherTypeOfCollateral3Colr01600105] = field(
        default=None,
        metadata={
            "name": "OthrTpOfColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    coll_ownrsh: Optional[CollateralOwnership3Colr01600105] = field(
        default=None,
        metadata={
            "name": "CollOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    isse_dt: Optional[DateFormat14ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    xpry_dt: Optional[DateFormat14ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    ltd_cvrg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LtdCvrgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    issr: Optional[PartyIdentification178ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    blckd_qty: Optional[FinancialInstrumentQuantity33ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "BlckdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    mkt_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    coll_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "CollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat29ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr01600105] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr01600105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class SecuritiesCollateral13Colr01600105(ISO20022MessageElement):
    asst_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AsstNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scty_id: Optional[SecurityIdentification19Colr01600105] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    mtrty_dt: Optional[DateAndDateTime2ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    coll_ownrsh: Optional[CollateralOwnership3Colr01600105] = field(
        default=None,
        metadata={
            "name": "CollOwnrsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    ltd_cvrg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LtdCvrgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    qty: Optional[FinancialInstrumentQuantity33ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    blckd_qty: Optional[FinancialInstrumentQuantity33ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "BlckdQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    pric: Optional[Price7Colr01600105] = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    mkt_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    coll_val: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "CollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Colr01600105] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet3Colr01600105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat29ChoiceColr01600105] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )


@dataclass
class Summary3Colr01600105(ISO20022MessageElement):
    xpsd_amt_pty_a: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "XpsdAmtPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    xpsd_amt_pty_b: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "XpsdAmtPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    xpsr_tp: Optional[ExposureType13Code] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    ttl_val_of_coll: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "TtlValOfColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    net_xcss_dfcit: Optional[ActiveCurrencyAndAmountColr01600105] = field(
        default=None,
        metadata={
            "name": "NetXcssDfcit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    net_xcss_dfcit_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "NetXcssDfcitInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    valtn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValtnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    reqd_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    summry_dtls: Optional[SummaryAmounts2Colr01600105] = field(
        default=None,
        metadata={
            "name": "SummryDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class CollateralValuation13Colr01600105(ISO20022MessageElement):
    coll_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_tp: Optional[CollateralType8Code] = field(
        default=None,
        metadata={
            "name": "CollTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    coll_drctn: Optional[CollateralDirection1Code] = field(
        default=None,
        metadata={
            "name": "CollDrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    sttlm_sts: Optional[SettlementStatus3Code] = field(
        default=None,
        metadata={
            "name": "SttlmSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    apld_xcss_ind: Optional[CollateralAppliedExcess1Code] = field(
        default=None,
        metadata={
            "name": "ApldXcssInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    valtn_amts: Optional[CollateralAmount1Colr01600105] = field(
        default=None,
        metadata={
            "name": "ValtnAmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    day_cnt_bsis: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "DayCntBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ccy_hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CcyHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    adjstd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjstdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    scties_coll: Optional[SecuritiesCollateral13Colr01600105] = field(
        default=None,
        metadata={
            "name": "SctiesColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    csh_coll: Optional[CashCollateral4Colr01600105] = field(
        default=None,
        metadata={
            "name": "CshColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    othr_coll: Optional[OtherCollateral10Colr01600105] = field(
        default=None,
        metadata={
            "name": "OthrColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class Collateral53Colr01600105(ISO20022MessageElement):
    acct_id: Optional[CollateralAccount3Colr01600105] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet5Colr01600105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    rpt_summry: Optional[Summary3Colr01600105] = field(
        default=None,
        metadata={
            "name": "RptSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    coll_valtn: list[CollateralValuation13Colr01600105] = field(
        default_factory=list,
        metadata={
            "name": "CollValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class CollateralAndExposureReportV05Colr01600105(ISO20022MessageElement):
    rpt_params: Optional[ReportParameters6Colr01600105] = field(
        default=None,
        metadata={
            "name": "RptParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    pgntn: Optional[Pagination1Colr01600105] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    oblgtn: Optional[Obligation11Colr01600105] = field(
        default=None,
        metadata={
            "name": "Oblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "required": True,
        },
    )
    agrmt: Optional[Agreement4Colr01600105] = field(
        default=None,
        metadata={
            "name": "Agrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )
    coll_rpt: list[Collateral53Colr01600105] = field(
        default_factory=list,
        metadata={
            "name": "CollRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Colr01600105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05",
        },
    )


@dataclass
class Colr01600105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05"

    coll_and_xpsr_rpt: Optional[CollateralAndExposureReportV05Colr01600105] = field(
        default=None,
        metadata={
            "name": "CollAndXpsrRpt",
            "type": "Element",
            "required": True,
        },
    )
