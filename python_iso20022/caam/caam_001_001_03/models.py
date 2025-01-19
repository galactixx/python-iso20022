from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.caam.caam_001_001_03.enums import (
    Atmstatus3Code,
    FailureReason5Code,
    FailureReason6Code,
    Tr34Status1Code,
)
from python_iso20022.caam.enums import (
    Algorithm14Code,
    Atmcommand6Code,
    AtmsecurityScheme3Code,
    AtmsecurityScheme4Code,
    Atmstatus2Code,
    MessageProtection1Code,
    TerminalManagementActionResult2Code,
)
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    Atmdevice2Code,
    Atmstatus1Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    CryptographicKeyType3Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    KeyUsage1Code,
    MessageFunction11Code,
    PartyType12Code,
    Pinformat4Code,
    TransactionEnvironment2Code,
    TransactionEnvironment3Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03"


@dataclass
class AtmcommandIdentification1Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommandIdentification1"

    orgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Atmequipment2Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMEquipment2"

    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmwr_prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmwrPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmwr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmwrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    frmwr_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmwrVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmsecurityConfiguration2Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMSecurityConfiguration2"

    max_smmtrc_key: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSmmtrcKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_asmmtrc_key: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAsmmtrcKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_rsakey_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxRSAKeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_root_key_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxRootKeyLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Acquirer7Caam00100103(ISO20022MessageElement):
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Caam00100103(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Utmcoordinates1Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Atmcommand11Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommand11"

    tp: Optional[Atmcommand6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    reqrd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReqrdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    prcd_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PrcdDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Caam00100103] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    rslt: Optional[TerminalManagementActionResult2Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    addtl_err_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlErrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Atmcommand12Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMCommand12"

    tp: Optional[Atmcommand6Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    cmd_id: Optional[AtmcommandIdentification1Caam00100103] = field(
        default=None,
        metadata={
            "name": "CmdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AtmconfigurationParameter1Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmmessageFunction2Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmsecurityConfiguration3Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMSecurityConfiguration3"

    asmmtrc_ncrptn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsmmtrcNcrptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    asmmtrc_key_std_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AsmmtrcKeyStdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    asmmtrc_ncrptn_algo: list[Algorithm7Code] = field(
        default_factory=list,
        metadata={
            "name": "AsmmtrcNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    smmtrc_trnsprt_key: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmmtrcTrnsprtKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    smmtrc_trnsprt_key_algo: list[Algorithm13Code] = field(
        default_factory=list,
        metadata={
            "name": "SmmtrcTrnsprtKeyAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    smmtrc_ncrptn_algo: list[Algorithm15Code] = field(
        default_factory=list,
        metadata={
            "name": "SmmtrcNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    ncrptn_frmt: list[EncryptionFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AtmsecurityConfiguration4Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMSecurityConfiguration4"

    max_certs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxCerts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_sgntrs: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxSgntrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgtl_sgntr_algo: list[Algorithm14Code] = field(
        default_factory=list,
        metadata={
            "name": "DgtlSgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AtmsecurityConfiguration5Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMSecurityConfiguration5"

    pinfrmt: list[Pinformat4Code] = field(
        default_factory=list,
        metadata={
            "name": "PINFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    pinlngth_cpblties: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Atmstatus1Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMStatus1"

    cur_sts: Optional[Atmstatus1Code] = field(
        default=None,
        metadata={
            "name": "CurSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    dmndd_sts: Optional[Atmstatus1Code] = field(
        default=None,
        metadata={
            "name": "DmnddSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AlgorithmIdentification16Caam00100103(ISO20022MessageElement):
    algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )


@dataclass
class CryptographicKey11Caam00100103(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )
    scty_domn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyDomnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    seq_cntr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    tp: Optional[CryptographicKeyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    fctn: list[KeyUsage1Code] = field(
        default_factory=list,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_occurs": 1,
        },
    )
    actvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    deactvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DeactvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    key_chck_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "KeyChckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    cur_sts: Optional[Atmstatus3Code] = field(
        default=None,
        metadata={
            "name": "CurSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    failr_rsn: Optional[FailureReason6Code] = field(
        default=None,
        metadata={
            "name": "FailrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class EncapsulatedContent3Caam00100103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Caam00100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCaam00100103(ISO20022MessageElement):
    geogc_cordints: Optional[GeographicCoordinates1Caam00100103] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    utmcordints: Optional[Utmcoordinates1Caam00100103] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class Parameter5Caam00100103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class Parameter6Caam00100103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class Parameter7Caam00100103(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class RelativeDistinguishedName1Caam00100103(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Caam00100103(ISO20022MessageElement):
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmequipment1Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMEquipment1"

    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cfgtn_param: list[AtmconfigurationParameter1Caam00100103] = field(
        default_factory=list,
        metadata={
            "name": "CfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AtmsecurityConfiguration1Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMSecurityConfiguration1"

    keys: Optional[AtmsecurityConfiguration2Caam00100103] = field(
        default=None,
        metadata={
            "name": "Keys",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    ncrptn: Optional[AtmsecurityConfiguration3Caam00100103] = field(
        default=None,
        metadata={
            "name": "Ncrptn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    macalgo: list[Algorithm12Code] = field(
        default_factory=list,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    dgst_algo: list[Algorithm11Code] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    dgtl_sgntr: Optional[AtmsecurityConfiguration4Caam00100103] = field(
        default=None,
        metadata={
            "name": "DgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    pin: Optional[AtmsecurityConfiguration5Caam00100103] = field(
        default=None,
        metadata={
            "name": "PIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    msg_prtcn: list[MessageProtection1Code] = field(
        default_factory=list,
        metadata={
            "name": "MsgPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AlgorithmIdentification12Caam00100103(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter5Caam00100103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AlgorithmIdentification13Caam00100103(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00100103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AlgorithmIdentification14Caam00100103(ISO20022MessageElement):
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00100103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AlgorithmIdentification15Caam00100103(ISO20022MessageElement):
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Caam00100103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class CertificateIssuer1Caam00100103(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caam00100103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class PostalAddress17Caam00100103(ISO20022MessageElement):
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCaam00100103] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class Traceability4Caam00100103(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification77Caam00100103] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )


@dataclass
class AtmsecurityDevice2Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMSecurityDevice2"

    dvc_prprty: Optional[Atmequipment2Caam00100103] = field(
        default=None,
        metadata={
            "name": "DvcPrprty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    cur_cfgtn: Optional[AtmsecurityConfiguration1Caam00100103] = field(
        default=None,
        metadata={
            "name": "CurCfgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    spprtd_cfgtn: Optional[AtmsecurityConfiguration1Caam00100103] = field(
        default=None,
        metadata={
            "name": "SpprtdCfgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    cur_sts: Optional[Atmstatus2Code] = field(
        default=None,
        metadata={
            "name": "CurSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    incdnt: Optional[FailureReason5Code] = field(
        default=None,
        metadata={
            "name": "Incdnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    bndg_stat: Optional[Tr34Status1Code] = field(
        default=None,
        metadata={
            "name": "BndgStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AutomatedTellerMachine5Caam00100103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lctn: Optional[PostalAddress17Caam00100103] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    lctn_ctgy: Optional[TransactionEnvironment2Code] = field(
        default=None,
        metadata={
            "name": "LctnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    eqpmnt: Optional[Atmequipment1Caam00100103] = field(
        default=None,
        metadata={
            "name": "Eqpmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    out_of_svc_dvc: list[Atmdevice2Code] = field(
        default_factory=list,
        metadata={
            "name": "OutOfSvcDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    msg_prtcn: Optional[MessageProtection1Code] = field(
        default=None,
        metadata={
            "name": "MsgPrtcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class EncryptedContent3Caam00100103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Caam00100103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Caam00100103(ISO20022MessageElement):
    msg_fctn: Optional[AtmmessageFunction2Caam00100103] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Caam00100103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class IssuerAndSerialNumber1Caam00100103(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Caam00100103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Caam00100103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Caam00100103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Caam00100103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam00100103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class Parameter8Caam00100103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam00100103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    salt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SaltLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Atmenvironment6Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMEnvironment6"

    acqrr: Optional[Acquirer7Caam00100103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    atmmgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hstg_ntty: Optional[TerminalHosting1Caam00100103] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    atm: Optional[AutomatedTellerMachine5Caam00100103] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )


@dataclass
class AtmsecurityContext5Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMSecurityContext5"

    cur_scty_schme: Optional[AtmsecurityScheme3Code] = field(
        default=None,
        metadata={
            "name": "CurSctySchme",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    scty_schme_cpblties: list[AtmsecurityScheme4Code] = field(
        default_factory=list,
        metadata={
            "name": "SctySchmeCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    scty_dvc: Optional[AtmsecurityDevice2Caam00100103] = field(
        default=None,
        metadata={
            "name": "SctyDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    key: list[CryptographicKey11Caam00100103] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    hst_chllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "HstChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class AlgorithmIdentification11Caam00100103(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter4Caam00100103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AlgorithmIdentification17Caam00100103(ISO20022MessageElement):
    algo: Optional[Algorithm14Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter8Caam00100103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class Recipient5ChoiceCaam00100103(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caam00100103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00100103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AtmdeviceReport3Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMDeviceReport3"

    envt: Optional[Atmenvironment6Caam00100103] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    atmgbl_sts: Optional[Atmstatus1Caam00100103] = field(
        default=None,
        metadata={
            "name": "ATMGblSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    cmd_rslt: list[Atmcommand11Caam00100103] = field(
        default_factory=list,
        metadata={
            "name": "CmdRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    cmd_cntxt: Optional[Atmcommand12Caam00100103] = field(
        default=None,
        metadata={
            "name": "CmdCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    atmscty_cntxt: Optional[AtmsecurityContext5Caam00100103] = field(
        default=None,
        metadata={
            "name": "ATMSctyCntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class KeyTransport4Caam00100103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaam00100103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Caam00100103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Signer3Caam00100103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sgnr_id: Optional[Recipient5ChoiceCaam00100103] = field(
        default=None,
        metadata={
            "name": "SgnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    dgst_algo: Optional[AlgorithmIdentification16Caam00100103] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    sgntr_algo: Optional[AlgorithmIdentification17Caam00100103] = field(
        default=None,
        metadata={
            "name": "SgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCaam00100103(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport4Caam00100103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    kek: Optional[Kek4Caam00100103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00100103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class SignedData4Caam00100103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: list[AlgorithmIdentification16Caam00100103] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_occurs": 1,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam00100103] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    sgnr: list[Signer3Caam00100103] = field(
        default_factory=list,
        metadata={
            "name": "Sgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class AuthenticatedData4Caam00100103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00100103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Caam00100103] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam00100103] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Caam00100103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00100103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Caam00100103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class ContentInformationType10Caam00100103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Caam00100103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )


@dataclass
class ContentInformationType13Caam00100103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Caam00100103] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    sgnd_data: Optional[SignedData4Caam00100103] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class AtmdeviceReportV03Caam00100103(ISO20022MessageElement):
    class Meta:
        name = "ATMDeviceReportV03"

    hdr: Optional[Header31Caam00100103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
            "required": True,
        },
    )
    prtctd_atmdvc_rpt: Optional[ContentInformationType10Caam00100103] = field(
        default=None,
        metadata={
            "name": "PrtctdATMDvcRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    atmdvc_rpt: Optional[AtmdeviceReport3Caam00100103] = field(
        default=None,
        metadata={
            "name": "ATMDvcRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType13Caam00100103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03",
        },
    )


@dataclass
class Caam00100103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caam.001.001.03"

    atmdvc_rpt: Optional[AtmdeviceReportV03Caam00100103] = field(
        default=None,
        metadata={
            "name": "ATMDvcRpt",
            "type": "Element",
            "required": True,
        },
    )
