# -*- coding: utf-8 -*-
"""Reseller user API. Mirrors vendor SGCSdk\\api\\reseller\\sgc_user. No admin key in header."""

from sgc_python_sdk.object.common.sgc_auth import sgc_auth
from sgc_python_sdk.object.reseller.sgc_reseller import sgc_reseller
from sgc_python_sdk.config.common.sgc_common_api_params import (
    API_COMMON_PARAM_USERID,
    API_COMMON_PARAM_PASSWORD,
    API_COMMON_PARAM_API_KEY,
    API_COMMON_PARAM_OUTPUT_FORMAT,
    API_COMMON_METHOD_POST,
)
from sgc_python_sdk.config.common.sgc_constant import (
    SGC_API,
    SGC_ENDPOINT_RESELLER_CREATE_USER,
    SGC_ENDPOINT_RESELLER_READ_USER,
    SGC_ENDPOINT_RESELLER_UPDATE_USER,
    SGC_ENDPOINT_RESELLER_GENERATE_USER_PASSWORD,
    SGC_ENDPOINT_RESELLER_RESET_USER_PASSWORD,
)
from sgc_python_sdk.config.reseller.sgc_reseller_user_api_params import (
    API_RESELLER_USER_PARAM_USER_TYPE,
    API_RESELLER_USER_PARAM_USERNAME,
    API_RESELLER_USER_PARAM_EMAIL_ID,
    API_RESELLER_USER_PARAM_CONTACT_NO,
    API_RESELLER_USER_PARAM_FULL_NAME,
    API_RESELLER_USER_PARAM_ADDRESS,
    API_RESELLER_USER_PARAM_CITY,
    API_RESELLER_USER_PARAM_REGION,
    API_RESELLER_USER_PARAM_COUNTRY,
    API_RESELLER_USER_PARAM_DOMAIN_NAME,
    API_RESELLER_USER_PARAM_EXPIRY_DATE,
    API_RESELLER_USER_PARAM_ENABLE_CMS,
    API_RESELLER_USER_PARAM_USER_STATUS,
    API_RESELLER_USER_PARAM_NEWPASSWORD,
    API_RESELLER_USER_PARAM_DLT_ENTITY_ID,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_user:
    """Reseller user API (named sgc_user to match vendor; distinct from object.user.sgc_user)."""

    def __init__(self, auth: sgc_auth, reseller: sgc_reseller) -> None:
        self._auth = auth
        self._reseller = reseller
        self._useRestApi = False
        self._header = {API_COMMON_PARAM_API_KEY: self._auth.getApiKey() or ""}
        self._data = {
            API_COMMON_PARAM_USERID: self._auth.getUsername() or "",
            API_COMMON_PARAM_PASSWORD: self._auth.getPassword() or "",
            API_COMMON_PARAM_OUTPUT_FORMAT: self._reseller.getOutput(),
        }

    def useRestApi(self, useRestApi: bool) -> None:
        self._useRestApi = useRestApi

    def _reseller_data(self):
        return {
            API_RESELLER_USER_PARAM_USER_TYPE: self._reseller.getUserType() or "",
            API_RESELLER_USER_PARAM_USERNAME: self._reseller.getUserLoginName() or "",
            API_RESELLER_USER_PARAM_EMAIL_ID: self._reseller.getEmailId() or "",
            API_RESELLER_USER_PARAM_CONTACT_NO: self._reseller.getMobileNo() or "",
            API_RESELLER_USER_PARAM_FULL_NAME: self._reseller.getFullName() or "",
            API_RESELLER_USER_PARAM_ADDRESS: self._reseller.getAddress() or "",
            API_RESELLER_USER_PARAM_CITY: self._reseller.getCity() or "",
            API_RESELLER_USER_PARAM_REGION: self._reseller.getRegion() or "",
            API_RESELLER_USER_PARAM_COUNTRY: self._reseller.getCountry() or "",
            API_RESELLER_USER_PARAM_DOMAIN_NAME: self._reseller.getDomainName() or "",
            API_RESELLER_USER_PARAM_EXPIRY_DATE: self._reseller.getExpiryDate() or "",
            API_RESELLER_USER_PARAM_ENABLE_CMS: self._reseller.getEnableCMS() or "",
            API_RESELLER_USER_PARAM_DLT_ENTITY_ID: self._reseller.getDltEntityId() or "",
        }

    def CreateUser(self):
        data = dict(self._data, **self._reseller_data())
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_CREATE_USER, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def ReadUser(self):
        data = dict(self._data)
        data[API_RESELLER_USER_PARAM_USERNAME] = self._reseller.getUserLoginName() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_READ_USER, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def UpdateUser(self):
        data = dict(self._data, **self._reseller_data())
        data[API_RESELLER_USER_PARAM_USER_STATUS] = self._reseller.getUserStatus() or ""
        data[API_RESELLER_USER_PARAM_NEWPASSWORD] = self._reseller.getNewPassword() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_UPDATE_USER, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def GeneratePassword(self):
        data = dict(self._data)
        data[API_RESELLER_USER_PARAM_USERNAME] = self._reseller.getUserLoginName() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_GENERATE_USER_PASSWORD, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def ResetPassword(self):
        data = dict(self._data)
        data[API_RESELLER_USER_PARAM_USERNAME] = self._reseller.getUserLoginName() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_RESET_USER_PASSWORD, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()
