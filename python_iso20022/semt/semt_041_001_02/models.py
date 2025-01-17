from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.enums import (
    AddressType2Code,
    BeneficiaryCertificationType4Code,
    EventFrequency7Code,
    FormOfSecurity1Code,
    InvestmentFundRole2Code,
    OrderOriginatorEligibility1Code,
    PhysicalTransferType1Code,
    StatementUpdateType1Code,
)
from python_iso20022.semt.semt_041_001_02.enums import (
    FrequencyGranularityType1Code,
    PersonIdentificationType6Code,
    PriceSource2Code,
    SecuritiesBalanceType14Code,
    SenderBusinessRole1Code,
    TypeOfPrice13Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02"


@dataclass
class ActiveOrHistoricCurrencyAnd13DecimalAmountSemt04100102:
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
class DateAndDateTimeChoiceSemt04100102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceSemt04100102:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification30Semt04100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Semt04100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification56Semt04100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Bal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class IdentificationSource3ChoiceSemt04100102:
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Semt04100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class Number3ChoiceSemt04100102:
    shrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shrt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[0-9]{3}",
        },
    )
    lng: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[0-9]{5}",
        },
    )


@dataclass
class PaginationSemt04100102:
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class Period2Semt04100102:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Semt04100102:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BeneficiaryCertificationType9ChoiceSemt04100102:
    cd: Optional[BeneficiaryCertificationType4Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class DatePeriod1ChoiceSemt04100102:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    dt_mnth: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "DtMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    fr_dt_to_dt: Optional[Period2Semt04100102] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class Frequency22ChoiceSemt04100102:
    cd: Optional[EventFrequency7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class OtherIdentification1Semt04100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class OtherIdentification4ChoiceSemt04100102:
    cd: Optional[PersonIdentificationType6Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification36Semt04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class PostalAddress1Semt04100102:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmountChoiceSemt04100102:
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSemt04100102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class Role5ChoiceSemt04100102:
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification36Semt04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class SecuritiesAccount19Semt04100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Semt04100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SubBalanceQuantity5ChoiceSemt04100102:
    qty: Optional[FinancialInstrumentQuantity1ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification56Semt04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class SubBalanceType9ChoiceSemt04100102:
    cd: Optional[SecuritiesBalanceType14Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class SupplementaryData1Semt04100102:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Semt04100102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class UpdateType4ChoiceSemt04100102:
    cd: Optional[StatementUpdateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Semt04100102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AlternateIdentification4Semt04100102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[OtherIdentification4ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    xpry_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    issr_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class NameAndAddress5Semt04100102:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Semt04100102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class Price6Semt04100102:
    rate_or_amt: Optional[PriceRateOrAmountChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "RateOrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    tp: Optional[TypeOfPrice13Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    src: Optional[PriceSource2Code] = field(
        default=None,
        metadata={
            "name": "Src",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class SecurityIdentification19Semt04100102:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Statement59Semt04100102:
    sndr_biz_role: Optional[SenderBusinessRole1Code] = field(
        default=None,
        metadata={
            "name": "SndrBizRole",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    stmt_nb: Optional[Number3ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "StmtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    qry_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    stmt_dt_tm: Optional[DateAndDateTimeChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "StmtDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    stmt_prd: Optional[DatePeriod1ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "StmtPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    frqcy: Optional[Frequency22ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    frqcy_grnlrty: Optional[FrequencyGranularityType1Code] = field(
        default=None,
        metadata={
            "name": "FrqcyGrnlrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    upd_tp: Optional[UpdateType4ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "UpdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    actvty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ActvtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class SubBalanceBreakdown1Semt04100102:
    sub_bal_tp: Optional[SubBalanceType9ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "SubBalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    qty: Optional[SubBalanceQuantity5ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )


@dataclass
class FinancialInstrumentAggregateBalance2Semt04100102:
    sttld_bal: Optional[FinancialInstrumentQuantity1ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "SttldBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    tradd_bal: Optional[FinancialInstrumentQuantity1ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "TraddBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_brkdwn: list[SubBalanceBreakdown1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalBrkdwn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class PartyIdentification71ChoiceSemt04100102:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Semt04100102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Semt04100102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class FinancialInstrumentAggregateBalance1ChoiceSemt04100102:
    hldgs_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HldgsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    hldg_bal: Optional[FinancialInstrumentAggregateBalance2Semt04100102] = field(
        default=None,
        metadata={
            "name": "HldgBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class PartyIdentification100Semt04100102:
    id: Optional[PartyIdentification71ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class BeneficialOwner2Semt04100102:
    bnfcl_ownr_id: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "BnfclOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    addtl_id: Optional[AlternateIdentification4Semt04100102] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    ntlty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ntlty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    dmcl_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    non_dmcl_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonDmclCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    certfctn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CertfctnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    certfctn_tp: Optional[BeneficiaryCertificationType9ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "CertfctnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class FinancialInstrumentAggregateBalance1Semt04100102:
    itm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ItmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    hldgs: Optional[FinancialInstrumentAggregateBalance1ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Hldgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    pric: list[Price6Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class Intermediary29Semt04100102:
    id: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    role: Optional[Role5ChoiceSemt04100102] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    ordr_orgtr_elgblty: Optional[OrderOriginatorEligibility1Code] = field(
        default=None,
        metadata={
            "name": "OrdrOrgtrElgblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AggregateHoldingBalance1Semt04100102:
    fin_instrm_id: Optional[SecurityIdentification19Semt04100102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    hldg_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "HldgForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    hldg_phys_tp: Optional[PhysicalTransferType1Code] = field(
        default=None,
        metadata={
            "name": "HldgPhysTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_for_fin_instrm: list[FinancialInstrumentAggregateBalance1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalForFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AggregateHoldingBalance2Semt04100102:
    fin_instrm_id: Optional[SecurityIdentification19Semt04100102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bal_for_fin_instrm: list[FinancialInstrumentAggregateBalance1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalForFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AggregateHoldingBalance3Semt04100102:
    bal_for_acct: list[AggregateHoldingBalance1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalForAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "min_occurs": 1,
        },
    )
    agt: list[Intermediary29Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel19Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel18Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl9: list[AccountSubLevel19Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl9",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl9_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl9Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel17Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl8: list[AccountSubLevel18Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl8",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl8_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl8Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel16Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl7: list[AccountSubLevel17Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl7",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl7_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl7Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel15Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl6: list[AccountSubLevel16Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl6",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl6_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl6Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel14Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl5: list[AccountSubLevel15Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl5_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl5Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel13Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl4: list[AccountSubLevel14Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl4_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl4Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel12Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl3: list[AccountSubLevel13Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl3_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl3Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class AccountSubLevel11Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl2: list[AccountSubLevel12Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl2_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl2Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class SafekeepingAccount7Semt04100102:
    acct_id: Optional[SecuritiesAccount19Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    acct_svcr: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    bnfcl_ownr: list[BeneficialOwner2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BnfclOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    bal_dtls: list[AggregateHoldingBalance3Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "BalDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl1: list[AccountSubLevel11Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    acct_sub_lvl1_diff: list[AggregateHoldingBalance2Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "AcctSubLvl1Diff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class SecuritiesBalanceTransparencyReportV02Semt04100102:
    msg_id: Optional[MessageIdentification1Semt04100102] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    sndr_id: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "SndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    rcvr_id: Optional[PartyIdentification100Semt04100102] = field(
        default=None,
        metadata={
            "name": "RcvrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    pgntn: Optional[PaginationSemt04100102] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    stmt_gnl_dtls: Optional[Statement59Semt04100102] = field(
        default=None,
        metadata={
            "name": "StmtGnlDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
            "required": True,
        },
    )
    sfkpg_acct_and_hldgs: list[SafekeepingAccount7Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SfkpgAcctAndHldgs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Semt04100102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02",
        },
    )


@dataclass
class Semt04100102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02"

    scties_bal_trnsprncy_rpt: Optional[
        SecuritiesBalanceTransparencyReportV02Semt04100102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesBalTrnsprncyRpt",
            "type": "Element",
            "required": True,
        },
    )
