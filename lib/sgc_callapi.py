# -*- coding: utf-8 -*-
"""
HTTP client for SGC API. Mirrors PHP sgc_callapi.
Uses configurable base URL (local); no remote fetch.
Set SGC_DEBUG=1 or SGC_DEBUG=true to print full endpoint URL and parameters (sensitive values masked).
"""

import logging
import os
from typing import Any, Dict, List, Union

import requests

from sgc_python_sdk.config.common.sgc_constant import SERVER_HOST
from sgc_python_sdk.config.common.sgc_common_api_params import (
    API_COMMON_METHOD_GET,
    API_COMMON_METHOD_POST,
    API_COMMON_METHOD_FILE,
)

logger = logging.getLogger(__name__)

# Keys whose values are masked in debug output
_DEBUG_MASK_KEYS = frozenset({"apikey", "password", "adminkey"})


def _debug_print_request(
    method: str,
    url: str,
    data: Union[Dict[str, Any], List[tuple]],
    header: Dict[str, str],
    is_get: bool,
) -> None:
    """
    Print full API endpoint and parameters for debugging when SGC_DEBUG is set.
    Masks apikey, password, adminkey values.
    """
    debug_val = os.environ.get("SGC_DEBUG", "").strip().lower()
    if debug_val not in ("1", "true", "yes"):
        return
    payload = dict(data) if isinstance(data, dict) else dict(list(data))
    masked_params = {
        k: ("****" if (v and str(k).lower() in _DEBUG_MASK_KEYS) else v)
        for k, v in payload.items()
    }
    masked_headers = {
        k: ("****" if (v and str(k).lower() in _DEBUG_MASK_KEYS) else v)
        for k, v in (header or {}).items()
    }
    print("[SGC_DEBUG] === API request ===")
    print("[SGC_DEBUG] Method:", method)
    print("[SGC_DEBUG] URL:", url)
    print("[SGC_DEBUG] Headers:", masked_headers)
    if is_get:
        print("[SGC_DEBUG] Query params:", masked_params)
    else:
        print("[SGC_DEBUG] Body params:", masked_params)
    print("[SGC_DEBUG] ==================")


class sgc_callapi:
    """
    Performs HTTP request to SGC API (local base URL from SGC_API_BASE env).
    Mirrors PHP SMSGatewayCenterPhpSdk\\lib\\sgc_callapi.
    """

    def __init__(
        self,
        api: str,
        endpoint: str,
        data: Union[Dict[str, Any], List[tuple]],
        header: Dict[str, str],
        method: str = API_COMMON_METHOD_POST,
        rest_api: bool = False,
    ) -> None:
        """
        Execute request to SERVER_HOST + api + endpoint.
        SERVER_HOST is from env SGC_API_BASE (local API).
        If SGC_USE_INDEX_PHP=1, URL is base/index.php?url=SMSApi/... (avoids rewrite 404 on some servers).
        """
        self._response = None
        self._status_code = 0
        self._request_url = ""
        base = (SERVER_HOST or "").rstrip("/")
        use_index_php = os.environ.get("SGC_USE_INDEX_PHP", "").strip().lower() in ("1", "true", "yes")
        if use_index_php:
            # Explicit index.php?url= form so routing works when rewrite fails (e.g. /send/batch 404)
            url_path = (api.strip("/") + endpoint) if endpoint.startswith("/") else (api.strip("/") + "/" + endpoint)
            url = "{}?url={}".format(base + "/index.php", url_path)
        else:
            url = base + api + endpoint
        self._request_url = url
        payload = data if isinstance(data, dict) else dict(data)
        _debug_print_request(
            method, url, payload, header or {}, method == API_COMMON_METHOD_GET
        )
        try:
            if method == API_COMMON_METHOD_POST:
                resp = requests.post(
                    url,
                    data=data if isinstance(data, dict) else dict(data),
                    headers=header,
                    timeout=30,
                )
                self._status_code = resp.status_code
                self._response = resp.text
            elif method == API_COMMON_METHOD_GET:
                resp = requests.get(
                    url,
                    params=data if isinstance(data, dict) else dict(data),
                    headers=header,
                    timeout=30,
                )
                self._status_code = resp.status_code
                self._response = resp.text
            elif method == API_COMMON_METHOD_FILE:
                resp = requests.post(
                    url,
                    files=data if isinstance(data, list) else [],
                    headers=header,
                    timeout=60,
                )
                self._status_code = resp.status_code
                self._response = resp.text
            else:
                resp = requests.post(url, data=data, headers=header, timeout=30)
                self._status_code = resp.status_code
                self._response = resp.text
        except requests.RequestException as exc:
            logger.exception("SGC API request failed: %s", exc)
            self._status_code = 500
            self._response = str(exc) if str(exc) else "Request failed"
        except Exception as exc:
            logger.exception("Unexpected error: %s", exc)
            self._status_code = 500
            self._response = str(exc) if str(exc) else "Request failed"

    def getResponse(self) -> Any:
        """Return response body. Mirrors PHP getResponse()."""
        return self._response

    def getRequestUrl(self) -> str:
        """Return the full URL that was used for this request (for debugging)."""
        return self._request_url or ""

    def getStatusCode(self) -> int:
        """Return HTTP status code. Mirrors PHP getStatusCode()."""
        return self._status_code

    def setResponse(self, response: Any) -> None:
        """Set response. Mirrors PHP setResponse()."""
        self._response = response

    def setStatusCode(self, status_code: int) -> None:
        """Set status code. Mirrors PHP setStatusCode()."""
        self._status_code = status_code
