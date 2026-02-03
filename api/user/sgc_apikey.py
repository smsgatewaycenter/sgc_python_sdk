# -*- coding: utf-8 -*-
"""API key API. Mirrors vendor SGCSdk\\api\\user\\sgc_apikey. No admin key in header."""

from sgc_python_sdk.object.common.sgc_auth import sgc_auth
from sgc_python_sdk.object.user.sgc_user import sgc_user
from sgc_python_sdk.config.common.sgc_common_api_params import (
    API_COMMON_PARAM_USERID,
    API_COMMON_PARAM_PASSWORD,
    API_COMMON_PARAM_API_KEY,
    API_COMMON_PARAM_OUTPUT_FORMAT,
    API_COMMON_METHOD_GET,
    API_COMMON_METHOD_POST,
)
from sgc_python_sdk.config.common.sgc_constant import (
    SGC_API,
    SGC_ENDPOINT_APIKEY_CREATE,
    SGC_ENDPOINT_APIKEY_READ,
    SGC_ENDPOINT_APIKEY_UPDATE,
    SGC_ENDPOINT_APIKEY_DELETE,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_apikey:
    def __init__(self, auth: sgc_auth, user: sgc_user) -> None:
        self._auth = auth
        self._user = user
        self._useRestApi = False
        self._header = {API_COMMON_PARAM_API_KEY: self._auth.getApiKey() or ""}
        self._data = {
            API_COMMON_PARAM_USERID: self._auth.getUsername() or "",
            API_COMMON_PARAM_PASSWORD: self._auth.getPassword() or "",
            API_COMMON_PARAM_OUTPUT_FORMAT: self._user.getOutput(),
        }

    def useRestApi(self, useRestApi: bool) -> None:
        self._useRestApi = useRestApi

    def Create(self):
        return sgc_callapi(SGC_API, SGC_ENDPOINT_APIKEY_CREATE, self._data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def Read(self):
        return sgc_callapi(SGC_API, SGC_ENDPOINT_APIKEY_READ, self._data, self._header, API_COMMON_METHOD_GET, self._useRestApi).getResponse()

    def Update(self):
        return sgc_callapi(SGC_API, SGC_ENDPOINT_APIKEY_UPDATE, self._data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def Delete(self):
        return sgc_callapi(SGC_API, SGC_ENDPOINT_APIKEY_DELETE, self._data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()
