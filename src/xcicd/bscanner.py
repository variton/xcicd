
from xcicd.artifact.branch import Branch

def main(args: list[str]) -> None:
    current_branch_name = args[1]
    last_commit_message = args[2]

    branch = Branch(current_branch_name)

    if not branch.is_valid():
        raise RuntimeError(
            f"invalid branch name : {current_branch_name}"
        )
