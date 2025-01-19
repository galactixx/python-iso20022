from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.colr.colr_004_001_05.enums import MarginCallResponse1Code
from python_iso20022.colr.enums import (
    AgreementFramework1Code,
    CollateralAccountType1Code,
    ExposureConventionType1Code,
    ExposureType11Code,
    IndependentAmountConventionType1Code,
    RoundingMethod1Code,
    ThresholdType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05"


@dataclass
class ActiveCurrencyAndAmountColr00400105(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceColr00400105(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class GenericIdentification30Colr00400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Colr00400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress2Colr00400105(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Colr00400105(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AgreementFramework1ChoiceColr00400105(ISO20022MessageElement):
    agrmt_frmwk: Optional[AgreementFramework1Code] = field(
        default=None,
        metadata={
            "name": "AgrmtFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    prtry_id: Optional[GenericIdentification30Colr00400105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class Amount1Colr00400105(ISO20022MessageElement):
    agrd_amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "AgrdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    mrgn_call_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrgnCallReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CollateralAccountIdentificationType3ChoiceColr00400105(ISO20022MessageElement):
    tp: Optional[CollateralAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    prtry: Optional[GenericIdentification36Colr00400105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class IndependentAmount1Colr00400105(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    cnvntn: Optional[IndependentAmountConventionType1Code] = field(
        default=None,
        metadata={
            "name": "Cnvntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )


@dataclass
class IndependentAmount2Colr00400105(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    cnvntn: Optional[IndependentAmountConventionType1Code] = field(
        default=None,
        metadata={
            "name": "Cnvntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )


@dataclass
class MarginCollateral1Colr00400105(ISO20022MessageElement):
    held_by_pty_a: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "HeldByPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    held_by_pty_b: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "HeldByPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    prr_agrd_to_pty_a: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "PrrAgrdToPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    prr_agrd_to_pty_b: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "PrrAgrdToPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    in_trnst_to_pty_a: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "InTrnstToPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    in_trnst_to_pty_b: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "InTrnstToPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class NameAndAddress6Colr00400105(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Colr00400105] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )


@dataclass
class ResponseType1ChoiceColr00400105(ISO20022MessageElement):
    cd: Optional[MarginCallResponse1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    prtry: Optional[GenericIdentification30Colr00400105] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class SegregatedIndependentAmountMargin1Colr00400105(ISO20022MessageElement):
    min_trf_amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "MinTrfAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    rndg_amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "RndgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    rndg_mtd: Optional[RoundingMethod1Code] = field(
        default=None,
        metadata={
            "name": "RndgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class SupplementaryData1Colr00400105(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Colr00400105] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )


@dataclass
class VariationMargin1Colr00400105(ISO20022MessageElement):
    thrshld_amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "ThrshldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    thrshld_tp: Optional[ThresholdType1Code] = field(
        default=None,
        metadata={
            "name": "ThrshldTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    min_trf_amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "MinTrfAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    rndg_amt: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "RndgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    rndg_mtd: Optional[RoundingMethod1Code] = field(
        default=None,
        metadata={
            "name": "RndgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )


@dataclass
class AggregatedIndependentAmount1Colr00400105(ISO20022MessageElement):
    trad: Optional[IndependentAmount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "Trad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    val_at_rsk: Optional[IndependentAmount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "ValAtRsk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    net_opn_pos: Optional[IndependentAmount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "NetOpnPos",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    othr_amt: list[IndependentAmount2Colr00400105] = field(
        default_factory=list,
        metadata={
            "name": "OthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class AgreedAmount1Colr00400105(ISO20022MessageElement):
    vartn_mrgn_amt: Optional[Amount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "VartnMrgnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    sgrtd_indpdnt_amt: Optional[Amount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "SgrtdIndpdntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class Agreement4Colr00400105(ISO20022MessageElement):
    agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )
    agrmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AgrmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    agrmt_frmwk: Optional[AgreementFramework1ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "AgrmtFrmwk",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class BlockChainAddressWallet5Colr00400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Collateral1Colr00400105(ISO20022MessageElement):
    vartn_mrgn: Optional[MarginCollateral1Colr00400105] = field(
        default=None,
        metadata={
            "name": "VartnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    sgrtd_indpdnt_amt: Optional[MarginCollateral1Colr00400105] = field(
        default=None,
        metadata={
            "name": "SgrtdIndpdntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class CollateralAccount3Colr00400105(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Margin1Colr00400105(ISO20022MessageElement):
    vartn_mrgn: Optional[VariationMargin1Colr00400105] = field(
        default=None,
        metadata={
            "name": "VartnMrgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    sgrtd_indpdnt_amt_mrgn: Optional[SegregatedIndependentAmountMargin1Colr00400105] = (
        field(
            default=None,
            metadata={
                "name": "SgrtdIndpdntAmtMrgn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            },
        )
    )


@dataclass
class PartyIdentification178ChoiceColr00400105(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr00400105] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Colr00400105] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class Response1Colr00400105(ISO20022MessageElement):
    rspn_tp_dtls: list[ResponseType1ChoiceColr00400105] = field(
        default_factory=list,
        metadata={
            "name": "RspnTpDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_occurs": 1,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AgreedAmount1ChoiceColr00400105(ISO20022MessageElement):
    agrd_amt_dtls: Optional[AgreedAmount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "AgrdAmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    sgrtd_indpdnt_amt: Optional[Amount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "SgrtdIndpdntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class CollateralBalance1ChoiceColr00400105(ISO20022MessageElement):
    ttl_coll: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "TtlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    coll_dtls: Optional[Collateral1Colr00400105] = field(
        default=None,
        metadata={
            "name": "CollDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    sgrtd_indpdnt_amt: Optional[MarginCollateral1Colr00400105] = field(
        default=None,
        metadata={
            "name": "SgrtdIndpdntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class MarginTerms1ChoiceColr00400105(ISO20022MessageElement):
    mrgn_dtls: Optional[Margin1Colr00400105] = field(
        default=None,
        metadata={
            "name": "MrgnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    sgrtd_indpdnt_amt_mrgn: Optional[SegregatedIndependentAmountMargin1Colr00400105] = (
        field(
            default=None,
            metadata={
                "name": "SgrtdIndpdntAmtMrgn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            },
        )
    )


@dataclass
class Obligation9Colr00400105(ISO20022MessageElement):
    pty_a: Optional[PartyIdentification178ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "PtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    svcg_pty_a: Optional[PartyIdentification178ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    pty_b: Optional[PartyIdentification178ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "PtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    svcg_pty_b: Optional[PartyIdentification178ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "SvcgPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    coll_acct_id: Optional[CollateralAccount3Colr00400105] = field(
        default=None,
        metadata={
            "name": "CollAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet5Colr00400105] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    xpsr_tp: Optional[ExposureType11Code] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    valtn_dt: Optional[DateAndDateTime2ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "ValtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )


@dataclass
class MarginCall1Colr00400105(ISO20022MessageElement):
    xpsd_amt_pty_a: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "XpsdAmtPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    xpsd_amt_pty_b: Optional[ActiveCurrencyAndAmountColr00400105] = field(
        default=None,
        metadata={
            "name": "XpsdAmtPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    xpsr_cnvntn: Optional[ExposureConventionType1Code] = field(
        default=None,
        metadata={
            "name": "XpsrCnvntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    indpdnt_amt_pty_a: Optional[AggregatedIndependentAmount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "IndpdntAmtPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    indpdnt_amt_pty_b: Optional[AggregatedIndependentAmount1Colr00400105] = field(
        default=None,
        metadata={
            "name": "IndpdntAmtPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    mrgn_terms: Optional[MarginTerms1ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "MrgnTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    coll_bal: Optional[CollateralBalance1ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "CollBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class MarginCallResponseV05Colr00400105(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    oblgtn: Optional[Obligation9Colr00400105] = field(
        default=None,
        metadata={
            "name": "Oblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
            "required": True,
        },
    )
    agrmt: Optional[Agreement4Colr00400105] = field(
        default=None,
        metadata={
            "name": "Agrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    mrgn_dtls_due_to_a: Optional[MarginCall1Colr00400105] = field(
        default=None,
        metadata={
            "name": "MrgnDtlsDueToA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    mrgn_dtls_due_to_b: Optional[MarginCall1Colr00400105] = field(
        default=None,
        metadata={
            "name": "MrgnDtlsDueToB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    agrd_amt_due_to_a: Optional[AgreedAmount1ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "AgrdAmtDueToA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    agrd_amt_due_to_b: Optional[AgreedAmount1ChoiceColr00400105] = field(
        default=None,
        metadata={
            "name": "AgrdAmtDueToB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    rspn_dtls: Optional[Response1Colr00400105] = field(
        default=None,
        metadata={
            "name": "RspnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )
    splmtry_data: list[SupplementaryData1Colr00400105] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05",
        },
    )


@dataclass
class Colr00400105(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:colr.004.001.05"

    mrgn_call_rspn: Optional[MarginCallResponseV05Colr00400105] = field(
        default=None,
        metadata={
            "name": "MrgnCallRspn",
            "type": "Element",
            "required": True,
        },
    )
