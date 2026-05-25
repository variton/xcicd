"""curl_mgr module."""

class CurlMgr:
    """CurlMgr class."""
    
    op1 = "Accept: application/vnd.github+json"
    op2 = "Authorization: Bearer "
    op3 = "X-GitHub-Api-Version: 2022-11-28"
        
    @staticmethod
    def create_curl_cmd_with_token(http_method:str,
                                   token:str,
                                   api_method:str) -> str:
        curl_cmd = (f"curl -L -X {http_method} "
                    + f'-H "{CurlMgr.op1}" -H "{CurlMgr.op2}{token}" -H "{CurlMgr.op3}"'
                    + " "
                    + api_method)

        return curl_cmd
