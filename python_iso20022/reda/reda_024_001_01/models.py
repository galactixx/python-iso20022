from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01"


@dataclass
class ActiveCurrencyAndAmountReda02400101(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountReda02400101(ISO20022MessageElement):
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
class GenericIdentification36Reda02400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceReda02400101(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Reda02400101(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda02400101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountOrCoefficientPrice2ChoiceReda02400101(ISO20022MessageElement):
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amt_wth_ccy: Optional[ActiveOrHistoricCurrencyAndAmountReda02400101] = field(
        default=None,
        metadata={
            "name": "AmtWthCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    coeff: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Coeff",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class ForeignExchangeTerms23Reda02400101(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rsltg_amt: Optional[ActiveCurrencyAndAmountReda02400101] = field(
        default=None,
        metadata={
            "name": "RsltgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )


@dataclass
class OtherIdentification1Reda02400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceReda02400101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )


@dataclass
class PostalAddress1Reda02400101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceRateOrAmount6ChoiceReda02400101(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amt_wth_ccy: Optional[ActiveOrHistoricCurrencyAndAmountReda02400101] = field(
        default=None,
        metadata={
            "name": "AmtWthCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class SupplementaryData1Reda02400101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda02400101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Reda02400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Reda02400101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class SecurityIdentification19Reda02400101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Reda02400101] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CollateralValue5Reda02400101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification19Reda02400101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )
    valtn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )
    valtn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValtnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    valtn_pric: Optional[AmountOrCoefficientPrice2ChoiceReda02400101] = field(
        default=None,
        metadata={
            "name": "ValtnPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )
    valtn_cls_lk_pric: Optional[AmountOrCoefficientPrice2ChoiceReda02400101] = field(
        default=None,
        metadata={
            "name": "ValtnClsLkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    clean_pric: Optional[PriceRateOrAmount6ChoiceReda02400101] = field(
        default=None,
        metadata={
            "name": "CleanPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    acrd_intrst: Optional[PriceRateOrAmount6ChoiceReda02400101] = field(
        default=None,
        metadata={
            "name": "AcrdIntrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    cls_lk_hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ClsLkHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    pool_fctr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PoolFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fx: Optional[ForeignExchangeTerms23Reda02400101] = field(
        default=None,
        metadata={
            "name": "FX",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class PartyIdentification120ChoiceReda02400101(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Reda02400101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Reda02400101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class PartyIdentification136Reda02400101(ISO20022MessageElement):
    id: Optional[PartyIdentification120ChoiceReda02400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class SystemPartyIdentification8Reda02400101(ISO20022MessageElement):
    id: Optional[PartyIdentification136Reda02400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )
    rspnsbl_pty_id: Optional[PartyIdentification136Reda02400101] = field(
        default=None,
        metadata={
            "name": "RspnsblPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class SystemPartyIdentification2ChoiceReda02400101(ISO20022MessageElement):
    org_id: Optional[PartyIdentification136Reda02400101] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    cmbnd_id: Optional[SystemPartyIdentification8Reda02400101] = field(
        default=None,
        metadata={
            "name": "CmbndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class CollateralValueCreationRequestV01Reda02400101(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Reda02400101] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )
    coll_val: list[CollateralValue5Reda02400101] = field(
        default_factory=list,
        metadata={
            "name": "CollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "min_occurs": 1,
        },
    )
    pty_id: Optional[SystemPartyIdentification2ChoiceReda02400101] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Reda02400101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01",
        },
    )


@dataclass
class Reda02400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01"

    coll_val_cre_req: Optional[CollateralValueCreationRequestV01Reda02400101] = field(
        default=None,
        metadata={
            "name": "CollValCreReq",
            "type": "Element",
            "required": True,
        },
    )
