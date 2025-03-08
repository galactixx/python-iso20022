from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.catm.enums import (
    BatchTransactionType1Code,
    CancellationProcess2Code,
    DataSetCategory10Code,
    DataSetCategory18Code,
    ExchangePolicy2Code,
    FinancialCapture1Code,
    MessageFunction43Code,
    MessageItemCondition2Code,
    NetworkType2Code,
    PartyType15Code,
    ReconciliationCriteria1Code,
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
    CryptographicKeyType3Code,
    EncryptionFormat2Code,
    KeyUsage1Code,
    NetworkType1Code,
    NonFinancialRequestType2Code,
    PartyType7Code,
    PartyType33Code,
    PoicommunicationType2Code,
    RetailerMessage1Code,
    RetailerService2Code,
    RetailerService8Code,
    TimeUnit1Code,
    TypeOfAmount8Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13"


@dataclass
class GenericInformation1Catm00300113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class GeolocationGeographicCoordinates1Catm00300113(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeolocationUtmcoordinates1Catm00300113(ISO20022MessageElement):
    class Meta:
        name = "GeolocationUTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier7Catm00300113(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier7"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class LocalDateTime1Catm00300113(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    utcoffset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTCOffset",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class Organisation26Catm00300113(ISO20022MessageElement):
    cmon_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CmonNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "pattern": r"[0-9]{3,3}",
        },
    )
    mrchnt_ctgy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntCtgyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 3,
            "max_length": 4,
        },
    )
    regd_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegdIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginatorInformation1Catm00300113(ISO20022MessageElement):
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class PointOfInteractionComponentIdentification2Catm00300113(ISO20022MessageElement):
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prvdr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class AcquirerHostConfiguration9Catm00300113(ISO20022MessageElement):
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_to_snd: list[MessageFunction43Code] = field(
        default_factory=list,
        metadata={
            "name": "MsgToSnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )
    xtrnly_tp_spprtd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "XtrnlyTpSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class AlgorithmIdentification36Catm00300113(ISO20022MessageElement):
    algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )


@dataclass
class DataSetIdentification10Catm00300113(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp: Optional[DataSetCategory18Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class EncapsulatedContent3Catm00300113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification176Catm00300113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification186Catm00300113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp: Optional[PartyType7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )


@dataclass
class Geolocation1Catm00300113(ISO20022MessageElement):
    geogc_cordints: Optional[GeolocationGeographicCoordinates1Catm00300113] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    utmcordints: Optional[GeolocationUtmcoordinates1Catm00300113] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class Kekidentifier5Catm00300113(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier5"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )
    tp: Optional[CryptographicKeyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    fctn: list[KeyUsage1Code] = field(
        default_factory=list,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class MessageItemCondition2Catm00300113(ISO20022MessageElement):
    itm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    cond: Optional[MessageItemCondition2Code] = field(
        default=None,
        metadata={
            "name": "Cond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    val: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class NetworkParameters9Catm00300113(ISO20022MessageElement):
    ntwk_tp: Optional[NetworkType1Code] = field(
        default=None,
        metadata={
            "name": "NtwkTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    adr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class Parameter12Catm00300113(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class Parameter18Catm00300113(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class Parameter7Catm00300113(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class PhysicalInterfaceParameter1Catm00300113(ISO20022MessageElement):
    intrfc_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrfcNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    intrfc_tp: Optional[PoicommunicationType2Code] = field(
        default=None,
        metadata={
            "name": "IntrfcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_params: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AddtlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 2048,
            "format": "base64",
        },
    )


@dataclass
class ProcessRetry3Catm00300113(ISO20022MessageElement):
    dely: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "pattern": r"[0-9]{1,9}",
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    unit_of_tm: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class ProcessTiming6Catm00300113(ISO20022MessageElement):
    start_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    end_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    prd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "pattern": r"[0-9]{1,9}",
        },
    )
    unit_of_tm: Optional[TimeUnit1Code] = field(
        default=None,
        metadata={
            "name": "UnitOfTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class RelativeDistinguishedName1Catm00300113(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class SaleToPoiprotocolParameter3Catm00300113(ISO20022MessageElement):
    class Meta:
        name = "SaleToPOIProtocolParameter3"

    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    mrchnt_id: Optional[Organisation26Catm00300113] = field(
        default=None,
        metadata={
            "name": "MrchntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mrchnt_poiid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntPOIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sale_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SaleId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    allwd_sale_msg: list[RetailerMessage1Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdSaleMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    allwd_poimsg: list[RetailerMessage1Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdPOIMsg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    allwd_poisvc: list[RetailerService2Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdPOISvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    allwd_sale_dvc: list[RetailerService8Code] = field(
        default_factory=list,
        metadata={
            "name": "AllwdSaleDvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    xtrnly_tp_spprtd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "XtrnlyTpSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class AlgorithmIdentification31Catm00300113(ISO20022MessageElement):
    algo: Optional[Algorithm27Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter7Catm00300113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class AlgorithmIdentification32Catm00300113(ISO20022MessageElement):
    algo: Optional[Algorithm28Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter12Catm00300113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class AlgorithmIdentification34Catm00300113(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter18Catm00300113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class CertificateIssuer1Catm00300113(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )


@dataclass
class DigestedData6Catm00300113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Catm00300113] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00300113] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    dgst: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Dgst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class ExchangeConfiguration10Catm00300113(ISO20022MessageElement):
    xchg_plcy: list[ExchangePolicy2Code] = field(
        default_factory=list,
        metadata={
            "name": "XchgPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    re_try: Optional[ProcessRetry3Catm00300113] = field(
        default=None,
        metadata={
            "name": "ReTry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    tm_cond: Optional[ProcessTiming6Catm00300113] = field(
        default=None,
        metadata={
            "name": "TmCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    xchg_faild: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XchgFaild",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    xchg_dclnd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XchgDclnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class ExchangeConfiguration9Catm00300113(ISO20022MessageElement):
    xchg_plcy: list[ExchangePolicy2Code] = field(
        default_factory=list,
        metadata={
            "name": "XchgPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    max_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    max_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    re_try: Optional[ProcessRetry3Catm00300113] = field(
        default=None,
        metadata={
            "name": "ReTry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    tm_cond: Optional[ProcessTiming6Catm00300113] = field(
        default=None,
        metadata={
            "name": "TmCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class NetworkParameters7Catm00300113(ISO20022MessageElement):
    adr: list[NetworkParameters9Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    usr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    accs_cd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AccsCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceProviderParameters3Catm00300113(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    svc_prvdr_id: list[GenericIdentification176Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "SvcPrvdrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    appl_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst: list[AcquirerHostConfiguration9Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Hst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    non_fin_actn_spprtd: list[NonFinancialRequestType2Code] = field(
        default_factory=list,
        metadata={
            "name": "NonFinActnSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class TmsprotocolParameters7Catm00300113(ISO20022MessageElement):
    class Meta:
        name = "TMSProtocolParameters7"

    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    termnl_mgr_id: Optional[GenericIdentification176Catm00300113] = field(
        default=None,
        metadata={
            "name": "TermnlMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )
    mntnc_svc: list[DataSetCategory10Code] = field(
        default_factory=list,
        metadata={
            "name": "MntncSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    appl_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    poiid: Optional[str] = field(
        default=None,
        metadata={
            "name": "POIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    initg_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_pty_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptPtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    file_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FileTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    msg_itm: list[MessageItemCondition2Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "MsgItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    xtrnly_tp_spprtd: list[str] = field(
        default_factory=list,
        metadata={
            "name": "XtrnlyTpSpprtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class AcquirerProtocolExchangeBehavior2Catm00300113(ISO20022MessageElement):
    fin_captr: Optional[FinancialCapture1Code] = field(
        default=None,
        metadata={
            "name": "FinCaptr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    btch_trf: Optional[ExchangeConfiguration9Catm00300113] = field(
        default=None,
        metadata={
            "name": "BtchTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    cmpltn_xchg: Optional[ExchangeConfiguration10Catm00300113] = field(
        default=None,
        metadata={
            "name": "CmpltnXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    cxl_xchg: Optional[CancellationProcess2Code] = field(
        default=None,
        metadata={
            "name": "CxlXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class ClockSynchronisation3Catm00300113(ISO20022MessageElement):
    poitm_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "POITmZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    synctn_svr: list[NetworkParameters7Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "SynctnSvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    dely: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Dely",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class EncryptedContent7Catm00300113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification32Catm00300113] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification177Catm00300113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    issr: Optional[PartyType33Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rmot_accs: Optional[NetworkParameters7Catm00300113] = field(
        default=None,
        metadata={
            "name": "RmotAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    glctn: Optional[Geolocation1Catm00300113] = field(
        default=None,
        metadata={
            "name": "Glctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class HostCommunicationParameter6Catm00300113(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    hst_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    adr: Optional[NetworkParameters7Catm00300113] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    key: list[Kekidentifier5Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    ntwk_svc_prvdr: Optional[NetworkParameters7Catm00300113] = field(
        default=None,
        metadata={
            "name": "NtwkSvcPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    phys_intrfc: Optional[PhysicalInterfaceParameter1Catm00300113] = field(
        default=None,
        metadata={
            "name": "PhysIntrfc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class IssuerAndSerialNumber2Catm00300113(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Catm00300113] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Kek9Catm00300113(ISO20022MessageElement):
    class Meta:
        name = "KEK9"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier7Catm00300113] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification32Catm00300113] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class NetworkParameters8Catm00300113(ISO20022MessageElement):
    tp: Optional[NetworkType2Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    accs: Optional[NetworkParameters7Catm00300113] = field(
        default=None,
        metadata={
            "name": "Accs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )


@dataclass
class Parameter16Catm00300113(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00300113] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    salt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SaltLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    trlr_fld: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrlrFld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    oidcrv_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "OIDCrvNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class Parameter17Catm00300113(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat2Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    dgst_algo: Optional[Algorithm26Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification34Catm00300113] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class AcquirerProtocolParameters16Catm00300113(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    acqrr_id: list[GenericIdentification176Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "AcqrrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    appl_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst: list[AcquirerHostConfiguration9Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Hst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    on_line_tx: Optional[AcquirerProtocolExchangeBehavior2Catm00300113] = field(
        default=None,
        metadata={
            "name": "OnLineTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    off_line_tx: Optional[AcquirerProtocolExchangeBehavior2Catm00300113] = field(
        default=None,
        metadata={
            "name": "OffLineTx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    rcncltn_xchg: Optional[ExchangeConfiguration9Catm00300113] = field(
        default=None,
        metadata={
            "name": "RcncltnXchg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    rcncltn_by_acqrr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RcncltnByAcqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    ttls_per_ccy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TtlsPerCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    splt_ttls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpltTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    splt_ttl_crit: list[ReconciliationCriteria1Code] = field(
        default_factory=list,
        metadata={
            "name": "SpltTtlCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    cmpltn_advc_mndtd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CmpltnAdvcMndtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    amt_qlfr_for_rsvatn: list[TypeOfAmount8Code] = field(
        default_factory=list,
        metadata={
            "name": "AmtQlfrForRsvatn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    rcncltn_err: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RcncltnErr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    card_data_vrfctn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardDataVrfctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    ntfy_off_line_cxl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtfyOffLineCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    btch_trf_cntt: list[BatchTransactionType1Code] = field(
        default_factory=list,
        metadata={
            "name": "BtchTrfCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    file_trf_btch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FileTrfBtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    btch_dgtl_sgntr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BtchDgtlSgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    msg_itm: list[MessageItemCondition2Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "MsgItm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    prtct_card_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtctCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    prvt_card_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrvtCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    mndtry_scty_trlr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MndtrySctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class AlgorithmIdentification33Catm00300113(ISO20022MessageElement):
    algo: Optional[Algorithm29Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter16Catm00300113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class AlgorithmIdentification35Catm00300113(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    param: Optional[Parameter17Catm00300113] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class MerchantConfigurationParameters6Catm00300113(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    mrchnt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MrchntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    param_frmt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamFrmtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )
    prxy: Optional[NetworkParameters8Catm00300113] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    othr_params_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OthrParamsLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_end: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    othr_params: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "OthrParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )


@dataclass
class PaymentTerminalParameters8Catm00300113(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    vndr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "VndrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    param_frmt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamFrmtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )
    clck_synctn: Optional[ClockSynchronisation3Catm00300113] = field(
        default=None,
        metadata={
            "name": "ClckSynctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    tm_zone_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TmZoneLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 70,
        },
    )
    lcl_dt_tm: list[LocalDateTime1Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "LclDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    othr_params_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OthrParamsLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_end: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    othr_params: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "OthrParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )


@dataclass
class Recipient13ChoiceCatm00300113(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber2Catm00300113] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    sbjt_key_idr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SbjtKeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class Traceability8Catm00300113(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification177Catm00300113] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    prtcol_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 6,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )


@dataclass
class KeyTransport10Catm00300113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient13ChoiceCatm00300113] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification35Catm00300113] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Signer8Catm00300113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    sgnr_id: Optional[Recipient13ChoiceCatm00300113] = field(
        default=None,
        metadata={
            "name": "SgnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    dgst_algo: Optional[AlgorithmIdentification36Catm00300113] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    sgnd_attrbts: list[GenericInformation1Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "SgndAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    sgntr_algo: Optional[AlgorithmIdentification33Catm00300113] = field(
        default=None,
        metadata={
            "name": "SgntrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    sgntr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 3000,
            "format": "base64",
        },
    )


@dataclass
class Tmsheader1Catm00300113(ISO20022MessageElement):
    class Meta:
        name = "TMSHeader1"

    dwnld_trf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DwnldTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    frmt_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "FrmtVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    initg_pty: Optional[GenericIdentification176Catm00300113] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    rcpt_pty: Optional[GenericIdentification177Catm00300113] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    tracblt: list[Traceability8Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class Recipient15ChoiceCatm00300113(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport10Catm00300113] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    kek: Optional[Kek9Catm00300113] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    key_idr: Optional[Kekidentifier7Catm00300113] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class SignedData9Catm00300113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dgst_algo: list[AlgorithmIdentification36Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00300113] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    cert: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    sgnr: list[Signer8Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Sgnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class AuthenticatedData10Catm00300113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient15ChoiceCatm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification31Catm00300113] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catm00300113] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData11Catm00300113(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgtr_inf: Optional[OriginatorInformation1Catm00300113] = field(
        default=None,
        metadata={
            "name": "OrgtrInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    rcpt: list[Recipient15ChoiceCatm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent7Catm00300113] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class ContentInformationType38Catm00300113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData10Catm00300113] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    sgnd_data: Optional[SignedData9Catm00300113] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class ContentInformationType39Catm00300113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData11Catm00300113] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    authntcd_data: Optional[AuthenticatedData10Catm00300113] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    sgnd_data: Optional[SignedData9Catm00300113] = field(
        default=None,
        metadata={
            "name": "SgndData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    dgstd_data: Optional[DigestedData6Catm00300113] = field(
        default=None,
        metadata={
            "name": "DgstdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class ContentInformationType40Catm00300113(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData11Catm00300113] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )


@dataclass
class ApplicationParameters13Catm00300113(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    appl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    param_frmt_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParamFrmtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 8,
        },
    )
    params_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ParamsLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_end: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    params: list[bytes] = field(
        default_factory=list,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    ncrptd_params: Optional[ContentInformationType40Catm00300113] = field(
        default=None,
        metadata={
            "name": "NcrptdParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class CryptographicKey18Catm00300113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    addtl_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 256,
        },
    )
    scty_prfl: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctyPrfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    itm_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItmNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    tp: Optional[CryptographicKeyType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    fctn: list[KeyUsage1Code] = field(
        default_factory=list,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    actvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    deactvtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DeactvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    key_val: Optional[ContentInformationType39Catm00300113] = field(
        default=None,
        metadata={
            "name": "KeyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    cmpnt_wth_authrsd_accs: list[GenericIdentification186Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "CmpntWthAuthrsdAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    prtctd_cmpnt_wth_authrsd_accs: list[ContentInformationType39Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "PrtctdCmpntWthAuthrsdAccs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    key_chck_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "KeyChckVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )
    addtl_mgmt_inf: list[GenericInformation1Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "AddtlMgmtInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class ExternallyDefinedData5Catm00300113(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 1025,
        },
    )
    val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )
    prtctd_val: Optional[ContentInformationType39Catm00300113] = field(
        default=None,
        metadata={
            "name": "PrtctdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class PackageType5Catm00300113(ISO20022MessageElement):
    packg_id: Optional[GenericIdentification176Catm00300113] = field(
        default=None,
        metadata={
            "name": "PackgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    packg_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PackgLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_start: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetStart",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    offset_end: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OffsetEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_inclusive": Decimal("1"),
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    packg_blck: list[ExternallyDefinedData5Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "PackgBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class SecurityParameters16Catm00300113(ISO20022MessageElement):
    actn_tp: Optional[TerminalManagementAction3Code] = field(
        default=None,
        metadata={
            "name": "ActnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    poichllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "POIChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    tmchllng: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TMChllng",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )
    scty_elmt: list[CryptographicKey18Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "SctyElmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class TerminalPackageType5Catm00300113(ISO20022MessageElement):
    poicmpnt_id: list[PointOfInteractionComponentIdentification2Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "POICmpntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    packg: list[PackageType5Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )


@dataclass
class AcceptorConfigurationContent13Catm00300113(ISO20022MessageElement):
    rplc_cfgtn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RplcCfgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    tmsprtcol_params: list[TmsprotocolParameters7Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "TMSPrtcolParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    acqrr_prtcol_params: list[AcquirerProtocolParameters16Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "AcqrrPrtcolParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    svc_prvdr_params: list[ServiceProviderParameters3Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "SvcPrvdrParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    mrchnt_params: list[MerchantConfigurationParameters6Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "MrchntParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    termnl_params: list[PaymentTerminalParameters8Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "TermnlParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    appl_params: list[ApplicationParameters13Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "ApplParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    hst_com_params: list[HostCommunicationParameter6Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "HstComParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    scty_params: list[SecurityParameters16Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "SctyParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    sale_to_poiparams: list[SaleToPoiprotocolParameter3Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "SaleToPOIParams",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    termnl_packg: list[TerminalPackageType5Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "TermnlPackg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class AcceptorConfigurationDataSet5Catm00300113(ISO20022MessageElement):
    id: Optional[DataSetIdentification10Catm00300113] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    seq_cntr: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqCntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "pattern": r"[0-9]{1,9}",
        },
    )
    last_seq: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastSeq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    poiid: list[GenericIdentification176Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "POIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    cfgtn_scp: Optional[PartyType15Code] = field(
        default=None,
        metadata={
            "name": "CfgtnScp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )
    cntt: Optional[AcceptorConfigurationContent13Catm00300113] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )


@dataclass
class AcceptorConfiguration13Catm00300113(ISO20022MessageElement):
    termnl_mgr_id: Optional[GenericIdentification176Catm00300113] = field(
        default=None,
        metadata={
            "name": "TermnlMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    poigrp_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "POIGrpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_length": 1,
            "max_length": 35,
        },
    )
    data_set: list[AcceptorConfigurationDataSet5Catm00300113] = field(
        default_factory=list,
        metadata={
            "name": "DataSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "min_occurs": 1,
        },
    )


@dataclass
class AcceptorConfigurationUpdateV13Catm00300113(ISO20022MessageElement):
    hdr: Optional[Tmsheader1Catm00300113] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    accptr_cfgtn: Optional[AcceptorConfiguration13Catm00300113] = field(
        default=None,
        metadata={
            "name": "AccptrCfgtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
            "required": True,
        },
    )
    scty_trlr: Optional[ContentInformationType38Catm00300113] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13",
        },
    )


@dataclass
class Catm00300113(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catm.003.001.13"

    accptr_cfgtn_upd: Optional[AcceptorConfigurationUpdateV13Catm00300113] = field(
        default=None,
        metadata={
            "name": "AccptrCfgtnUpd",
            "type": "Element",
            "required": True,
        },
    )
