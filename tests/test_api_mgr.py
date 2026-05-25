""" test_api_mgr module."""

import pytest

from xcicd.github.api_mgr import ApiMgr

def test_create_pull_api_method():
    pull_api_method = ApiMgr.create_pull_api_method("alpha/test", 1)

    result = "https://api.github.com/repos/alpha/test/pulls/1"
    assert result == pull_api_method 

def test_delete_api_method():
    delete_api_method = ApiMgr.create_delete_api_method("alpha/test", "XCI-2-DOC-GTB")

    result = "https://api.github.com/repos/alpha/test/git/XCI-2-DOC-GTB"
    assert result == delete_api_method 
