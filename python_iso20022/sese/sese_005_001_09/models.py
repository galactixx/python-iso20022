from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    BeneficiaryCertificationCompletion1Code,
    DistributionPolicy1Code,
    FormOfSecurity1Code,
    IncomePreference2Code,
    InvestmentFundFee1Code,
    InvestmentFundRole2Code,
    NamePrefix1Code,
    PhysicalTransferType1Code,
    PriceMethod1Code,
    RoundingDirection2Code,
    SafekeepingPlace1Code,
    SafekeepingPlace2Code,
    SettlementTransactionCondition11Code,
    TaxableIncomePerShareCalculated2Code,
    TaxationBasis2Code,
    TaxationBasis5Code,
    TaxExemptReason1Code,
    TaxType17Code,
    TradeTransactionCondition5Code,
    TypeOfIdentification1Code,
    TypeOfPrice10Code,
    UktaxGroupUnit1Code,
    WaivingInstruction1Code,
)
from python_iso20022.sese.enums import (
    BusinessFlowType1Code,
    ChargeBearer1Code,
    ChargePaymentMethod1Code,
    HoldingsPlanType1Code,
    InvestmentFundFee2Code,
    OtherAmountType1Code,
    SettlementDate1Code,
    StampDutyType2Code,
    TaxType16Code,
    TransferInFunction1Code,
    TransferReason1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09"


@dataclass
class ActiveCurrencyAnd13DecimalAmountSese00500109(ISO20022MessageElement):
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
class ActiveCurrencyAndAmountSese00500109(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAnd13DecimalAmountSese00500109(ISO20022MessageElement):
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
class ActiveOrHistoricCurrencyAndAmountSese00500109(ISO20022MessageElement):
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
class CopyInformation5Sese00500109(ISO20022MessageElement):
    cpy_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CpyInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    orgnl_rcvr: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class DateAndDateTime2ChoiceSese00500109(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Extension1Sese00500109(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    txt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Txt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class GenericIdentification1Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification27Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class GenericIdentification30Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification36Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification47Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]{1,4}",
        },
    )


@dataclass
class IdentificationSource1ChoiceSese00500109(ISO20022MessageElement):
    dmst: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dmst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MarketPracticeVersion1Sese00500109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class MessageIdentification1Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation1Sese00500109(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )


@dataclass
class Quantity42ChoiceSese00500109(ISO20022MessageElement):
    ttl_units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TtlUnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    trf_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrfRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class SubAccount5Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    chrtc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Chrtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AlternateSecurityIdentification7Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    id_src: Optional[IdentificationSource1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "IdSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class ChargeBasis2ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TaxationBasis5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class ChargePaymentMethod1ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[ChargePaymentMethod1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class ChargeType5ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[InvestmentFundFee1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class ChargeType6ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[InvestmentFundFee2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class ContactIdentification2Sese00500109(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix1Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    gvn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "GvnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DateFormat1ChoiceSese00500109(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    cd: Optional[SettlementDate1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class ExemptionReason1ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class GenericIdentification78Sese00500109(ISO20022MessageElement):
    tp: Optional[GenericIdentification30Sese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class IdentificationType42ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TypeOfIdentification1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class OtherAmountType1ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[OtherAmountType1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry_cd: Optional[GenericIdentification1Sese00500109] = field(
        default=None,
        metadata={
            "name": "PrtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class PostalAddress1Sese00500109(ISO20022MessageElement):
    adr_tp: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PriceValue1Sese00500109(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAnd13DecimalAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class Role4ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[InvestmentFundRole2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndIdentification1Sese00500109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace1Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass
class SafekeepingPlaceTypeAndText6Sese00500109(ISO20022MessageElement):
    sfkpg_plc_tp: Optional[SafekeepingPlace2Code] = field(
        default=None,
        metadata={
            "name": "SfkpgPlcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SecuritiesAccount19Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[GenericIdentification30Sese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SettlementTransactionCondition30ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[SettlementTransactionCondition11Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TaxBasis1ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TaxationBasis2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TaxType1ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TaxType16Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TaxType3ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TaxType17Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TaxableIncomePerShareCalculated2ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TaxableIncomePerShareCalculated2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TradeTransactionCondition8ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TradeTransactionCondition5Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification30Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TransferReason1ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TransferReason1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification27Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TypeOfPrice46ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[TypeOfPrice10Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class WaivingInstruction2ChoiceSese00500109(ISO20022MessageElement):
    cd: Optional[WaivingInstruction1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification47Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class AlternatePartyIdentification7Sese00500109(ISO20022MessageElement):
    id_tp: Optional[IdentificationType42ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    altrn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ChargeOrCommissionDiscount1Sese00500109(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis: Optional[WaivingInstruction2ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class ChargeOrCommissionDiscount2Sese00500109(ISO20022MessageElement):
    amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis: Optional[WaivingInstruction2ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class NameAndAddress4Sese00500109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese00500109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class NameAndAddress5Sese00500109(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    adr: Optional[PostalAddress1Sese00500109] = field(
        default=None,
        metadata={
            "name": "Adr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class OtherAmount1Sese00500109(ISO20022MessageElement):
    tp: Optional[OtherAmountType1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class PartyTextInformation6Sese00500109(ISO20022MessageElement):
    dclrtn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "DclrtnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    pty_ctct_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "PtyCtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 140,
        },
    )
    regn_dtls: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    regn_adr: Optional[PostalAddress1Sese00500109] = field(
        default=None,
        metadata={
            "name": "RegnAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class SafekeepingPlaceFormat28ChoiceSese00500109(ISO20022MessageElement):
    id: Optional[SafekeepingPlaceTypeAndText6Sese00500109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    tp_and_id: Optional[SafekeepingPlaceTypeAndIdentification1Sese00500109] = field(
        default=None,
        metadata={
            "name": "TpAndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prtry: Optional[GenericIdentification78Sese00500109] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class SecurityIdentification25ChoiceSese00500109(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    sedol: Optional[str] = field(
        default=None,
        metadata={
            "name": "SEDOL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    cusip: Optional[str] = field(
        default=None,
        metadata={
            "name": "CUSIP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ric: Optional[str] = field(
        default=None,
        metadata={
            "name": "RIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tckr_symb: Optional[str] = field(
        default=None,
        metadata={
            "name": "TckrSymb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    blmbrg: Optional[str] = field(
        default=None,
        metadata={
            "name": "Blmbrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"(BBG)[BCDFGHJKLMNPQRSTVWXYZ\d]{8}\d",
        },
    )
    cta: Optional[str] = field(
        default=None,
        metadata={
            "name": "CTA",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    quick: Optional[str] = field(
        default=None,
        metadata={
            "name": "QUICK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    wrtppr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wrtppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    dtch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dtch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    vlrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vlrn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    scvm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SCVM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    belgn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Belgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    cmon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cmon",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 12,
        },
    )
    othr_prtry_id: Optional[AlternateSecurityIdentification7Sese00500109] = field(
        default=None,
        metadata={
            "name": "OthrPrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TaxCalculationInformation10Sese00500109(ISO20022MessageElement):
    bsis: Optional[TaxBasis1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    taxbl_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "TaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class TaxCalculationInformation11Sese00500109(ISO20022MessageElement):
    bsis: Optional[TaxBasis1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    taxbl_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "TaxblAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class UnitPrice23Sese00500109(ISO20022MessageElement):
    tp: Optional[TypeOfPrice46ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    val: Optional[PriceValue1Sese00500109] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    pric_mtd: Optional[PriceMethod1Code] = field(
        default=None,
        metadata={
            "name": "PricMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    acrd_intrst_nav: Optional[ActiveOrHistoricCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "AcrdIntrstNAV",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    nb_of_days_acrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfDaysAcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    taxbl_incm_per_shr: Optional[ActiveCurrencyAnd13DecimalAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    taxbl_incm_per_shr_clctd: Optional[
        TaxableIncomePerShareCalculated2ChoiceSese00500109
    ] = field(
        default=None,
        metadata={
            "name": "TaxblIncmPerShrClctd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class DeliveryParameters4Sese00500109(ISO20022MessageElement):
    regd_adr_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RegdAdrInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    nm_and_adr: Optional[NameAndAddress4Sese00500109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ctct_prsn: Optional[ContactIdentification2Sese00500109] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class FinancialInstrument88Sese00500109(ISO20022MessageElement):
    id: Optional[SecurityIdentification25ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    splmtry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SplmtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    clss_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClssTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    dstrbtn_plcy: Optional[DistributionPolicy1Code] = field(
        default=None,
        metadata={
            "name": "DstrbtnPlcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    dmtrlsd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmtrlsdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class PartyIdentification122ChoiceSese00500109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese00500109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class PartyIdentification123ChoiceSese00500109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification36Sese00500109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese00500109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class PartyIdentification125ChoiceSese00500109(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    prtry_id: Optional[GenericIdentification1Sese00500109] = field(
        default=None,
        metadata={
            "name": "PrtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    nm_and_adr: Optional[NameAndAddress5Sese00500109] = field(
        default=None,
        metadata={
            "name": "NmAndAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class PartyIdentification139Sese00500109(ISO20022MessageElement):
    pty: Optional[PartyIdentification125ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Pty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


@dataclass
class PartyIdentification141Sese00500109(ISO20022MessageElement):
    id: Optional[PartyIdentification122ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese00500109] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation1Sese00500109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class PartyIdentificationAndAccount194Sese00500109(ISO20022MessageElement):
    id: Optional[PartyIdentification123ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    altrn_id: Optional[AlternatePartyIdentification7Sese00500109] = field(
        default=None,
        metadata={
            "name": "AltrnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sfkpg_acct: Optional[SecuritiesAccount19Sese00500109] = field(
        default=None,
        metadata={
            "name": "SfkpgAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prcg_dt: Optional[DateAndDateTime2ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "PrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prcg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[PartyTextInformation6Sese00500109] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Account27Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class Account31Sese00500109(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svcr: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "Svcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sub_acct_dtls: Optional[SubAccount5Sese00500109] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class AdditionalReference10Sese00500109(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalReference11Sese00500109(ISO20022MessageElement):
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref_issr: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "RefIssr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    msg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Fee5Sese00500109(ISO20022MessageElement):
    tp: Optional[ChargeType5ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    bsis: Optional[ChargeBasis2ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    std_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "StdAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    std_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StdRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dscnt_dtls: Optional[ChargeOrCommissionDiscount1Sese00500109] = field(
        default=None,
        metadata={
            "name": "DscntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    non_std_slaref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSLARef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    inftv_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InftvInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )


@dataclass
class Fee7Sese00500109(ISO20022MessageElement):
    tp: Optional[ChargeType6ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    bsis: Optional[ChargeBasis2ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    dscnt_dtls: Optional[ChargeOrCommissionDiscount2Sese00500109] = field(
        default=None,
        metadata={
            "name": "DscntDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    chrg_br: Optional[ChargeBearer1Code] = field(
        default=None,
        metadata={
            "name": "ChrgBr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class ForeignExchangeTerms37Sese00500109(ISO20022MessageElement):
    to_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "ToAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    fr_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "FrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    qtd_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    qtn_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "QtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    qtg_instn: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "QtgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class SettlementParties94Sese00500109(ISO20022MessageElement):
    dpstry: Optional[PartyIdentification141Sese00500109] = field(
        default=None,
        metadata={
            "name": "Dpstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    pty1: Optional[PartyIdentificationAndAccount194Sese00500109] = field(
        default=None,
        metadata={
            "name": "Pty1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    pty2: Optional[PartyIdentificationAndAccount194Sese00500109] = field(
        default=None,
        metadata={
            "name": "Pty2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    pty3: Optional[PartyIdentificationAndAccount194Sese00500109] = field(
        default=None,
        metadata={
            "name": "Pty3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    pty4: Optional[PartyIdentificationAndAccount194Sese00500109] = field(
        default=None,
        metadata={
            "name": "Pty4",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    pty5: Optional[PartyIdentificationAndAccount194Sese00500109] = field(
        default=None,
        metadata={
            "name": "Pty5",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Tax35Sese00500109(ISO20022MessageElement):
    tp: Optional[TaxType3ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    apld_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "ApldAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    apld_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApldRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation10Sese00500109] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Tax38Sese00500109(ISO20022MessageElement):
    tp: Optional[TaxType1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    bsis: Optional[TaxBasis1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Bsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    xmptn_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "XmptnInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    xmptn_rsn: Optional[ExemptionReason1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "XmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    rcpt_id: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    tax_clctn_dtls: Optional[TaxCalculationInformation11Sese00500109] = field(
        default=None,
        metadata={
            "name": "TaxClctnDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Fees2Sese00500109(ISO20022MessageElement):
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_fee: list[Fee7Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "IndvFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class FundSettlementParameters15Sese00500109(ISO20022MessageElement):
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSese00500109] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSese00500109] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dlvrg_sd_dtls: Optional[SettlementParties94Sese00500109] = field(
        default=None,
        metadata={
            "name": "DlvrgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class FundSettlementParameters16Sese00500109(ISO20022MessageElement):
    trad_tx_cond: list[TradeTransactionCondition8ChoiceSese00500109] = field(
        default_factory=list,
        metadata={
            "name": "TradTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sttlm_tx_cond: list[SettlementTransactionCondition30ChoiceSese00500109] = field(
        default_factory=list,
        metadata={
            "name": "SttlmTxCond",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    scties_sttlm_sys_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SctiesSttlmSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcvg_sd_dtls: Optional[SettlementParties94Sese00500109] = field(
        default=None,
        metadata={
            "name": "RcvgSdDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Intermediary43Sese00500109(ISO20022MessageElement):
    id: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    acct: Optional[Account27Sese00500109] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    role: Optional[Role4ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ctct_prsn: Optional[ContactIdentification2Sese00500109] = field(
        default=None,
        metadata={
            "name": "CtctPrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TotalFeesAndTaxes42Sese00500109(ISO20022MessageElement):
    ttl_ovrhd_apld: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "TtlOvrhdApld",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ttl_fees: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "TtlFees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ttl_taxs: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "TtlTaxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    comrcl_agrmt_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComrclAgrmtRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    indv_fee: list[Fee5Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "IndvFee",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    indv_tax: list[Tax35Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class DeliverInformation21Sese00500109(ISO20022MessageElement):
    trfr: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "Trfr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    trfr_regd_acct: Optional[Account31Sese00500109] = field(
        default=None,
        metadata={
            "name": "TrfrRegdAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    intrmy_inf: list[Intermediary43Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    dmtrlsd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmtrlsdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    incm_pref: Optional[IncomePreference2Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    bnfcry_certfctn_cmpltn: Optional[BeneficiaryCertificationCompletion1Code] = field(
        default=None,
        metadata={
            "name": "BnfcryCertfctnCmpltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    reqd_trad_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdTradDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    reqd_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sttlm_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "SttlmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    stmp_dty: Optional[StampDutyType2Code] = field(
        default=None,
        metadata={
            "name": "StmpDty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    net_amt: Optional[ActiveCurrencyAndAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "NetAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    fees: list[Fees2Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "Fees",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    indv_tax: list[Tax38Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "IndvTax",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    fxdtls: list[ForeignExchangeTerms37Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "FXDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sttlm_pties_dtls: Optional[FundSettlementParameters15Sese00500109] = field(
        default=None,
        metadata={
            "name": "SttlmPtiesDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    phys_trf: Optional[PhysicalTransferType1Code] = field(
        default=None,
        metadata={
            "name": "PhysTrf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    phys_trf_dtls: Optional[DeliveryParameters4Sese00500109] = field(
        default=None,
        metadata={
            "name": "PhysTrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    clnt_ref: Optional[AdditionalReference10Sese00500109] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class InvestmentAccount71Sese00500109(ISO20022MessageElement):
    ownr_id: list[PartyIdentification139Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "OwnrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    acct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_dsgnt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctDsgnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr: Optional[PartyIdentification139Sese00500109] = field(
        default=None,
        metadata={
            "name": "AcctSvcr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sub_acct_dtls: Optional[SubAccount5Sese00500109] = field(
        default=None,
        metadata={
            "name": "SubAcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    intrmy_inf: list[Intermediary43Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "IntrmyInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    scties_form: Optional[FormOfSecurity1Code] = field(
        default=None,
        metadata={
            "name": "SctiesForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    dmtrlsd_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DmtrlsdInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    incm_pref: Optional[IncomePreference2Code] = field(
        default=None,
        metadata={
            "name": "IncmPref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    bnfcry_certfctn_cmpltn: Optional[BeneficiaryCertificationCompletion1Code] = field(
        default=None,
        metadata={
            "name": "BnfcryCertfctnCmpltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sfkpg_plc: Optional[SafekeepingPlaceFormat28ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "SfkpgPlc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    sttlm_pties_dtls: Optional[FundSettlementParameters16Sese00500109] = field(
        default=None,
        metadata={
            "name": "SttlmPtiesDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Unit12Sese00500109(ISO20022MessageElement):
    units_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnitsNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    ordr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OrdrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    acqstn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AcqstnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    cert_nb: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CertNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    grp1_or2_units: Optional[UktaxGroupUnit1Code] = field(
        default=None,
        metadata={
            "name": "Grp1Or2Units",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pric_dtls: Optional[UnitPrice23Sese00500109] = field(
        default=None,
        metadata={
            "name": "PricDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    tx_ovrhd: Optional[TotalFeesAndTaxes42Sese00500109] = field(
        default=None,
        metadata={
            "name": "TxOvrhd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    othr_amt: list[OtherAmount1Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "OthrAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Transfer36Sese00500109(ISO20022MessageElement):
    trf_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    clnt_ref: Optional[AdditionalReference10Sese00500109] = field(
        default=None,
        metadata={
            "name": "ClntRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    ctr_pty_ref: Optional[AdditionalReference10Sese00500109] = field(
        default=None,
        metadata={
            "name": "CtrPtyRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    biz_flow_tp: Optional[BusinessFlowType1Code] = field(
        default=None,
        metadata={
            "name": "BizFlowTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    reqd_trf_dt: Optional[DateFormat1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "ReqdTrfDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    reqd_sttlm_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReqdSttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    trf_ordr_dt_form: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TrfOrdrDtForm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    trf_rsn: Optional[TransferReason1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "TrfRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    hldgs_plan_tp: list[HoldingsPlanType1Code] = field(
        default_factory=list,
        metadata={
            "name": "HldgsPlanTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "max_occurs": 3,
        },
    )
    fin_instrm_dtls: Optional[FinancialInstrument88Sese00500109] = field(
        default=None,
        metadata={
            "name": "FinInstrmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    qty: Optional[Quantity42ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    units_dtls: list[Unit12Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "UnitsDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    rndg: Optional[RoundingDirection2Code] = field(
        default=None,
        metadata={
            "name": "Rndg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    orgnl_cost: Optional[ActiveCurrencyAnd13DecimalAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "OrgnlCost",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    avrg_pric: Optional[ActiveOrHistoricCurrencyAnd13DecimalAmountSese00500109] = field(
        default=None,
        metadata={
            "name": "AvrgPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    trf_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrfCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    own_acct_trf_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OwnAcctTrfInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    non_std_sttlm_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "NonStdSttlmInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 350,
        },
    )
    trf_expnss_pmt_tp: Optional[ChargePaymentMethod1ChoiceSese00500109] = field(
        default=None,
        metadata={
            "name": "TrfExpnssPmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class TransferInInstructionV09Sese00500109(ISO20022MessageElement):
    msg_id: Optional[MessageIdentification1Sese00500109] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    pool_ref: Optional[AdditionalReference11Sese00500109] = field(
        default=None,
        metadata={
            "name": "PoolRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    prvs_ref: Optional[AdditionalReference10Sese00500109] = field(
        default=None,
        metadata={
            "name": "PrvsRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    rltd_ref: Optional[AdditionalReference10Sese00500109] = field(
        default=None,
        metadata={
            "name": "RltdRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    fctn: Optional[TransferInFunction1Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    mstr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MstrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trf_dtls: list[Transfer36Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "TrfDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "min_occurs": 1,
        },
    )
    acct_dtls: Optional[InvestmentAccount71Sese00500109] = field(
        default=None,
        metadata={
            "name": "AcctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
            "required": True,
        },
    )
    sttlm_dtls: Optional[DeliverInformation21Sese00500109] = field(
        default=None,
        metadata={
            "name": "SttlmDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    mkt_prctc_vrsn: Optional[MarketPracticeVersion1Sese00500109] = field(
        default=None,
        metadata={
            "name": "MktPrctcVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    cpy_dtls: Optional[CopyInformation5Sese00500109] = field(
        default=None,
        metadata={
            "name": "CpyDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )
    xtnsn: list[Extension1Sese00500109] = field(
        default_factory=list,
        metadata={
            "name": "Xtnsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09",
        },
    )


@dataclass
class Sese00500109(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:sese.005.001.09"

    trf_in_instr: Optional[TransferInInstructionV09Sese00500109] = field(
        default=None,
        metadata={
            "name": "TrfInInstr",
            "type": "Element",
            "required": True,
        },
    )
