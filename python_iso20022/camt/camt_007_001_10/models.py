from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.camt.enums import (
    Instruction1Code,
    PaymentInstrument1Code,
    PaymentType3Code,
    Priority5Code,
)
from python_iso20022.enums import AddressType2Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10"


@dataclass
class ClearingSystemIdentification2ChoiceCamt00700110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateTimePeriod1Camt00700110(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceCamt00700110(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Camt00700110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageHeader1Camt00700110(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class QueueTransactionIdentification1Camt00700110(ISO20022MessageElement):
    qid: Optional[str] = field(
        default=None,
        metadata={
            "name": "QId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Camt00700110(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceCamt00700110(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    prtry: Optional[GenericIdentification30Camt00700110] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Camt00700110(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateTimePeriod1ChoiceCamt00700110(ISO20022MessageElement):
    fr_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    to_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    dt_tm_rg: Optional[DateTimePeriod1Camt00700110] = field(
        default=None,
        metadata={
            "name": "DtTmRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class GenericFinancialIdentification1Camt00700110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentOrigin1ChoiceCamt00700110(ISO20022MessageElement):
    finmt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FINMT",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[0-9]{1,3}",
        },
    )
    xmlmsg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "XMLMsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instrm: Optional[PaymentInstrument1Code] = field(
        default=None,
        metadata={
            "name": "Instrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class PaymentType4ChoiceCamt00700110(ISO20022MessageElement):
    cd: Optional[PaymentType3Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Priority1ChoiceCamt00700110(ISO20022MessageElement):
    cd: Optional[Priority5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Camt00700110(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Camt00700110] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )


@dataclass
class PaymentInstruction33Camt00700110(ISO20022MessageElement):
    instr: Optional[Instruction1Code] = field(
        default=None,
        metadata={
            "name": "Instr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    tp: Optional[PaymentType4ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    prty: Optional[Priority1ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    prcg_vldty_tm: Optional[DateTimePeriod1ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "PrcgVldtyTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class PostalAddress27Camt00700110(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BranchData5Camt00700110(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00700110] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Camt00700110(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Camt00700110] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Camt00700110] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    othr: Optional[GenericFinancialIdentification1Camt00700110] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Camt00700110(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Camt00700110] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Camt00700110] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class LongPaymentIdentification4Camt00700110(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    intr_bk_sttlm_amt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )
    pmt_mtd: Optional[PaymentOrigin1ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "PmtMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00700110] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
                "required": True,
            },
        )
    )
    instd_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00700110] = (
        field(
            default=None,
            metadata={
                "name": "InstdAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
                "required": True,
            },
        )
    )
    ntry_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[BEOVW]{1,1}[0-9]{2,2}|DUM",
        },
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ShortPaymentIdentification4Camt00700110(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    intr_bk_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IntrBkSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )
    instg_agt: Optional[BranchAndFinancialInstitutionIdentification8Camt00700110] = (
        field(
            default=None,
            metadata={
                "name": "InstgAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
                "required": True,
            },
        )
    )


@dataclass
class PaymentIdentification8ChoiceCamt00700110(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 35,
        },
    )
    uetr: Optional[str] = field(
        default=None,
        metadata={
            "name": "UETR",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "pattern": r"[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}",
        },
    )
    qid: Optional[QueueTransactionIdentification1Camt00700110] = field(
        default=None,
        metadata={
            "name": "QId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    lng_biz_id: Optional[LongPaymentIdentification4Camt00700110] = field(
        default=None,
        metadata={
            "name": "LngBizId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    shrt_biz_id: Optional[ShortPaymentIdentification4Camt00700110] = field(
        default=None,
        metadata={
            "name": "ShrtBizId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )
    prtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class TransactionModification7Camt00700110(ISO20022MessageElement):
    pmt_id: Optional[PaymentIdentification8ChoiceCamt00700110] = field(
        default=None,
        metadata={
            "name": "PmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )
    new_pmt_val_set: Optional[PaymentInstruction33Camt00700110] = field(
        default=None,
        metadata={
            "name": "NewPmtValSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )


@dataclass
class ModifyTransactionV10Camt00700110(ISO20022MessageElement):
    msg_hdr: Optional[MessageHeader1Camt00700110] = field(
        default=None,
        metadata={
            "name": "MsgHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "required": True,
        },
    )
    mod: list[TransactionModification7Camt00700110] = field(
        default_factory=list,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Camt00700110] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10",
        },
    )


@dataclass
class Camt00700110(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10"

    modfy_tx: Optional[ModifyTransactionV10Camt00700110] = field(
        default=None,
        metadata={
            "name": "ModfyTx",
            "type": "Element",
            "required": True,
        },
    )
