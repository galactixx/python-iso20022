from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    CancelledStatusReason5Code,
    CreditDebitCode,
    DateType1Code,
    DateType8Code,
    NoReasonCode,
)
from python_iso20022.seev.enums import (
    CorporateActionEventType39Code,
    CorporateActionOption11Code,
    WithholdingTaxRateType1Code,
)
from python_iso20022.seev.seev_053_001_03.enums import (
    PendingCancellationReason7Code,
    RejectionReason61Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSeev05300103(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
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
class ActiveCurrencyAndAmountSeev05300103(ISO20022MessageElement):
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
class DateAndDateTime2ChoiceSeev05300103(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class DocumentIdentification9Seev05300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FinancialInstrumentQuantity1ChoiceSeev05300103(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class GenericIdentification30Seev05300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationSource3ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalAndCurrentQuantities1Seev05300103(ISO20022MessageElement):
    face_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    amtsd_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AmtsdVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class References26Seev05300103(ISO20022MessageElement):
    acct_svcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_infrstrctr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MktInfrstrctrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prcr_tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Seev05300103(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class BlockChainAddressWallet3Seev05300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    tp: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class CancelledReason9ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[CancelledStatusReason5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class CorporateActionEventType111ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType39Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class CorporateActionOption30ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[CorporateActionOption11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class DateCode19ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[DateType8Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class DateFormat58ChoiceSeev05300103(ISO20022MessageElement):
    dt_or_dt_tm: Optional[DateAndDateTime2ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "DtOrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    dt_cd: Optional[DateType1Code] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class NoSpecifiedReason1Seev05300103(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )


@dataclass
class OtherIdentification1Seev05300103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    sfx: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    tp: Optional[IdentificationSource3ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )


@dataclass
class PendingCancellationReason8ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[PendingCancellationReason7Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class ProprietaryReason4Seev05300103(ISO20022MessageElement):
    rsn: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class Quantity6ChoiceSeev05300103(ISO20022MessageElement):
    qty: Optional[FinancialInstrumentQuantity1ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    orgnl_and_cur_face: Optional[OriginalAndCurrentQuantities1Seev05300103] = field(
        default=None,
        metadata={
            "name": "OrgnlAndCurFace",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class RateType42ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[WithholdingTaxRateType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class RejectedReason38ChoiceSeev05300103(ISO20022MessageElement):
    cd: Optional[RejectionReason61Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class SupplementaryData1Seev05300103(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Seev05300103] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )


@dataclass
class CancelledStatusReason12Seev05300103(ISO20022MessageElement):
    rsn_cd: Optional[CancelledReason9ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class CashAccountIdentification9ChoiceSeev05300103(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    blck_chain_csh_wllt: Optional[BlockChainAddressWallet3Seev05300103] = field(
        default=None,
        metadata={
            "name": "BlckChainCshWllt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 34,
        },
    )


@dataclass
class DateFormat43ChoiceSeev05300103(ISO20022MessageElement):
    dt: Optional[DateAndDateTime2ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    dt_cd: Optional[DateCode19ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "DtCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class PendingCancellationStatusReason11Seev05300103(ISO20022MessageElement):
    rsn_cd: Optional[PendingCancellationReason8ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class ProprietaryStatusAndReason6Seev05300103(ISO20022MessageElement):
    prtry_sts: Optional[GenericIdentification30Seev05300103] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    prtry_rsn: list[ProprietaryReason4Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "PrtryRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class RateTypeAndPercentageRate12Seev05300103(ISO20022MessageElement):
    rate_tp: Optional[RateType42ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )


@dataclass
class RejectedStatusReason36Seev05300103(ISO20022MessageElement):
    rsn_cd: Optional[RejectedReason38ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "RsnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    addtl_rsn_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRsnInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 210,
        },
    )


@dataclass
class SecurityIdentification19Seev05300103(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: list[OtherIdentification1Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class CancelledStatus11ChoiceSeev05300103(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    rsn: list[CancelledStatusReason12Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class CorporateActionGeneralInformation181Seev05300103(ISO20022MessageElement):
    corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    offcl_corp_actn_evt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffclCorpActnEvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType111ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    fin_instrm_id: Optional[SecurityIdentification19Seev05300103] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class PendingCancellationStatus14ChoiceSeev05300103(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    rsn: list[PendingCancellationStatusReason11Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class RateAndAmountFormat55ChoiceSeev05300103(ISO20022MessageElement):
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "total_digits": 14,
            "fraction_digits": 13,
        },
    )
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSeev05300103] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    rate_tp_and_rate: Optional[RateTypeAndPercentageRate12Seev05300103] = field(
        default=None,
        metadata={
            "name": "RateTpAndRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class RejectedStatus38ChoiceSeev05300103(ISO20022MessageElement):
    no_spcfd_rsn: Optional[NoReasonCode] = field(
        default=None,
        metadata={
            "name": "NoSpcfdRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    rsn: list[RejectedStatusReason36Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class SecuritiesOption76Seev05300103(ISO20022MessageElement):
    fin_instrm_id: Optional[SecurityIdentification19Seev05300103] = field(
        default=None,
        metadata={
            "name": "FinInstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    entitld_qty: Optional[Quantity6ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "EntitldQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    pmt_dt: Optional[DateFormat58ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )


@dataclass
class CashOption106Seev05300103(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    csh_acct_id: Optional[CashAccountIdentification9ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    grss_csh_amt: Optional[ActiveCurrencyAndAmountSeev05300103] = field(
        default=None,
        metadata={
            "name": "GrssCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    net_csh_amt: Optional[ActiveCurrencyAndAmountSeev05300103] = field(
        default=None,
        metadata={
            "name": "NetCshAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    entitld_amt: Optional[ActiveCurrencyAndAmountSeev05300103] = field(
        default=None,
        metadata={
            "name": "EntitldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    whldg_tax_rate: list[RateAndAmountFormat55ChoiceSeev05300103] = field(
        default_factory=list,
        metadata={
            "name": "WhldgTaxRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    whldg_tax_amt: Optional[ActiveCurrencyAndAmountSeev05300103] = field(
        default=None,
        metadata={
            "name": "WhldgTaxAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    earlst_pmt_dt: Optional[DateAndDateTime2ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "EarlstPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    pmt_dt: Optional[DateFormat43ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )


@dataclass
class MarketClaimCancellationRequestStatus2ChoiceSeev05300103(ISO20022MessageElement):
    cxl_cmpltd: Optional[CancelledStatus11ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "CxlCmpltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    accptd: Optional[NoSpecifiedReason1Seev05300103] = field(
        default=None,
        metadata={
            "name": "Accptd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    rjctd: Optional[RejectedStatus38ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "Rjctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    pdg_cxl: Optional[PendingCancellationStatus14ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "PdgCxl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    prtry_sts: Optional[ProprietaryStatusAndReason6Seev05300103] = field(
        default=None,
        metadata={
            "name": "PrtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class CorporateActionOption234Seev05300103(ISO20022MessageElement):
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    optn_tp: Optional[CorporateActionOption30ChoiceSeev05300103] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    scties_mvmnt_dtls: list[SecuritiesOption76Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    csh_mvmnt_dtls: list[CashOption106Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class MarketClaimCancellationRequestStatusAdviceV03Seev05300103(ISO20022MessageElement):
    mkt_clm_cxl_req_id: Optional[DocumentIdentification9Seev05300103] = field(
        default=None,
        metadata={
            "name": "MktClmCxlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    tx_ref: Optional[References26Seev05300103] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionGeneralInformation181Seev05300103] = (
        field(
            default=None,
            metadata={
                "name": "CorpActnGnlInf",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
                "required": True,
            },
        )
    )
    mkt_clm_cxl_req_sts: Optional[
        MarketClaimCancellationRequestStatus2ChoiceSeev05300103
    ] = field(
        default=None,
        metadata={
            "name": "MktClmCxlReqSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
            "required": True,
        },
    )
    mkt_clm_dtls: Optional[CorporateActionOption234Seev05300103] = field(
        default=None,
        metadata={
            "name": "MktClmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )
    splmtry_data: list[SupplementaryData1Seev05300103] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03",
        },
    )


@dataclass
class Seev05300103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.053.001.03"

    mkt_clm_cxl_req_sts_advc: Optional[
        MarketClaimCancellationRequestStatusAdviceV03Seev05300103
    ] = field(
        default=None,
        metadata={
            "name": "MktClmCxlReqStsAdvc",
            "type": "Element",
            "required": True,
        },
    )
