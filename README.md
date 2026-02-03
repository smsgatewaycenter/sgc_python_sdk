# SGC Python SDK

Python client for the **SGC (SMS Gateway Center) API**. Send SMS, manage account, sender IDs, schedules, contacts, groups, and more. Works with [Unify SMS Gateway Center](https://unify.smsgateway.center).

**Requirements:** Python 3.7+, `requests>=2.28.0`

---

## Prerequisites: Get Your API Credentials

You must have a registered account and API credentials from **Unify SMS Gateway Center** before using this SDK.

1. **Register or log in** at **[https://unify.smsgateway.center](https://unify.smsgateway.center)**.
2. After login, get your **API credentials** from your account/settings (username, password, and **API key**).
3. Create or use an existing **Sender ID** for sending SMS (required for the send API).

Without valid credentials from Unify, all API calls will return authentication errors (e.g. invalid credentials).

---

## Installation

### From PyPI

```bash
pip install sgc-python-sdk
```

### From GitHub

```bash
pip install git+https://github.com/YOUR_USERNAME/sgc-python-sdk.git
```

Replace `YOUR_USERNAME` with the actual GitHub username or organization.

### Local / development

```bash
cd /path/to/parent-of-sgc_python_sdk
pip install -r sgc_python_sdk/requirements.txt
```

To use the package from your code, set `PYTHONPATH` to the parent directory of `sgc_python_sdk`:

```bash
export PYTHONPATH=/path/to/parent-of-sgc_python_sdk
python -c "from sgc_python_sdk import sgc_auth, sgc_account; print('OK')"
```

---

## Configuration

Set these environment variables with your **Unify** credentials:

| Variable       | Required | Description |
|----------------|----------|-------------|
| `SGC_API_BASE` | No       | API base URL. Default: `https://unify.smsgateway.center` |
| `SGC_USER`     | Yes      | Your Unify username |
| `SGC_PASS`     | Yes      | Your Unify password |
| `SGC_APIKEY`   | Yes      | Your API key from Unify |

Optional (for sending SMS and debugging):

| Variable           | Description |
|--------------------|-------------|
| `SGC_SMS_PHONE`    | Recipient number for the test script (e.g. `919876543210`) |
| `SGC_SMS_SENDER`   | Your Sender ID for the test script (e.g. `SMSGAT`) |
| `SGC_SMS_TEXT`     | Message text (default: `Test from SGC Python SDK`) |
| `SGC_SMS_TEST`     | Set to `true` for test mode (no real delivery when supported) |
| `SGC_DEBUG`        | Set to `1` to print full request URL and parameters (sensitive values masked) |
| `SGC_USE_INDEX_PHP`| Set to `1` if Send SMS returns 404 (uses `index.php?url=...` style URL) |

---

## How to Test

After installing and setting your credentials, run the included test script to verify account, profile, sender IDs, schedule, and (optionally) send SMS.

1. **Set your Unify credentials and API base:**

   ```bash
   export SGC_API_BASE="https://unify.smsgateway.center"
   export SGC_USER="your_unify_username"
   export SGC_PASS="your_unify_password"
   export SGC_APIKEY="your_api_key_from_unify"
   ```

2. **Run the test script:**

   - **If you installed via pip (PyPI or GitHub):**
     ```bash
     python -m sgc_python_sdk.test_sdk
     ```
     Or from the repo root:
     ```bash
     python sgc_python_sdk/test_sdk.py
     ```
   - **If using locally with PYTHONPATH:**
     ```bash
     export PYTHONPATH=/path/to/parent-of-sgc_python_sdk
     python sgc_python_sdk/test_sdk.py
     ```

3. **What the test does:**
   - **1) Account ReadAccountStatus** – checks your account status.
   - **2) Account ReadProfile** – fetches your profile.
   - **3) SenderId Read** – lists your sender IDs.
   - **4) Schedule Read** – lists scheduled messages.
   - **5) Send SMS (batch)** – only runs if you set `SGC_SMS_PHONE` and `SGC_SMS_SENDER` (see below).

4. **To test sending an SMS**, set the recipient and a valid Sender ID from your account:

   ```bash
   export SGC_SMS_PHONE="919876543210"
   export SGC_SMS_SENDER="YourSenderId"
   python sgc_python_sdk/test_sdk.py
   ```

   Use `SGC_SMS_TEST=true` for test mode (no real delivery when the API supports it). Use `SGC_DEBUG=1` to see the full request URL and parameters.

If you see **invalid credentials (216)**, double-check your username, password, and API key from [Unify SMS Gateway Center](https://unify.smsgateway.center).

---

## Quick Start: Use in Your Code

```python
from sgc_python_sdk import sgc_auth, sgc_user, sgc_account, sgc_senderid, sgc_sms, sgc_sms_send

# Use your Unify credentials
auth = sgc_auth()
auth.setUsername("your_unify_username")
auth.setPassword("your_unify_password")
auth.setApiKey("your_api_key_from_unify")

# Account status
user = sgc_user("json")
acc = sgc_account(auth, user)
print(acc.ReadAccountStatus())

# Send SMS (batch)
sms = sgc_sms("json")
sms.setSenderId("YourSenderId")   # Must exist in your Unify account
sms.setText("Hello from SDK")
sms.setPhone("919876543210")
sms.setMsgType("text")
sms.setTestMessage("false")       # "true" for test mode
sms.setDuplicateCheck("true")
sender = sgc_sms_send(auth, sms)
print(sender.batch())
```

You can also use environment variables and leave credentials out of code:

```python
import os
from sgc_python_sdk import sgc_auth, sgc_user, sgc_account

auth = sgc_auth()
auth.setUsername(os.environ.get("SGC_USER", ""))
auth.setPassword(os.environ.get("SGC_PASS", ""))
auth.setApiKey(os.environ.get("SGC_APIKEY", ""))

user = sgc_user("json")
acc = sgc_account(auth, user)
print(acc.ReadAccountStatus())
```

---

## API Overview

| Area        | Class / module           | Main actions |
|------------|---------------------------|--------------|
| Account    | `sgc_account`             | ReadAccountStatus, ReadProfile, etc. |
| Sender ID  | `sgc_senderid`            | Read, Create, Update, Delete |
| Schedule   | `sgc_schedule`            | Read, Update, Delete |
| Send SMS   | `sgc_sms_send`            | `batch()`, `phonebook()`, `file()` |
| API Key    | `sgc_apikey`              | Create, Read, Update, Delete |
| Contact    | `sgc_contact`             | CRUD |
| Group      | `sgc_group`               | CRUD |
| Password   | `sgc_password`            | Change |
| Reseller   | `sgc_reseller_user_api`, `sgc_credit_management` | User and credit management |

Boolean parameters such as `testMessage` and `duplicateCheck` must be `"true"` or `"false"`; the SDK normalizes them for you.

---

## Troubleshooting

- **Invalid credentials (216)**  
  Ensure you are using the correct username, password, and API key from [https://unify.smsgateway.center](https://unify.smsgateway.center).

- **Send SMS returns 404**  
  Set `SGC_USE_INDEX_PHP=1` so the client uses the `index.php?url=...` style URL.

- **Parameter testMessage / duplicateCheck error (147)**  
  The SDK sends `"true"` or `"false"` automatically; ensure you are on a recent SDK version.

- **See exact request URL and parameters**  
  Set `SGC_DEBUG=1` and run your script again; the full URL and body params will be printed (sensitive values masked).

---
