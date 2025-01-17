from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.catm.enums import (
    DataSetCategory19Code,
    TerminalManagementAction3Code,
)
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm26Code,
    Algorithm27Code,
    Algorithm28Code,
    Algorithm29Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    EncryptionFormat2Code,
    NetworkType1Code,
    PartyType33Code,
    Response2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08"


@dataclass
class GenericInformation1Catm00600108:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GeolocationGeographicCoordinates1Catm00600108:
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    long: Optional[str] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeolocationUtmcoordinates1Catm00600108:
    class Meta:
        name = "GeolocationUTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    utmestwrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMEstwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    utmnrthwrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMNrthwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier7Catm00600108:
    class Meta:
        name = "KEKIdentifier7"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class MaintenanceIdentificationAssociation1Catm00600108:
    mstr_tmid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrTMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tmid: Optional[str] = field(
        default=None,
        metadata={
            "name": "TMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginatorInformation1Catm00600108:
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class AlgorithmIdentification36Catm00600108:
    algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )


@dataclass
class EncapsulatedContent3Catm00600108:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification176Catm00600108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Geolocation1Catm00600108:
    geogc_cordints: Optional[GeolocationGeographicCoordinates1Catm00600108] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    utmcordints: Optional[GeolocationUtmcoordinates1Catm00600108] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class NetworkParameters9Catm00600108:
    ntwk_tp: Optional[NetworkType1Code] = field(
        default=None,
        metadata={
            "name": "NtwkTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    adr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class Parameter12Catm00600108:
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class Parameter18Catm00600108:
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class Parameter7Catm00600108:
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class RelativeDistinguishedName1Catm00600108:
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AlgorithmIdentification31Catm00600108:
    algo: Optional[Algorithm27Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    param: Optional[Parameter7Catm00600108] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class AlgorithmIdentification32Catm00600108:
    algo: Optional[Algorithm28Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    param: Optional[Parameter12Catm00600108] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class AlgorithmIdentification34Catm00600108:
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    param: Optional[Parameter18Catm00600108] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class CertificateIssuer1Catm00600108:
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_occurs": 1,
        },
    )


@dataclass
class DigestedData6Catm00600108:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Catm00600108] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00600108] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    dgst: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class NetworkParameters7Catm00600108:
    adr: list[NetworkParameters9Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_occurs": 1,
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    svr_cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SvrCert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    svr_cert_idr: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SvrCertIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    clnt_cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "ClntCert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EncryptedContent7Catm00600108:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification32Catm00600108] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification177Catm00600108:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmot_accs: Optional[NetworkParameters7Catm00600108] = field(
        default=None,
        metadata={
            "name": "RmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    glctn: Optional[Geolocation1Catm00600108] = field(
        default=None,
        metadata={
            "name": "Glctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class IssuerAndSerialNumber2Catm00600108:
    issr: Optional[CertificateIssuer1Catm00600108] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Kek9Catm00600108:
    class Meta:
        name = "KEK9"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier7Catm00600108] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification32Catm00600108] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter16Catm00600108:
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00600108] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    salt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SaltLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trlr_fld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrlrFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    oidcrv_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OIDCrvNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Parameter17Catm00600108:
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00600108] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class AlgorithmIdentification33Catm00600108:
    algo: Optional[Algorithm29Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    param: Optional[Parameter16Catm00600108] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class AlgorithmIdentification35Catm00600108:
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    param: Optional[Parameter17Catm00600108] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class Recipient13ChoiceCatm00600108:
    issr_and_srl_nb: Optional[IssuerAndSerialNumber2Catm00600108] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    sbjt_key_idr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SbjtKeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class Traceability8Catm00600108:
    rlay_id: Optional[GenericIdentification177Catm00600108] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    prtcol_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 6,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )


@dataclass
class KeyTransport10Catm00600108:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient13ChoiceCatm00600108] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification35Catm00600108] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Signer8Catm00600108:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sgnr_id: Optional[Recipient13ChoiceCatm00600108] = field(
        default=None,
        metadata={
            "name": "SgnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Catm00600108] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    sgnd_attrbts: list[GenericInformation1Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "SgndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    sgntr_algo: Optional[AlgorithmIdentification33Catm00600108] = field(
        default=None,
        metadata={
            "name": "SgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )


@dataclass
class Tmsheader1Catm00600108:
    class Meta:
        name = "TMSHeader1"

    dwnld_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DwnldTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    frmt_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    xchg_id: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    initg_pty: Optional[GenericIdentification176Catm00600108] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification177Catm00600108] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    tracblt: list[Traceability8Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class Recipient15ChoiceCatm00600108:
    key_trnsprt: Optional[KeyTransport10Catm00600108] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    kek: Optional[Kek9Catm00600108] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    key_idr: Optional[Kekidentifier7Catm00600108] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class SignedData9Catm00600108:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: list[AlgorithmIdentification36Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00600108] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    sgnr: list[Signer8Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "Sgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class AuthenticatedData10Catm00600108:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient15ChoiceCatm00600108] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification31Catm00600108] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00600108] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData11Catm00600108:
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgtr_inf: Optional[OriginatorInformation1Catm00600108] = field(
        default=None,
        metadata={
            "name": "OrgtrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    rcpt: list[Recipient15ChoiceCatm00600108] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent7Catm00600108] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class ContentInformationType38Catm00600108:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData10Catm00600108] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    sgnd_data: Optional[SignedData9Catm00600108] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class ContentInformationType39Catm00600108:
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData11Catm00600108] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    authntcd_data: Optional[AuthenticatedData10Catm00600108] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    sgnd_data: Optional[SignedData9Catm00600108] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    dgstd_data: Optional[DigestedData6Catm00600108] = field(
        default=None,
        metadata={
            "name": "DgstdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class MaintenanceDelegation17Catm00600108:
    mntnc_svc: list[DataSetCategory19Code] = field(
        default_factory=list,
        metadata={
            "name": "MntncSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_occurs": 1,
        },
    )
    rspn: Optional[Response2Code] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    rspn_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RspnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlgtn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "DlgtnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    poisubset: list[str] = field(
        default_factory=list,
        metadata={
            "name": "POISubset",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlgtn_scp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DlgtnScpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlgtn_scp_def: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DlgtnScpDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )
    dlgtn_proof: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DlgtnProof",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    prtctd_dlgtn_proof: Optional[ContentInformationType39Catm00600108] = field(
        default=None,
        metadata={
            "name": "PrtctdDlgtnProof",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    poiid_assoctn: list[MaintenanceIdentificationAssociation1Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "POIIdAssoctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class MaintenanceDelegationResponse8Catm00600108:
    tmid: Optional[GenericIdentification176Catm00600108] = field(
        default=None,
        metadata={
            "name": "TMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    mstr_tmid: Optional[GenericIdentification176Catm00600108] = field(
        default=None,
        metadata={
            "name": "MstrTMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )
    tmdt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TMDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    tmchllng_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TMChllngVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    dlgtn_rspn: list[MaintenanceDelegation17Catm00600108] = field(
        default_factory=list,
        metadata={
            "name": "DlgtnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "min_occurs": 1,
        },
    )


@dataclass
class MaintenanceDelegationResponseV08Catm00600108:
    hdr: Optional[Tmsheader1Catm00600108] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    mntnc_dlgtn_rspn: Optional[MaintenanceDelegationResponse8Catm00600108] = field(
        default=None,
        metadata={
            "name": "MntncDlgtnRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
            "required": True,
        },
    )
    scty_trlr: Optional[ContentInformationType38Catm00600108] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08",
        },
    )


@dataclass
class Catm00600108:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catm.006.001.08"

    mntnc_dlgtn_rspn: Optional[MaintenanceDelegationResponseV08Catm00600108] = field(
        default=None,
        metadata={
            "name": "MntncDlgtnRspn",
            "type": "Element",
            "required": True,
        },
    )
