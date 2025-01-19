from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.caad.enums import (
    CardServiceType4Code,
    ReconciliationActivityType1Code,
    ReconciliationCategory1Code,
    ReconciliationFunction1Code,
    ReconciliationImpact1Code,
    ReconciliationMessageType2Code,
)
from python_iso20022.enums import (
    Algorithm5Code,
    Algorithm7Code,
    Algorithm8Code,
    Algorithm13Code,
    Algorithm20Code,
    Algorithm23Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    ContentType3Code,
    CreditDebit3Code,
    EncryptedDataFormat1Code,
    EncryptionFormat3Code,
    PartyType9Code,
    PartyType17Code,
    PartyType18Code,
    PartyType26Code,
    PartyType32Code,
    TypeOfAmount21Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04"


@dataclass
class AdditionalData1Caad00500104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class BatchManagementInformation1Caad00500104(ISO20022MessageElement):
    colltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    btch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BtchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,15}",
        },
    )
    msg_chcksm_inpt_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MsgChcksmInptVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EncryptedData2ChoiceCaad00500104(ISO20022MessageElement):
    binry: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    hex_binry: Optional[str] = field(
        default=None,
        metadata={
            "name": "HexBinry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,9999}",
        },
    )


@dataclass
class Jurisdiction2Caad00500104(ISO20022MessageElement):
    dmst_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmstInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    dmst_qlfctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstQlfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Caad00500104(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Kekidentifier6Caad00500104(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier6"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Macdata1Caad00500104(ISO20022MessageElement):
    class Meta:
        name = "MACData1"

    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    initlstn_vctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )


@dataclass
class Reconciliation4Caad00500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Caad00500104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AdditionalData2Caad00500104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dtls: list[AdditionalData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class AdditionalFee3Caad00500104(ISO20022MessageElement):
    tp: Optional[TypeOfAmount21Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prgm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prgm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dscrptr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dscrptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
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
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcncltn_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    rcncltn_fctv_xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcncltnFctvXchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "total_digits": 25,
            "fraction_digits": 13,
        },
    )
    assgnr: Optional[PartyType32Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    othr_assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AdditionalFeeReconciliation3Caad00500104(ISO20022MessageElement):
    impct: Optional[ReconciliationImpact1Code] = field(
        default=None,
        metadata={
            "name": "Impct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    tp: Optional[TypeOfAmount21Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Cnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AlgorithmIdentification26Caad00500104(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    param: Optional[Algorithm5Code] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class ContentInformationType41Caad00500104(ISO20022MessageElement):
    macdata: Optional[Macdata1Caad00500104] = field(
        default=None,
        metadata={
            "name": "MACData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    mac: Optional[str] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "pattern": r"([0-9A-F][0-9A-F]){1,8}",
        },
    )


@dataclass
class EncryptedDataElement2Caad00500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data: Optional[EncryptedData2ChoiceCaad00500104] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    clear_txt_frmt: Optional[EncryptedDataFormat1Code] = field(
        default=None,
        metadata={
            "name": "ClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    othr_clear_txt_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrClearTxtFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialReconciliation3Caad00500104(ISO20022MessageElement):
    impct: Optional[ReconciliationImpact1Code] = field(
        default=None,
        metadata={
            "name": "Impct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    tp: Optional[ReconciliationCategory1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Cnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class GenericIdentification183Caad00500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class LocalData14Caad00500104(ISO20022MessageElement):
    lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "pattern": r"[a-z]{2,3}",
        },
    )
    ncodg_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 210,
        },
    )
    addtl_data: list[AdditionalData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class MessageReconciliation3Caad00500104(ISO20022MessageElement):
    tp: Optional[ReconciliationMessageType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Cnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Parameter14Caad00500104(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat3Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class Parameter7Caad00500104(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class ProcessingResult26Caad00500104(ISO20022MessageElement):
    rspn_src_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_tp: Optional[PartyType26Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    rspn_src_othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcOthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_src_assgnr: Optional[PartyType9Code] = field(
        default=None,
        metadata={
            "name": "RspnSrcAssgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    rspn_src_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    rspn_src_shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnSrcShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9A-Z]{2,2}",
        },
    )
    addtl_inf: list[AdditionalData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class ProgrammeMode5Caad00500104(ISO20022MessageElement):
    apld_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApldId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: list[AdditionalData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class RelativeDistinguishedName1Caad00500104(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SettlementService6Caad00500104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    dfrrd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Dfrrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Tm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cut_off_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CutOffTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    rptg_ntty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_ntty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RptgNttyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: list[AdditionalData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class SupplementaryData1Caad00500104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Caad00500104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )


@dataclass
class Traceability10Caad00500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType17Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    othr_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    assgnr: Optional[PartyType18Code] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[A-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class AlgorithmIdentification25Caad00500104(ISO20022MessageElement):
    algo: Optional[Algorithm23Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    param: Optional[Parameter7Caad00500104] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class AlgorithmIdentification28Caad00500104(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    param: Optional[Parameter14Caad00500104] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class CertificateIssuer1Caad00500104(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class EncryptedData2Caad00500104(ISO20022MessageElement):
    ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1}",
        },
    )
    key_set_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeySetIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,8}",
        },
    )
    drvd_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrvdInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"([0-9A-F][0-9A-F]){1,32}",
        },
    )
    algo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_lngth: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,4}",
        },
    )
    key_prtcn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    key_indx: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyIndx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pddg_mtd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PddgMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_frmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcrptdFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,2}",
        },
    )
    ncrptd_elmt: list[EncryptedDataElement2Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class Header71Caad00500104(ISO20022MessageElement):
    msg_fctn: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    re_trnsmssn_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    btch_mgmt_inf: Optional[BatchManagementInformation1Caad00500104] = field(
        default=None,
        metadata={
            "name": "BtchMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    initg_pty: Optional[GenericIdentification183Caad00500104] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification183Caad00500104] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    trac_data: list[AdditionalData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "TracData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    tracblt: list[Traceability10Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class Parameter13Caad00500104(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm20Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification26Caad00500104] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class PartyIdentification286Caad00500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "pattern": r"[0-9]{1,11}",
        },
    )
    assgnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Assgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{3,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lgl_corp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LglCorpNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 99,
        },
    )
    addtl_id: list[AdditionalData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    lcl_data: Optional[LocalData14Caad00500104] = field(
        default=None,
        metadata={
            "name": "LclData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class TransactionTotals14Caad00500104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    chckpt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChckptRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fin: list[FinancialReconciliation3Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "Fin",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    msg: list[MessageReconciliation3Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "Msg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    addtl_fee_rcncltn: list[AdditionalFeeReconciliation3Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFeeRcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "pattern": r"[0-9]{2,3}",
        },
    )
    amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    cdt_dbt: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class AlgorithmIdentification27Caad00500104(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    param: Optional[Parameter13Caad00500104] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class EncryptedContent8Caad00500104(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification25Caad00500104] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    ncrptd_data_elmt: list[EncryptedDataElement2Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "NcrptdDataElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_occurs": 1,
        },
    )


@dataclass
class IssuerAndSerialNumber1Caad00500104(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Caad00500104] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek6Caad00500104(ISO20022MessageElement):
    class Meta:
        name = "KEK6"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier6Caad00500104] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification28Caad00500104] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Recipient5ChoiceCaad00500104(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caad00500104] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    key_idr: Optional[Kekidentifier2Caad00500104] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class KeyTransport6Caad00500104(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaad00500104] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification27Caad00500104] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient7ChoiceCaad00500104(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport6Caad00500104] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    kek: Optional[Kek6Caad00500104] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    key_idr: Optional[Kekidentifier6Caad00500104] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class EnvelopedData12Caad00500104(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient7ChoiceCaad00500104] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent8Caad00500104] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class ProtectedData2Caad00500104(ISO20022MessageElement):
    cntt_tp: Optional[ContentType3Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData12Caad00500104] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    ncrptd_data: Optional[EncryptedData2Caad00500104] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class ReconciliationInitiationV04Caad00500104(ISO20022MessageElement):
    hdr: Optional[Header71Caad00500104] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    rcncltn_fctn: Optional[ReconciliationFunction1Code] = field(
        default=None,
        metadata={
            "name": "RcncltnFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    rcncltn_actvty_tp: Optional[ReconciliationActivityType1Code] = field(
        default=None,
        metadata={
            "name": "RcncltnActvtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    othr_rcncltn_actvty_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRcncltnActvtyTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcncltn_tp: Optional[CardServiceType4Code] = field(
        default=None,
        metadata={
            "name": "RcncltnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "required": True,
        },
    )
    othr_rcncltn_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "OthrRcncltnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ReqdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{3}",
        },
    )
    orgtr: Optional[PartyIdentification286Caad00500104] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    sndr: Optional[PartyIdentification286Caad00500104] = field(
        default=None,
        metadata={
            "name": "Sndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    rcvr: Optional[PartyIdentification286Caad00500104] = field(
        default=None,
        metadata={
            "name": "Rcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    dstn: Optional[PartyIdentification286Caad00500104] = field(
        default=None,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    prgrmm: list[ProgrammeMode5Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "Prgrmm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    sys_trac_audt_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SysTracAudtNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "pattern": r"[0-9]{1,12}",
        },
    )
    trnsmssn_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TrnsmssnDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    rtrvl_ref_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "RtrvlRefNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "length": 12,
        },
    )
    life_cycl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LifeCyclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
            "length": 15,
        },
    )
    rcncltn_ttls: list[TransactionTotals14Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "RcncltnTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    jursdctn: Optional[Jurisdiction2Caad00500104] = field(
        default=None,
        metadata={
            "name": "Jursdctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    sttlm_svc: Optional[SettlementService6Caad00500104] = field(
        default=None,
        metadata={
            "name": "SttlmSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    addtl_fee: list[AdditionalFee3Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    rcncltn: Optional[Reconciliation4Caad00500104] = field(
        default=None,
        metadata={
            "name": "Rcncltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    addtl_data: list[AdditionalData2Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    prcg_rslt: Optional[ProcessingResult26Caad00500104] = field(
        default=None,
        metadata={
            "name": "PrcgRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    prtctd_data: list[ProtectedData2Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    splmtry_data: list[SupplementaryData1Caad00500104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )
    scty_trlr: Optional[ContentInformationType41Caad00500104] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04",
        },
    )


@dataclass
class Caad00500104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caad.005.001.04"

    rcncltn_initn: Optional[ReconciliationInitiationV04Caad00500104] = field(
        default=None,
        metadata={
            "name": "RcncltnInitn",
            "type": "Element",
            "required": True,
        },
    )
