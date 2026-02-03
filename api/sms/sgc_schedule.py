# -*- coding: utf-8 -*-
"""Schedule API. Mirrors vendor SGCSdk\\api\\sms\\sgc_schedule. No admin key in header."""

from sgc_python_sdk.object.common.sgc_auth import sgc_auth
from sgc_python_sdk.object.sms.sgc_sms import sgc_sms
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
    SGC_ENDPOINT_SCHEDULE_READ,
    SGC_ENDPOINT_SCHEDULE_UPDATE,
    SGC_ENDPOINT_SCHEDULE_DELETE,
)
from sgc_python_sdk.config.sms.sgc_sms_schedule_api_params import (
    API_SMS_SCHEDULE_PARAM_FROM_DATE,
    API_SMS_SCHEDULE_PARAM_TO_DATE,
    API_SMS_SCHEDULE_PARAM_UUID,
    API_SMS_SCHEDULE_PARAM_SCHEDULE_TIME,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_schedule:
    def __init__(self, auth: sgc_auth, sms: sgc_sms) -> None:
        self._auth = auth
        self._sms = sms
        self._useRestApi = False
        self._header = {API_COMMON_PARAM_API_KEY: self._auth.getApiKey() or ""}
        self._data = {
            API_COMMON_PARAM_USERID: self._auth.getUsername() or "",
            API_COMMON_PARAM_PASSWORD: self._auth.getPassword() or "",
            API_COMMON_PARAM_OUTPUT_FORMAT: self._sms.getOutput(),
        }

    def useRestApi(self, useRestApi: bool) -> None:
        self._useRestApi = useRestApi

    def Read(self):
        data = dict(self._data)
        data[API_SMS_SCHEDULE_PARAM_FROM_DATE] = self._sms.getFromDate() or ""
        data[API_SMS_SCHEDULE_PARAM_TO_DATE] = self._sms.getToDate() or ""
        data[API_SMS_SCHEDULE_PARAM_UUID] = self._sms.getUuId() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_SCHEDULE_READ, data, self._header, API_COMMON_METHOD_GET, self._useRestApi).getResponse()

    def Update(self):
        data = dict(self._data)
        data[API_SMS_SCHEDULE_PARAM_SCHEDULE_TIME] = self._sms.getScheduleTime() or ""
        data[API_SMS_SCHEDULE_PARAM_UUID] = self._sms.getUuId() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_SCHEDULE_UPDATE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def Delete(self):
        data = dict(self._data)
        data[API_SMS_SCHEDULE_PARAM_UUID] = self._sms.getUuId() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_SCHEDULE_DELETE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()
