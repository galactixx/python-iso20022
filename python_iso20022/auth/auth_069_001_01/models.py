from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.auth_069_001_01.enums import (
    ExoticOptionStyle1Code,
    Frequency11Code,
    OptionEventType1Code,
    OptionStyle5Code,
    UnitOfMeasure8Code,
)
from python_iso20022.auth.enums import (
    PhysicalTransferType4Code,
    RateBasis1Code,
    SchemeIdentificationType1Code,
)
from python_iso20022.enums import (
    InterestComputationMethod2Code,
    OptionType1Code,
    Standardisation1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01"


@dataclass
class ActiveCurrencyAnd24AmountAuth06900101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 24,
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
class ActiveCurrencyAndAmountAuth06900101:
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
class DerivativeClassification1Auth06900101:
    asst_clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_pdct: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_pdct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_cmmdty: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubCmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrument59Auth06900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class GeneralCollateral2Auth06900101:
    elgbl_fin_instrm_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ElgblFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_occurs": 1,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification168Auth06900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Auth06900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProductClassification1Auth06900101:
    asst_clss: Optional[str] = field(
        default=None,
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_pdct: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_pdct: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sub_cmmdty: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubCmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth06900101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class FinancialInstrumentAttributes90Auth06900101:
    ntnl: Optional[ActiveCurrencyAndAmountAuth06900101] = field(
        default=None,
        metadata={
            "name": "Ntnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    unit_val: Optional[ActiveCurrencyAndAmountAuth06900101] = field(
        default=None,
        metadata={
            "name": "UnitVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    indx_id: Optional[GenericIdentification168Auth06900101] = field(
        default=None,
        metadata={
            "name": "IndxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    indx_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndxUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrst_rate_terms: Optional[InterestComputationMethod2Code] = field(
        default=None,
        metadata={
            "name": "IntrstRateTerms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class GenericIdentification165Auth06900101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class InterestRateContractTerm1Auth06900101:
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class OpenInterest1Auth06900101:
    grss_ntnl_amt: Optional[ActiveCurrencyAnd24AmountAuth06900101] = field(
        default=None,
        metadata={
            "name": "GrssNtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    nb_of_lots: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfLots",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class OptionEventType1ChoiceAuth06900101:
    cd: Optional[OptionEventType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Auth06900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class SpecificCollateral2Auth06900101:
    fin_instrm_id: Optional[FinancialInstrument59Auth06900101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth06900101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06900101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )


@dataclass
class UnitOfMeasure5ChoiceAuth06900101:
    cd: Optional[UnitOfMeasure8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Auth06900101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class ContractSize1Auth06900101:
    lot_sz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LotSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    unit: Optional[UnitOfMeasure5ChoiceAuth06900101] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class FinancialInstrumentAttributes88Auth06900101:
    ctrct_term: Optional[InterestRateContractTerm1Auth06900101] = field(
        default=None,
        metadata={
            "name": "CtrctTerm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    stdstn: list[Standardisation1Code] = field(
        default_factory=list,
        metadata={
            "name": "Stdstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "max_occurs": 3,
        },
    )
    pmt_frqcy: Optional[Frequency11Code] = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )


@dataclass
class OptionEvent2Auth06900101:
    tp: Optional[OptionEventType1ChoiceAuth06900101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RepurchaseAgreementType1ChoiceAuth06900101:
    spcfc_coll: Optional[SpecificCollateral2Auth06900101] = field(
        default=None,
        metadata={
            "name": "SpcfcColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    gnl_coll: Optional[GeneralCollateral2Auth06900101] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class FinancialInstrumentAttributes89Auth06900101:
    ctrct_sz: Optional[ContractSize1Auth06900101] = field(
        default=None,
        metadata={
            "name": "CtrctSz",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    dlvry_tp: Optional[PhysicalTransferType4Code] = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    undrlyg_id: Optional[GenericIdentification165Auth06900101] = field(
        default=None,
        metadata={
            "name": "UndrlygId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    pric_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class Option14Auth06900101:
    xprtn_style: list[OptionStyle5Code] = field(
        default_factory=list,
        metadata={
            "name": "XprtnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_occurs": 1,
            "max_occurs": 4,
        },
    )
    optn_style: Optional[ExoticOptionStyle1Code] = field(
        default=None,
        metadata={
            "name": "OptnStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    optn_tp: Optional[OptionType1Code] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    brrr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrrrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    evt_tp: Optional[OptionEvent2Auth06900101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class RepurchaseAgreement3Auth06900101:
    pdct_clssfctn: Optional[ProductClassification1Auth06900101] = field(
        default=None,
        metadata={
            "name": "PdctClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    rp_agrmt_tp: Optional[RepurchaseAgreementType1ChoiceAuth06900101] = field(
        default=None,
        metadata={
            "name": "RpAgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    trpty_agt: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class DefinedAttributes1ChoiceAuth06900101:
    qty_dfnd_attrbts: Optional[FinancialInstrumentAttributes89Auth06900101] = field(
        default=None,
        metadata={
            "name": "QtyDfndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    val_dfnd_attrbts: Optional[FinancialInstrumentAttributes90Auth06900101] = field(
        default=None,
        metadata={
            "name": "ValDfndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class DerivativeUnderlyingLeg1Auth06900101:
    ctrct_attrbts: Optional[FinancialInstrumentAttributes88Auth06900101] = field(
        default=None,
        metadata={
            "name": "CtrctAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    dfnd_attrbts: Optional[DefinedAttributes1ChoiceAuth06900101] = field(
        default=None,
        metadata={
            "name": "DfndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class Derivative3Auth06900101:
    deriv_clssfctn: Optional[DerivativeClassification1Auth06900101] = field(
        default=None,
        metadata={
            "name": "DerivClssfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    deriv_undrlyg_leg: list[DerivativeUnderlyingLeg1Auth06900101] = field(
        default_factory=list,
        metadata={
            "name": "DerivUndrlygLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    optn_attrbts: Optional[Option14Auth06900101] = field(
        default=None,
        metadata={
            "name": "OptnAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class Product1ChoiceAuth06900101:
    deriv: Optional[Derivative3Auth06900101] = field(
        default=None,
        metadata={
            "name": "Deriv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    scties_fincg_tx: Optional[RepurchaseAgreement3Auth06900101] = field(
        default=None,
        metadata={
            "name": "SctiesFincgTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    scty: Optional[FinancialInstrument59Auth06900101] = field(
        default=None,
        metadata={
            "name": "Scty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class ClearedProduct1Auth06900101:
    tradg_vn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TradgVn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_occurs": 1,
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    ccppdct_id: Optional[GenericIdentification168Auth06900101] = field(
        default=None,
        metadata={
            "name": "CCPPdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    uvrsl_pdct_id: Optional[GenericIdentification168Auth06900101] = field(
        default=None,
        metadata={
            "name": "UvrslPdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )
    pdct: Optional[Product1ChoiceAuth06900101] = field(
        default=None,
        metadata={
            "name": "Pdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    opn_intrst: Optional[OpenInterest1Auth06900101] = field(
        default=None,
        metadata={
            "name": "OpnIntrst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "required": True,
        },
    )
    trds_clrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrdsClrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class CcpclearedProductReportV01Auth06900101:
    class Meta:
        name = "CCPClearedProductReportV01"

    clrd_pdct: list[ClearedProduct1Auth06900101] = field(
        default_factory=list,
        metadata={
            "name": "ClrdPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06900101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01",
        },
    )


@dataclass
class Auth06900101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.069.001.01"

    ccpclrd_pdct_rpt: Optional[CcpclearedProductReportV01Auth06900101] = field(
        default=None,
        metadata={
            "name": "CCPClrdPdctRpt",
            "type": "Element",
            "required": True,
        },
    )
