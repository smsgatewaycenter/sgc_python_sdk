# -*- coding: utf-8 -*-
"""Account API. Mirrors vendor SGCSdk\\api\\user\\sgc_account. No admin key in header."""

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
    SGC_ENDPOINT_ACCOUNT_READ_STATUS,
    SGC_ENDPOINT_ACCOUNT_READ_PROFILE,
    SGC_ENDPOINT_ACCOUNT_READ_CREDIT_HISTORY,
    SGC_ENDPOINT_ACCOUNT_UPDATE_PROFILE,
)
from sgc_python_sdk.config.user.sgc_user_account_api_params import (
    API_USER_ACCOUNT_PARAM_FROM_DATE,
    API_USER_ACCOUNT_PARAM_TO_DATE,
    API_USER_ACCOUNT_PARAM_EMAIL_ID,
    API_USER_ACCOUNT_PARAM_CONTACT_NO,
    API_USER_ACCOUNT_PARAM_FULL_NAME,
    API_USER_ACCOUNT_PARAM_ADDRESS,
    API_USER_ACCOUNT_PARAM_REGION,
    API_USER_ACCOUNT_PARAM_COUNTRY,
    API_USER_ACCOUNT_PARAM_CITY,
    API_USER_ACCOUNT_PARAM_PROFILE_IMAGE,
    API_USER_ACCOUNT_PARAM_DOMAIN_NAME,
    API_USER_ACCOUNT_PARAM_INDUSTRY,
    API_USER_ACCOUNT_PARAM_DLTENTITYID,
    API_USER_ACCOUNT_PARAM_USERTIMEZONE,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_account:
    """Account operations. Header uses only apikey (no adminkey)."""

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

    def ReadAccountStatus(self):
        r = sgc_callapi(SGC_API, SGC_ENDPOINT_ACCOUNT_READ_STATUS, self._data, self._header, API_COMMON_METHOD_POST, self._useRestApi)
        return r.getResponse()

    def ReadProfile(self):
        r = sgc_callapi(SGC_API, SGC_ENDPOINT_ACCOUNT_READ_PROFILE, self._data, self._header, API_COMMON_METHOD_GET, self._useRestApi)
        return r.getResponse()

    def ReadCreditHistory(self):
        data = dict(self._data)
        data[API_USER_ACCOUNT_PARAM_FROM_DATE] = self._user.getFromDate() or ""
        data[API_USER_ACCOUNT_PARAM_TO_DATE] = self._user.getToDate() or ""
        r = sgc_callapi(SGC_API, SGC_ENDPOINT_ACCOUNT_READ_CREDIT_HISTORY, data, self._header, API_COMMON_METHOD_GET, self._useRestApi)
        return r.getResponse()

    def UpdateProfile(self):
        data = dict(self._data)
        data[API_USER_ACCOUNT_PARAM_EMAIL_ID] = self._user.getEmail() or ""
        data[API_USER_ACCOUNT_PARAM_CONTACT_NO] = self._user.getMobileNo() or ""
        data[API_USER_ACCOUNT_PARAM_FULL_NAME] = self._user.getFullName() or ""
        data[API_USER_ACCOUNT_PARAM_ADDRESS] = self._user.getAddress() or ""
        data[API_USER_ACCOUNT_PARAM_REGION] = self._user.getRegion() or ""
        data[API_USER_ACCOUNT_PARAM_COUNTRY] = self._user.getCountry() or ""
        data[API_USER_ACCOUNT_PARAM_CITY] = self._user.getCity() or ""
        data[API_USER_ACCOUNT_PARAM_PROFILE_IMAGE] = self._user.getProfilePic() or ""
        data[API_USER_ACCOUNT_PARAM_DOMAIN_NAME] = self._user.getDomainName() or ""
        data[API_USER_ACCOUNT_PARAM_INDUSTRY] = self._user.getIndustry() or ""
        data[API_USER_ACCOUNT_PARAM_DLTENTITYID] = self._user.getDltEntityId() or ""
        data[API_USER_ACCOUNT_PARAM_USERTIMEZONE] = self._user.getUserTimezone() or ""
        r = sgc_callapi(SGC_API, SGC_ENDPOINT_ACCOUNT_UPDATE_PROFILE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi)
        return r.getResponse()
