from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.auth.auth_055_001_01.enums import MarginType2Code
from python_iso20022.auth.enums import SchemeIdentificationType1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01"


@dataclass
class ActiveCurrencyAndAmountAuth05500101:
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
class GenericIdentification36Auth05500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth05500101:
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Amount3Auth05500101:
    orgnl_amt: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "OrgnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
        },
    )
    rptg_amt: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "RptgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class AmountAndDirection102Auth05500101:
    amt: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    sgn: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class GenericIdentification165Auth05500101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[SchemeIdentificationType1Code] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
        },
    )


@dataclass
class MarginType2ChoiceAuth05500101:
    cd: Optional[MarginType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
        },
    )
    prtry: Optional[GenericIdentification36Auth05500101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
        },
    )


@dataclass
class SupplementaryData1Auth05500101:
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth05500101] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class DefaultFundRequirement1Auth05500101:
    clr_mmb_id: Optional[GenericIdentification165Auth05500101] = field(
        default=None,
        metadata={
            "name": "ClrMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    svc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class InitialMarginExposure1Auth05500101:
    amt: Optional[Amount3Auth05500101] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    tp: Optional[MarginType2ChoiceAuth05500101] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    core_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CoreInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class IntraDayMarginCall1Auth05500101:
    mrgn_acct_id: Optional[GenericIdentification165Auth05500101] = field(
        default=None,
        metadata={
            "name": "MrgnAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    intra_day_call: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "IntraDayCall",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    tm_stmp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class IntraDayRequirement1Auth05500101:
    intra_day_mrgn_call: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "IntraDayMrgnCall",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    peak_initl_mrgn_lblty: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "PeakInitlMrgnLblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    peak_vartn_mrgn_lblty: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "PeakVartnMrgnLblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    aggt_peak_lblty: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "AggtPeakLblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    mrgn_acct_id: Optional[GenericIdentification165Auth05500101] = field(
        default=None,
        metadata={
            "name": "MrgnAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class InitialMarginRequirement1Auth05500101:
    initl_mrgn_xpsr: list[InitialMarginExposure1Auth05500101] = field(
        default_factory=list,
        metadata={
            "name": "InitlMrgnXpsr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_occurs": 1,
        },
    )
    cdt: Optional[ActiveCurrencyAndAmountAuth05500101] = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class EndOfDayRequirement2Auth05500101:
    initl_mrgn_rqrmnts: Optional[InitialMarginRequirement1Auth05500101] = field(
        default=None,
        metadata={
            "name": "InitlMrgnRqrmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    vartn_mrgn_rqrmnts: Optional[AmountAndDirection102Auth05500101] = field(
        default=None,
        metadata={
            "name": "VartnMrgnRqrmnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )
    mrgn_acct_id: Optional[GenericIdentification165Auth05500101] = field(
        default=None,
        metadata={
            "name": "MrgnAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "required": True,
        },
    )


@dataclass
class CcpmemberRequirementsReportV01Auth05500101:
    class Meta:
        name = "CCPMemberRequirementsReportV01"

    intra_day_rqrmnt_amt: list[IntraDayRequirement1Auth05500101] = field(
        default_factory=list,
        metadata={
            "name": "IntraDayRqrmntAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_occurs": 1,
        },
    )
    intra_day_mrgn_call: list[IntraDayMarginCall1Auth05500101] = field(
        default_factory=list,
        metadata={
            "name": "IntraDayMrgnCall",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
        },
    )
    end_of_day_rqrmnt: list[EndOfDayRequirement2Auth05500101] = field(
        default_factory=list,
        metadata={
            "name": "EndOfDayRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_occurs": 1,
        },
    )
    dflt_fnd_rqrmnt: list[DefaultFundRequirement1Auth05500101] = field(
        default_factory=list,
        metadata={
            "name": "DfltFndRqrmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth05500101] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01",
        },
    )


@dataclass
class Auth05500101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.055.001.01"

    ccpmmb_rqrmnts_rpt: Optional[CcpmemberRequirementsReportV01Auth05500101] = field(
        default=None,
        metadata={
            "name": "CCPMmbRqrmntsRpt",
            "type": "Element",
            "required": True,
        },
    )
