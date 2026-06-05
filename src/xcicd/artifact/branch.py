"""branch.py module."""

BTASKS = ["DEV","DOC","INIT","TEST","UPE","FIX"]

class Branch:
    """Branch class."""

    def __init__(self, name:str) -> None:

        try:
            self.project_,self.id_,self.task_,self.description_ = name.split('-')
        except ValueError:
            raise ValueError(
                f"Invalid branch name format: {name}"
            )

    def is_valid(self) -> bool:
        if len(self.project_) != 3 or self.project_.isupper() != True:
            return False 

        if self.id_.isdigit() != True:
            return False

        if len(self.task_) > 4 or self.task_.isupper() != True or self.task_ not in BTASKS:
            return False

        if len(self.description_) > 6 or self.description_.isupper() != True:
            return False
        return True

    def get_project(self) -> str:
        return self.project_

    def get_id(self) -> str:
        return self.id_

    def get_task(self) -> str:
        return self.task_
