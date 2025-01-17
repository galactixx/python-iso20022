from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.caam.enums import Atmoperation1Code
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    AtmcassetteType1Code,
    Atmcommand4Code,
    AtmcounterType1Code,
    AtmmediaType1Code,
    AtmmediaType3Code,
    AtmnoteType1Code,
    Atmstatus1Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    MessageFunction8Code,
    MessageFunction11Code,
    PartyType12Code,
    Response4Code,
    ResultDetail4Code,
    TmscontactLevel2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02"


@dataclass
class AtmcommandIdentification1Caam01000102:
    class Meta:
        name = "ATMCommandIdentification1"

    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GeographicCoordinates1Caam01000102:
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    long: Optional[str] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Caam01000102:
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class TransactionIdentifier1Caam01000102:
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Caam01000102:
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    utmestwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMEstwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    utmnrthwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMNrthwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmcassetteCounters4Caam01000102:
    class Meta:
        name = "ATMCassetteCounters4"

    tp: Optional[AtmcounterType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    added_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AddedNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rmvd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RmvdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dspnsd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DspnsdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dpstd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DpstdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcycld_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcycldNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rtrctd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RtrctdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rjctd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RjctdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    presntd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PresntdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmconfigurationParameter1Caam01000102:
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmmessageFunction2Caam01000102:
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmtotals1Caam01000102:
    class Meta:
        name = "ATMTotals1"

    mdia_tp: Optional[AtmmediaType1Code] = field(
        default=None,
        metadata={
            "name": "MdiaTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    atmbal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    atmcur: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMCur",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    atmbal_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMBalNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    atmcur_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ATMCurNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class EncapsulatedContent3Caam01000102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Caam01000102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCaam01000102:
    geogc_cordints: Optional[GeographicCoordinates1Caam01000102] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    utmcordints: Optional[Utmcoordinates1Caam01000102] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Parameter5Caam01000102:
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Parameter6Caam01000102:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Parameter7Caam01000102:
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class RelativeDistinguishedName1Caam01000102:
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ResponseType7Caam01000102:
    rspn: Optional[Response4Code] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    rspn_rsn: Optional[ResultDetail4Code] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    addtl_rspn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AtmcassetteCounters3Caam01000102:
    class Meta:
        name = "ATMCassetteCounters3"

    unit_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    mdia_ctgy: Optional[AtmmediaType3Code] = field(
        default=None,
        metadata={
            "name": "MdiaCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    cur_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cur_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    flow_ttls: list[AtmcassetteCounters4Caam01000102] = field(
        default_factory=list,
        metadata={
            "name": "FlowTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AtmcommandParameters1ChoiceCaam01000102:
    class Meta:
        name = "ATMCommandParameters1Choice"

    atmreqrd_gbl_sts: Optional[Atmstatus1Code] = field(
        default=None,
        metadata={
            "name": "ATMReqrdGblSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    xpctd_msg_fctn: Optional[MessageFunction8Code] = field(
        default=None,
        metadata={
            "name": "XpctdMsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    reqrd_cfgtn_param: Optional[AtmconfigurationParameter1Caam01000102] = field(
        default=None,
        metadata={
            "name": "ReqrdCfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AlgorithmIdentification12Caam01000102:
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter5Caam01000102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AlgorithmIdentification13Caam01000102:
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam01000102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AlgorithmIdentification14Caam01000102:
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam01000102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AlgorithmIdentification15Caam01000102:
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter7Caam01000102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class CertificateIssuer1Caam01000102:
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caam01000102] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_occurs": 1,
        },
    )


@dataclass
class PostalAddress17Caam01000102:
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCaam01000102] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Traceability4Caam01000102:
    rlay_id: Optional[GenericIdentification77Caam01000102] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )


@dataclass
class Atmcassette2Caam01000102:
    class Meta:
        name = "ATMCassette2"

    phys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    logcl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[AtmcassetteType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    sub_tp: list[AtmnoteType1Code] = field(
        default_factory=list,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    mdia_tp: Optional[AtmmediaType1Code] = field(
        default=None,
        metadata={
            "name": "MdiaTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    mdia_cntrs: list[AtmcassetteCounters3Caam01000102] = field(
        default_factory=list,
        metadata={
            "name": "MdiaCntrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Atmcommand7Caam01000102:
    class Meta:
        name = "ATMCommand7"

    tp: Optional[Atmcommand4Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    urgcy: Optional[TmscontactLevel2Code] = field(
        default=None,
        metadata={
            "name": "Urgcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Caam01000102] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    cmd_params: Optional[AtmcommandParameters1ChoiceCaam01000102] = field(
        default=None,
        metadata={
            "name": "CmdParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AutomatedTellerMachine3Caam01000102:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn: Optional[PostalAddress17Caam01000102] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class EncryptedContent3Caam01000102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Caam01000102] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header32Caam01000102:
    msg_fctn: Optional[AtmmessageFunction2Caam01000102] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    re_trnsmssn_cntr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReTrnsmssnCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Caam01000102] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class IssuerAndSerialNumber1Caam01000102:
    issr: Optional[CertificateIssuer1Caam01000102] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Caam01000102:
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Caam01000102] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Caam01000102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Caam01000102:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam01000102] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Atmtransaction26Caam01000102:
    class Meta:
        name = "ATMTransaction26"

    tp_of_opr: Optional[Atmoperation1Code] = field(
        default=None,
        metadata={
            "name": "TpOfOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    tx_id: Optional[TransactionIdentifier1Caam01000102] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tx_rspn: Optional[ResponseType7Caam01000102] = field(
        default=None,
        metadata={
            "name": "TxRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    atmttls: list[Atmtotals1Caam01000102] = field(
        default_factory=list,
        metadata={
            "name": "ATMTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    csstt: list[Atmcassette2Caam01000102] = field(
        default_factory=list,
        metadata={
            "name": "Csstt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    cmd: list[Atmcommand7Caam01000102] = field(
        default_factory=list,
        metadata={
            "name": "Cmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AlgorithmIdentification11Caam01000102:
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    param: Optional[Parameter4Caam01000102] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Recipient5ChoiceCaam01000102:
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caam01000102] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    key_idr: Optional[Kekidentifier2Caam01000102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AtmreconciliationAcknowledgement2Caam01000102:
    class Meta:
        name = "ATMReconciliationAcknowledgement2"

    atm: Optional[AutomatedTellerMachine3Caam01000102] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    tx: Optional[Atmtransaction26Caam01000102] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )


@dataclass
class KeyTransport4Caam01000102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaam01000102] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Caam01000102] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCaam01000102:
    key_trnsprt: Optional[KeyTransport4Caam01000102] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    kek: Optional[Kek4Caam01000102] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    key_idr: Optional[Kekidentifier2Caam01000102] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class AuthenticatedData4Caam01000102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam01000102] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Caam01000102] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam01000102] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Caam01000102:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam01000102] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Caam01000102] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class ContentInformationType10Caam01000102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Caam01000102] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Caam01000102:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Caam01000102] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )


@dataclass
class AtmreconciliationAcknowledgementV02Caam01000102:
    class Meta:
        name = "ATMReconciliationAcknowledgementV02"

    hdr: Optional[Header32Caam01000102] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
            "required": True,
        },
    )
    prtctd_atmrcncltn_ack: Optional[ContentInformationType10Caam01000102] = field(
        default=None,
        metadata={
            "name": "PrtctdATMRcncltnAck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    atmrcncltn_ack: Optional[AtmreconciliationAcknowledgement2Caam01000102] = field(
        default=None,
        metadata={
            "name": "ATMRcncltnAck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )
    scty_trlr: Optional[ContentInformationType15Caam01000102] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02",
        },
    )


@dataclass
class Caam01000102:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caam.010.001.02"

    atmrcncltn_ack: Optional[AtmreconciliationAcknowledgementV02Caam01000102] = field(
        default=None,
        metadata={
            "name": "ATMRcncltnAck",
            "type": "Element",
            "required": True,
        },
    )
