from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.caam.enums import Atmoperation2Code
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    AtmcassetteStatus1Code,
    AtmcassetteType1Code,
    AtmcounterType3Code,
    AtmmediaType3Code,
    AtmmediaType4Code,
    AtmnoteType1Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    EncryptionFormat1Code,
    MessageFunction11Code,
    PartyType12Code,
    TransactionEnvironment3Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01"


@dataclass
class Acquirer7Caam01500101(ISO20022MessageElement):
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Acquirer8Caam01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Caam01500101(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class TransactionIdentifier3Caam01500101(ISO20022MessageElement):
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    hst_tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HstTxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmcassetteCounters5Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMCassetteCounters5"

    tp: Optional[AtmcounterType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    added_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AddedNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rmvd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RmvdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rmvd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RmvdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    dspnsd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DspnsdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dpstd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DpstdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    dpstd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DpstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rcycld_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RcycldNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rtrctd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RtrctdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rtrctd_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RtrctdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    rjctd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RjctdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    presntd_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PresntdNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    initl_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    initl_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class AtmmessageFunction2Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EncapsulatedContent3Caam01500101(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Caam01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCaam01500101(ISO20022MessageElement):
    geogc_cordints: Optional[GeographicCoordinates1Caam01500101] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    utmcordints: Optional[Utmcoordinates1Caam01500101] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class Parameter5Caam01500101(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class Parameter6Caam01500101(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class Parameter7Caam01500101(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class RelativeDistinguishedName1Caam01500101(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Caam01500101(ISO20022MessageElement):
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmcassetteCounters6Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMCassetteCounters6"

    unit_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    mdia_ctgy: Optional[AtmmediaType3Code] = field(
        default=None,
        metadata={
            "name": "MdiaCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    initl_cnt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InitlCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    cur_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CurNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    flow_ttls: list[AtmcassetteCounters5Caam01500101] = field(
        default_factory=list,
        metadata={
            "name": "FlowTtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AlgorithmIdentification12Caam01500101(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter5Caam01500101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AlgorithmIdentification13Caam01500101(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam01500101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AlgorithmIdentification14Caam01500101(ISO20022MessageElement):
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam01500101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AlgorithmIdentification15Caam01500101(ISO20022MessageElement):
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter7Caam01500101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class CertificateIssuer1Caam01500101(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caam01500101] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class PostalAddress17Caam01500101(ISO20022MessageElement):
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCaam01500101] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class Traceability4Caam01500101(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification77Caam01500101] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )


@dataclass
class Atmcassette3Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMCassette3"

    phys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    logcl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogclId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[AtmcassetteType1Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    sub_tp: list[AtmnoteType1Code] = field(
        default_factory=list,
        metadata={
            "name": "SubTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    mdia_tp: Optional[AtmmediaType4Code] = field(
        default=None,
        metadata={
            "name": "MdiaTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    mdia_cntrs: list[AtmcassetteCounters6Caam01500101] = field(
        default_factory=list,
        metadata={
            "name": "MdiaCntrs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    csstt_sts: Optional[AtmcassetteStatus1Code] = field(
        default=None,
        metadata={
            "name": "CssttSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AutomatedTellerMachine3Caam01500101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lctn: Optional[PostalAddress17Caam01500101] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class EncryptedContent3Caam01500101(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Caam01500101] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Caam01500101(ISO20022MessageElement):
    msg_fctn: Optional[AtmmessageFunction2Caam01500101] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Caam01500101] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class IssuerAndSerialNumber1Caam01500101(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Caam01500101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Caam01500101] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Caam01500101] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Caam01500101(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam01500101] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class Atmenvironment7Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMEnvironment7"

    acqrr: Optional[Acquirer7Caam01500101] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    atmmgr: Optional[Acquirer8Caam01500101] = field(
        default=None,
        metadata={
            "name": "ATMMgr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    hstg_ntty: Optional[TerminalHosting1Caam01500101] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    atm: Optional[AutomatedTellerMachine3Caam01500101] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )


@dataclass
class Atmtransaction30Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMTransaction30"

    tp_of_opr: Optional[Atmoperation2Code] = field(
        default=None,
        metadata={
            "name": "TpOfOpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    tx_id: Optional[TransactionIdentifier3Caam01500101] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csstt: list[Atmcassette3Caam01500101] = field(
        default_factory=list,
        metadata={
            "name": "Csstt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AlgorithmIdentification11Caam01500101(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter4Caam01500101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class Recipient5ChoiceCaam01500101(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caam01500101] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    key_idr: Optional[Kekidentifier2Caam01500101] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AtmreconciliationRequestComponent1Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMReconciliationRequestComponent1"

    envt: Optional[Atmenvironment7Caam01500101] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    tx: Optional[Atmtransaction30Caam01500101] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class KeyTransport4Caam01500101(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaam01500101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Caam01500101] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCaam01500101(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport4Caam01500101] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    kek: Optional[Kek4Caam01500101] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    key_idr: Optional[Kekidentifier2Caam01500101] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class AuthenticatedData4Caam01500101(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam01500101] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Caam01500101] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam01500101] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Caam01500101(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam01500101] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Caam01500101] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class ContentInformationType10Caam01500101(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Caam01500101] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Caam01500101(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Caam01500101] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )


@dataclass
class AtmreconciliationRequestV01Caam01500101(ISO20022MessageElement):
    class Meta:
        name = "ATMReconciliationRequestV01"

    hdr: Optional[Header31Caam01500101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
            "required": True,
        },
    )
    prtctd_atmrcncltn_req: Optional[ContentInformationType10Caam01500101] = field(
        default=None,
        metadata={
            "name": "PrtctdATMRcncltnReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    atmrcncltn_req: Optional[AtmreconciliationRequestComponent1Caam01500101] = field(
        default=None,
        metadata={
            "name": "ATMRcncltnReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )
    scty_trlr: Optional[ContentInformationType15Caam01500101] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01",
        },
    )


@dataclass
class Caam01500101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01"

    atmrcncltn_req: Optional[AtmreconciliationRequestV01Caam01500101] = field(
        default=None,
        metadata={
            "name": "ATMRcncltnReq",
            "type": "Element",
            "required": True,
        },
    )
