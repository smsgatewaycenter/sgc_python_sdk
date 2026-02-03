# -*- coding: utf-8 -*-
"""Group API. Mirrors vendor SGCSdk\\api\\user\\sgc_group. No admin key in header."""

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
    SGC_ENDPOINT_GROUP_CREATE,
    SGC_ENDPOINT_GROUP_READ,
    SGC_ENDPOINT_GROUP_UPDATE,
    SGC_ENDPOINT_GROUP_DELETE,
)
from sgc_python_sdk.config.user.sgc_user_group_api_params import (
    API_USER_GROUP_PARAM_GROUP_NAME,
    API_USER_GROUP_PARAM_GROUP_ID,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_group:
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
        data = dict(self._data)
        data[API_USER_GROUP_PARAM_GROUP_NAME] = self._user.getGroupName() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_GROUP_CREATE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def Read(self):
        return sgc_callapi(SGC_API, SGC_ENDPOINT_GROUP_READ, self._data, self._header, API_COMMON_METHOD_GET, self._useRestApi).getResponse()

    def Update(self):
        data = dict(self._data)
        data[API_USER_GROUP_PARAM_GROUP_NAME] = self._user.getGroupName() or ""
        data[API_USER_GROUP_PARAM_GROUP_ID] = self._user.getId() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_GROUP_UPDATE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def Delete(self):
        data = dict(self._data)
        data[API_USER_GROUP_PARAM_GROUP_ID] = self._user.getId() or ""
        data[API_USER_GROUP_PARAM_GROUP_NAME] = self._user.getGroupName() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_GROUP_DELETE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()
