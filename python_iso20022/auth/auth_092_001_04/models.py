from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.auth.auth_092_001_04.enums import ReportingMessageStatus2Code
from python_iso20022.auth.enums import (
    DerivativeEventType3Code,
    NotApplicable1Code,
    ReportPeriodActivity1Code,
    TransactionOperationType10Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04"


@dataclass
class AgreementType2ChoiceAuth09200104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class DateAndDateTime2ChoiceAuth09200104(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class GenericIdentification175Auth09200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PortfolioIdentification3Auth09200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtfl_tx_xmptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtflTxXmptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth09200104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ValidationRuleSchemeName1ChoiceAuth09200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericValidationRuleIdentification1Auth09200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    schme_nm: Optional[ValidationRuleSchemeName1ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MasterAgreement8Auth09200104(ISO20022MessageElement):
    tp: Optional[AgreementType2ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NaturalPersonIdentification2Auth09200104(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth09200104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification38Auth09200104(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth09200104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class PortfolioCode3ChoiceAuth09200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 52,
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class PortfolioCode5ChoiceAuth09200104(ISO20022MessageElement):
    prtfl: Optional[PortfolioIdentification3Auth09200104] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    no_prtfl: Optional[NotApplicable1Code] = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class SupplementaryData1Auth09200104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth09200104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )


@dataclass
class UniqueTransactionIdentifier2ChoiceAuth09200104(ISO20022MessageElement):
    unq_tx_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: Optional[GenericIdentification175Auth09200104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class MarginPortfolio3Auth09200104(ISO20022MessageElement):
    initl_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "InitlMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    vartn_mrgn_prtfl_cd: Optional[PortfolioCode5ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "VartnMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class NaturalPersonIdentification3Auth09200104(ISO20022MessageElement):
    id: Optional[NaturalPersonIdentification2Auth09200104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth09200104(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth09200104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class RejectionReason70Auth09200104(ISO20022MessageElement):
    msg_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    sts: Optional[ReportingMessageStatus2Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    dtld_vldtn_rule: Optional[GenericValidationRuleIdentification1Auth09200104] = field(
        default=None,
        metadata={
            "name": "DtldVldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class CollateralPortfolioCode5ChoiceAuth09200104(ISO20022MessageElement):
    prtfl: Optional[PortfolioCode3ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    mrgn_prtfl_cd: Optional[MarginPortfolio3Auth09200104] = field(
        default=None,
        metadata={
            "name": "MrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class CounterpartyData92Auth09200104(ISO20022MessageElement):
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth09200104] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            },
        )
    )


@dataclass
class LegalPersonIdentification1Auth09200104(ISO20022MessageElement):
    id: Optional[OrganisationIdentification15ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class NumberOfTransactionsPerValidationRule6Auth09200104(ISO20022MessageElement):
    dtld_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DtldNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    rpt_sts: list[RejectionReason70Auth09200104] = field(
        default_factory=list,
        metadata={
            "name": "RptSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class DetailedReportStatistics7Auth09200104(ISO20022MessageElement):
    ttl_nb_of_rpts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRpts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_rpts_accptd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRptsAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_rpts_rjctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRptsRjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    nb_of_rpts_rjctd_per_err: list[
        NumberOfTransactionsPerValidationRule6Auth09200104
    ] = field(
        default_factory=list,
        metadata={
            "name": "NbOfRptsRjctdPerErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class PartyIdentification248ChoiceAuth09200104(ISO20022MessageElement):
    lgl: Optional[LegalPersonIdentification1Auth09200104] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    ntrl: Optional[NaturalPersonIdentification3Auth09200104] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class TradeTransactionIdentification24Auth09200104(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    actn_tp: Optional[TransactionOperationType10Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    rptg_tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    deriv_evt_tp: Optional[DerivativeEventType3Code] = field(
        default=None,
        metadata={
            "name": "DerivEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    deriv_evt_tm_stmp: Optional[DateAndDateTime2ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "DerivEvtTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    othr_ctr_pty: Optional[PartyIdentification248ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    unq_idr: Optional[UniqueTransactionIdentifier2ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "UnqIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    mstr_agrmt: Optional[MasterAgreement8Auth09200104] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    coll_prtfl_cd: Optional[CollateralPortfolioCode5ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class RejectionReason71Auth09200104(ISO20022MessageElement):
    tx_id: Optional[TradeTransactionIdentification24Auth09200104] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    sts: Optional[ReportingMessageStatus2Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    dtld_vldtn_rule: list[GenericValidationRuleIdentification1Auth09200104] = field(
        default_factory=list,
        metadata={
            "name": "DtldVldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class DetailedTransactionStatistics30Auth09200104(ISO20022MessageElement):
    ttl_nb_of_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_txs_accptd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_txs_rjctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsRjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_crrctd_rjctns: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlCrrctdRjctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    txs_rjctns_rsn: list[RejectionReason71Auth09200104] = field(
        default_factory=list,
        metadata={
            "name": "TxsRjctnsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class DetailedTransactionStatistics7ChoiceAuth09200104(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    dtld_sttstcs: Optional[DetailedTransactionStatistics30Auth09200104] = field(
        default=None,
        metadata={
            "name": "DtldSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class RejectionStatistics9Auth09200104(ISO20022MessageElement):
    ctr_pty_id: Optional[CounterpartyData92Auth09200104] = field(
        default=None,
        metadata={
            "name": "CtrPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    rpt_sttstcs: Optional[DetailedReportStatistics7Auth09200104] = field(
        default=None,
        metadata={
            "name": "RptSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    deriv_sttstcs: Optional[DetailedTransactionStatistics7ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "DerivSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )


@dataclass
class DetailedStatisticsPerCounterparty19Auth09200104(ISO20022MessageElement):
    ref_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RefDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    ttl_nb_of_rpts: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRpts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_rpts_accptd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRptsAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_rpts_rjctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRptsRjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_txs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_txs_accptd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_nb_of_txs_rjctd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsRjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    ttl_crrctd_rjctns: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlCrrctdRjctns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 20,
            "fraction_digits": 0,
        },
    )
    rjctn_sttstcs: list[RejectionStatistics9Auth09200104] = field(
        default_factory=list,
        metadata={
            "name": "RjctnSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class StatisticsPerCounterparty18ChoiceAuth09200104(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )
    rpt: Optional[DetailedStatisticsPerCounterparty19Auth09200104] = field(
        default=None,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class DerivativesTradeRejectionStatisticalReportV04Auth09200104(ISO20022MessageElement):
    rjctn_sttstcs: Optional[StatisticsPerCounterparty18ChoiceAuth09200104] = field(
        default=None,
        metadata={
            "name": "RjctnSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth09200104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04",
        },
    )


@dataclass
class Auth09200104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.092.001.04"

    derivs_trad_rjctn_sttstcl_rpt: Optional[
        DerivativesTradeRejectionStatisticalReportV04Auth09200104
    ] = field(
        default=None,
        metadata={
            "name": "DerivsTradRjctnSttstclRpt",
            "type": "Element",
            "required": True,
        },
    )
