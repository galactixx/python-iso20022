from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.enums import AddressType2Code, CreditDebitCode, FormOfSecurity1Code
from python_iso20022.seev.enums import (
    CashBalanceType1Code,
    CorporateActionEventProcessingType1Code,
    CorporateActionEventType2Code,
    CorporateActionMandatoryVoluntary1Code,
    CorporateActionOptionType1Code,
    SecuritiesBalanceType10Code,
    StampDutyType1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01"


@dataclass
class AccountIdentification2ChoiceSeev02100101:
    csh_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountSeev02100101:
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
class AlternateSecurityIdentification3Seev02100101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry_id_src: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtryIdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndDateTimeChoiceSeev02100101:
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class DocumentIdentification8Seev02100101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class GenericIdentification1Seev02100101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification13Seev02100101:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class CashBalanceType1FormatTypeSeev02100101:
    cd: Optional[CashBalanceType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class CorporateActionEventProcessingType1FormatChoiceSeev02100101:
    cd: Optional[CorporateActionEventProcessingType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class CorporateActionEventType2FormatChoiceSeev02100101:
    cd: Optional[CorporateActionEventType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class CorporateActionMandatoryVoluntary1FormatChoiceSeev02100101:
    cd: Optional[CorporateActionMandatoryVoluntary1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class CorporateActionOption1FormatChoiceSeev02100101:
    cd: Optional[CorporateActionOptionType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class PostalAddress1Seev02100101:
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class SecuritiesBalanceType10FormatChoiceSeev02100101:
    cd: Optional[SecuritiesBalanceType10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class SecurityIdentification7Seev02100101:
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "pattern": r"[A-Z0-9]{12,12}",
        },
    )
    othr_id: Optional[AlternateSecurityIdentification3Seev02100101] = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class StampDutyType1FormatChoiceSeev02100101:
    cd: Optional[StampDutyType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    prtry: Optional[GenericIdentification13Seev02100101] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class UnitOrFaceAmount1ChoiceSeev02100101:
    unit: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    face_amt: Optional[ActiveCurrencyAndAmountSeev02100101] = field(
        default=None,
        metadata={
            "name": "FaceAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class NameAndAddress5Seev02100101:
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Seev02100101] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class PartyIdentification2ChoiceSeev02100101:
    bicor_bei: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICOrBEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "pattern": r"[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Seev02100101] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Seev02100101] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class CashAccount18Seev02100101:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    acct_id: Optional[AccountIdentification2ChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    bal_tp: Optional[CashBalanceType1FormatTypeSeev02100101] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class FinancialInstrumentDescription3Seev02100101:
    scty_id: Optional[SecurityIdentification7Seev02100101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    plc_of_listg: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcOfListg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    sfkpg_plc: Optional[PartyIdentification2ChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class SecuritiesAccount8Seev02100101:
    cdt_dbt_ind: Optional[CreditDebitCode] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    acct_ownr_id: Optional[PartyIdentification2ChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "AcctOwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    bal_tp: Optional[SecuritiesBalanceType10FormatChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "BalTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    optn_tp: Optional[CorporateActionOption1FormatChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "OptnTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    optn_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "OptnNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "pattern": r"[0-9]{3}",
        },
    )
    scty_hldg_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctyHldgForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    stmp_dty: Optional[StampDutyType1FormatChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "StmpDty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class CashMovement3Seev02100101:
    pstng_dt_tm: Optional[DateAndDateTimeChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "PstngDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    pstng_amt: Optional[ActiveCurrencyAndAmountSeev02100101] = field(
        default=None,
        metadata={
            "name": "PstngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    acct_dtls: list[CashAccount18Seev02100101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class CorporateActionInformation1Seev02100101:
    agt_id: Optional[PartyIdentification2ChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "AgtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    issr_corp_actn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssrCorpActnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    corp_actn_prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorpActnPrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_length": 1,
            "max_length": 35,
        },
    )
    evt_tp: Optional[CorporateActionEventType2FormatChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "EvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    mndtry_vlntry_evt_tp: Optional[
        CorporateActionMandatoryVoluntary1FormatChoiceSeev02100101
    ] = field(
        default=None,
        metadata={
            "name": "MndtryVlntryEvtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    evt_prcg_tp: Optional[
        CorporateActionEventProcessingType1FormatChoiceSeev02100101
    ] = field(
        default=None,
        metadata={
            "name": "EvtPrcgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    undrlyg_scty: Optional[FinancialInstrumentDescription3Seev02100101] = field(
        default=None,
        metadata={
            "name": "UndrlygScty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )


@dataclass
class CorporateActionSecuritiesMovement1Seev02100101:
    pstng_dt_tm: Optional[DateAndDateTimeChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "PstngDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    scty_id: Optional[SecurityIdentification7Seev02100101] = field(
        default=None,
        metadata={
            "name": "SctyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    pstng_qty: Optional[UnitOrFaceAmount1ChoiceSeev02100101] = field(
        default=None,
        metadata={
            "name": "PstngQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    acct_dtls: list[SecuritiesAccount8Seev02100101] = field(
        default_factory=list,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class AgentCamovementConfirmationV01Seev02100101:
    class Meta:
        name = "AgentCAMovementConfirmationV01"

    id: Optional[DocumentIdentification8Seev02100101] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    agt_camvmnt_instr_id: Optional[DocumentIdentification8Seev02100101] = field(
        default=None,
        metadata={
            "name": "AgtCAMvmntInstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    agt_caelctn_sts_advc_id: Optional[DocumentIdentification8Seev02100101] = field(
        default=None,
        metadata={
            "name": "AgtCAElctnStsAdvcId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    agt_cagbl_dstrbtn_sts_advc_id: Optional[DocumentIdentification8Seev02100101] = (
        field(
            default=None,
            metadata={
                "name": "AgtCAGblDstrbtnStsAdvcId",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            },
        )
    )
    corp_actn_gnl_inf: Optional[CorporateActionInformation1Seev02100101] = field(
        default=None,
        metadata={
            "name": "CorpActnGnlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
            "required": True,
        },
    )
    scties_mvmnt_dtls: list[CorporateActionSecuritiesMovement1Seev02100101] = field(
        default_factory=list,
        metadata={
            "name": "SctiesMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )
    csh_mvmnt_dtls: list[CashMovement3Seev02100101] = field(
        default_factory=list,
        metadata={
            "name": "CshMvmntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01",
        },
    )


@dataclass
class Seev02100101:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:seev.021.001.01"

    agt_camvmnt_conf: Optional[AgentCamovementConfirmationV01Seev02100101] = field(
        default=None,
        metadata={
            "name": "AgtCAMvmntConf",
            "type": "Element",
            "required": True,
        },
    )
