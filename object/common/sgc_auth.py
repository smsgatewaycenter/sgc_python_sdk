# -*- coding: utf-8 -*-
"""
Auth object for API requests. Mirrors vendor SGCSdk\\object\\sgc_auth.
Admin key is not exposed in user SDK.
"""

from typing import Optional


class sgc_auth:
    """Holds username, password, and API key for SGC API. No admin key in user SDK."""

    def __init__(self) -> None:
        self._username: Optional[str] = None
        self._password: Optional[str] = None
        self._apiKey: Optional[str] = None

    def getUsername(self) -> Optional[str]:
        return self._username

    def getPassword(self) -> Optional[str]:
        return self._password

    def getApiKey(self) -> Optional[str]:
        return self._apiKey

    def setUsername(self, username: Optional[str]) -> None:
        self._username = username

    def setPassword(self, password: Optional[str]) -> None:
        self._password = password

    def setApiKey(self, apiKey: Optional[str]) -> None:
        self._apiKey = apiKey
