from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.caam.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    AttributeType1Code,
    BytePadding1Code,
    ContentType2Code,
    EncryptionFormat1Code,
    MessageFunction7Code,
    PartyType12Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01"


@dataclass
class Acquirer7Caam00800101(ISO20022MessageElement):
    """
    Acquirer7 Acquirer of the withdrawal transaction, in charge of the funds
    settlement with the issuer.

    :ivar acqrg_instn: AcquiringInstitution Identification of the
        acquirer.
    :ivar brnch: Branch Identification of the acquirer branch.
    """

    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AutomatedTellerMachine7Caam00800101(ISO20022MessageElement):
    """
    AutomatedTellerMachine7 ATM information.

    :ivar id: Identification ATM terminal device identification for the
        acquirer and the issuer.
    :ivar addtl_id: AdditionalIdentification ATM terminal device
        identification for the ATM manager.
    :ivar seq_nb: SequenceNumber ATM terminal device identification for
        the branch.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Kekidentifier2Caam00800101(ISO20022MessageElement):
    """
    KEKIdentifier2 Identification of a key encryption key (KEK), using previously
    distributed symmetric key.

    :ivar key_id: KeyIdentification Identification of the cryptographic
        key.
    :ivar key_vrsn: KeyVersion Version of the cryptographic key.
    :ivar seq_nb: SequenceNumber Number of usages of the cryptographic
        key.
    :ivar derivtn_id: DerivationIdentification Identification used for
        derivation of a unique key from a master key provided for the
        data protection.
    """

    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class Atmenvironment9Caam00800101(ISO20022MessageElement):
    """
    ATMEnvironment9 Environment of the ATM.

    :ivar acqrr: Acquirer Acquirer of the ATM transaction, in charge of
        the funds settlement with the issuer.
    :ivar atmmgr_id: ATMManagerIdentification Identification of the ATM
        manager.
    :ivar atm: ATM ATM information.
    """

    class Meta:
        name = "ATMEnvironment9"

    acqrr: Optional[Acquirer7Caam00800101] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    atmmgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    atm: Optional[AutomatedTellerMachine7Caam00800101] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )


@dataclass
class AtmmessageFunction1Caam00800101(ISO20022MessageElement):
    """
    ATMMessageFunction1 Identifies the type of process related to an ATM message.

    :ivar fctn: Function Type of requested function.
    :ivar atmsvc_cd: ATMServiceCode Codification of the type of service
        for the ATM.
    :ivar hst_svc_cd: HostServiceCode Codification of the type of
        service for the ATM manager host.
    """

    class Meta:
        name = "ATMMessageFunction1"

    fctn: Optional[MessageFunction7Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class EncapsulatedContent3Caam00800101(ISO20022MessageElement):
    """
    EncapsulatedContent3 Data to authenticate.

    :ivar cntt_tp: ContentType Type of data which have been
        authenticated.
    :ivar cntt: Content Actual data to authenticate.
    """

    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Caam00800101(ISO20022MessageElement):
    """
    GenericIdentification77 Identification of an entity.

    :ivar id: Identification Identification of the entity.
    :ivar tp: Type Type of identified entity.
    :ivar issr: Issuer Entity assigning the identification  (for example
        merchant, acceptor, acquirer, or tax authority).
    :ivar ctry: Country Country of the entity (ISO 3166-1 alpha-2 or
        alpha-3)
    :ivar shrt_nm: ShortName Name of the entity.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Parameter5Caam00800101(ISO20022MessageElement):
    """
    Parameter5 Parameters associated to a mask generator cryptographic function.

    :ivar dgst_algo: DigestAlgorithm Digest algorithm used in the mask
        generator function.
    """

    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class Parameter6Caam00800101(ISO20022MessageElement):
    """
    Parameter6 Parameters associated to a cryptographic encryption algorithm.

    :ivar ncrptn_frmt: EncryptionFormat Format of data before
        encryption, if the format is not plaintext or implicit.
    :ivar initlstn_vctr: InitialisationVector Initialisation vector of a
        cipher block chaining (CBC) mode encryption.
    :ivar bpddg: BytePadding Byte padding for a cypher block chaining
        mode encryption, if the padding is not implicit.
    """

    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class Parameter7Caam00800101(ISO20022MessageElement):
    """
    Parameter7 Parameters associated to the MAC algorithm.

    :ivar initlstn_vctr: InitialisationVector Initialisation vector of a
        cipher block chaining (CBC) mode encryption.
    :ivar bpddg: BytePadding Byte padding for a cypher block chaining
        mode encryption, if the padding is not implicit.
    """

    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class RelativeDistinguishedName1Caam00800101(ISO20022MessageElement):
    """
    RelativeDistinguishedName1 Relative distinguished name defined by X.500 and
    X.509.

    :ivar attr_tp: AttributeType Type of attribute of a distinguished
        name (see X.500).
    :ivar attr_val: AttributeValue Value of the attribute of a
        distinguished name (see X.500).
    """

    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class AlgorithmIdentification12Caam00800101(ISO20022MessageElement):
    """
    AlgorithmIdentification12 Mask generator function cryptographic algorithm and
    parameters.

    :ivar algo: Algorithm Mask generator function cryptographic
        algorithm.
    :ivar param: Parameter Parameters associated to the mask generator
        function cryptographic algorithm
    """

    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter5Caam00800101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class AlgorithmIdentification13Caam00800101(ISO20022MessageElement):
    """
    AlgorithmIdentification13 Cryptographic algorithm and parameters for the
    protection of the transported key.

    :ivar algo: Algorithm Identification of the algorithm.
    :ivar param: Parameter Parameters associated to the encryption
        algorithm.
    """

    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00800101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class AlgorithmIdentification14Caam00800101(ISO20022MessageElement):
    """
    AlgorithmIdentification14 Cryptographic algorithm and parameters for
    encryptions with a symmetric cryptographic key.

    :ivar algo: Algorithm Identification of the encryption algorithm.
    :ivar param: Parameter Parameters associated with the CBC (Chain
        Block Chaining) encryption algorithm.
    """

    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter6Caam00800101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class AlgorithmIdentification15Caam00800101(ISO20022MessageElement):
    """
    AlgorithmIdentification15 Identification of a cryptographic algorithm and
    parameters for the MAC computation.

    :ivar algo: Algorithm Identification of the MAC algorithm.
    :ivar param: Parameter Parameters associated to the MAC algorithm.
    """

    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter7Caam00800101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class CertificateIssuer1Caam00800101(ISO20022MessageElement):
    """
    CertificateIssuer1 Certificate issuer name (see X.509).

    :ivar rltv_dstngshd_nm: RelativeDistinguishedName Relative
        distinguished name inside a X.509 certificate.
    """

    rltv_dstngshd_nm: list[RelativeDistinguishedName1Caam00800101] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_occurs": 1,
        },
    )


@dataclass
class HostToAtmacknowledgement1Caam00800101(ISO20022MessageElement):
    """
    HostToATMAcknowledgement1 Information related to the acknowledgement from an
    ATM to contact the ATM manager.

    :ivar envt: Environment Environment of the ATM.
    """

    class Meta:
        name = "HostToATMAcknowledgement1"

    envt: Optional[Atmenvironment9Caam00800101] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )


@dataclass
class Traceability4Caam00800101(ISO20022MessageElement):
    """
    Traceability4 Identification of partners involved in exchange from the ATM to
    the issuer, with the relative timestamp of their exchanges.

    :ivar rlay_id: RelayIdentification Identification of a partner of a
        message exchange.
    :ivar seq_nb: SequenceNumber Identification of the relay node in the
        path, to enable identification of several hosts in parallel.
    :ivar trac_dt_tm_in: TraceDateTimeIn Date and time of incoming data
        exchange for relaying or processing.
    :ivar trac_dt_tm_out: TraceDateTimeOut Date and time of the outgoing
        exchange for relaying or processing.
    """

    rlay_id: Optional[GenericIdentification77Caam00800101] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )


@dataclass
class EncryptedContent3Caam00800101(ISO20022MessageElement):
    """
    EncryptedContent3 Encrypted data with an encryption key.

    :ivar cntt_tp: ContentType Type of data which have been encrypted.
    :ivar cntt_ncrptn_algo: ContentEncryptionAlgorithm Algorithm used to
        encrypt the data.
    :ivar ncrptd_data: EncryptedData Encrypted data, result of the
        content encryption.
    """

    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Caam00800101] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header20Caam00800101(ISO20022MessageElement):
    """
    Header20 Information related to the protocol management on a segment of the
    path from the ATM to the acquirer.

    :ivar msg_fctn: MessageFunction Identifies the type of process
        related to the message.
    :ivar prtcol_vrsn: ProtocolVersion Version of the ATM protocol
        specifications.
    :ivar xchg_id: ExchangeIdentification Unique identification of an
        exchange occurrence.
    :ivar cre_dt_tm: CreationDateTime Date and time at which the message
        was created.
    :ivar initg_pty: InitiatingParty Unique identification of the
        partner that has initiated the exchange.
    :ivar rcpt_pty: RecipientParty Unique identification of the partner
        that is the recipient of the message exchange.
    :ivar prc_stat: ProcessState State of the sender of the message
        inside the process flow.
    :ivar tracblt: Traceability Identification of partners involved in
        exchange from the merchant to the issuer, with the relative
        timestamp of their exchanges.
    """

    msg_fctn: Optional[AtmmessageFunction1Caam00800101] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Caam00800101] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class IssuerAndSerialNumber1Caam00800101(ISO20022MessageElement):
    """
    IssuerAndSerialNumber1 Certificate issuer name and serial number  (see X.509).

    :ivar issr: Issuer Certificate issuer name (see X.509).
    :ivar srl_nb: SerialNumber Certificate serial number (see X.509).
    """

    issr: Optional[CertificateIssuer1Caam00800101] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Caam00800101(ISO20022MessageElement):
    """
    KEK4 Key encryption key (KEK), using previously distributed symmetric key.

    :ivar vrsn: Version Version of the data structure.
    :ivar kekid: KEKIdentification Identification of the key encryption
        key (KEK).
    :ivar key_ncrptn_algo: KeyEncryptionAlgorithm Algorithm to encrypt
        the key encryption key (KEK).
    :ivar ncrptd_key: EncryptedKey Encrypted key encryption key (KEK).
    """

    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Caam00800101] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Caam00800101] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Caam00800101(ISO20022MessageElement):
    """
    Parameter4 Parameters of the asymmetric encryption algorithm.

    :ivar ncrptn_frmt: EncryptionFormat Format of data before
        encryption, if the format is not plaintext or implicit.
    :ivar dgst_algo: DigestAlgorithm Identification of the digest
        algorithm.
    :ivar msk_gnrtr_algo: MaskGeneratorAlgorithm Mask generator function
        cryptographic algorithm and parameters.
    """

    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Caam00800101] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class AlgorithmIdentification11Caam00800101(ISO20022MessageElement):
    """
    AlgorithmIdentification11 Cryptographic algorithms and parameters for the
    protection of transported keys by an asymmetric key.

    :ivar algo: Algorithm Asymmetric encryption algorithm of a transport
        key.
    :ivar param: Parameter Parameters of the encryption algorithm.
    """

    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    param: Optional[Parameter4Caam00800101] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class Recipient5ChoiceCaam00800101(ISO20022MessageElement):
    """
    Recipient5Choice Identification of a cryptographic asymmetric key.

    :ivar issr_and_srl_nb: IssuerAndSerialNumber Certificate issuer name
        and serial number (see ITU X.509).
    :ivar key_idr: KeyIdentifier Identifier of a cryptographic
        asymmetric key, previously exchanged between initiator and
        recipient.
    """

    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Caam00800101] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00800101] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class KeyTransport4Caam00800101(ISO20022MessageElement):
    """
    KeyTransport4 Key encryption key (KEK), encrypted with a previously distributed
    asymmetric public key.

    :ivar vrsn: Version Version of the data structure.
    :ivar rcpt_id: RecipientIdentification Identification of a
        cryptographic asymmetric key for the recipient.
    :ivar key_ncrptn_algo: KeyEncryptionAlgorithm Algorithm to encrypt
        the key encryption key (KEK).
    :ivar ncrptd_key: EncryptedKey Encrypted key encryption key (KEK).
    """

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCaam00800101] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Caam00800101] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCaam00800101(ISO20022MessageElement):
    """
    Recipient4Choice Transport key or key encryption key (KEK) for the recipient.

    :ivar key_trnsprt: KeyTransport Encryption key using previously
        distributed asymmetric public key.
    :ivar kek: KEK Key encryption key using previously distributed
        symmetric key.
    :ivar key_idr: KeyIdentifier Identification of a protection key
        without a session key, shared and previously exchanged between
        the initiator and the recipient.
    """

    key_trnsprt: Optional[KeyTransport4Caam00800101] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    kek: Optional[Kek4Caam00800101] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    key_idr: Optional[Kekidentifier2Caam00800101] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class AuthenticatedData4Caam00800101(ISO20022MessageElement):
    """
    AuthenticatedData4 Message authentication code (MAC), computed on the data to
    protect with an encryption key.

    :ivar vrsn: Version Version of the data structure.
    :ivar rcpt: Recipient Session key or protection key identification
        used by the recipient.
    :ivar macalgo: MACAlgorithm Algorithm to compute message
        authentication code (MAC).
    :ivar ncpsltd_cntt: EncapsulatedContent Data to authenticate.
    :ivar mac: MAC Message authentication code value.
    """

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00800101] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Caam00800101] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Caam00800101] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Caam00800101(ISO20022MessageElement):
    """
    EnvelopedData4 Encrypted data with encryption key.

    :ivar vrsn: Version Version of the data structure.
    :ivar rcpt: Recipient Session key or identification of the
        protection key used by the recipient.
    :ivar ncrptd_cntt: EncryptedContent Data protection by encryption
        (digital envelope), with an encryption key.
    """

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCaam00800101] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Caam00800101] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class ContentInformationType10Caam00800101(ISO20022MessageElement):
    """
    ContentInformationType10 General cryptographic message syntax (CMS) containing
    encrypted data.

    :ivar cntt_tp: ContentType Type of data protection.
    :ivar envlpd_data: EnvelopedData Data protection by encryption or by
        a digital envelope, with an encryption key.
    """

    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Caam00800101] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Caam00800101(ISO20022MessageElement):
    """
    ContentInformationType15 General cryptographic message syntax (CMS) containing
    authenticated data.

    :ivar cntt_tp: ContentType Type of data protection.
    :ivar authntcd_data: AuthenticatedData Data protection by a message
        authentication code (MAC).
    """

    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Caam00800101] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )


@dataclass
class HostToAtmacknowledgementV01Caam00800101(ISO20022MessageElement):
    """
    HostToATMAcknowledgementV01 The HostToATMAcknowledgement message is sent by an
    ATM to a host to acknowledge the receipt of a HostToATMRequest message.

    :ivar hdr: Header Information related to the protocol management on
        a segment of the path from the ATM to the acquirer.
    :ivar prtctd_hst_to_atmack: ProtectedHostToATMAcknowledgement
        Encrypted body of the message.
    :ivar hst_to_atmack: HostToATMAcknowledgement Information related to
        the acknowledgement from an ATM to contact the ATM manager.
    :ivar scty_trlr: SecurityTrailer Trailer of the message containing a
        MAC.
    """

    class Meta:
        name = "HostToATMAcknowledgementV01"

    hdr: Optional[Header20Caam00800101] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
            "required": True,
        },
    )
    prtctd_hst_to_atmack: Optional[ContentInformationType10Caam00800101] = field(
        default=None,
        metadata={
            "name": "PrtctdHstToATMAck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    hst_to_atmack: Optional[HostToAtmacknowledgement1Caam00800101] = field(
        default=None,
        metadata={
            "name": "HstToATMAck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )
    scty_trlr: Optional[ContentInformationType15Caam00800101] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01",
        },
    )


@dataclass
class Caam00800101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01"

    hst_to_atmack: Optional[HostToAtmacknowledgementV01Caam00800101] = field(
        default=None,
        metadata={
            "name": "HstToATMAck",
            "type": "Element",
            "required": True,
        },
    )
