from dataclasses import dataclass, field
from typing import Optional

from python_iso20022.auth.enums import (
    ReportingMessageStatus1Code,
    ReportPeriodActivity1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02"


@dataclass
class AgreementType2ChoiceAuth08400102(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class GenericIdentification175Auth08400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth08400102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class ValidationRuleSchemeName1ChoiceAuth08400102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericValidationRuleIdentification1Auth08400102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    schme_nm: Optional[ValidationRuleSchemeName1ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MasterAgreement7Auth08400102(ISO20022MessageElement):
    tp: Optional[AgreementType2ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 50,
        },
    )
    othr_mstr_agrmt_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrMstrAgrmtDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class NaturalPersonIdentification2Auth08400102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth08400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification38Auth08400102(ISO20022MessageElement):
    id: Optional[GenericIdentification175Auth08400102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )
    dmcl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmcl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class SupplementaryData1Auth08400102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth08400102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )


@dataclass
class OrganisationIdentification15ChoiceAuth08400102(ISO20022MessageElement):
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: Optional[OrganisationIdentification38Auth08400102] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class RejectionReason45Auth08400102(ISO20022MessageElement):
    msg_rpt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgRptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    sts: Optional[ReportingMessageStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    dtld_vldtn_rule: Optional[GenericValidationRuleIdentification1Auth08400102] = field(
        default=None,
        metadata={
            "name": "DtldVldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class NumberOfTransactionsPerValidationRule5Auth08400102(ISO20022MessageElement):
    dtld_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DtldNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    rpt_sts: list[RejectionReason45Auth08400102] = field(
        default_factory=list,
        metadata={
            "name": "RptSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class PartyIdentification236ChoiceAuth08400102(ISO20022MessageElement):
    lgl: Optional[OrganisationIdentification15ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    ntrl: Optional[NaturalPersonIdentification2Auth08400102] = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class TradeTransactionIdentification17Auth08400102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    rpt_submitg_ntty: Optional[OrganisationIdentification15ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "RptSubmitgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth08400102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            },
        )
    )


@dataclass
class DetailedReportStatistics5Auth08400102(ISO20022MessageElement):
    ttl_nb_of_rpts: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRpts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ttl_nb_of_rpts_accptd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRptsAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ttl_nb_of_rpts_rjctd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfRptsRjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    nb_of_rpts_rjctd_per_err: list[
        NumberOfTransactionsPerValidationRule5Auth08400102
    ] = field(
        default_factory=list,
        metadata={
            "name": "NbOfRptsRjctdPerErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class TradeTransactionIdentification16Auth08400102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[PartyIdentification236ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth08400102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            },
        )
    )
    coll_prtfl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrtflId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )


@dataclass
class TradeTransactionIdentification20Auth08400102(ISO20022MessageElement):
    tech_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    rptg_ctr_pty: Optional[OrganisationIdentification15ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    othr_ctr_pty: Optional[PartyIdentification236ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    ntty_rspnsbl_for_rpt: Optional[OrganisationIdentification15ChoiceAuth08400102] = (
        field(
            default=None,
            metadata={
                "name": "NttyRspnsblForRpt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            },
        )
    )
    unq_trad_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnqTradIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_length": 1,
            "max_length": 52,
        },
    )
    mstr_agrmt: Optional[MasterAgreement7Auth08400102] = field(
        default=None,
        metadata={
            "name": "MstrAgrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    agt_lndr: Optional[OrganisationIdentification15ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "AgtLndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    trpty_agt: Optional[OrganisationIdentification15ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "TrptyAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class TransactionIdentification3ChoiceAuth08400102(ISO20022MessageElement):
    tx: Optional[TradeTransactionIdentification20Auth08400102] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    mrgn_rptg: Optional[TradeTransactionIdentification16Auth08400102] = field(
        default=None,
        metadata={
            "name": "MrgnRptg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    coll_reuse: Optional[TradeTransactionIdentification17Auth08400102] = field(
        default=None,
        metadata={
            "name": "CollReuse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class RejectionReason53Auth08400102(ISO20022MessageElement):
    tx_id: Optional[TransactionIdentification3ChoiceAuth08400102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    sts: Optional[ReportingMessageStatus1Code] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
        },
    )
    dtld_vldtn_rule: list[GenericValidationRuleIdentification1Auth08400102] = field(
        default_factory=list,
        metadata={
            "name": "DtldVldtnRule",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class DetailedTransactionStatistics13Auth08400102(ISO20022MessageElement):
    ttl_nb_of_txs: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ttl_nb_of_txs_accptd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsAccptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    ttl_nb_of_txs_rjctd: Optional[str] = field(
        default=None,
        metadata={
            "name": "TtlNbOfTxsRjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    txs_rjctns_rsn: list[RejectionReason53Auth08400102] = field(
        default_factory=list,
        metadata={
            "name": "TxsRjctnsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class DetailedTransactionStatistics2ChoiceAuth08400102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    dtld_sttstcs: Optional[DetailedTransactionStatistics13Auth08400102] = field(
        default=None,
        metadata={
            "name": "DtldSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class TradeData29Auth08400102(ISO20022MessageElement):
    rpt_sttstcs: list[DetailedReportStatistics5Auth08400102] = field(
        default_factory=list,
        metadata={
            "name": "RptSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_occurs": 1,
        },
    )
    tx_sttstcs: list[DetailedTransactionStatistics2ChoiceAuth08400102] = field(
        default_factory=list,
        metadata={
            "name": "TxSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth08400102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class TradeData35ChoiceAuth08400102(ISO20022MessageElement):
    data_set_actn: Optional[ReportPeriodActivity1Code] = field(
        default=None,
        metadata={
            "name": "DataSetActn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )
    rpt: list[TradeData29Auth08400102] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class SecuritiesFinancingReportingTransactionStatusAdviceV02Auth08400102(
    ISO20022MessageElement
):
    tx_rpt_sts_and_rsn: list[TradeData35ChoiceAuth08400102] = field(
        default_factory=list,
        metadata={
            "name": "TxRptStsAndRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth08400102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
        },
    )


@dataclass
class Auth08400102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02"

    scties_fincg_rptg_tx_sts_advc: Optional[
        SecuritiesFinancingReportingTransactionStatusAdviceV02Auth08400102
    ] = field(
        default=None,
        metadata={
            "name": "SctiesFincgRptgTxStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
