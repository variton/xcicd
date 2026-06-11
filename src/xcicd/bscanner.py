
from xcicd.artifact.branch import Branch

def main(args: list[str]) -> None:
    project_id = args[1]
    repository = args[2] 
    current_branch_name = args[3]
    last_commit_message = args[4]

    if current_branch_name == "main" or current_branch_name == "master":
        return

    try:
        branch = Branch(current_branch_name)
        branch.is_valid(project_id)
    except ValueError as e:
        raise RuntimeError(
            f"Invalid branch name : {current_branch_name} -> {str(e)}"
        )
