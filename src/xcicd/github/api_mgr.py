"""api_mgr module."""

class ApiMgr:
    """ApiMgr class."""
    
    root_path_ = "https://api.github.com/repos/" 

    @staticmethod
    def create_pull_api_method(_repo:str,_pull_request_id:int) -> str:
        """create pull api method."""
        return f"{ApiMgr.root_path_}{_repo}/pulls/{_pull_request_id}"

    @staticmethod
    def create_delete_api_method(_repo:str,_branch:str) -> str:
        """create pull api method."""
        return f"{ApiMgr.root_path_}{_repo}/git/{_branch}"
