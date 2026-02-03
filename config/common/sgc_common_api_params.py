# -*- coding: utf-8 -*-
"""
Common API parameter names and values. Mirrors web project:
SMSApi/config/common/sgc_common_api_params.php
"""

# Output format
API_COMMON_OUTPUT_FORMAT = ("plain", "json", "xml")
API_COMMON_OUTPUT_FORMAT_TEXT = "plain"
API_COMMON_OUTPUT_FORMAT_JSON = "json"
API_COMMON_OUTPUT_FORMAT_XML = "xml"
API_COMMON_TEXT_OUTPUT_HEADER = "plain"

# Common params (param names sent in requests). Admin-only params (e.g. adminkey) are not exposed in user SDK.
API_COMMON_PARAM_USERID = "userid"
API_COMMON_PARAM_PASSWORD = "password"
API_COMMON_PARAM_API_KEY = "apikey"
API_COMMON_PARAM_OUTPUT_FORMAT = "output"
API_COMMON_PARAM_UUID = "uuid"
API_COMMON_PARAM_ID = "id"

# Static
API_COMMON_CONST_TRUE = "true"
API_COMMON_CONST_FALSE = "false"
API_COMMON_CONST_SUCCESS = "success"
API_COMMON_CONST_ERROR = "error"

# Method
API_COMMON_METHOD_GET = "GET"
API_COMMON_METHOD_POST = "POST"
API_COMMON_METHOD_FILE = "FILE"

# Response
API_COMMON_OUTPUT_TEXT_RESPONSE_SEPARATOR = " | "
