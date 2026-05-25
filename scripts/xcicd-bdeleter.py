
import sys

from xcicd.github.git_mgr import GitMgr

def main(args:list[str]) -> None:
    repo = args[1]
    branch = args[2]
    token = args[3]
    
    try:
        git_mgr = GitMgr(repo,branch,toke)
        git_mgr.remove()
    except Exception as e:
        print(e)
       
if __name__ == "__main__":
    
    if len(sys.argv) < 4:
        raise("missing arguments: \n branchdeleter \
              REPO CURRENT_BRANCH TOKEN")

    main(sys.argv)
