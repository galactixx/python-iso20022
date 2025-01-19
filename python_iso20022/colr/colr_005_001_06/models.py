from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.colr.colr_005_001_06.enums import (
    CollateralManagementCancellationReason1Code,
)
from python_iso20022.colr.enums import (
    CollateralAccountType1Code,
    CollateralTransactionType1Code,
    ExposureType11Code,
)
from python_iso20022.enums import CollateralRole1Code, DateType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06"


@dataclass
class ActiveOrHistoricCurrencyAndAmountColr00500106(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceColr00500106(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class GenericIdentification30Colr00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Colr00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PostalAddress2Colr00500106(ISO20022MessageElement):
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class Reference3ChoiceColr00500106(ISO20022MessageElement):
    clnt_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClntCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_prpsl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrpslId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_prpsl_rspn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollPrpslRspnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_sbstitn_conf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollSbstitnConfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_sbstitn_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollSbstitnReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    coll_sbstitn_rspn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollSbstitnRspnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cmon_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 52,
        },
    )
    dspt_ntfctn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DsptNtfctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrst_pmt_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstPmtReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrst_pmt_rspn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstPmtRspnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrst_pmt_stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstPmtStmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrgn_call_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrgnCallReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrgn_call_rspn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrgnCallRspnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trpty_agt_svc_prvdr_coll_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrptyAgtSvcPrvdrCollTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Colr00500106(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class CollateralAccountIdentificationType3ChoiceColr00500106(ISO20022MessageElement):
    tp: Optional[CollateralAccountType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    prtry: Optional[GenericIdentification36Colr00500106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class CollateralCancellationType1ChoiceColr00500106(ISO20022MessageElement):
    cd: Optional[CollateralManagementCancellationReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Colr00500106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class CollateralTransactionType1ChoiceColr00500106(ISO20022MessageElement):
    cd: Optional[CollateralTransactionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Colr00500106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class Date3ChoiceColr00500106(ISO20022MessageElement):
    cd: Optional[DateType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Colr00500106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class ExposureType21ChoiceColr00500106(ISO20022MessageElement):
    cd: Optional[ExposureType11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    prtry: Optional[GenericIdentification30Colr00500106] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class NameAndAddress6Colr00500106(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[PostalAddress2Colr00500106] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )


@dataclass
class SupplementaryData1Colr00500106(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Colr00500106] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )


@dataclass
class BlockChainAddressWallet5Colr00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ClosingDate4ChoiceColr00500106(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    cd: Optional[Date3ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class CollateralAccount3Colr00500106(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[CollateralAccountIdentificationType3ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CollateralCancellationReason1Colr00500106(ISO20022MessageElement):
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cxl_rsn_cd: Optional[CollateralCancellationType1ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "CxlRsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )


@dataclass
class PartyIdentification178ChoiceColr00500106(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Colr00500106] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    nm_and_adr: Optional[NameAndAddress6Colr00500106] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class Obligation8Colr00500106(ISO20022MessageElement):
    pty_a: Optional[PartyIdentification178ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "PtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )
    svcg_pty_a: Optional[PartyIdentification178ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "SvcgPtyA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    pty_b: Optional[PartyIdentification178ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "PtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )
    svcg_pty_b: Optional[PartyIdentification178ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "SvcgPtyB",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    coll_acct_id: Optional[CollateralAccount3Colr00500106] = field(
        default=None,
        metadata={
            "name": "CollAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    blck_chain_adr_or_wllt: Optional[BlockChainAddressWallet5Colr00500106] = field(
        default=None,
        metadata={
            "name": "BlckChainAdrOrWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    xpsr_tp: Optional[ExposureType21ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "XpsrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    coll_tx_tp: Optional[CollateralTransactionType1ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "CollTxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    coll_sd: Optional[CollateralRole1Code] = field(
        default=None,
        metadata={
            "name": "CollSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    xpsr_amt: Optional[ActiveOrHistoricCurrencyAndAmountColr00500106] = field(
        default=None,
        metadata={
            "name": "XpsrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    valtn_dt: Optional[DateAndDateTime2ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "ValtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    clsg_dt: Optional[ClosingDate4ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "ClsgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    reqd_exctn_dt: Optional[DateAndDateTime2ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )
    sttlm_prc: Optional[GenericIdentification30Colr00500106] = field(
        default=None,
        metadata={
            "name": "SttlmPrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class CollateralManagementCancellationRequestV06Colr00500106(ISO20022MessageElement):
    ref: Optional[Reference3ChoiceColr00500106] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )
    oblgtn: Optional[Obligation8Colr00500106] = field(
        default=None,
        metadata={
            "name": "Oblgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )
    cxl_rsn: Optional[CollateralCancellationReason1Colr00500106] = field(
        default=None,
        metadata={
            "name": "CxlRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Colr00500106] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06",
        },
    )


@dataclass
class Colr00500106(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:colr.005.001.06"

    coll_mgmt_cxl_req: Optional[
        CollateralManagementCancellationRequestV06Colr00500106
    ] = field(
        default=None,
        metadata={
            "name": "CollMgmtCxlReq",
            "type": "Element",
            "required": True,
        },
    )
