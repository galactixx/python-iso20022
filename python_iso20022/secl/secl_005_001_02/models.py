from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    ClearingAccountType1Code,
    CollateralType1Code,
    CreditDebitCode,
    EventFrequency6Code,
    ShortLong1Code,
    TypeOfIdentification1Code,
)
from python_iso20022.secl.secl_005_001_02.enums import (
    MarginProduct1Code,
    MarginType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02"


@dataclass
class ActiveCurrencyAndAmountSecl00500102(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSecl00500102(ISO20022MessageElement):
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
class DateAndDateTimeChoiceSecl00500102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class GenericIdentification29Secl00500102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Secl00500102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSecl00500102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaginationSecl00500102(ISO20022MessageElement):
    pg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "pattern": r"[0-9]{1,5}",
        },
    )
    last_pg_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastPgInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation1Secl00500102(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class PostalAddress2Secl00500102(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Secl00500102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Amount2Secl00500102(ISO20022MessageElement):
    orgnl_ccy_amt: Optional[ActiveCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "OrgnlCcyAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    rptg_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RptgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class AmountAndDirection20Secl00500102(ISO20022MessageElement):
    amt: Optional[ActiveOrHistoricCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class Collateral6Secl00500102(ISO20022MessageElement):
    pst_hrcut_val: Optional[ActiveCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "PstHrcutVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    mkt_val: Optional[ActiveCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    coll_tp: Optional[CollateralType1Code] = field(
        default=None,
        metadata={
            "name": "CollTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )


@dataclass
class IdentificationType6ChoiceSecl00500102(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Secl00500102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class MarginProductType1ChoiceSecl00500102(ISO20022MessageElement):
    cd: Optional[MarginProduct1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Secl00500102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class MarginResult1ChoiceSecl00500102(ISO20022MessageElement):
    xcss_amt: Optional[ActiveCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "XcssAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    dfcit_amt: Optional[ActiveCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "DfcitAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class MarginType1ChoiceSecl00500102(ISO20022MessageElement):
    cd: Optional[MarginType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Secl00500102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class NameAndAddress6Secl00500102(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Secl00500102] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )


@dataclass
class OtherIdentification1Secl00500102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentification35ChoiceSecl00500102(ISO20022MessageElement):
    bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "BIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification29Secl00500102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class ReportParameters3Secl00500102(ISO20022MessageElement):
    rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rpt_dt_and_tm: Optional[DateAndDateTimeChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "RptDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    rpt_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    clctn_dt_and_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClctnDtAndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    frqcy: Optional[EventFrequency6Code] = field(
        default=None,
        metadata={
            "name": "Frqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    rpt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "pattern": r"[0-9]{5}",
        },
    )


@dataclass
class SecuritiesAccount18Secl00500102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[ClearingAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupplementaryData1Secl00500102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Secl00500102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )


@dataclass
class AlternatePartyIdentification4Secl00500102(ISO20022MessageElement):
    id_tp: Optional[IdentificationType6ChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Margin4Secl00500102(ISO20022MessageElement):
    tp: Optional[MarginType1ChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    amt: Optional[Amount2Secl00500102] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class MarginCalculation1Secl00500102(ISO20022MessageElement):
    ttl_mrgn_amt: Optional[AmountAndDirection20Secl00500102] = field(
        default=None,
        metadata={
            "name": "TtlMrgnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    coll_on_dpst: list[Collateral6Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "CollOnDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    min_rqrmnt_dpst: Optional[ActiveCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "MinRqrmntDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrgn_rslt: Optional[MarginResult1ChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "MrgnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class PartyIdentification33ChoiceSecl00500102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification29Secl00500102] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Secl00500102] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class SecurityIdentification14Secl00500102(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: list[OtherIdentification1Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TotalVariationMargin1Secl00500102(ISO20022MessageElement):
    shrt_lng_ind: Optional[ShortLong1Code] = field(
        default=None,
        metadata={
            "name": "ShrtLngInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    amt_dtls: Optional[Amount2Secl00500102] = field(
        default=None,
        metadata={
            "name": "AmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )


@dataclass
class PartyIdentificationAndAccount31Secl00500102(ISO20022MessageElement):
    id: Optional[PartyIdentification33ChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    altrn_id: Optional[AlternatePartyIdentification4Secl00500102] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    addtl_inf: Optional[PartyTextInformation1Secl00500102] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    clr_acct: Optional[SecuritiesAccount18Secl00500102] = field(
        default=None,
        metadata={
            "name": "ClrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class VariationMargin3Secl00500102(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification14Secl00500102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    ttl_vartn_mrgn: list[TotalVariationMargin1Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "TtlVartnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_occurs": 1,
        },
    )
    ttl_mrk_to_mkt: Optional[Amount2Secl00500102] = field(
        default=None,
        metadata={
            "name": "TtlMrkToMkt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    mrk_to_mkt_netd: list[Amount2Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "MrkToMktNetd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrk_to_mkt_grss: list[Amount2Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "MrkToMktGrss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrk_to_mkt_fls: list[Amount2Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "MrkToMktFls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    fls_hrcut: Optional[Amount2Secl00500102] = field(
        default=None,
        metadata={
            "name": "FlsHrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class Margin3Secl00500102(ISO20022MessageElement):
    initl_mrgn: Optional[Amount2Secl00500102] = field(
        default=None,
        metadata={
            "name": "InitlMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    vartn_mrgn: list[VariationMargin3Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "VartnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    othr_mrgn: list[Margin4Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "OthrMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class MarginCalculation2Secl00500102(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification14Secl00500102] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    xpsr_amt: Optional[Amount2Secl00500102] = field(
        default=None,
        metadata={
            "name": "XpsrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    ttl_mrgn_amt: Optional[AmountAndDirection20Secl00500102] = field(
        default=None,
        metadata={
            "name": "TtlMrgnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    coll_on_dpst: list[Collateral6Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "CollOnDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    min_rqrmnt_dpst: Optional[ActiveCurrencyAndAmountSecl00500102] = field(
        default=None,
        metadata={
            "name": "MinRqrmntDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrgn_rslt: Optional[MarginResult1ChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "MrgnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrgn_tp_amt: Optional[Margin3Secl00500102] = field(
        default=None,
        metadata={
            "name": "MrgnTpAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class MarginReport2Secl00500102(ISO20022MessageElement):
    mrgn_pdct: list[MarginProductType1ChoiceSecl00500102] = field(
        default_factory=list,
        metadata={
            "name": "MrgnPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrgn_acct: Optional[SecuritiesAccount18Secl00500102] = field(
        default=None,
        metadata={
            "name": "MrgnAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    collsd_mrgn_acct_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CollsdMrgnAcctInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    non_clr_mmb: list[PartyIdentificationAndAccount31Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "NonClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrgn_clctn_summry: Optional[MarginCalculation1Secl00500102] = field(
        default=None,
        metadata={
            "name": "MrgnClctnSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    mrgn_clctn: list[MarginCalculation2Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "MrgnClctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class MarginReportV02Secl00500102(ISO20022MessageElement):
    rpt_params: Optional[ReportParameters3Secl00500102] = field(
        default=None,
        metadata={
            "name": "RptParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    pgntn: Optional[PaginationSecl00500102] = field(
        default=None,
        metadata={
            "name": "Pgntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    clr_mmb: Optional[PartyIdentification35ChoiceSecl00500102] = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "required": True,
        },
    )
    rpt_summry: Optional[MarginCalculation1Secl00500102] = field(
        default=None,
        metadata={
            "name": "RptSummry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )
    rpt_dtls: list[MarginReport2Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "RptDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Secl00500102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02",
        },
    )


@dataclass
class Secl00500102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02"

    mrgn_rpt: Optional[MarginReportV02Secl00500102] = field(
        default=None,
        metadata={
            "name": "MrgnRpt",
            "type": "Element",
            "required": True,
        },
    )
