# -*- coding: utf-8 -*-
"""SMS send API params. Mirrors vendor sgc_sms_send_api_params."""

API_SMS_SEND_API_NAME = "send"
API_SMS_SEND_METHOD_BATCH = "simple"
API_SMS_SEND_METHOD_PHONEBOOK = "group"
API_SMS_SEND_METHOD_FILE_UPLOAD = "bulk"
# sendMethod values (param sent in request body)
API_SMS_SEND_METHOD_QUICK = "quick"
API_SMS_SEND_PARAM_SEND_METHOD = "sendMethod"
API_SMS_SEND_PARAM_MOBILE = "mobile"
API_SMS_SEND_PARAM_MESSAGE_TEXT = "msg"
API_SMS_SEND_PARAM_MESSAGE_TYPE = "msgType"
API_SMS_SEND_PARAM_SCHEDULE_TIME = "scheduleTime"
API_SMS_SEND_PARAM_SENDER_ID = "senderid"
API_SMS_SEND_PARAM_TEST_MESSAGE = "testMessage"
API_SMS_SEND_PARAM_GROUP_NAME = "group"
API_SMS_SEND_PARAM_DUPLICATE_CHECK = "duplicatecheck"
API_SMS_SEND_PARAM_FILE_NAME = "file"
