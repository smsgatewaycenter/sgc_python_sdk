# -*- coding: utf-8 -*-
"""Password API. Mirrors vendor SGCSdk\\api\\user\\sgc_password. No admin key in header."""

from sgc_python_sdk.object.common.sgc_auth import sgc_auth
from sgc_python_sdk.object.user.sgc_user import sgc_user
from sgc_python_sdk.config.common.sgc_common_api_params import (
    API_COMMON_PARAM_USERID,
    API_COMMON_PARAM_PASSWORD,
    API_COMMON_PARAM_API_KEY,
    API_COMMON_PARAM_OUTPUT_FORMAT,
    API_COMMON_METHOD_POST,
)
from sgc_python_sdk.config.common.sgc_constant import SGC_API, SGC_ENDPOINT_PASSWORD_CHANGE
from sgc_python_sdk.config.user.sgc_user_password_api_params import (
    API_USER_PASSWORD_PARAM_NEW_PASSWORD,
    API_USER_PASSWORD_PARAM_CONFIRM_PASSWORD,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_password:
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

    def Change(self):
        data = dict(self._data)
        data[API_USER_PASSWORD_PARAM_NEW_PASSWORD] = self._user.getNewPassword() or ""
        data[API_USER_PASSWORD_PARAM_CONFIRM_PASSWORD] = self._user.getConfirmPassword() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_PASSWORD_CHANGE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()
