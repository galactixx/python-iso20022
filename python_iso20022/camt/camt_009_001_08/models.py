from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.enums import LimitType3Code, QueryType2Code
from python_iso20022.enums import AddressType2Code, CreditDebitCode

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08"


@dataclass
class AccountSchemeName1ChoiceCamt00900108(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountRangeBoundary1Camt00900108(ISO20022MessageElement):
    bdry_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BdryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    incl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt00900108(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt00900108(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt00900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt00900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LimitReturnCriteria2Camt00900108(ISO20022MessageElement):
    start_dt_tm_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StartDtTmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    sts_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    usd_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsdAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    usd_pctg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsdPctgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class MarketInfrastructureIdentification1ChoiceCamt00900108(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PercentageRangeBoundary1Camt00900108(ISO20022MessageElement):
    bdry_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BdryRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    incl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )


@dataclass
class Period2Camt00900108(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt00900108(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceCamt00900108(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    prtry: Optional[GenericIdentification30Camt00900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt00900108(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPeriod2ChoiceCamt00900108(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    prd: Optional[Period2Camt00900108] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class FromToAmountRange1Camt00900108(ISO20022MessageElement):
    fr_amt: Optional[AmountRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )
    to_amt: Optional[AmountRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )


@dataclass
class FromToPercentageRange1Camt00900108(ISO20022MessageElement):
    fr: Optional[PercentageRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )
    to: Optional[PercentageRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )


@dataclass
class GenericAccountIdentification1Camt00900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt00900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LimitType1ChoiceCamt00900108(ISO20022MessageElement):
    cd: Optional[LimitType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RequestType4ChoiceCamt00900108(ISO20022MessageElement):
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt00900108] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class SupplementaryData1Camt00900108(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt00900108] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )


@dataclass
class SystemIdentification2ChoiceCamt00900108(ISO20022MessageElement):
    mkt_infrstrctr_id: Optional[
        MarketInfrastructureIdentification1ChoiceCamt00900108
    ] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt00900108(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt00900108] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class ImpliedCurrencyAmountRange1ChoiceCamt00900108(ISO20022MessageElement):
    fr_amt: Optional[AmountRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    to_amt: Optional[AmountRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    fr_to_amt: Optional[FromToAmountRange1Camt00900108] = field(
        default=None,
        metadata={
            "name": "FrToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    eqamt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EQAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    neqamt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NEQAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class MessageHeader9Camt00900108(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class PercentageRange1ChoiceCamt00900108(ISO20022MessageElement):
    fr: Optional[PercentageRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    to: Optional[PercentageRangeBoundary1Camt00900108] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    fr_to: Optional[FromToPercentageRange1Camt00900108] = field(
        default=None,
        metadata={
            "name": "FrTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    eq: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EQ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    neq: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NEQ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class PostalAddress27Camt00900108(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ActiveCurrencyAndAmountRange3Camt00900108(ISO20022MessageElement):
    amt: Optional[ImpliedCurrencyAmountRange1ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class BranchData5Camt00900108(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00900108] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Camt00900108(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt00900108] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00900108] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt00900108] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class ImpliedCurrencyAndAmountRange1Camt00900108(ISO20022MessageElement):
    amt: Optional[ImpliedCurrencyAmountRange1ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class ActiveAmountRange3ChoiceCamt00900108(ISO20022MessageElement):
    impld_ccy_and_amt_rg: Optional[ImpliedCurrencyAndAmountRange1Camt00900108] = field(
        default=None,
        metadata={
            "name": "ImpldCcyAndAmtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    ccy_and_amt_rg: Optional[ActiveCurrencyAndAmountRange3Camt00900108] = field(
        default=None,
        metadata={
            "name": "CcyAndAmtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Camt00900108(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Camt00900108] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Camt00900108] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class LimitSearchCriteria7Camt00900108(ISO20022MessageElement):
    sys_id: Optional[SystemIdentification2ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    bil_lmt_ctr_pty_id: list[
        BranchAndFinancialInstitutionIdentification8Camt00900108
    ] = field(
        default_factory=list,
        metadata={
            "name": "BilLmtCtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    dflt_lmt_tp: list[LimitType1ChoiceCamt00900108] = field(
        default_factory=list,
        metadata={
            "name": "DfltLmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    cur_lmt_tp: list[LimitType1ChoiceCamt00900108] = field(
        default_factory=list,
        metadata={
            "name": "CurLmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    acct_ownr: Optional[BranchAndFinancialInstitutionIdentification8Camt00900108] = (
        field(
            default=None,
            metadata={
                "name": "AcctOwnr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            },
        )
    )
    acct_id: Optional[AccountIdentification4ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    usd_amt: Optional[ActiveAmountRange3ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "UsdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    usd_pctg: Optional[PercentageRange1ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "UsdPctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    lmt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "LmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lmt_amt: Optional[ActiveAmountRange3ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "LmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    lmt_vld_as_of_dt: Optional[DateAndPeriod2ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "LmtVldAsOfDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class LimitCriteria7Camt00900108(ISO20022MessageElement):
    new_qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewQryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sch_crit: list[LimitSearchCriteria7Camt00900108] = field(
        default_factory=list,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    rtr_crit: Optional[LimitReturnCriteria2Camt00900108] = field(
        default=None,
        metadata={
            "name": "RtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class LimitCriteria7ChoiceCamt00900108(ISO20022MessageElement):
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_crit: Optional[LimitCriteria7Camt00900108] = field(
        default=None,
        metadata={
            "name": "NewCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class LimitQuery5Camt00900108(ISO20022MessageElement):
    qry_tp: Optional[QueryType2Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    lmt_crit: Optional[LimitCriteria7ChoiceCamt00900108] = field(
        default=None,
        metadata={
            "name": "LmtCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class GetLimitV08Camt00900108(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader9Camt00900108] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
            "required": True,
        },
    )
    lmt_qry_def: Optional[LimitQuery5Camt00900108] = field(
        default=None,
        metadata={
            "name": "LmtQryDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )
    splmtry_data: list[SupplementaryData1Camt00900108] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08",
        },
    )


@dataclass
class Camt00900108(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08"

    get_lmt: Optional[GetLimitV08Camt00900108] = field(
        default=None,
        metadata={
            "name": "GetLmt",
            "type": "Element",
            "required": True,
        },
    )
