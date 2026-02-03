# -*- coding: utf-8 -*-
"""Reseller credit management API. Mirrors vendor SGCSdk\\api\\reseller\\sgc_credit_management. No admin key in header."""

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
    SGC_ENDPOINT_RESELLER_READ_CREDIT_HISTORY,
    SGC_ENDPOINT_RESELLER_ADD_CREDIT,
    SGC_ENDPOINT_RESELLER_REMOVE_CREDIT,
)
from sgc_python_sdk.config.reseller.sgc_reseller_credit_management_api_params import (
    API_RESELLER_CREDIT_MANAGEMENT_CREDIT,
    API_RESELLER_CREDIT_MANAGEMENT_PRODUCT,
    API_RESELLER_CREDIT_MANAGEMENT_TRANSACTION_TYPE,
    API_RESELLER_CREDIT_MANAGEMENT_COMMENT,
    API_RESELLER_CREDIT_MANAGEMENT_USER_LOGIN_NAME,
    API_RESELLER_CREDIT_MANAGEMENT_FROM_DATE,
    API_RESELLER_CREDIT_MANAGEMENT_TO_DATE,
    API_RESELLER_CREDIT_MANAGEMENT_EXPIRYDATE,
)
from sgc_python_sdk.lib.sgc_callapi import sgc_callapi


class sgc_credit_management:
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

    def ReadUserCreditUsage(self):
        data = dict(self._data)
        data[API_RESELLER_CREDIT_MANAGEMENT_FROM_DATE] = self._reseller.getFromDate() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_TO_DATE] = self._reseller.getToDate() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_USER_LOGIN_NAME] = self._reseller.getUserLoginName() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_READ_CREDIT_HISTORY, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def AddCredit(self):
        data = dict(self._data)
        data[API_RESELLER_CREDIT_MANAGEMENT_CREDIT] = self._reseller.getCredit() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_PRODUCT] = self._reseller.getProduct() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_TRANSACTION_TYPE] = self._reseller.getTransactionType() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_COMMENT] = self._reseller.getComment() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_USER_LOGIN_NAME] = self._reseller.getUserLoginName() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_EXPIRYDATE] = self._reseller.getExpiryDate() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_ADD_CREDIT, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()

    def RemoveCredit(self):
        data = dict(self._data)
        data[API_RESELLER_CREDIT_MANAGEMENT_CREDIT] = self._reseller.getCredit() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_COMMENT] = self._reseller.getComment() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_PRODUCT] = self._reseller.getProduct() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_TRANSACTION_TYPE] = self._reseller.getTransactionType() or ""
        data[API_RESELLER_CREDIT_MANAGEMENT_USER_LOGIN_NAME] = self._reseller.getUserLoginName() or ""
        return sgc_callapi(SGC_API, SGC_ENDPOINT_RESELLER_REMOVE_CREDIT, data, self._header, API_COMMON_METHOD_POST, self._useRestApi).getResponse()
