from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_029_001_05.enums import (
    NonFinancialPartySector1Code,
    TransactionOperationType8Code,
)
from python_iso20022.auth.enums import (
    AnyMic1Code,
    DerivativeEventType3Code,
    FinancialInstrumentContractType2Code,
    FinancialPartySectorType2Code,
    Frequency14Code,
    ModificationLevel1Code,
    NotAvailable1Code,
    NotReported1Code,
    Operation3Code,
    PartyNatureType1Code,
    ProductType4Code,
    WeekDay3Code,
)
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05"


@dataclass
class BasketQuery1Auth02900105:
    strr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Strr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 52,
        },
    )
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class DatePeriod1Auth02900105:
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )


@dataclass
class DateTimePeriod1Auth02900105:
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )


@dataclass
class GenericIdentification1Auth02900105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification175Auth02900105:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 72,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductClassificationCriteria1Auth02900105:
    clssfctn_fin_instrm: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ClssfctnFinInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{6,6}",
        },
    )
    unq_pdct_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class SecurityIdentification20ChoiceAuth02900105:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class SecurityIdentificationQueryCriteria1Auth02900105:
    isin: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth02900105:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CorporateSectorCriteria6Auth02900105:
    fisctr: list[FinancialPartySectorType2Code] = field(
        default_factory=list,
        metadata={
            "name": "FISctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    nfisctr: list[NonFinancialPartySector1Code] = field(
        default_factory=list,
        metadata={
            "name": "NFISctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class DateOrBlankQuery2ChoiceAuth02900105:
    rg: Optional[DatePeriod1Auth02900105] = field(
        default=None,
        metadata={
            "name": "Rg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class DateTimeOrBlankQuery1ChoiceAuth02900105:
    rg: Optional[DateTimePeriod1Auth02900105] = field(
        default=None,
        metadata={
            "name": "Rg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class IsinqueryCriteria1Auth02900105:
    class Meta:
        name = "ISINQueryCriteria1"

    idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class NaturalPersonIdentification2Auth02900105:
    id: Optional[GenericIdentification175Auth02900105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification38Auth02900105:
    id: Optional[GenericIdentification175Auth02900105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PostalAddress1Auth02900105:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecuritiesTradeVenueCriteria1ChoiceAuth02900105:
    mic: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    any_mic: Optional[AnyMic1Code] = field(
        default=None,
        metadata={
            "name": "AnyMIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class SecurityIdentificationQuery4ChoiceAuth02900105:
    isin: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    altrntv_instrm_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AltrntvInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 52,
        },
    )
    not_avlbl: Optional[NotAvailable1Code] = field(
        default=None,
        metadata={
            "name": "NotAvlbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    unq_pdct_idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 52,
        },
    )
    indx: list[SecurityIdentification20ChoiceAuth02900105] = field(
        default_factory=list,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    bskt: list[BasketQuery1Auth02900105] = field(
        default_factory=list,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class SupplementaryData1Auth02900105:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth02900105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )


@dataclass
class TradeQueryExecutionFrequency3Auth02900105:
    frqcy_tp: Optional[Frequency14Code] = field(
        default=None,
        metadata={
            "name": "FrqcyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    dlvry_day: list[WeekDay3Code] = field(
        default_factory=list,
        metadata={
            "name": "DlvryDay",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    day_of_mnth: list[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "DayOfMnth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_inclusive": Decimal("1"),
            "max_inclusive": Decimal("31"),
        },
    )


@dataclass
class UpiqueryCriteria1Auth02900105:
    class Meta:
        name = "UPIQueryCriteria1"

    idr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Idr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_length": 1,
            "max_length": 52,
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class NameAndAddress5Auth02900105:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Auth02900105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class NaturalPersonIdentification3Auth02900105:
    id: Optional[NaturalPersonIdentification2Auth02900105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth02900105:
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth02900105] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class TradeAdditionalQueryCriteria9Auth02900105:
    actn_tp: list[TransactionOperationType8Code] = field(
        default_factory=list,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    exctn_vn: Optional[SecuritiesTradeVenueCriteria1ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "ExctnVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    ntr_of_ctr_pty: Optional[PartyNatureType1Code] = field(
        default=None,
        metadata={
            "name": "NtrOfCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    corp_sctr: Optional[CorporateSectorCriteria6Auth02900105] = field(
        default=None,
        metadata={
            "name": "CorpSctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    asst_clss: list[ProductType4Code] = field(
        default_factory=list,
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    pdct_clssfctn: Optional[ProductClassificationCriteria1Auth02900105] = field(
        default=None,
        metadata={
            "name": "PdctClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    lvl: Optional[ModificationLevel1Code] = field(
        default=None,
        metadata={
            "name": "Lvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    evt_tp: list[DerivativeEventType3Code] = field(
        default_factory=list,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class TradeDateTimeQueryCriteria6Auth02900105:
    rptg_dt_tm: Optional[DateTimePeriod1Auth02900105] = field(
        default=None,
        metadata={
            "name": "RptgDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    exctn_dt_tm: Optional[DateTimePeriod1Auth02900105] = field(
        default=None,
        metadata={
            "name": "ExctnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    mtrty_dt: Optional[DateOrBlankQuery2ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    fctv_dt: Optional[DatePeriod1Auth02900105] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    valtn_dt_tm: Optional[DateTimePeriod1Auth02900105] = field(
        default=None,
        metadata={
            "name": "ValtnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    xprtn_dt: Optional[DateOrBlankQuery2ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    early_termntn_dt: Optional[DatePeriod1Auth02900105] = field(
        default=None,
        metadata={
            "name": "EarlyTermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    coll_tm_stmp: Optional[DateTimeOrBlankQuery1ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "CollTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    hstrcl_as_of_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "HstrclAsOfDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class TradeRecurrentQuery7Auth02900105:
    qry_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 1000,
        },
    )
    frqcy: list[TradeQueryExecutionFrequency3Auth02900105] = field(
        default_factory=list,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "min_occurs": 1,
        },
    )
    vld_until: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "VldUntil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )


@dataclass
class TradeSecurityIdentificationQueryCriteria3Auth02900105:
    oprtr: Optional[Operation3Code] = field(
        default=None,
        metadata={
            "name": "Oprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    id: list[SecurityIdentificationQueryCriteria1Auth02900105] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    ctrct_tp: list[FinancialInstrumentContractType2Code] = field(
        default_factory=list,
        metadata={
            "name": "CtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    isin: list[IsinqueryCriteria1Auth02900105] = field(
        default_factory=list,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    unq_pdct_idr: list[UpiqueryCriteria1Auth02900105] = field(
        default_factory=list,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    undrlyg_instrm_id: list[SecurityIdentificationQuery4ChoiceAuth02900105] = field(
        default_factory=list,
        metadata={
            "name": "UndrlygInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class LegalPersonIdentification1Auth02900105:
    id: Optional[OrganisationIdentification15ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification121ChoiceAuth02900105:
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lgl_ntty_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglNttyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Auth02900105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    prtry_id: Optional[GenericIdentification1Auth02900105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class TradePartyIdentificationQuery11ChoiceAuth02900105:
    id: list[OrganisationIdentification15ChoiceAuth02900105] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class PartyIdentification248ChoiceAuth02900105:
    lgl: Optional[LegalPersonIdentification1Auth02900105] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    ntrl: Optional[NaturalPersonIdentification3Auth02900105] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class TradePartyIdentificationQuery10ChoiceAuth02900105:
    id: list[PartyIdentification248ChoiceAuth02900105] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    not_rptd: Optional[NotReported1Code] = field(
        default=None,
        metadata={
            "name": "NotRptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class TradePartyQueryCriteria7Auth02900105:
    oprtr: Optional[Operation3Code] = field(
        default=None,
        metadata={
            "name": "Oprtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    rptg_ctr_pty: Optional[TradePartyIdentificationQuery10ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    othr_ctr_pty: Optional[TradePartyIdentificationQuery10ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    bnfcry: Optional[TradePartyIdentificationQuery10ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    ntty_rspnsbl_for_rpt: Optional[
        TradePartyIdentificationQuery11ChoiceAuth02900105
    ] = field(
        default=None,
        metadata={
            "name": "NttyRspnsblForRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    submitg_agt: Optional[TradePartyIdentificationQuery11ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "SubmitgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    brkr: Optional[TradePartyIdentificationQuery11ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    ccp: Optional[TradePartyIdentificationQuery11ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    clr_mmb: Optional[TradePartyIdentificationQuery10ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class TradeQueryCriteria14Auth02900105:
    trad_life_cycl_hstry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TradLifeCyclHstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    mrgn_life_cycl_hstry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MrgnLifeCyclHstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    outsdng_trad_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OutsdngTradInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    trad_pty_crit: Optional[TradePartyQueryCriteria7Auth02900105] = field(
        default=None,
        metadata={
            "name": "TradPtyCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    fin_instrm_crit: Optional[TradeSecurityIdentificationQueryCriteria3Auth02900105] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmCrit",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            },
        )
    )
    tm_crit: Optional[TradeDateTimeQueryCriteria6Auth02900105] = field(
        default=None,
        metadata={
            "name": "TmCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    othr_crit: Optional[TradeAdditionalQueryCriteria9Auth02900105] = field(
        default=None,
        metadata={
            "name": "OthrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class TradeReportQuery18ChoiceAuth02900105:
    ad_hoc_qry: Optional[TradeQueryCriteria14Auth02900105] = field(
        default=None,
        metadata={
            "name": "AdHocQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )
    rcrnt_qry: Optional[TradeRecurrentQuery7Auth02900105] = field(
        default=None,
        metadata={
            "name": "RcrntQry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class DerivativesTradeReportQueryV05Auth02900105:
    rqstng_authrty: Optional[PartyIdentification121ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "RqstngAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    trad_qry_data: Optional[TradeReportQuery18ChoiceAuth02900105] = field(
        default=None,
        metadata={
            "name": "TradQryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth02900105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05",
        },
    )


@dataclass
class Auth02900105:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.029.001.05"

    derivs_trad_rpt_qry: Optional[DerivativesTradeReportQueryV05Auth02900105] = field(
        default=None,
        metadata={
            "name": "DerivsTradRptQry",
            "type": "Element",
            "required": True,
        },
    )
