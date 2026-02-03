# -*- coding: utf-8 -*-
"""SMS send API. Mirrors vendor SGCSdk\\api\\sms\\sgc_sms_send. No admin key in header."""

from sgc_python_sdk.object.common.sgc_auth import sgc_auth
from sgc_python_sdk.object.sms.sgc_sms import sgc_sms
from sgc_python_sdk.config.common.sgc_common_api_params import (
    API_COMMON_PARAM_USERID,
    API_COMMON_PARAM_PASSWORD,
    API_COMMON_PARAM_API_KEY,
    API_COMMON_PARAM_OUTPUT_FORMAT,
    API_COMMON_METHOD_POST,
)
from sgc_python_sdk.config.common.sgc_constant import (
    SGC_API,
    SGC_ENDPOINT_SMS_BATCH,
    SGC_ENDPOINT_SMS_PHONEBOOK,
    SGC_ENDPOINT_SMS_FILE,
)
from sgc_python_sdk.config.sms.sgc_sms_send_api_params import (
    API_SMS_SEND_PARAM_SEND_METHOD,
    API_SMS_SEND_METHOD_QUICK,
    API_SMS_SEND_METHOD_PHONEBOOK,
    API_SMS_SEND_METHOD_FILE_UPLOAD,
    API_SMS_SEND_PARAM_MESSAGE_TEXT,
    API_SMS_SEND_PARAM_MESSAGE_TYPE,
    API_SMS_SEND_PARAM_SCHEDULE_TIME,
    API_SMS_SEND_PARAM_SENDER_ID,
    API_SMS_SEND_PARAM_TEST_MESSAGE,
    API_SMS_SEND_PARAM_DUPLICATE_CHECK,
    API_SMS_SEND_PARAM_MOBILE,
    API_SMS_SEND_PARAM_GROUP_NAME,
    API_SMS_SEND_PARAM_FILE_NAME,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


def _normalize_boolean_param(value: object, default: str) -> str:
    """
    Return API-expected "true" or "false". Empty/None -> default.
    API (e.g. status 147) requires exactly "true" or "false", not empty string.
    """
    if value is None or (isinstance(value, str) and not value.strip()):
        return default
    return "true" if str(value).strip().lower() == "true" else "false"


class sgc_sms_send:
    def __init__(self, auth: sgc_auth, sms: sgc_sms) -> None:
        self._auth = auth
        self._sms = sms
        self._useRestApi = False
        self._last_status_code = 0
        self._last_request_url = ""
        self._header = {API_COMMON_PARAM_API_KEY: self._auth.getApiKey() or ""}
        self._data = {
            API_COMMON_PARAM_USERID: self._auth.getUsername() or "",
            API_COMMON_PARAM_PASSWORD: self._auth.getPassword() or "",
            API_COMMON_PARAM_OUTPUT_FORMAT: self._sms.getOutput(),
        }

    def useRestApi(self, useRestApi: bool) -> None:
        self._useRestApi = useRestApi

    def getLastStatusCode(self) -> int:
        """Return HTTP status code of the last API call (e.g. batch/phonebook/file)."""
        return self._last_status_code

    def getLastRequestUrl(self) -> str:
        """Return the full URL used for the last API call (for debugging)."""
        return self._last_request_url or ""

    def batch(self):
        data = dict(self._data)
        data[API_SMS_SEND_PARAM_SEND_METHOD] = self._sms.getSendMethod() or API_SMS_SEND_METHOD_QUICK
        data[API_SMS_SEND_PARAM_MESSAGE_TEXT] = self._sms.getText() or ""
        data[API_SMS_SEND_PARAM_MESSAGE_TYPE] = self._sms.getMsgType() or ""
        data[API_SMS_SEND_PARAM_SCHEDULE_TIME] = self._sms.getScheduleTime() or ""
        data[API_SMS_SEND_PARAM_SENDER_ID] = self._sms.getSenderId() or ""
        data[API_SMS_SEND_PARAM_TEST_MESSAGE] = _normalize_boolean_param(self._sms.getTestMessage(), "false")
        data[API_SMS_SEND_PARAM_DUPLICATE_CHECK] = _normalize_boolean_param(self._sms.getDuplicateCheck(), "true")
        data[API_SMS_SEND_PARAM_MOBILE] = self._sms.getPhone() or ""
        call = sgc_callapi(SGC_API, SGC_ENDPOINT_SMS_BATCH, data, self._header, API_COMMON_METHOD_POST, self._useRestApi)
        self._last_status_code = call.getStatusCode()
        self._last_request_url = call.getRequestUrl()
        return call.getResponse()

    def phonebook(self):
        data = dict(self._data)
        data[API_SMS_SEND_PARAM_SEND_METHOD] = self._sms.getSendMethod() or API_SMS_SEND_METHOD_PHONEBOOK
        data[API_SMS_SEND_PARAM_MESSAGE_TEXT] = self._sms.getText() or ""
        data[API_SMS_SEND_PARAM_MESSAGE_TYPE] = self._sms.getMsgType() or ""
        data[API_SMS_SEND_PARAM_SCHEDULE_TIME] = self._sms.getScheduleTime() or ""
        data[API_SMS_SEND_PARAM_SENDER_ID] = self._sms.getSenderId() or ""
        data[API_SMS_SEND_PARAM_TEST_MESSAGE] = _normalize_boolean_param(self._sms.getTestMessage(), "false")
        data[API_SMS_SEND_PARAM_DUPLICATE_CHECK] = _normalize_boolean_param(self._sms.getDuplicateCheck(), "true")
        data[API_SMS_SEND_PARAM_GROUP_NAME] = self._sms.getGroupName() or ""
        call = sgc_callapi(SGC_API, SGC_ENDPOINT_SMS_PHONEBOOK, data, self._header, API_COMMON_METHOD_POST, self._useRestApi)
        self._last_status_code = call.getStatusCode()
        self._last_request_url = call.getRequestUrl()
        return call.getResponse()

    def file(self):
        data = dict(self._data)
        data[API_SMS_SEND_PARAM_SEND_METHOD] = self._sms.getSendMethod() or API_SMS_SEND_METHOD_FILE_UPLOAD
        data[API_SMS_SEND_PARAM_MESSAGE_TEXT] = self._sms.getText() or ""
        data[API_SMS_SEND_PARAM_MESSAGE_TYPE] = self._sms.getMsgType() or ""
        data[API_SMS_SEND_PARAM_SCHEDULE_TIME] = self._sms.getScheduleTime() or ""
        data[API_SMS_SEND_PARAM_SENDER_ID] = self._sms.getSenderId() or ""
        data[API_SMS_SEND_PARAM_TEST_MESSAGE] = _normalize_boolean_param(self._sms.getTestMessage(), "false")
        data[API_SMS_SEND_PARAM_DUPLICATE_CHECK] = _normalize_boolean_param(self._sms.getDuplicateCheck(), "true")
        data[API_SMS_SEND_PARAM_FILE_NAME] = self._sms.getFile() or ""
        call = sgc_callapi(SGC_API, SGC_ENDPOINT_SMS_FILE, data, self._header, API_COMMON_METHOD_POST, self._useRestApi)
        self._last_status_code = call.getStatusCode()
        self._last_request_url = call.getRequestUrl()
        return call.getResponse()
