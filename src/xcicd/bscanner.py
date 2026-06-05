
from xcicd.artifact.branch import Branch

def main(args: list[str]) -> None:
    project_id = args[1]
    current_branch_name = args[2]
    last_commit_message = args[3]

    branch = Branch(current_branch_name)

    if not branch.is_valid(project_id):
        raise RuntimeError(
            f"invalid branch name : {current_branch_name}"
        )
