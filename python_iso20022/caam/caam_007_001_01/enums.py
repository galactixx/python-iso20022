from enum import Enum


class MessageFunction8Code(Enum):
    """
    MessageFunction8Code Identifies the type of process requested by the host to an
    ATM.

    :cvar BALN: ATMBalance Provide the ATM counters resettting those
        that are applicable.
    :cvar GSTS: ATMGlobalStatus Global status of the ATM.
    :cvar DSEC: SecurityDetails Security detailed report.
    :cvar INQC: CountersInquiry Current value of counters, no
        reinitialisation of the counters.
    :cvar KEYQ: KeyExchangeRequest Request of a key exchange.
    :cvar SSTS: SecurityKeyStatus Status of cryptographic keys.
    """

    BALN = "BALN"
    GSTS = "GSTS"
    DSEC = "DSEC"
    INQC = "INQC"
    KEYQ = "KEYQ"
    SSTS = "SSTS"
