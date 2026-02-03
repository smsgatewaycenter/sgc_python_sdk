# -*- coding: utf-8 -*-
"""Contact API. Mirrors vendor SGCSdk\\api\\user\\sgc_contact. No admin key in header."""

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
    SGC_ENDPOINT_CONTACT_CREATE,
    SGC_ENDPOINT_CONTACT_READ,
    SGC_ENDPOINT_CONTACT_UPDATE,
    SGC_ENDPOINT_CONTACT_DELETE,
)
from sgc_python_sdk.config.user.sgc_user_contact_api_params import (
    API_USER_CONTACT_PARAM_GROUP_NAME,
    API_USER_CONTACT_PARAM_GROUP_ID,
    API_USER_CONTACT_PARAM_CONTACT_NAME,
    API_USER_CONTACT_PARAM_MOBILE_NO,
    API_USER_CONTACT_PARAM_CONTACT_ID,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_contact:
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
        data[API_USER_CONTACT_PARAM_GROUP_NAME] = self._user.getGroupName() or ""
        data[API_USER_CONTACT_PARAM_GROUP_ID] = self._user.getGroupId() or ""
        data[API_USER_CONTACT_PARAM_CONTACT_NAME] = self._user.getContactName() or ""
        data[API_USER_CONTACT_PARAM_MOBILE_NO] = self._user.getMobileNo() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_CONTACT_CREATE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def Read(self):
        data = dict(self._data)
        data[API_USER_CONTACT_PARAM_GROUP_NAME] = self._user.getGroupName() or ""
        data[API_USER_CONTACT_PARAM_GROUP_ID] = self._user.getGroupId() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_CONTACT_READ, data, self._header, API_COMMON_METHOD_GET, self._useRestApi).getResponse()

    def Update(self):
        data = dict(self._data)
        data[API_USER_CONTACT_PARAM_GROUP_NAME] = self._user.getGroupName() or ""
        data[API_USER_CONTACT_PARAM_GROUP_ID] = self._user.getGroupId() or ""
        data[API_USER_CONTACT_PARAM_CONTACT_NAME] = self._user.getContactName() or ""
        data[API_USER_CONTACT_PARAM_MOBILE_NO] = self._user.getMobileNo() or ""
        data[API_USER_CONTACT_PARAM_CONTACT_ID] = self._user.getContactId() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_CONTACT_UPDATE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def Delete(self):
        data = dict(self._data)
        data[API_USER_CONTACT_PARAM_CONTACT_ID] = self._user.getContactId() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_CONTACT_DELETE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()
