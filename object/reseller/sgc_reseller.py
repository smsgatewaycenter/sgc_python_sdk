# -*- coding: utf-8 -*-
"""
Reseller context object. Mirrors vendor SGCSdk\\object\\sgc_reseller.
"""

from typing import Optional


class sgc_reseller:
    """Holds reseller-related request parameters (client user, credit, etc.)."""

    def __init__(self, output: str = "json") -> None:
        self._output = output
        self._credit: Optional[str] = None
        self._comment: Optional[str] = None
        self._userLoginName: Optional[str] = None
        self._fromDate: Optional[str] = None
        self._toDate: Optional[str] = None
        self._userType: Optional[str] = None
        self._emailId: Optional[str] = None
        self._mobileNo: Optional[str] = None
        self._fullName: Optional[str] = None
        self._address: Optional[str] = None
        self._region: Optional[str] = None
        self._country: Optional[str] = None
        self._city: Optional[str] = None
        self._newPassword: Optional[str] = None
        self._domainName: Optional[str] = None
        self._expiryDate: Optional[str] = None
        self._enableCMS: Optional[str] = None
        self._userStatus: Optional[str] = None
        self._product: Optional[str] = None
        self._transactionType: Optional[str] = None
        self._dltEntityId: Optional[str] = None

    def getOutput(self) -> str:
        return self._output or "json"

    def getCredit(self) -> Optional[str]:
        return self._credit

    def getComment(self) -> Optional[str]:
        return self._comment

    def getUserLoginName(self) -> Optional[str]:
        return self._userLoginName

    def getFromDate(self) -> Optional[str]:
        return self._fromDate

    def getToDate(self) -> Optional[str]:
        return self._toDate

    def getUserType(self) -> Optional[str]:
        return self._userType

    def getEmailId(self) -> Optional[str]:
        return self._emailId

    def getMobileNo(self) -> Optional[str]:
        return self._mobileNo

    def getFullName(self) -> Optional[str]:
        return self._fullName

    def getAddress(self) -> Optional[str]:
        return self._address

    def getRegion(self) -> Optional[str]:
        return self._region

    def getCountry(self) -> Optional[str]:
        return self._country

    def getCity(self) -> Optional[str]:
        return self._city

    def getNewPassword(self) -> Optional[str]:
        return self._newPassword

    def getDomainName(self) -> Optional[str]:
        return self._domainName

    def getExpiryDate(self) -> Optional[str]:
        return self._expiryDate

    def getEnableCMS(self) -> Optional[str]:
        return self._enableCMS

    def getUserStatus(self) -> Optional[str]:
        return self._userStatus

    def getProduct(self) -> Optional[str]:
        return self._product

    def getTransactionType(self) -> Optional[str]:
        return self._transactionType

    def getDltEntityId(self) -> Optional[str]:
        return self._dltEntityId

    def setOutput(self, output: str) -> None:
        self._output = output

    def setCredit(self, v: Optional[str]) -> None:
        self._credit = v

    def setComment(self, v: Optional[str]) -> None:
        self._comment = v

    def setUserLoginName(self, v: Optional[str]) -> None:
        self._userLoginName = v

    def setFromDate(self, v: Optional[str]) -> None:
        self._fromDate = v

    def setToDate(self, v: Optional[str]) -> None:
        self._toDate = v

    def setUserType(self, v: Optional[str]) -> None:
        self._userType = v

    def setEmailId(self, v: Optional[str]) -> None:
        self._emailId = v

    def setMobileNo(self, v: Optional[str]) -> None:
        self._mobileNo = v

    def setFullName(self, v: Optional[str]) -> None:
        self._fullName = v

    def setAddress(self, v: Optional[str]) -> None:
        self._address = v

    def setRegion(self, v: Optional[str]) -> None:
        self._region = v

    def setCountry(self, v: Optional[str]) -> None:
        self._country = v

    def setCity(self, v: Optional[str]) -> None:
        self._city = v

    def setNewPassword(self, v: Optional[str]) -> None:
        self._newPassword = v

    def setDomainName(self, v: Optional[str]) -> None:
        self._domainName = v

    def setExpiryDate(self, v: Optional[str]) -> None:
        self._expiryDate = v

    def setEnableCMS(self, v: Optional[str]) -> None:
        self._enableCMS = v

    def setUserStatus(self, v: Optional[str]) -> None:
        self._userStatus = v

    def setProduct(self, v: Optional[str]) -> None:
        self._product = v

    def setTransactionType(self, v: Optional[str]) -> None:
        self._transactionType = v

    def setDltEntityId(self, v: Optional[str]) -> None:
        self._dltEntityId = v
