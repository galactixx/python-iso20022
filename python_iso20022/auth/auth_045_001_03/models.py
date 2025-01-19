from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_045_001_03.enums import (
    NonEquityAssetClass1Code,
    NonEquitySubClassSegmentationCriteria1Code,
)
from python_iso20022.auth.enums import (
    NonEquityInstrumentReportingClassification1Code,
    TradingVenue2Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03"


@dataclass
class ActiveOrHistoricCurrencyAndAmountAuth04500103(ISO20022MessageElement):
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
class Period2Auth04500103(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )


@dataclass
class StatisticsTransparency2Auth04500103(ISO20022MessageElement):
    ttl_nb_of_txs_exctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsExctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    ttl_vol_of_txs_exctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlVolOfTxsExctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth04500103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class NonEquitySubClassSegmentationCriterion1Auth04500103(ISO20022MessageElement):
    crit_nm: Optional[NonEquitySubClassSegmentationCriteria1Code] = field(
        default=None,
        metadata={
            "name": "CritNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )
    crit_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "CritVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 1000,
        },
    )


@dataclass
class Period4ChoiceAuth04500103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    fr_dt_to_dt: Optional[Period2Auth04500103] = field(
        default=None,
        metadata={
            "name": "FrDtToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )


@dataclass
class SupplementaryData1Auth04500103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth04500103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )


@dataclass
class TonsOrCurrency2ChoiceAuth04500103(ISO20022MessageElement):
    nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    amt: Optional[ActiveOrHistoricCurrencyAndAmountAuth04500103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )


@dataclass
class TradingVenueIdentification2Auth04500103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    tp: Optional[TradingVenue2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )


@dataclass
class NonEquitySubClass1Auth04500103(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    sgmttn_crit: list[NonEquitySubClassSegmentationCriterion1Auth04500103] = field(
        default_factory=list,
        metadata={
            "name": "SgmttnCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class TradingVenueIdentification1ChoiceAuth04500103(ISO20022MessageElement):
    mkt_id_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktIdCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ntl_cmptnt_authrty: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtlCmptntAuthrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    othr: Optional[TradingVenueIdentification2Auth04500103] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )


@dataclass
class AssetClassAndSubClassIdentification2Auth04500103(ISO20022MessageElement):
    asst_clss: Optional[NonEquityAssetClass1Code] = field(
        default=None,
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )
    deriv_sub_clss: Optional[NonEquitySubClass1Auth04500103] = field(
        default=None,
        metadata={
            "name": "DerivSubClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    fin_instrm_clssfctn: Optional[NonEquityInstrumentReportingClassification1Code] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmClssfctn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            },
        )
    )


@dataclass
class InstrumentAndSubClassIdentification2Auth04500103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    deriv_sub_clss: Optional[NonEquitySubClass1Auth04500103] = field(
        default=None,
        metadata={
            "name": "DerivSubClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    fin_instrm_clssfctn: Optional[NonEquityInstrumentReportingClassification1Code] = (
        field(
            default=None,
            metadata={
                "name": "FinInstrmClssfctn",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            },
        )
    )


@dataclass
class SecuritiesMarketReportHeader1Auth04500103(ISO20022MessageElement):
    rptg_ntty: Optional[TradingVenueIdentification1ChoiceAuth04500103] = field(
        default=None,
        metadata={
            "name": "RptgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth04500103] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )
    submissn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SubmissnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )


@dataclass
class InstrumentOrSubClassIdentification2ChoiceAuth04500103(ISO20022MessageElement):
    isinand_sub_clss: Optional[InstrumentAndSubClassIdentification2Auth04500103] = (
        field(
            default=None,
            metadata={
                "name": "ISINAndSubClss",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            },
        )
    )
    asst_clss_and_sub_clss: Optional[
        AssetClassAndSubClassIdentification2Auth04500103
    ] = field(
        default=None,
        metadata={
            "name": "AsstClssAndSubClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )


@dataclass
class TransparencyDataReport20Auth04500103(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[InstrumentOrSubClassIdentification2ChoiceAuth04500103] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )
    full_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    tradg_vn: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    rptg_prd: Optional[Period4ChoiceAuth04500103] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    lqdty: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lqdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    pre_trad_lrg_in_scale_thrshld: Optional[TonsOrCurrency2ChoiceAuth04500103] = field(
        default=None,
        metadata={
            "name": "PreTradLrgInScaleThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    pst_trad_lrg_in_scale_thrshld: Optional[TonsOrCurrency2ChoiceAuth04500103] = field(
        default=None,
        metadata={
            "name": "PstTradLrgInScaleThrshld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )
    pre_trad_instrm_sz_spcfc_thrshld: Optional[TonsOrCurrency2ChoiceAuth04500103] = (
        field(
            default=None,
            metadata={
                "name": "PreTradInstrmSzSpcfcThrshld",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            },
        )
    )
    pst_trad_instrm_sz_spcfc_thrshld: Optional[TonsOrCurrency2ChoiceAuth04500103] = (
        field(
            default=None,
            metadata={
                "name": "PstTradInstrmSzSpcfcThrshld",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            },
        )
    )
    sttstcs: Optional[StatisticsTransparency2Auth04500103] = field(
        default=None,
        metadata={
            "name": "Sttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )


@dataclass
class FinancialInstrumentReportingNonEquityTradingActivityResultV03Auth04500103(
    ISO20022MessageElement
):
    rpt_hdr: Optional[SecuritiesMarketReportHeader1Auth04500103] = field(
        default=None,
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "required": True,
        },
    )
    non_eqty_trnsprncy_data: list[TransparencyDataReport20Auth04500103] = field(
        default_factory=list,
        metadata={
            "name": "NonEqtyTrnsprncyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth04500103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03",
        },
    )


@dataclass
class Auth04500103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03"

    fin_instrm_rptg_non_eqty_tradg_actvty_rslt: Optional[
        FinancialInstrumentReportingNonEquityTradingActivityResultV03Auth04500103
    ] = field(
        default=None,
        metadata={
            "name": "FinInstrmRptgNonEqtyTradgActvtyRslt",
            "type": "Element",
            "required": True,
        },
    )
