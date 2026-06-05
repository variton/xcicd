import pytest

from xcicd.artifact.branch import Branch


@pytest.mark.parametrize("branch_name, project_id", [
    ("ABC-123-DEV-DESC", "ABC"),
    ("XYZ-001-DOC-README", "XYZ"),
    ("PRJ-999-TEST-ABC", "PRJ"),
    ("APP-42-INIT-BUG", "APP"),
    ("APP-42-FIX-BUG", "APP"),
])
def test_valid_branch_names(branch_name, project_id):
    branch = Branch(branch_name)

    assert branch.is_valid(project_id) is True


@pytest.mark.parametrize("branch_name, project_id", [
    ("ABC-123-DEV-DESC", "XYZ"),      # project mismatch
    ("AB-123-DEV-DESC", "AB"),        # project too short
    ("ABCD-123-DEV-DESC", "ABCD"),    # project too long
    ("abc-123-DEV-DESC", "abc"),      # project lowercase
    ("ABC-ID-DEV-DESC", "ABC"),       # id not numeric
    ("ABC-123-dev-DESC", "ABC"),      # task lowercase
    ("ABC-123-BAD-DESC", "ABC"),      # task not allowed
    ("ABC-123-ABCDE-DESC", "ABC"),    # task longer than 4
    ("ABC-123-DEV-TOOLONG", "ABC"),   # description longer than 6
    ("ABC-123-DEV-desc", "ABC"),      # description lowercase
])
def test_invalid_branch_names(branch_name, project_id):
    branch = Branch(branch_name)

    assert branch.is_valid(project_id) is False


@pytest.mark.parametrize("branch_name", [
    "ABC-123-DEV",
    "ABC-123-DEV-DESC-EXTRA",
    "ABC",
    "",
])
def test_invalid_branch_format_raises_value_error(branch_name):
    with pytest.raises(ValueError, match="Invalid branch name format"):
        Branch(branch_name)


def test_getters():
    branch = Branch("ABC-123-DEV-DESC")

    assert branch.get_project() == "ABC"
    assert branch.get_id() == "123"
    assert branch.get_task() == "DEV"
