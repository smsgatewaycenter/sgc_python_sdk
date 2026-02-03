# -*- coding: utf-8 -*-
"""
SMS context object. Mirrors vendor SGCSdk\\object\\sgc_sms.
"""

from typing import Optional


class sgc_sms:
    """Holds SMS-related request parameters (text, phone, senderId, etc.)."""

    def __init__(self, output: str = "json") -> None:
        self._output = output
        self._text: Optional[str] = None
        self._phone: Optional[str] = None
        self._msgType: Optional[str] = None
        self._scheduleTime: Optional[str] = None
        self._senderId: Optional[str] = None
        self._groupName: Optional[str] = None
        self._duplicateCheck: Optional[str] = None
        self._testMessage: Optional[str] = None
        self._file: Optional[str] = None
        self._fromDate: Optional[str] = None
        self._toDate: Optional[str] = None
        self._uuId: Optional[str] = None
        self._sendMethod: Optional[str] = None

    def getOutput(self) -> str:
        return self._output or "json"

    def getText(self) -> Optional[str]:
        return self._text

    def getPhone(self) -> Optional[str]:
        return self._phone

    def getMsgType(self) -> Optional[str]:
        return self._msgType

    def getScheduleTime(self) -> Optional[str]:
        return self._scheduleTime

    def getSenderId(self) -> Optional[str]:
        return self._senderId

    def getGroupName(self) -> Optional[str]:
        return self._groupName

    def getDuplicateCheck(self) -> Optional[str]:
        return self._duplicateCheck

    def getTestMessage(self) -> Optional[str]:
        return self._testMessage

    def getFile(self) -> Optional[str]:
        return self._file

    def getFromDate(self) -> Optional[str]:
        return self._fromDate

    def getToDate(self) -> Optional[str]:
        return self._toDate

    def getUuId(self) -> Optional[str]:
        return self._uuId

    def getSendMethod(self) -> Optional[str]:
        return self._sendMethod

    def setSendMethod(self, v: Optional[str]) -> None:
        self._sendMethod = v

    def setOutput(self, output: str) -> None:
        self._output = output

    def setText(self, v: Optional[str]) -> None:
        self._text = v

    def setPhone(self, v: Optional[str]) -> None:
        self._phone = v

    def setMsgType(self, v: Optional[str]) -> None:
        self._msgType = v

    def setScheduleTime(self, v: Optional[str]) -> None:
        self._scheduleTime = v

    def setSenderId(self, v: Optional[str]) -> None:
        self._senderId = v

    def setGroupName(self, v: Optional[str]) -> None:
        self._groupName = v

    def setDuplicateCheck(self, v: Optional[str]) -> None:
        self._duplicateCheck = v

    def setTestMessage(self, v: Optional[str]) -> None:
        self._testMessage = v

    def setFile(self, v: Optional[str]) -> None:
        self._file = v

    def setFromDate(self, v: Optional[str]) -> None:
        self._fromDate = v

    def setToDate(self, v: Optional[str]) -> None:
        self._toDate = v

    def setUuId(self, v: Optional[str]) -> None:
        self._uuId = v
