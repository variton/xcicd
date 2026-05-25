""" test_api_mgr module."""

import pytest

from xcicd.github.curl_mgr import CurlMgr

def test_create_curl_cmd_with_token_():
    curl_cmd= CurlMgr.create_curl_cmd_with_token("GET", "token", "https://api.github.com/repos/alpha/test/pulls/1")

    result = "curl -L -X GET -H \"Accept: application/vnd.github+json\" -H \"Authorization: Bearer token\" -H \"X-GitHub-Api-Version: 2022-11-28\" https://api.github.com/repos/alpha/test/pulls/1"
    assert result == curl_cmd 
