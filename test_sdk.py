# -*- coding: utf-8 -*-
"""
Simple test script for sgc_python_sdk.
Run from project root (web/) with: python -m sgc_python_sdk.test_sdk
Or: PYTHONPATH=/path/to/web python sgc_python_sdk/test_sdk.py

Set env SGC_API_BASE to your API base (default: http://localhost/web).
Set SGC_USER, SGC_PASS, SGC_APIKEY for real API calls.
Set SGC_DEBUG=1 to print full API URL and parameters (apikey/password masked) for each request.
If Send SMS returns 404, set SGC_USE_INDEX_PHP=1 to use index.php?url=... (avoids rewrite issues).

To test sending SMS, set:
  SGC_SMS_PHONE   - recipient number (e.g. 919876543210)
  SGC_SMS_TEXT    - message text (default: "Test from SGC Python SDK")
  SGC_SMS_SENDER  - your sender ID (use one from SenderId Read; e.g. SMSGAT)
  SGC_SMS_TEST    - set to "true" for test mode (no real delivery, if API supports it)
"""

import os
import sys

# Ensure package is importable when run as script
_web_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _web_root not in sys.path:
    sys.path.insert(0, _web_root)

from sgc_python_sdk import (
    sgc_auth,
    sgc_user,
    sgc_sms,
    sgc_account,
    sgc_apikey,
    sgc_senderid,
    sgc_sms_send,
    sgc_schedule,
)


def main():
    base = os.environ.get("SGC_API_BASE", "https://unify.smsgateway.center")
    username = os.environ.get("SGC_USER", "test")
    password = os.environ.get("SGC_PASS", "********")
    apikey = os.environ.get("SGC_APIKEY", "")

    print("SGC Python SDK test")
    print("  SGC_API_BASE:", base)
    print("  user:", username)
    print()

    auth = sgc_auth()
    auth.setUsername(username)
    auth.setPassword(password)
    auth.setApiKey(apikey)

    user = sgc_user("json")

    # 1) Account – read status
    print("1) Account ReadAccountStatus:")
    acc = sgc_account(auth, user)
    try:
        resp = acc.ReadAccountStatus()
        print("   Response:", resp[:200] if resp and len(resp) > 200 else resp)
        print("   Type: ", type(resp))
    except Exception as e:
        print("   Error:", e)
    print()

    # 2) Account – read profile
    print("2) Account ReadProfile:")
    try:
        resp = acc.ReadProfile()
        print("   Response:", resp[:200] if resp and len(resp) > 200 else resp)
    except Exception as e:
        print("   Error:", e)
    print()

    # 3) SenderId – read (list)
    print("3) SenderId Read:")
    sid = sgc_senderid(auth, user)
    try:
        resp = sid.Read()
        print("   Response:", resp[:200] if resp and len(resp) > 200 else resp)
    except Exception as e:
        print("   Error:", e)
    print()

    # 4) Schedule – read (no dates needed for list)
    print("4) Schedule Read:")
    sms_obj = sgc_sms("json")
    sched = sgc_schedule(auth, sms_obj)
    try:
        resp = sched.Read()
        print("   Response:", resp[:200] if resp and len(resp) > 200 else resp)
    except Exception as e:
        print("   Error:", e)
    print()

    # 5) Send SMS (batch) – only if SGC_SMS_PHONE and SGC_SMS_SENDER are set
    sms_phone = os.environ.get("SGC_SMS_PHONE", "").strip()
    sms_sender = os.environ.get("SGC_SMS_SENDER", "").strip()
    if sms_phone and sms_sender:
        print("5) Send SMS (batch):")
        sms_text = os.environ.get("SGC_SMS_TEXT", "Test from SGC Python SDK")
        test_mode = os.environ.get("SGC_SMS_TEST", "").strip().lower()
        send_sms = sgc_sms("json")
        send_sms.setSenderId(sms_sender)
        send_sms.setText(sms_text)
        send_sms.setSendMethod("quick")
        send_sms.setPhone(sms_phone)
        send_sms.setMsgType("text")
        send_sms.setDuplicateCheck("true")
        send_sms.setTestMessage("true" if test_mode == "true" else "false")
        sender = sgc_sms_send(auth, send_sms)
        try:
            resp = sender.batch()
            full_url = sender.getLastRequestUrl()
            if full_url:
                print("   URL:", full_url)
            status = sender.getLastStatusCode()
            if status:
                print("   HTTP status:", status)
            if resp is None or (isinstance(resp, str) and not resp.strip()):
                print("   Response: (empty)")
            else:
                print("   Response:", resp[:500] if len(resp) > 500 else resp)
        except Exception as e:
            print("   Error:", e)
        print()
    else:
        print("5) Send SMS: skipped (set SGC_SMS_PHONE and SGC_SMS_SENDER to test send).")
        print()

    print("Done. Set SGC_USER, SGC_PASS, SGC_APIKEY and ensure API is up for real calls.")


if __name__ == "__main__":
    main()
