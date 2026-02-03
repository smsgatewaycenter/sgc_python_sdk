# -*- coding: utf-8 -*-
"""
SGC API base URL and endpoint paths. Mirrors web project vendor SDK:
system/vendor/sgcsdk/sgcapi/src/config/common/sgc_constant.php
Base URL from environment SGC_API_BASE (default: http://localhost/web).
"""

import os

# Base URL: from env for local/other hosts; no remote fetch by default
SERVER_HOST = os.environ.get("SGC_API_BASE", "https://unify.smsgateway.center")
SGC_API = "/SMSApi"
SGC_OTP_API = "/OTPApi"

# Sender ID API endpoints
SGC_ENDPOINT_SENDER_ID_CREATE = "/senderid/create"
SGC_ENDPOINT_SENDER_ID_READ = "/senderid/read"
SGC_ENDPOINT_SENDER_ID_UPDATE = "/senderid/update"
SGC_ENDPOINT_SENDER_ID_DELETE = "/senderid/delete"

# Template API endpoints
SGC_ENDPOINT_TEMPLATE_CREATE = "/template/create"
SGC_ENDPOINT_TEMPLATE_READ = "/template/read"
SGC_ENDPOINT_TEMPLATE_UPDATE = "/template/update"
SGC_ENDPOINT_TEMPLATE_DELETE = "/template/delete"

# Draft API endpoints
SGC_ENDPOINT_DRAFT_CREATE = "/draft/create"
SGC_ENDPOINT_DRAFT_READ = "/draft/read"
SGC_ENDPOINT_DRAFT_UPDATE = "/draft/update"
SGC_ENDPOINT_DRAFT_DELETE = "/draft/delete"

# Webhook API endpoints
SGC_ENDPOINT_WEBHOOK_CREATE = "/webhook/create"
SGC_ENDPOINT_WEBHOOK_READ = "/webhook/read"
SGC_ENDPOINT_WEBHOOK_UPDATE = "/webhook/update"
SGC_ENDPOINT_WEBHOOK_DELETE = "/webhook/delete"

# Account API endpoints
SGC_ENDPOINT_ACCOUNT_READ_STATUS = "/account/readstatus"
SGC_ENDPOINT_ACCOUNT_READ_PROFILE = "/account/readprofile"
SGC_ENDPOINT_ACCOUNT_UPDATE_PROFILE = "/account/updateprofile"
SGC_ENDPOINT_ACCOUNT_READ_CREDIT_HISTORY = "/account/readcredithistory"

# Password API endpoints
SGC_ENDPOINT_PASSWORD_CHANGE = "/password/change"
SGC_ENDPOINT_PASSWORD_FORGOT = "/password/forgot"
SGC_ENDPOINT_PASSWORD_RESET = "/password/reset"

# API key endpoints
SGC_ENDPOINT_APIKEY_CREATE = "/apikey/create"
SGC_ENDPOINT_APIKEY_READ = "/apikey/read"
SGC_ENDPOINT_APIKEY_UPDATE = "/apikey/update"
SGC_ENDPOINT_APIKEY_DELETE = "/apikey/delete"

# Group API endpoints
SGC_ENDPOINT_GROUP_CREATE = "/group/create"
SGC_ENDPOINT_GROUP_READ = "/group/read"
SGC_ENDPOINT_GROUP_UPDATE = "/group/update"
SGC_ENDPOINT_GROUP_DELETE = "/group/delete"

# Contact API endpoints
SGC_ENDPOINT_CONTACT_CREATE = "/contact/create"
SGC_ENDPOINT_CONTACT_READ = "/contact/read"
SGC_ENDPOINT_CONTACT_UPDATE = "/contact/update"
SGC_ENDPOINT_CONTACT_DELETE = "/contact/delete"

# SMS API endpoints
SGC_ENDPOINT_SMS_BATCH = "/send"
SGC_ENDPOINT_SMS_PHONEBOOK = "/send"
SGC_ENDPOINT_SMS_FILE = "/send"

# OTP API endpoints
SGC_ENDPOINT_OTP_SEND = "/send"
SGC_ENDPOINT_OTP_VERIFY = "/send"

# Schedule API endpoints
SGC_ENDPOINT_SCHEDULE_READ = "/schedule/read"
SGC_ENDPOINT_SCHEDULE_UPDATE = "/schedule/update"
SGC_ENDPOINT_SCHEDULE_DELETE = "/schedule/delete"

# Campaign API endpoints
SGC_ENDPOINT_CAMPAIGN_READ = "/campaign/read"
SGC_ENDPOINT_CAMPAIGN_UPDATE = "/campaign/update"
SGC_ENDPOINT_CAMPAIGN_DELETE = "/campaign/delete"

# Linktrack API endpoints
SGC_ENDPOINT_LINKTRACK_CREATE = "/linktrack/create"
SGC_ENDPOINT_LINKTRACK_READ = "/linktrack/read"
SGC_ENDPOINT_LINKTRACK_REPORT = "/linktrack/report"
SGC_ENDPOINT_LINKTRACK_DELETE = "/linktrack/delete"

# Report API endpoints
SGC_ENDPOINT_REPORT_GETSTATUS = "/report/status"
SGC_ENDPOINT_REPORT_GET = "/report/day"
SGC_ENDPOINT_REPORT_SUMMARY = "/report/summary"
SGC_ENDPOINT_REPORT_FILEUPLOAD = "/report/fileupload"

# Info API endpoints
SGC_ENDPOINT_INFO_MSG = "/info/msg"
SGC_ENDPOINT_INFO_DELIVERY_CODES = "/info/deliverycodes"
SGC_ENDPOINT_INFO_RESPONSE_CODES = "/info/responsecodes"

# Reseller user API endpoints
SGC_ENDPOINT_RESELLER_CREATE_USER = "/reseller/createuser"
SGC_ENDPOINT_RESELLER_UPDATE_USER = "/reseller/updateuser"
SGC_ENDPOINT_RESELLER_READ_USER = "/reseller/readuser"
SGC_ENDPOINT_RESELLER_GENERATE_USER_PASSWORD = "/reseller/generateuserpassword"
SGC_ENDPOINT_RESELLER_RESET_USER_PASSWORD = "/reseller/resetuserpassword"

# Reseller credit management API endpoints
SGC_ENDPOINT_RESELLER_ADD_CREDIT = "/reseller/addcredit"
SGC_ENDPOINT_RESELLER_REMOVE_CREDIT = "/reseller/removecredit"
SGC_ENDPOINT_RESELLER_READ_CREDIT_HISTORY = "/reseller/readcredithistory"
