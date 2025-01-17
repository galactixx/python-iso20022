from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.caam.enums import (
    Algorithm14Code,
    Atmcommand6Code,
    AtmsecurityScheme3Code,
    MessageProtection1Code,
    Tr34Command1Code,
)
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    Atmstatus1Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    CryptographicKeyType3Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    KeyUsage1Code,
    MessageFunction8Code,
    MessageFunction11Code,
    PartyType12Code,
    Pinformat4Code,
    TmscontactLevel2Code,
    TransactionEnvironment3Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03"


@dataclass
class AtmcommandIdentification1Caam00400103:
    class Meta:
        name = "ATMCommandIdentification1"

    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AtmsecurityConfiguration2Caam00400103:
    class Meta:
        name = "ATMSecurityConfiguration2"

    max_smmtrc_key: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSmmtrcKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_asmmtrc_key: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAsmmtrcKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_rsakey_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxRSAKeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_root_key_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxRootKeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Acquirer7Caam00400103:
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Acquirer8Caam00400103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Caam00400103:
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Caam00400103:
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class PublicRsakey1Caam00400103:
    class Meta:
        name = "PublicRSAKey1"

    mdlus: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Mdlus",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    expnt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Expnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Utmcoordinates1Caam00400103:
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmconfigurationParameter1Caam00400103:
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmmessageFunction2Caam00400103:
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmsecurityConfiguration3Caam00400103:
    class Meta:
        name = "ATMSecurityConfiguration3"

    asmmtrc_ncrptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsmmtrcNcrptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    asmmtrc_key_std_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsmmtrcKeyStdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    asmmtrc_ncrptn_algo: list[Algorithm7Code] = field(
        default_factory=list,
        metadata={
            "name": "AsmmtrcNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    smmtrc_trnsprt_key: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmmtrcTrnsprtKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    smmtrc_trnsprt_key_algo: list[Algorithm13Code] = field(
        default_factory=list,
        metadata={
            "name": "SmmtrcTrnsprtKeyAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    smmtrc_ncrptn_algo: list[Algorithm15Code] = field(
        default_factory=list,
        metadata={
            "name": "SmmtrcNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    ncrptn_frmt: list[EncryptionFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AtmsecurityConfiguration4Caam00400103:
    class Meta:
        name = "ATMSecurityConfiguration4"

    max_certs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxCerts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_sgntrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSgntrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgtl_sgntr_algo: list[Algorithm14Code] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AtmsecurityConfiguration5Caam00400103:
    class Meta:
        name = "ATMSecurityConfiguration5"

    pinfrmt: list[Pinformat4Code] = field(
        default_factory=list,
        metadata={
            "name": "PINFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    pinlngth_cpblties: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AlgorithmIdentification16Caam00400103:
    algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )


@dataclass
class EncapsulatedContent3Caam00400103:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Caam00400103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCaam00400103:
    geogc_cordints: Optional[GeographicCoordinates1Caam00400103] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    utmcordints: Optional[Utmcoordinates1Caam00400103] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Parameter5Caam00400103:
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Parameter6Caam00400103:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Parameter7Caam00400103:
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class RelativeDistinguishedName1Caam00400103:
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TrrelatedData2Caam00400103:
    class Meta:
        name = "TRRelatedData2"

    tr34_cmd: Optional[Tr34Command1Code] = field(
        default=None,
        metadata={
            "name": "TR34Cmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    trblck: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TRBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class TerminalHosting1Caam00400103:
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmcommandParameters1ChoiceCaam00400103:
    class Meta:
        name = "ATMCommandParameters1Choice"

    atmreqrd_gbl_sts: Optional[Atmstatus1Code] = field(
        default=None,
        metadata={
            "name": "ATMReqrdGblSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    xpctd_msg_fctn: Optional[MessageFunction8Code] = field(
        default=None,
        metadata={
            "name": "XpctdMsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    reqrd_cfgtn_param: Optional[AtmconfigurationParameter1Caam00400103] = field(
        default=None,
        metadata={
            "name": "ReqrdCfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AtmsecurityConfiguration1Caam00400103:
    class Meta:
        name = "ATMSecurityConfiguration1"

    keys: Optional[AtmsecurityConfiguration2Caam00400103] = field(
        default=None,
        metadata={
            "name": "Keys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    ncrptn: Optional[AtmsecurityConfiguration3Caam00400103] = field(
        default=None,
        metadata={
            "name": "Ncrptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    macalgo: list[Algorithm12Code] = field(
        default_factory=list,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    dgst_algo: list[Algorithm11Code] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    dgtl_sgntr: Optional[AtmsecurityConfiguration4Caam00400103] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    pin: Optional[AtmsecurityConfiguration5Caam00400103] = field(
        default=None,
        metadata={
            "name": "PIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    msg_prtcn: list[MessageProtection1Code] = field(
        default_factory=list,
        metadata={
            "name": "MsgPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AlgorithmIdentification12Caam00400103:
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter5Caam00400103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AlgorithmIdentification13Caam00400103:
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00400103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AlgorithmIdentification14Caam00400103:
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00400103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AlgorithmIdentification15Caam00400103:
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Caam00400103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class CertificateIssuer1Caam00400103:
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caam00400103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class PostalAddress17Caam00400103:
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCaam00400103] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Traceability4Caam00400103:
    rlay_id: Optional[GenericIdentification77Caam00400103] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )


@dataclass
class Atmcommand13Caam00400103:
    class Meta:
        name = "ATMCommand13"

    tp: Optional[Atmcommand6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    urgcy: Optional[TmscontactLevel2Code] = field(
        default=None,
        metadata={
            "name": "Urgcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Caam00400103] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    cmd_params: Optional[AtmcommandParameters1ChoiceCaam00400103] = field(
        default=None,
        metadata={
            "name": "CmdParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AutomatedTellerMachine3Caam00400103:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn: Optional[PostalAddress17Caam00400103] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class EncryptedContent3Caam00400103:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Caam00400103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Caam00400103:
    msg_fctn: Optional[AtmmessageFunction2Caam00400103] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Caam00400103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class IssuerAndSerialNumber1Caam00400103:
    issr: Optional[CertificateIssuer1Caam00400103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Caam00400103:
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Caam00400103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Caam00400103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Caam00400103:
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam00400103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Parameter8Caam00400103:
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam00400103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    salt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SaltLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trlr_fld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrlrFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Atmenvironment7Caam00400103:
    class Meta:
        name = "ATMEnvironment7"

    acqrr: Optional[Acquirer7Caam00400103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    atmmgr: Optional[Acquirer8Caam00400103] = field(
        default=None,
        metadata={
            "name": "ATMMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    hstg_ntty: Optional[TerminalHosting1Caam00400103] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    atm: Optional[AutomatedTellerMachine3Caam00400103] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )


@dataclass
class AlgorithmIdentification11Caam00400103:
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter4Caam00400103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AlgorithmIdentification17Caam00400103:
    algo: Optional[Algorithm14Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter8Caam00400103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Recipient5ChoiceCaam00400103:
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caam00400103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00400103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class KeyTransport4Caam00400103:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaam00400103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Caam00400103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Signer3Caam00400103:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sgnr_id: Optional[Recipient5ChoiceCaam00400103] = field(
        default=None,
        metadata={
            "name": "SgnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    dgst_algo: Optional[AlgorithmIdentification16Caam00400103] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    sgntr_algo: Optional[AlgorithmIdentification17Caam00400103] = field(
        default=None,
        metadata={
            "name": "SgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCaam00400103:
    key_trnsprt: Optional[KeyTransport4Caam00400103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    kek: Optional[Kek4Caam00400103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00400103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class SignedData4Caam00400103:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: list[AlgorithmIdentification16Caam00400103] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_occurs": 1,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam00400103] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    sgnr: list[Signer3Caam00400103] = field(
        default_factory=list,
        metadata={
            "name": "Sgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class AuthenticatedData4Caam00400103:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00400103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Caam00400103] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam00400103] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class ContentInformationType14Caam00400103:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    sgnd_data: Optional[SignedData4Caam00400103] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )


@dataclass
class EnvelopedData4Caam00400103:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00400103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Caam00400103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Atmequipment3Caam00400103:
    class Meta:
        name = "ATMEquipment3"

    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sgnd_srl_nb: Optional[ContentInformationType14Caam00400103] = field(
        default=None,
        metadata={
            "name": "SgndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    frmwr_prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmwrPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmwr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmwrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmwr_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmwrVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmsignature2ChoiceCaam00400103:
    class Meta:
        name = "ATMSignature2Choice"

    dgtl_sgntr: Optional[ContentInformationType14Caam00400103] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    trrltd_data: Optional[TrrelatedData2Caam00400103] = field(
        default=None,
        metadata={
            "name": "TRRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class ContentInformationType10Caam00400103:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Caam00400103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )


@dataclass
class ContentInformationType13Caam00400103:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Caam00400103] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    sgnd_data: Optional[SignedData4Caam00400103] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AtmsecurityContext3Caam00400103:
    class Meta:
        name = "ATMSecurityContext3"

    cur_scty_schme: Optional[AtmsecurityScheme3Code] = field(
        default=None,
        metadata={
            "name": "CurSctySchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    dvc_prprty: Optional[Atmequipment3Caam00400103] = field(
        default=None,
        metadata={
            "name": "DvcPrprty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    cur_cfgtn: Optional[AtmsecurityConfiguration1Caam00400103] = field(
        default=None,
        metadata={
            "name": "CurCfgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class KeyChoiceValue2Caam00400103:
    ncrptd_key_val: Optional[ContentInformationType10Caam00400103] = field(
        default=None,
        metadata={
            "name": "NcrptdKeyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    trrltd_data: Optional[TrrelatedData2Caam00400103] = field(
        default=None,
        metadata={
            "name": "TRRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class CryptographicKey12Caam00400103:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    scty_domn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyDomnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    seq_cntr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tp: Optional[CryptographicKeyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    fctn: list[KeyUsage1Code] = field(
        default_factory=list,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    actvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    deactvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DeactvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    key_chck_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "KeyChckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    pblc_key_val: Optional[PublicRsakey1Caam00400103] = field(
        default=None,
        metadata={
            "name": "PblcKeyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    key_chc_val: Optional[KeyChoiceValue2Caam00400103] = field(
        default=None,
        metadata={
            "name": "KeyChcVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class SecurityParameters10Caam00400103:
    hst_chllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "HstChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    key: list[CryptographicKey12Caam00400103] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    sgntr_chc: Optional[Atmsignature2ChoiceCaam00400103] = field(
        default=None,
        metadata={
            "name": "SgntrChc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AtmkeyDownloadResponse4Caam00400103:
    class Meta:
        name = "ATMKeyDownloadResponse4"

    envt: Optional[Atmenvironment7Caam00400103] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    atmscty_cntxt: Optional[AtmsecurityContext3Caam00400103] = field(
        default=None,
        metadata={
            "name": "ATMSctyCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    atmchllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ATMChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    hst_scty_params: Optional[SecurityParameters10Caam00400103] = field(
        default=None,
        metadata={
            "name": "HstSctyParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    cmd: list[Atmcommand13Caam00400103] = field(
        default_factory=list,
        metadata={
            "name": "Cmd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class AtmkeyDownloadResponseV03Caam00400103:
    class Meta:
        name = "ATMKeyDownloadResponseV03"

    hdr: Optional[Header31Caam00400103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
            "required": True,
        },
    )
    prtctd_atmkey_dwnld_rspn: Optional[ContentInformationType10Caam00400103] = field(
        default=None,
        metadata={
            "name": "PrtctdATMKeyDwnldRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    atmkey_dwnld_rspn: Optional[AtmkeyDownloadResponse4Caam00400103] = field(
        default=None,
        metadata={
            "name": "ATMKeyDwnldRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType13Caam00400103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03",
        },
    )


@dataclass
class Caam00400103:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caam.004.001.03"

    atmkey_dwnld_rspn: Optional[AtmkeyDownloadResponseV03Caam00400103] = field(
        default=None,
        metadata={
            "name": "ATMKeyDwnldRspn",
            "type": "Element",
            "required": True,
        },
    )
