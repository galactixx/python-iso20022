from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import AddressType2Code, CreditDebitCode, FormOfSecurity1Code
from python_iso20022.seev.enums import (
    CorporateActionEventProcessingType1Code,
    CorporateActionEventType2Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionOptionType1Code,
    SecuritiesBalanceType10Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01"


@dataclass
class AccountIdentification2ChoiceSeev01400101(ISO20022MessageElement):
    csh_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountSeev01400101(ISO20022MessageElement):
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
class AlternateSecurityIdentification3Seev01400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    dmst_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "DmstIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceSeev01400101(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class DocumentIdentification8Seev01400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev01400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev01400101(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CorporateActionEventProcessingType1FormatChoiceSeev01400101(
    ISO20022MessageElement
):
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev01400101(ISO20022MessageElement):
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary1FormatChoiceSeev01400101(
    ISO20022MessageElement
):
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class CorporateActionOption1FormatChoiceSeev01400101(ISO20022MessageElement):
    cd: Optional[CorporateActionOptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class PostalAddress1Seev01400101(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecuritiesBalanceType10FormatChoiceSeev01400101(ISO20022MessageElement):
    cd: Optional[SecuritiesBalanceType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev01400101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev01400101(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev01400101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class UnitOrFaceAmount1ChoiceSeev01400101(ISO20022MessageElement):
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountSeev01400101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class NameAndAddress5Seev01400101(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev01400101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev01400101(ISO20022MessageElement):
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev01400101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev01400101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class CashAccount19Seev01400101(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    acct_id: Optional[AccountIdentification2ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev01400101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev01400101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class SecuritiesAccount7Seev01400101(ISO20022MessageElement):
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount9Seev01400101(ISO20022MessageElement):
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal_tp: Optional[SecuritiesBalanceType10FormatChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    scty_hldg_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctyHldgForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class CorporateActionCashMovements2Seev01400101(ISO20022MessageElement):
    pstng_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstngId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstng_dt_tm: Optional[DateAndDateTimeChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "PstngDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    pstng_amt: Optional[ActiveCurrencyAndAmountSeev01400101] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    acct_dtls: list[CashAccount19Seev01400101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class CorporateActionInformation1Seev01400101(ISO20022MessageElement):
    agt_id: Optional[PartyIdentification2ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    issr_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnPrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType2FormatChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary1FormatChoiceSeev01400101
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    evt_prcg_tp: Optional[
        CorporateActionEventProcessingType1FormatChoiceSeev01400101
    ] = field(
        default=None,
        metadata={
            "name": "EvtPrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev01400101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )


@dataclass
class CorporateActionSecuritiesMovement2Seev01400101(ISO20022MessageElement):
    scty_id: Optional[SecurityIdentification7Seev01400101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    pstng_dt_tm: Optional[DateAndDateTimeChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "PstngDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    pstng_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstngId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pstng_qty: Optional[UnitOrFaceAmount1ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    acct_dtls: list[SecuritiesAccount9Seev01400101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class CorporateActionElection3Seev01400101(ISO20022MessageElement):
    acct_dtls: Optional[SecuritiesAccount7Seev01400101] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    instd_undrlyg_scties_qty: Optional[UnitOrFaceAmount1ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "InstdUndrlygSctiesQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    instd_scties_qty_to_rcv: Optional[UnitOrFaceAmount1ChoiceSeev01400101] = field(
        default=None,
        metadata={
            "name": "InstdSctiesQtyToRcv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    propsd_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PropsdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    csh_mvmnt_dtls: list[CorporateActionCashMovements2Seev01400101] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )
    scties_mvmnt_dtls: list[CorporateActionSecuritiesMovement2Seev01400101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class AgentCaelectionCancellationRequestV01Seev01400101(ISO20022MessageElement):
    class Meta:
        name = "AgentCAElectionCancellationRequestV01"

    id: Optional[DocumentIdentification8Seev01400101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    agt_caelctn_advc_id: Optional[DocumentIdentification8Seev01400101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    corp_actn_gnl_inf: Optional[CorporateActionInformation1Seev01400101] = field(
        default=None,
        metadata={
            "name": "CorpActnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
            "required": True,
        },
    )
    elctn_dtls: Optional[CorporateActionElection3Seev01400101] = field(
        default=None,
        metadata={
            "name": "ElctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01",
        },
    )


@dataclass
class Seev01400101(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01"

    agt_caelctn_cxl_req: Optional[AgentCaelectionCancellationRequestV01Seev01400101] = (
        field(
            default=None,
            metadata={
                "name": "AgtCAElctnCxlReq",
                "type": "Element",
                "required": True,
            },
        )
    )
