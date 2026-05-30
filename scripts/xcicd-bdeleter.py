
import sys

from xcicd.github.git_mgr import GitMgr

def main(args:list[str]) -> None:
    repo = args[1]
    current_branch = args[2]
    token = args[3]
    
    try:
        git_mgr = GitMgr(repo,token)
        git_mgr.remove_branch(current_branch)
    except Exception as e:
        print(e)
       
if __name__ == "__main__":
    
    if len(sys.argv) < 4:
        raise("missing arguments: \n branchdeleter \
              REPO CURRENT_BRANCH TOKEN")

    main(sys.argv)
