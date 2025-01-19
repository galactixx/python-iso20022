from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from python_iso20022.auth.enums import ProductType7Code
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01"


@dataclass
class ActiveCurrencyAnd24AmountAuth06100101(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountAuth06100101(ISO20022MessageElement):
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
class FinancialInstrument59Auth06100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    sctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth06100101(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Deposit1Auth06100101(ISO20022MessageElement):
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )
    val: Optional[ActiveCurrencyAndAmountAuth06100101] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )
    ctr_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class GeneralCollateral3Auth06100101(ISO20022MessageElement):
    fin_instrm_id: list[FinancialInstrument59Auth06100101] = field(
        default_factory=list,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )
    elgbl_fin_instrm_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ElgblFinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )


@dataclass
class OtherInvestment1Auth06100101(ISO20022MessageElement):
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth06100101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )


@dataclass
class SecurityIdentificationAndAmount1Auth06100101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    mkt_val: Optional[ActiveCurrencyAnd24AmountAuth06100101] = field(
        default=None,
        metadata={
            "name": "MktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )
    fin_instrm_tp: Optional[ProductType7Code] = field(
        default=None,
        metadata={
            "name": "FinInstrmTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )


@dataclass
class SpecificCollateral2Auth06100101(ISO20022MessageElement):
    fin_instrm_id: Optional[FinancialInstrument59Auth06100101] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Auth06100101(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth06100101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )


@dataclass
class RepurchaseAgreementType3ChoiceAuth06100101(ISO20022MessageElement):
    spcfc_coll: Optional[SpecificCollateral2Auth06100101] = field(
        default=None,
        metadata={
            "name": "SpcfcColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )
    gnl_coll: Optional[GeneralCollateral3Auth06100101] = field(
        default=None,
        metadata={
            "name": "GnlColl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )


@dataclass
class RepurchaseAgreement2Auth06100101(ISO20022MessageElement):
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )
    scnd_leg_pric: Optional[ActiveCurrencyAndAmountAuth06100101] = field(
        default=None,
        metadata={
            "name": "ScndLegPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )
    coll_mkt_val: Optional[ActiveCurrencyAndAmountAuth06100101] = field(
        default=None,
        metadata={
            "name": "CollMktVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )
    ctr_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    rp_agrmt_tp: Optional[RepurchaseAgreementType3ChoiceAuth06100101] = field(
        default=None,
        metadata={
            "name": "RpAgrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "required": True,
        },
    )
    trpty_agt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class Investment1ChoiceAuth06100101(ISO20022MessageElement):
    uscrd_csh_dpst: Optional[Deposit1Auth06100101] = field(
        default=None,
        metadata={
            "name": "UscrdCshDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )
    cntrl_bk_dpst: Optional[Deposit1Auth06100101] = field(
        default=None,
        metadata={
            "name": "CntrlBkDpst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )
    rp_agrmt: Optional[RepurchaseAgreement2Auth06100101] = field(
        default=None,
        metadata={
            "name": "RpAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )
    othr_invstmts: Optional[OtherInvestment1Auth06100101] = field(
        default=None,
        metadata={
            "name": "OthrInvstmts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )
    outrght_invstmt: Optional[SecurityIdentificationAndAmount1Auth06100101] = field(
        default=None,
        metadata={
            "name": "OutrghtInvstmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )


@dataclass
class CcpinvestmentsReportV01Auth06100101(ISO20022MessageElement):
    class Meta:
        name = "CCPInvestmentsReportV01"

    invstmt: list[Investment1ChoiceAuth06100101] = field(
        default_factory=list,
        metadata={
            "name": "Invstmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth06100101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01",
        },
    )


@dataclass
class Auth06100101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.061.001.01"

    ccpinvstmts_rpt: Optional[CcpinvestmentsReportV01Auth06100101] = field(
        default=None,
        metadata={
            "name": "CCPInvstmtsRpt",
            "type": "Element",
            "required": True,
        },
    )
