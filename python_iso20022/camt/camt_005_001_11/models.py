from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.camt_005_001_11.enums import (
    CashPaymentStatus2Code,
    FinalStatusCode,
    ReportIndicator1Code,
)
from python_iso20022.camt.enums import (
    EntryStatus1Code,
    Instruction1Code,
    PaymentInstrument1Code,
    PaymentType3Code,
    PendingStatus4Code,
    Priority5Code,
    QueryType2Code,
)
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebitCode,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11"


@dataclass
class AccountCashEntryReturnCriteria3Camt00500111(ISO20022MessageElement):
    ntry_ref_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtryRefInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_tp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcctTpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ntry_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtryAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_ccy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcctCcyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ntry_sts_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtryStsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ntry_dt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NtryDtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_svcr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcctSvcrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_ownr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcctOwnrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class AccountSchemeName1ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AmountRangeBoundary1Camt00500111(ISO20022MessageElement):
    bdry_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BdryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    incl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification3ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 3,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Camt00500111(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod2Camt00500111(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )


@dataclass
class DateTimePeriod1Camt00500111(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Camt00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InstructionStatusReturnCriteria1Camt00500111(ISO20022MessageElement):
    pmt_instr_sts_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtInstrStsInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    pmt_instr_sts_dt_tm_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtInstrStsDtTmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_instr_sts_rsn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtInstrStsRsnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Camt00500111(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class QueueTransactionIdentification1Camt00500111(ISO20022MessageElement):
    qid: Optional[str] = field(
        default=None,
        metadata={
            "name": "QId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    pos_in_q: Optional[str] = field(
        default=None,
        metadata={
            "name": "PosInQ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt00500111(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class SystemReturnCriteria2Camt00500111(ISO20022MessageElement):
    sys_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SysIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    mmb_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MmbIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ctry_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CtryIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcctIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class AddressType3ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prtry: Optional[GenericIdentification30Camt00500111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt00500111(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Camt00500111(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class DatePeriodSearch1ChoiceCamt00500111(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    fr_to_dt: Optional[DatePeriod2Camt00500111] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    eqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    neqdt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NEQDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class DateTimePeriod1ChoiceCamt00500111(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    dt_tm_rg: Optional[DateTimePeriod1Camt00500111] = field(
        default=None,
        metadata={
            "name": "DtTmRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class FromToAmountRange1Camt00500111(ISO20022MessageElement):
    fr_amt: Optional[AmountRangeBoundary1Camt00500111] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    to_amt: Optional[AmountRangeBoundary1Camt00500111] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )


@dataclass
class GenericAccountIdentification1Camt00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Camt00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Camt00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Camt00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentOrigin1ChoiceCamt00500111(ISO20022MessageElement):
    finmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FINMT",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[0-9]{1,3}",
        },
    )
    xmlmsg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "XMLMsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instrm: Optional[PaymentInstrument1Code] = field(
        default=None,
        metadata={
            "name": "Instrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PaymentReturnCriteria4Camt00500111(ISO20022MessageElement):
    msg_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MsgIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    reqd_exctn_dt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReqdExctnDtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InstrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instr_sts_rtr_crit: Optional[InstructionStatusReturnCriteria1Camt00500111] = field(
        default=None,
        metadata={
            "name": "InstrStsRtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instd_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InstdAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    cdt_dbt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    intr_bk_sttlm_amt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prty_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrtyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prcg_vldty_tm_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrcgVldtyTmInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    purp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PurpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instr_cpy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InstrCpyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_mtind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtMTInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_tp_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtTpInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    tx_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TxIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    intr_bk_sttlm_dt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    end_to_end_id_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EndToEndIdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_mtd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PmtMtdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    dbtr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DbtrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    dbtr_agt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DbtrAgtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instg_rmbrsmnt_agt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instd_rmbrsmnt_agt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    intrmy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrmyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    cdtr_agt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CdtrAgtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    cdtr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CdtrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PaymentStatusCodeSearch2ChoiceCamt00500111(ISO20022MessageElement):
    pdg_sts: Optional[PendingStatus4Code] = field(
        default=None,
        metadata={
            "name": "PdgSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    fnl_sts: Optional[FinalStatusCode] = field(
        default=None,
        metadata={
            "name": "FnlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pdg_and_fnl_sts: Optional[CashPaymentStatus2Code] = field(
        default=None,
        metadata={
            "name": "PdgAndFnlSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PaymentType4ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[PaymentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Priority1ChoiceCamt00500111(ISO20022MessageElement):
    cd: Optional[Priority5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class RequestType4ChoiceCamt00500111(ISO20022MessageElement):
    pmt_ctrl: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtCtrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    enqry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Enqry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Camt00500111] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class SupplementaryData1Camt00500111(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt00500111] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )


@dataclass
class AccountIdentification4ChoiceCamt00500111(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Camt00500111] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class DateAndDateTimeSearch3ChoiceCamt00500111(ISO20022MessageElement):
    dt_tm_sch: Optional[DateTimePeriod1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "DtTmSch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    dt_sch: Optional[DatePeriodSearch1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "DtSch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class ImpliedCurrencyAmountRange1ChoiceCamt00500111(ISO20022MessageElement):
    fr_amt: Optional[AmountRangeBoundary1Camt00500111] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    to_amt: Optional[AmountRangeBoundary1Camt00500111] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    fr_to_amt: Optional[FromToAmountRange1Camt00500111] = field(
        default=None,
        metadata={
            "name": "FrToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    eqamt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EQAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    neqamt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NEQAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )


@dataclass
class InstructionStatusSearch5Camt00500111(ISO20022MessageElement):
    pmt_instr_sts: Optional[PaymentStatusCodeSearch2ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "PmtInstrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_instr_sts_dt_tm: Optional[DateTimePeriod1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "PmtInstrStsDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prtry_sts_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryStsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class MessageHeader9Camt00500111(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    req_tp: Optional[RequestType4ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "ReqTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class OrganisationIdentification39Camt00500111(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PersonIdentification18Camt00500111(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Camt00500111] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    othr: list[GenericPersonIdentification2Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PostalAddress27Camt00500111(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class TransactionReturnCriteria5Camt00500111(ISO20022MessageElement):
    pmt_to_rtr_crit: Optional[SystemReturnCriteria2Camt00500111] = field(
        default=None,
        metadata={
            "name": "PmtToRtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_fr_rtr_crit: Optional[SystemReturnCriteria2Camt00500111] = field(
        default=None,
        metadata={
            "name": "PmtFrRtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_csh_ntry_rtr_crit: Optional[AccountCashEntryReturnCriteria3Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "AcctCshNtryRtrCrit",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    pmt_rtr_crit: Optional[PaymentReturnCriteria4Camt00500111] = field(
        default=None,
        metadata={
            "name": "PmtRtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class AccountIdentificationSearchCriteria2ChoiceCamt00500111(ISO20022MessageElement):
    eq: Optional[AccountIdentification4ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "EQ",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    cttxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ncttxt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NCTTxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountRange3Camt00500111(ISO20022MessageElement):
    amt: Optional[ImpliedCurrencyAmountRange1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class ActiveOrHistoricCurrencyAndAmountRange2Camt00500111(ISO20022MessageElement):
    amt: Optional[ImpliedCurrencyAmountRange1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class BranchData5Camt00500111(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00500111] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Camt00500111(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt00500111] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00500111] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt00500111] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class ImpliedCurrencyAndAmountRange1Camt00500111(ISO20022MessageElement):
    amt: Optional[ImpliedCurrencyAmountRange1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class Party52ChoiceCamt00500111(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Camt00500111] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prvt_id: Optional[PersonIdentification18Camt00500111] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class ActiveAmountRange3ChoiceCamt00500111(ISO20022MessageElement):
    impld_ccy_and_amt_rg: Optional[ImpliedCurrencyAndAmountRange1Camt00500111] = field(
        default=None,
        metadata={
            "name": "ImpldCcyAndAmtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ccy_and_amt_rg: Optional[ActiveCurrencyAndAmountRange3Camt00500111] = field(
        default=None,
        metadata={
            "name": "CcyAndAmtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class ActiveOrHistoricAmountRange2ChoiceCamt00500111(ISO20022MessageElement):
    impld_ccy_and_amt_rg: Optional[ImpliedCurrencyAndAmountRange1Camt00500111] = field(
        default=None,
        metadata={
            "name": "ImpldCcyAndAmtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ccy_and_amt_rg: Optional[ActiveOrHistoricCurrencyAndAmountRange2Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "CcyAndAmtRg",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Camt00500111(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Camt00500111] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Camt00500111] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PartyIdentification272Camt00500111(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00500111] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    id: Optional[Party52ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Camt00500111] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class CashAccountEntrySearch8Camt00500111(ISO20022MessageElement):
    acct_id: list[AccountIdentificationSearchCriteria2ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ntry_amt: list[ActiveOrHistoricAmountRange2ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "NtryAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ntry_amt_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NtryAmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ntry_sts: list[EntryStatus1Code] = field(
        default_factory=list,
        metadata={
            "name": "NtrySts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ntry_dt: list[DateAndDateTimeSearch3ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "NtryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_ownr: Optional[PartyIdentification272Camt00500111] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_svcr: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "AcctSvcr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )


@dataclass
class LongPaymentIdentification4Camt00500111(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    intr_bk_sttlm_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    pmt_mtd: Optional[PaymentOrigin1ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
                "required": True,
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
                "required": True,
            },
        )
    )
    ntry_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[BEOVW]{1,1}[0-9]{2,2}|DUM",
        },
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Party50ChoiceCamt00500111(ISO20022MessageElement):
    pty: Optional[PartyIdentification272Camt00500111] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = field(
        default=None,
        metadata={
            "name": "Agt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class ShortPaymentIdentification4Camt00500111(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
                "required": True,
            },
        )
    )


@dataclass
class SystemSearch5Camt00500111(ISO20022MessageElement):
    sys_id: list[ClearingSystemIdentification3ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "SysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    mmb_id: list[BranchAndFinancialInstitutionIdentification8Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    acct_id: Optional[AccountIdentification4ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PaymentIdentification8ChoiceCamt00500111(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    qid: Optional[QueueTransactionIdentification1Camt00500111] = field(
        default=None,
        metadata={
            "name": "QId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    lng_biz_id: Optional[LongPaymentIdentification4Camt00500111] = field(
        default=None,
        metadata={
            "name": "LngBizId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    shrt_biz_id: Optional[ShortPaymentIdentification4Camt00500111] = field(
        default=None,
        metadata={
            "name": "ShrtBizId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class PaymentTransactionParty4Camt00500111(ISO20022MessageElement):
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    ultmt_dbtr: Optional[Party50ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    dbtr: Optional[Party50ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    dbtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "DbtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    instg_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt00500111
    ] = field(
        default=None,
        metadata={
            "name": "InstgRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instd_rmbrsmnt_agt: Optional[
        BranchAndFinancialInstitutionIdentification8Camt00500111
    ] = field(
        default=None,
        metadata={
            "name": "InstdRmbrsmntAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    intrmy_agt1: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt1",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    intrmy_agt2: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt2",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    intrmy_agt3: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "IntrmyAgt3",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    cdtr_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00500111] = (
        field(
            default=None,
            metadata={
                "name": "CdtrAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            },
        )
    )
    cdtr: Optional[Party50ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    ultmt_cdtr: Optional[Party50ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class PaymentSearch10Camt00500111(ISO20022MessageElement):
    msg_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    reqd_exctn_dt: list[DateAndDateTimeSearch3ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "ReqdExctnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_id: list[PaymentIdentification8ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "PmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    sts: list[InstructionStatusSearch5Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instd_amt: list[ActiveOrHistoricAmountRange2ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "InstdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instd_amt_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InstdAmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    intr_bk_sttlm_amt: list[ActiveAmountRange3ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    intr_bk_sttlm_amt_ccy: list[str] = field(
        default_factory=list,
        metadata={
            "name": "IntrBkSttlmAmtCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    pmt_mtd: list[PaymentOrigin1ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_tp: list[PaymentType4ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prty: list[Priority1ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    prcg_vldty_tm: list[DateTimePeriod1ChoiceCamt00500111] = field(
        default_factory=list,
        metadata={
            "name": "PrcgVldtyTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    instr: list[Instruction1Code] = field(
        default_factory=list,
        metadata={
            "name": "Instr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    tx_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: list[str] = field(
        default_factory=list,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    intr_bk_sttlm_dt: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    end_to_end_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pties: Optional[PaymentTransactionParty4Camt00500111] = field(
        default=None,
        metadata={
            "name": "Pties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class TransactionSearchCriteria11Camt00500111(ISO20022MessageElement):
    pmt_to: list[SystemSearch5Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "PmtTo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_fr: list[SystemSearch5Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "PmtFr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    pmt_sch: Optional[PaymentSearch10Camt00500111] = field(
        default=None,
        metadata={
            "name": "PmtSch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    acct_ntry_sch: Optional[CashAccountEntrySearch8Camt00500111] = field(
        default=None,
        metadata={
            "name": "AcctNtrySch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class TransactionCriteria11Camt00500111(ISO20022MessageElement):
    new_qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewQryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    sch_crit: list[TransactionSearchCriteria11Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "SchCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    stmt_rpt: Optional[ReportIndicator1Code] = field(
        default=None,
        metadata={
            "name": "StmtRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    rtr_crit: Optional[TransactionReturnCriteria5Camt00500111] = field(
        default=None,
        metadata={
            "name": "RtrCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class TransactionCriteria8ChoiceCamt00500111(ISO20022MessageElement):
    qry_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "QryNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "min_length": 1,
            "max_length": 35,
        },
    )
    new_crit: Optional[TransactionCriteria11Camt00500111] = field(
        default=None,
        metadata={
            "name": "NewCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class TransactionQuery8Camt00500111(ISO20022MessageElement):
    qry_tp: Optional[QueryType2Code] = field(
        default=None,
        metadata={
            "name": "QryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    tx_crit: Optional[TransactionCriteria8ChoiceCamt00500111] = field(
        default=None,
        metadata={
            "name": "TxCrit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class GetTransactionV11Camt00500111(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader9Camt00500111] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
            "required": True,
        },
    )
    tx_qry_def: Optional[TransactionQuery8Camt00500111] = field(
        default=None,
        metadata={
            "name": "TxQryDef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )
    splmtry_data: list[SupplementaryData1Camt00500111] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11",
        },
    )


@dataclass
class Camt00500111(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11"

    get_tx: Optional[GetTransactionV11Camt00500111] = field(
        default=None,
        metadata={
            "name": "GetTx",
            "type": "Element",
            "required": True,
        },
    )
