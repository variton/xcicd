
import sys

from xcicd.artifact.branch import Branch

def main(args:list[str]) -> None:
    current_branch_name = args[1]
    last_commit_message = args[2]

    branch = Branch(current_branch_name)
    if branch.is_valid() == False:
        raise RuntimeError("invalid branch name : "+current_branch_name)
       
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        raise RuntimeError("missing arguments: \n xcicd-bscanner \
                           CURRENT_BRANCH_NAME LAST_COMMIT")
    try:
        main(sys.argv)
    except Exception as e:
        raise RuntimeError(e.message)
