"""git_mgr module."""

from xcicd.github.api_mgr import ApiMgr
from xcicd.github.curl_mgr import CurlMgr
from xcicd.linux.scall import execute_cmd

class GitMgr:
    """Manage git actions operation."""

    def __init__(self, _repo: str, _current_branch: str, _token: str) -> None:
        """Initialize git manager object."""
        self.repo_ = _repo
        self.cbranch_ = _current_branch
        self.token_ = _token

    def remove(self) -> None:
        """Remove current branch."""
        # create api delete method 
        delete_api_method = ApiMgr.create_delete_api_method(self.repo_, self.cbranch_)
        # create curl command 
        curl_cmd = CurlMgr.create_curl_cmd_with_token("DELETE", self.token_, delete_api_method)
        try:
            execute_cmd(curl_cmd)
        except Exception as e:
            raise RuntimeError(f"Failed to remove branch {self.cbranch_}")
