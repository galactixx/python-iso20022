from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import (
    EventFrequency1Code,
    ShortLong1Code,
    StatementUpdateType1Code,
)
from python_iso20022.semt.enums import StatementBasis1Code
from python_iso20022.semt.semt_024_001_01.enums import (
    BalanceType13Code,
    FinancialAssetBalanceType1Code,
    FinancialAssetTypeCategory1Code,
    StatementSource1Code,
    TypeOfPrice30Code,
    Unrealised1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01"


@dataclass
class ActiveOrHistoricCurrencyAnd13DecimalAmountSemt02400101:
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
class ActiveOrHistoricCurrencyAndAmountSemt02400101:
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
class DateAndDateTimeChoiceSemt02400101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class DatePeriodDetailsSemt02400101:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification29Semt02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Semt02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt02400101:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaginationSemt02400101:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt02400101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AccountIdentification5Semt02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class AmountAndDirection30Semt02400101:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt02400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class AmountAndDirection31Semt02400101:
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSemt02400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class BalanceType6ChoiceSemt02400101:
    cd: Optional[BalanceType13Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class Frequency8ChoiceSemt02400101:
    cd: Optional[EventFrequency1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class OtherIdentification1Semt02400101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )


@dataclass
class PriceAndDirection1Semt02400101:
    val: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt02400101] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class StatementBasis6ChoiceSemt02400101:
    cd: Optional[StatementBasis1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class StatementSource1ChoiceSemt02400101:
    cd: Optional[StatementSource1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class SupplementaryData1Semt02400101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt02400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )


@dataclass
class TypeOfPrice27ChoiceSemt02400101:
    cd: Optional[TypeOfPrice30Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification29Semt02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class UpdateType4ChoiceSemt02400101:
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class AmountAndRate2Semt02400101:
    amt: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class BalanceType7ChoiceSemt02400101:
    cd: Optional[FinancialAssetBalanceType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prtry: Optional[GenericIdentification30Semt02400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    acct: Optional[AccountIdentification5Semt02400101] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class PriceValueAndRate4Semt02400101:
    val: Optional[PriceAndDirection1Semt02400101] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class Report4Semt02400101:
    rpt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "pattern": r"[0-9]{1,5}",
        },
    )
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt_dt_tm: Optional[DateAndDateTimeChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "RptDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    cre_dt_tm: Optional[DateAndDateTimeChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    prvs_rpt_dt_tm: Optional[DateAndDateTimeChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "PrvsRptDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    frqcy: Optional[Frequency8ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    upd_tp: Optional[UpdateType4ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    rpt_bsis: Optional[StatementBasis6ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "RptBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    rpt_prd: Optional[DatePeriodDetailsSemt02400101] = field(
        default=None,
        metadata={
            "name": "RptPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    rpt_src: Optional[StatementSource1ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "RptSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    audtd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudtdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class SecuritiesAccount21Semt02400101:
    acct: Optional[AccountIdentification5Semt02400101] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    sub_acct: Optional[AccountIdentification5Semt02400101] = field(
        default=None,
        metadata={
            "name": "SubAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    rptg_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    fxrate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FXRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SecurityIdentification14Semt02400101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: list[OtherIdentification1Semt02400101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class BalanceDetails6Semt02400101:
    ctgy: Optional[FinancialAssetTypeCategory1Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    tp: Optional[BalanceType7ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    urlsd: Optional[Unrealised1Code] = field(
        default=None,
        metadata={
            "name": "Urlsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    amt: Optional[AmountAndDirection31Semt02400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )


@dataclass
class PriceInformation10Semt02400101:
    cur_pric: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt02400101] = field(
        default=None,
        metadata={
            "name": "CurPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    tp: Optional[TypeOfPrice27ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    prvs_pric: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt02400101] = field(
        default=None,
        metadata={
            "name": "PrvsPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    amt_of_chng: Optional[PriceValueAndRate4Semt02400101] = field(
        default=None,
        metadata={
            "name": "AmtOfChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class BalanceDetails5Semt02400101:
    tp: Optional[BalanceType6ChoiceSemt02400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    urlsd: Optional[Unrealised1Code] = field(
        default=None,
        metadata={
            "name": "Urlsd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    amt: Optional[AmountAndDirection31Semt02400101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    dtld_bal: list[BalanceDetails6Semt02400101] = field(
        default_factory=list,
        metadata={
            "name": "DtldBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class InvestmentFund1Semt02400101:
    fin_instrm_id: Optional[SecurityIdentification14Semt02400101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ttl_units_outsdng: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlUnitsOutsdng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    txnl_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TxnlUnits",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ttl_val: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    pric: list[PriceInformation10Semt02400101] = field(
        default_factory=list,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    splmtry_data: list[SupplementaryData1Semt02400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class PortfolioBalance1Semt02400101:
    summry_bal: list[BalanceDetails5Semt02400101] = field(
        default_factory=list,
        metadata={
            "name": "SummryBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    dtld_bal: list[BalanceDetails6Semt02400101] = field(
        default_factory=list,
        metadata={
            "name": "DtldBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class TotalPortfolioValuation1Semt02400101:
    ttl_prtfl_val: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlPrtflVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    prvs_ttl_prtfl_val: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "PrvsTtlPrtflVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    ttl_prtfl_val_chng: Optional[AmountAndRate2Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlPrtflValChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    ttl_book_val: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlBookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    prvs_ttl_book_val: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "PrvsTtlBookVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    ttl_book_val_chng: Optional[AmountAndRate2Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlBookValChng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    ttl_rcts: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlRcts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    ttl_dsbrsmnts: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlDsbrsmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    incm_rcvd: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "IncmRcvd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    expnss_pd: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "ExpnssPd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    urlsd_gn_or_loss: Optional[AmountAndDirection31Semt02400101] = field(
        default=None,
        metadata={
            "name": "UrlsdGnOrLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    realsd_gn_or_loss: Optional[AmountAndDirection31Semt02400101] = field(
        default=None,
        metadata={
            "name": "RealsdGnOrLoss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    acrd_incm: Optional[AmountAndDirection30Semt02400101] = field(
        default=None,
        metadata={
            "name": "AcrdIncm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    invstmt_fnd_dtls: list[InvestmentFund1Semt02400101] = field(
        default_factory=list,
        metadata={
            "name": "InvstmtFndDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class TotalPortfolioValuationReportV01Semt02400101:
    pgntn: Optional[PaginationSemt02400101] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    rpt_gnl_dtls: Optional[Report4Semt02400101] = field(
        default=None,
        metadata={
            "name": "RptGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    acct_dtls: Optional[SecuritiesAccount21Semt02400101] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    ttl_prtfl_valtn: Optional[TotalPortfolioValuation1Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlPrtflValtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
            "required": True,
        },
    )
    bal: Optional[PortfolioBalance1Semt02400101] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )
    splmtry_data: Optional[SupplementaryData1Semt02400101] = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01",
        },
    )


@dataclass
class Semt02400101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01"

    ttl_prtfl_valtn_rpt: Optional[TotalPortfolioValuationReportV01Semt02400101] = field(
        default=None,
        metadata={
            "name": "TtlPrtflValtnRpt",
            "type": "Element",
            "required": True,
        },
    )
