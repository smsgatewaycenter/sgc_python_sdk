# -*- coding: utf-8 -*-
"""
User context object for account, contact, group, senderid, password APIs.
Mirrors vendor SGCSdk\\object\\sgc_user (main fields used by api modules).
"""

from typing import Optional


class sgc_user:
    """Holds user-related request parameters for SGC user APIs."""

    def __init__(self, output: str = "json") -> None:
        self._output = output
        self._email: Optional[str] = None
        self._mobileNo: Optional[str] = None
        self._fullName: Optional[str] = None
        self._address: Optional[str] = None
        self._region: Optional[str] = None
        self._country: Optional[str] = None
        self._city: Optional[str] = None
        self._fromDate: Optional[str] = None
        self._toDate: Optional[str] = None
        self._groupName: Optional[str] = None
        self._groupId: Optional[str] = None
        self._contactName: Optional[str] = None
        self._contactId: Optional[str] = None
        self._newPassword: Optional[str] = None
        self._confirmPassword: Optional[str] = None
        self._senderId: Optional[str] = None
        self._id: Optional[str] = None
        self._profilePic: Optional[str] = None
        self._domainName: Optional[str] = None
        self._industry: Optional[str] = None
        self._dltEntityId: Optional[str] = None
        self._userTimezone: Optional[str] = None

    def getOutput(self) -> str:
        return self._output or "json"

    def getEmail(self) -> Optional[str]:
        return self._email

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

    def getFromDate(self) -> Optional[str]:
        return self._fromDate

    def getToDate(self) -> Optional[str]:
        return self._toDate

    def getGroupName(self) -> Optional[str]:
        return self._groupName

    def getGroupId(self) -> Optional[str]:
        return self._groupId

    def getContactName(self) -> Optional[str]:
        return self._contactName

    def getContactId(self) -> Optional[str]:
        return self._contactId

    def getNewPassword(self) -> Optional[str]:
        return self._newPassword

    def getConfirmPassword(self) -> Optional[str]:
        return self._confirmPassword

    def getSenderId(self) -> Optional[str]:
        return self._senderId

    def getId(self) -> Optional[str]:
        return self._id

    def getProfilePic(self) -> Optional[str]:
        return self._profilePic

    def getDomainName(self) -> Optional[str]:
        return self._domainName

    def getIndustry(self) -> Optional[str]:
        return self._industry

    def getDltEntityId(self) -> Optional[str]:
        return self._dltEntityId

    def getUserTimezone(self) -> Optional[str]:
        return self._userTimezone

    def setOutput(self, output: str) -> None:
        self._output = output

    def setEmail(self, v: Optional[str]) -> None:
        self._email = v

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

    def setFromDate(self, v: Optional[str]) -> None:
        self._fromDate = v

    def setToDate(self, v: Optional[str]) -> None:
        self._toDate = v

    def setGroupName(self, v: Optional[str]) -> None:
        self._groupName = v

    def setGroupId(self, v: Optional[str]) -> None:
        self._groupId = v

    def setContactName(self, v: Optional[str]) -> None:
        self._contactName = v

    def setContactId(self, v: Optional[str]) -> None:
        self._contactId = v

    def setNewPassword(self, v: Optional[str]) -> None:
        self._newPassword = v

    def setConfirmPassword(self, v: Optional[str]) -> None:
        self._confirmPassword = v

    def setSenderId(self, v: Optional[str]) -> None:
        self._senderId = v

    def setId(self, v: Optional[str]) -> None:
        self._id = v

    def setProfilePic(self, v: Optional[str]) -> None:
        self._profilePic = v

    def setDomainName(self, v: Optional[str]) -> None:
        self._domainName = v

    def setIndustry(self, v: Optional[str]) -> None:
        self._industry = v

    def setDltEntityId(self, v: Optional[str]) -> None:
        self._dltEntityId = v

    def setUserTimezone(self, v: Optional[str]) -> None:
        self._userTimezone = v
