from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.catm.catm_008_001_07.enums import ResultDetail3Code
from python_iso20022.catm.enums import CardPaymentServiceType10Code
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

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07"


@dataclass
class GenericInformation1Catm00800107(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GeolocationGeographicCoordinates1Catm00800107(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeolocationUtmcoordinates1Catm00800107(ISO20022MessageElement):
    class Meta:
        name = "GeolocationUTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier7Catm00800107(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier7"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class AlgorithmIdentification36Catm00800107(ISO20022MessageElement):
    algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )


@dataclass
class EncapsulatedContent3Catm00800107(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification176Catm00800107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Geolocation1Catm00800107(ISO20022MessageElement):
    geogc_cordints: Optional[GeolocationGeographicCoordinates1Catm00800107] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    utmcordints: Optional[GeolocationUtmcoordinates1Catm00800107] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class NetworkParameters9Catm00800107(ISO20022MessageElement):
    ntwk_tp: Optional[NetworkType1Code] = field(
        default=None,
        metadata={
            "name": "NtwkTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    adr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class Parameter12Catm00800107(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class Parameter18Catm00800107(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class Parameter7Catm00800107(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class RelativeDistinguishedName1Catm00800107(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class ResponseType6Catm00800107(ISO20022MessageElement):
    rspn: Optional[Response2Code] = field(
        default=None,
        metadata={
            "name": "Rspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    rspn_dtl: Optional[ResultDetail3Code] = field(
        default=None,
        metadata={
            "name": "RspnDtl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    addtl_rspn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AlgorithmIdentification31Catm00800107(ISO20022MessageElement):
    algo: Optional[Algorithm27Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    param: Optional[Parameter7Catm00800107] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class AlgorithmIdentification32Catm00800107(ISO20022MessageElement):
    algo: Optional[Algorithm28Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    param: Optional[Parameter12Catm00800107] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class AlgorithmIdentification34Catm00800107(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    param: Optional[Parameter18Catm00800107] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class CertificateIssuer1Catm00800107(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catm00800107] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_occurs": 1,
        },
    )


@dataclass
class CertificateManagementResponse3Catm00800107(ISO20022MessageElement):
    poiid: Optional[GenericIdentification176Catm00800107] = field(
        default=None,
        metadata={
            "name": "POIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    tmid: Optional[GenericIdentification176Catm00800107] = field(
        default=None,
        metadata={
            "name": "TMId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    cert_svc: Optional[CardPaymentServiceType10Code] = field(
        default=None,
        metadata={
            "name": "CertSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    rslt: Optional[ResponseType6Catm00800107] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    poichllng_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "POIChllngVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    tmsdt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TMSDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    clnt_cert: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ClntCert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )
    clnt_cert_pth: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "ClntCertPth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )
    svr_cert_pth: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SvrCertPth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 10240,
            "format": "base64",
        },
    )


@dataclass
class NetworkParameters7Catm00800107(ISO20022MessageElement):
    adr: list[NetworkParameters9Catm00800107] = field(
        default_factory=list,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_occurs": 1,
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification177Catm00800107(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmot_accs: Optional[NetworkParameters7Catm00800107] = field(
        default=None,
        metadata={
            "name": "RmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    glctn: Optional[Geolocation1Catm00800107] = field(
        default=None,
        metadata={
            "name": "Glctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class IssuerAndSerialNumber2Catm00800107(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Catm00800107] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Kek9Catm00800107(ISO20022MessageElement):
    class Meta:
        name = "KEK9"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier7Catm00800107] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification32Catm00800107] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter16Catm00800107(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00800107] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    salt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SaltLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trlr_fld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrlrFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    oidcrv_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OIDCrvNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Parameter17Catm00800107(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00800107] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class AlgorithmIdentification33Catm00800107(ISO20022MessageElement):
    algo: Optional[Algorithm29Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    param: Optional[Parameter16Catm00800107] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class AlgorithmIdentification35Catm00800107(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    param: Optional[Parameter17Catm00800107] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class Recipient13ChoiceCatm00800107(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber2Catm00800107] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    sbjt_key_idr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SbjtKeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class Traceability8Catm00800107(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification177Catm00800107] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    prtcol_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 6,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )


@dataclass
class KeyTransport10Catm00800107(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient13ChoiceCatm00800107] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification35Catm00800107] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Signer8Catm00800107(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sgnr_id: Optional[Recipient13ChoiceCatm00800107] = field(
        default=None,
        metadata={
            "name": "SgnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Catm00800107] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    sgnd_attrbts: list[GenericInformation1Catm00800107] = field(
        default_factory=list,
        metadata={
            "name": "SgndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    sgntr_algo: Optional[AlgorithmIdentification33Catm00800107] = field(
        default=None,
        metadata={
            "name": "SgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )


@dataclass
class Tmsheader1Catm00800107(ISO20022MessageElement):
    class Meta:
        name = "TMSHeader1"

    dwnld_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DwnldTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    frmt_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    initg_pty: Optional[GenericIdentification176Catm00800107] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification177Catm00800107] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    tracblt: list[Traceability8Catm00800107] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class Recipient15ChoiceCatm00800107(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport10Catm00800107] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    kek: Optional[Kek9Catm00800107] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    key_idr: Optional[Kekidentifier7Catm00800107] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class SignedData9Catm00800107(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: list[AlgorithmIdentification36Catm00800107] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00800107] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    sgnr: list[Signer8Catm00800107] = field(
        default_factory=list,
        metadata={
            "name": "Sgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class AuthenticatedData10Catm00800107(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient15ChoiceCatm00800107] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification31Catm00800107] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00800107] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class ContentInformationType38Catm00800107(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData10Catm00800107] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )
    sgnd_data: Optional[SignedData9Catm00800107] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class CertificateManagementResponseV07Catm00800107(ISO20022MessageElement):
    hdr: Optional[Tmsheader1Catm00800107] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    cert_mgmt_rspn: Optional[CertificateManagementResponse3Catm00800107] = field(
        default=None,
        metadata={
            "name": "CertMgmtRspn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
            "required": True,
        },
    )
    scty_trlr: Optional[ContentInformationType38Catm00800107] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07",
        },
    )


@dataclass
class Catm00800107(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07"

    cert_mgmt_rspn: Optional[CertificateManagementResponseV07Catm00800107] = field(
        default=None,
        metadata={
            "name": "CertMgmtRspn",
            "type": "Element",
            "required": True,
        },
    )
