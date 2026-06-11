"""branch.py module."""

BTASKS = ["DEV","DOC","INIT","TEST","UPE","FIX"]

class Branch:
    """Branch class."""

    def __init__(self, name:str) -> None:
        
        if name.count('-') != 3:
            raise ValueError(
                f"Invalid branch name format: {name}"
            )

        self.project_,self.id_,self.task_,self.description_ = name.split('-')

    def is_valid(self,project_id:str) -> None:
        if self.project_ != project_id:
            raise ValueError(
                f"The project name should be {project_id}"
            )

        if len(self.project_) != 3 or not self.project_.isupper():
            raise ValueError(
                f"The project name should have 3 characters example: XYZ"
            )

        if not self.id_.isdigit():
            raise ValueError(
                f"The id {self.id_} used for the branch should be a digit"
            )

        if self.task_.isupper() != True or self.task_ not in BTASKS:
            raise ValueError(
                f"The task {self.task_} should be among the following {', '.join(BTASKS)}"
            )

        if len(self.description_) > 6 or self.description_.isupper() != True:
            raise ValueError(
                f"The description {self.description_} should not be longuer than 6 chars"
            )

    def get_project(self) -> str:
        return self.project_

    def get_id(self) -> str:
        return self.id_

    def get_task(self) -> str:
        return self.task_
