
from xcicd.artifact.branch import Branch

def main(args: list[str]) -> None:
    project_id = args[1]
    repository = args[2] 
    current_branch_name = args[3]
    last_commit_message = args[4]

    print(project_id)
    print(repository)
    print(current_branch_name)
    print(last_commit_message)

    branch = Branch(current_branch_name)

    if not branch.is_valid(project_id):
        raise RuntimeError(
            f"invalid branch name : {current_branch_name}"
        )
