from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from python_iso20022.auth.enums import SchemeIdentificationType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01"


@dataclass
class ActiveCurrencyAndAmountAuth05600101:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05600101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AmountAndDirection102Auth05600101:
    amt: Optional[ActiveCurrencyAndAmountAuth05600101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification165Auth05600101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth05600101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05600101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )


@dataclass
class SettlementAccount1Auth05600101:
    id: Optional[GenericIdentification165Auth05600101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )
    end_of_day_initl_mrgn_clld: Optional[AmountAndDirection102Auth05600101] = field(
        default=None,
        metadata={
            "name": "EndOfDayInitlMrgnClld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )
    end_of_day_vartn_mrgn_clld: Optional[AmountAndDirection102Auth05600101] = field(
        default=None,
        metadata={
            "name": "EndOfDayVartnMrgnClld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )
    end_of_day_dflt_fnd_clld: Optional[AmountAndDirection102Auth05600101] = field(
        default=None,
        metadata={
            "name": "EndOfDayDfltFndClld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )
    end_of_day_sttlm_clld: Optional[AmountAndDirection102Auth05600101] = field(
        default=None,
        metadata={
            "name": "EndOfDaySttlmClld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )
    end_of_day_othr_clld: Optional[AmountAndDirection102Auth05600101] = field(
        default=None,
        metadata={
            "name": "EndOfDayOthrClld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )
    end_of_day_lqdty_clld: Optional[AmountAndDirection102Auth05600101] = field(
        default=None,
        metadata={
            "name": "EndOfDayLqdtyClld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "required": True,
        },
    )


@dataclass
class CcpmemberObligationsReportV01Auth05600101:
    class Meta:
        name = "CCPMemberObligationsReportV01"

    sttlm_acct: list[SettlementAccount1Auth05600101] = field(
        default_factory=list,
        metadata={
            "name": "SttlmAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05600101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01",
        },
    )


@dataclass
class Auth05600101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.056.001.01"

    ccpmmb_oblgtns_rpt: Optional[CcpmemberObligationsReportV01Auth05600101] = field(
        default=None,
        metadata={
            "name": "CCPMmbOblgtnsRpt",
            "type": "Element",
            "required": True,
        },
    )
