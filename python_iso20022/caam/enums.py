from enum import Enum


class Algorithm11Code(Enum):
    """
    Algorithm11Code Identification of a digest algorithm.

    :cvar HS25: SHA256 Message digest algorithm SHA-256 as defined in
        FIPS 180-1 and 2 - (ASN.1 Object Identifier: id-sha256).
    :cvar HS38: SHA384 Message digest algorithm SHA-384 as defined in
        FIPS 180-1 and 2 - (ASN.1 Object Identifier: id-sha384).
    :cvar HS51: SHA512 Message digest algorithm SHA-512 as defined in
        FIPS 180-1 and 2 - (ASN.1 Object Identifier: id-sha512).
    :cvar HS01: SHA1 Message digest algorithm SHA-1 as defined in FIPS
        180-1 - (ASN.1 Object Identifier: id-sha1).
    """

    HS25 = "HS25"
    HS38 = "HS38"
    HS51 = "HS51"
    HS01 = "HS01"


class Algorithm12Code(Enum):
    """
    Algorithm12Code Cryptographic algorithms for the MAC (Message Authentication
    Code).

    :cvar MACC: RetailCBCMAC Retail CBC (Chaining Block Cypher) MAC
        (Message Authentication Code) (cf. ISO 9807, ANSI X9.19) -
        (ASN.1 Object Identifier: id-retail-cbc-mac).
    :cvar MCCS: RetailSHA256MAC Retail-CBC-MAC with SHA-256 (Secure HAsh
        standard)  - (ASN.1 Object Identifier: id-retail-cbc-mac-
        sha-256).
    :cvar CMA1: SHA256CMACwithAES128 CMAC (Cipher based Message
        Authentication Code) defined by the National Institute of
        Standards and Technology (NIST 800-38B - May 2005), using the
        block cipher Advanced Encryption Standard with a 128 bits
        cryptographic key, approved by the Federal Information
        Processing Standards (FIPS 197 - November 6, 2001 - Advanced
        Encryption Standard). The CMAC algorithm is computed on the
        SHA-256 digest of the message.
    :cvar MCC1: RetailSHA1MAC Retail-CBC-MAC with SHA-1 (Secure Hash
        standard) - (ASN.1 Object Identifier: id-retail-cbc-mac-sha-1).
    :cvar CMA9: SHA384CMACwithAES192 CMAC (Cipher based Message
        Authentication Code) defined by the National Institute of
        Standards and Technology (NIST 800-38B - May 2005), using the
        block cipher Advanced Encryption Standard with a 192 bits
        cryptographic key, approved by the Federal Information
        Processing Standards (FIPS 197 - November 6, 2001 - Advanced
        Encryption Standard). The CMAC algorithm is computed on the
        SHA-384 digest of the message.
    :cvar CMA5: SHA512CMACwithAES256 CMAC (Cipher based Message
        Authentication Code) defined by the National Institute of
        Standards and Technology (NIST 800-38B - May 2005), using the
        block cipher Advanced Encryption Standard with a 256 bits
        cryptographic key, approved by the Federal Information
        Processing Standards (FIPS 197 - November 6, 2001 - Advanced
        Encryption Standard). The CMAC algorithm is computed on the
        SHA-512 digest of the message.
    """

    MACC = "MACC"
    MCCS = "MCCS"
    CMA1 = "CMA1"
    MCC1 = "MCC1"
    CMA9 = "CMA9"
    CMA5 = "CMA5"


class Algorithm13Code(Enum):
    """
    Algorithm13Code Cryptographic algorithms for the protection of transported
    keys.

    :cvar EA2_C: AES128CBC AES (Advanced Encryption Standard) CBC
        (Chaining Block Cypher) encryption with a 128 bits cryptographic
        key as defined by the Federal Information Processing Standards
        (FIPS 197 - November 6, 2001 - Advanced Encryption Standard).
    :cvar E3_DC: DES112CBC Triple DES (Data Encryption Standard) CBC
        (Chaining Block Cypher) encryption with double length key (112
        Bit) as defined in FIPS PUB 46-3 - (ASN.1 Object Identifier:
        des-ede3-cbc).
    :cvar DKP9: DUKPT2009 DUKPT (Derived Unique Key Per Transaction)
        algorithm, as specified in ANSI X9.24-2009 Annex A.
    :cvar UKPT: UKPT UKPT (Unique Key Per Transaction) or Master Session
        Key key encryption - (ASN.1 Object Identifier: id-ukpt-wrap).
    :cvar UKA1: UKPTwithAES128 UKPT (Unique Key Per Transaction) or
        Master Session Key key encryption, using Advanced Encryption
        Standard with a 128 bits cryptographic key, approved by the
        Federal Information Processing Standards (FIPS 197 - November 6,
        2001 - Advanced Encryption Standard).
    :cvar EA9_C: AES192CBC AES (Advanced Encryption Standard) CBC
        (Chaining Block Cypher) encryption with a 192 bits cryptographic
        key as defined by the Federal Information Processing Standards
        (FIPS 197 – November 6, 2001 - Advanced Encryption Standard).
    :cvar EA5_C: AES256CBC AES (Advanced Encryption Standard) CBC
        (Chaining Block Cypher) encryption with a 256 bits cryptographic
        key as defined by the Federal Information Processing Standards
        (FIPS 197 – November 6, 2001 - Advanced Encryption Standard).
    """

    EA2_C = "EA2C"
    E3_DC = "E3DC"
    DKP9 = "DKP9"
    UKPT = "UKPT"
    UKA1 = "UKA1"
    EA9_C = "EA9C"
    EA5_C = "EA5C"


class Algorithm14Code(Enum):
    ERS2 = "ERS2"
    ERS1 = "ERS1"
    RPSS = "RPSS"


class Algorithm15Code(Enum):
    """
    Algorithm15Code Cryptographic algorithms for encryptions with a symmetric
    cryptographic key.

    :cvar EA2_C: AES128CBC AES (Advanced Encryption Standard) CBC
        (Chaining Block Cypher) encryption with a 128 bits cryptographic
        key as defined by the Federal Information Processing Standards
        (FIPS 197 - November 6, 2001 - Advanced Encryption Standard).
    :cvar E3_DC: DES112CBC Triple DES (Data Encryption Standard) CBC
        (Chaining Block Cypher) encryption with double length key (112
        Bit) as defined in FIPS PUB 46-3 - (ASN.1 Object Identifier:
        des-ede3-cbc).
    :cvar EA9_C: AES192CBC AES (Advanced Encryption Standard) CBC
        (Chaining Block Cypher) encryption with a 192 bits cryptographic
        key as defined by the Federal Information Processing Standards
        (FIPS 197 – November 6, 2001 - Advanced Encryption Standard).
    :cvar EA5_C: AES256CBC AES (Advanced Encryption Standard) CBC
        (Chaining Block Cypher) encryption with a 256 bits cryptographic
        key as defined by the Federal Information Processing Standards
        (FIPS 197 – November 6, 2001 - Advanced Encryption Standard).
    """

    EA2_C = "EA2C"
    E3_DC = "E3DC"
    EA9_C = "EA9C"
    EA5_C = "EA5C"


class Algorithm7Code(Enum):
    """
    Algorithm7Code Asymmetric encryption algorithm of a transport key.

    :cvar ERSA: RSAEncryption RSA encryption algorithm - (ASN.1 Object
        Identifier: rsaEncryption).
    :cvar RSAO: RSAES-OAEP RSA encryption scheme based on Optimal
        Asymmetric Encryption scheme (PKCS #1 version 2.1) - (ASN.1
        Object Identifier: id-RSAES-OAEP).
    """

    ERSA = "ERSA"
    RSAO = "RSAO"


class Algorithm8Code(Enum):
    """
    Algorithm8Code Mask generator functions of the RSAES-OAEP encryption algorithm
    (RSA Encryption Scheme: Optimal Asymmetric Encryption Padding).

    :cvar MGF1: MGF1 Generator Function, used for RSA encryption and RSA
        igital signature (PKCS #1 version 2.1) - (ASN.1 Object
        Identifier: id-mgf1).
    """

    MGF1 = "MGF1"


class Atmcommand6Code(Enum):
    ABAL = "ABAL"
    ASTS = "ASTS"
    CFGT = "CFGT"
    CCNT = "CCNT"
    DISC = "DISC"
    KACT = "KACT"
    KDAC = "KDAC"
    KDWL = "KDWL"
    KRMV = "KRMV"
    SCFU = "SCFU"
    SSCU = "SSCU"
    SSTU = "SSTU"
    SNDM = "SNDM"
    HKCG = "HKCG"
    HKRV = "HKRV"
    KCHG = "KCHG"


class Atmoperation1Code(Enum):
    ADJU = "ADJU"
    INSR = "INSR"
    LOAD = "LOAD"
    REMV = "REMV"
    UNLD = "UNLD"


class AtmsecurityScheme3Code(Enum):
    APPK = "APPK"
    CERT = "CERT"
    FRAN = "FRAN"
    DTCH = "DTCH"
    LUXG = "LUXG"
    MANU = "MANU"
    PKIP = "PKIP"
    SIGN = "SIGN"
    NONE = "NONE"
    TR34 = "TR34"


class AtmsecurityScheme4Code(Enum):
    APPK = "APPK"
    CERT = "CERT"
    FRAN = "FRAN"
    DTCH = "DTCH"
    LUXG = "LUXG"
    MANU = "MANU"
    PKIP = "PKIP"
    SIGN = "SIGN"
    TR34 = "TR34"


class AtmserviceType10Code(Enum):
    TRFC = "TRFC"
    TRFI = "TRFI"
    TRFP = "TRFP"
    ASTS = "ASTS"
    BLCQ = "BLCQ"
    CDVF = "CDVF"
    CHSN = "CHSN"
    CMPF = "CMPF"
    DCCS = "DCCS"
    XRTD = "XRTD"
    XRTW = "XRTW"
    MCHG = "MCHG"
    DPSN = "DPSN"
    PINC = "PINC"
    PINR = "PINR"
    PINU = "PINU"
    PATH = "PATH"
    PRFL = "PRFL"
    EMVS = "EMVS"
    STDR = "STDR"
    SPRV = "SPRV"
    DPSV = "DPSV"


class Atmstatus2Code(Enum):
    OPER = "OPER"
    OUTS = "OUTS"


class AttributeType1Code(Enum):
    """
    AttributeType1Code Type of attribute of a distinguished name (DN).

    :cvar CNAT: CommonName Common name of the attribute (ASN.1 Object
        Identifier: id-at-commonName).
    :cvar LATT: Locality Locality of the attribute (ASN.1 Object
        Identifier: id-at-localityName).
    :cvar OATT: OrganisationName Organization name of the attribute
        (ASN.1 Object Identifier: id-at-organizationName).
    :cvar OUAT: OrganisationUnitName Organization unit name of the
        attribute (ASN.1 Object Identifier: id-at-
        organizationalUnitName).
    :cvar CATT: CountryName Country name of the attribute (ASN.1 Object
        Identifier: id-at-countryName).
    """

    CNAT = "CNAT"
    LATT = "LATT"
    OATT = "OATT"
    OUAT = "OUAT"
    CATT = "CATT"


class BytePadding1Code(Enum):
    """
    BytePadding1Code Byte padding for a cypher block chaining mode encryption, if
    the padding is not implicit.

    :cvar LNGT: LengthPadding Message to encrypt is completed by a byte
        value containing the total number of added bytes.
    :cvar NUL8: Null80Padding Message to encrypt is completed by one bit
        of value 1, followed by null bits until the encryption block
        length is reached.
    :cvar NULG: NullLengthPadding Message to encrypt is completed by
        null byte values, the last byte containing the total number of
        added bytes.
    :cvar NULL: NullPadding Message to encrypt is completed by null
        bytes.
    :cvar RAND: RandomPadding Message to encrypt is completed by random
        value, the last byte containing the total number of added bytes.
    """

    LNGT = "LNGT"
    NUL8 = "NUL8"
    NULG = "NULG"
    NULL = "NULL"
    RAND = "RAND"


class ContentType2Code(Enum):
    """
    ContentType2Code Identification of the type of a Cryptographic Message Syntax
    (CMS) data structure.

    :cvar DATA: PlainData Generic, non cryptographic, or unqualified
        data content - (ASN.1 Object Identifier: id-data).
    :cvar SIGN: SignedData Digital signature - (ASN.1 Object Identifier:
        id-signedData).
    :cvar EVLP: EnvelopedData Encrypted data, with encryption key -
        (ASN.1 Object Identifier: id-envelopedData).
    :cvar DGST: DigestedData Message digest - (ASN.1 Object Identifier:
        id-digestedData).
    :cvar AUTH: AuthenticatedData MAC (Message Authentication Code),
        with encryption key - (ASN.1 Object Identifier: id-ct-authData).
    """

    DATA = "DATA"
    SIGN = "SIGN"
    EVLP = "EVLP"
    DGST = "DGST"
    AUTH = "AUTH"


class EncryptionFormat1Code(Enum):
    """
    EncryptionFormat1Code Format of data before encryption, if the format is not
    plaintext or implicit.

    :cvar TR31: TR31 Format of a cryptographic key specified by the ANSI
        X9 TR-31 standard.
    :cvar TR34: TR34 Format of a cryptographic key specified by the ANSI
        X9 TR-34 standard.
    """

    TR31 = "TR31"
    TR34 = "TR34"


class MessageFunction7Code(Enum):
    """
    MessageFunction7Code Identifies the type of process related to an ATM message.

    :cvar BALN: ATMBalance Provide the ATM counters resettting those
        that are applicable.
    :cvar CMPA: ATMCompletionAcknowledgement Acknowledgement of a
        completion advice.
    :cvar CMPD: ATMCompletionAdvice Advice of an ATM transaction
        completion.
    :cvar ACMD: ATMControl Global ATM commands.
    :cvar DVCC: ATMDeviceControl Maintenance commands to perform.
    :cvar DIAQ: ATMDiagnosticRequest Request for a diagnostic.
    :cvar DIAP: ATMDiagnosticResponse Response to a diagnostic request.
    :cvar GSTS: ATMGlobalStatus Global status of the ATM.
    :cvar INQQ: ATMInquiryRequest Request for an inquiry.
    :cvar INQP: ATMInquiryResponse Response to an inquiry request.
    :cvar KYAQ: ATMKeyDownloadRequest Request for a key download.
    :cvar KYAP: ATMKeyDownloadResponse Response to a key download.
    :cvar PINQ: ATMPINManagementRequest Request for a cardholder PIN
        management.
    :cvar PINP: ATMPINManagementResponse Response to a cardholder PIN
        management request.
    :cvar RJAQ: ATMRequestReject Rejected request message.
    :cvar RJAP: ATMResponseReject Rejected response message.
    :cvar WITV: ATMWithdrawalAdvice Response of a withdrawal
        transaction.
    :cvar WITK: ATMWithdrawalAknowledgement Acknowledgement of a
        withdrawal transaction advice.
    :cvar WITQ: ATMWithdrawalRequest Request for a withdrawal
        transaction.
    :cvar WITP: ATMWithdrawalResponse Response to a withdrawal
        transaction request.
    :cvar INQC: CountersInquiry Current value of counters, no
        reinitialisation of the counters.
    :cvar H2_AP: HostToATMAcknowledgement Acknowledgement of a request
        from a host to an ATM for contacting.
    :cvar H2_AQ: HostToATMRequest Request from a host to an ATM to be
        contacted by this ATM.
    :cvar TMOP: ATMOperation Logical or physical operation on the ATM.
    :cvar CSEC: SecurityControl Security Commands.
    :cvar DSEC: SecurityDetails Security detailed report.
    :cvar SKSC: SecurityKeyCompletion Result of the key download with
        the status of the downloaded keys including key check values.
    :cvar SSTS: SecurityKeyStatus Status of cryptographic keys.
    """

    BALN = "BALN"
    CMPA = "CMPA"
    CMPD = "CMPD"
    ACMD = "ACMD"
    DVCC = "DVCC"
    DIAQ = "DIAQ"
    DIAP = "DIAP"
    GSTS = "GSTS"
    INQQ = "INQQ"
    INQP = "INQP"
    KYAQ = "KYAQ"
    KYAP = "KYAP"
    PINQ = "PINQ"
    PINP = "PINP"
    RJAQ = "RJAQ"
    RJAP = "RJAP"
    WITV = "WITV"
    WITK = "WITK"
    WITQ = "WITQ"
    WITP = "WITP"
    INQC = "INQC"
    H2_AP = "H2AP"
    H2_AQ = "H2AQ"
    TMOP = "TMOP"
    CSEC = "CSEC"
    DSEC = "DSEC"
    SKSC = "SKSC"
    SSTS = "SSTS"


class MessageProtection1Code(Enum):
    EVLP = "EVLP"
    MACB = "MACB"
    MACM = "MACM"
    UNPR = "UNPR"


class PartyType12Code(Enum):
    """
    PartyType12Code Type of identified entity.

    :cvar ACQR: Acquirer Entity acquiring card transactions.
    :cvar ATMG: ATMManager Entity managing the ATM.
    :cvar CISP: CardIssuerProcessor Entity providing issuing card
        payment processing services on behalf on an issuer.
    :cvar DLIS: DelegateIssuer Party to whom the card issuer delegates
        to authorise card payment transactions.
    :cvar HSTG: HostingEntity Entity hosting the ATM.
    :cvar ITAG: IntermediaryAgent Party acting on behalf of other
        parties to process or forward data to other parties.
    :cvar OATM: OriginatingATM ATM initiating the transaction.
    """

    ACQR = "ACQR"
    ATMG = "ATMG"
    CISP = "CISP"
    DLIS = "DLIS"
    HSTG = "HSTG"
    ITAG = "ITAG"
    OATM = "OATM"


class TerminalManagementActionResult2Code(Enum):
    CNTE = "CNTE"
    FMTE = "FMTE"
    HRDW = "HRDW"
    NSUP = "NSUP"
    SECR = "SECR"
    SUCC = "SUCC"
    SYNE = "SYNE"
    TIMO = "TIMO"
    UKRF = "UKRF"


class Tr34Command1Code(Enum):
    BIND = "BIND"
    HILR = "HILR"
    HILU = "HILU"
    RBND = "RBND"
    UBND = "UBND"
