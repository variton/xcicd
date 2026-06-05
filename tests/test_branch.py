import pytest

from xcicd.artifact.branch import Branch


@pytest.mark.parametrize("branch_name", [
    "ABC-123-DEV-DESC",
    "XYZ-001-DOC-README",
    "PRJ-999-TEST-ABC",
    "APP-42-INIT-BUG",
    "APP-42-FIX-BUG",
])
def test_valid_branch_names(branch_name):
    branch = Branch(branch_name)

    assert branch.is_valid() is True


@pytest.mark.parametrize("branch_name", [
    "AB-123-DEV-DESC",        # project too short
    "ABCD-123-DEV-DESC",      # project too long
    "abc-123-DEV-DESC",       # project lowercase
    "ABC-ID-DEV-DESC",        # id not numeric
    "ABC-123-dev-DESC",       # task lowercase
    "ABC-123-BAD-DESC",       # task not in BTASKS
    "ABC-123-TOOLONG-DESC",   # task longer than 4
    "ABC-123-DEV-TOOLONG",    # description longer than 6
    "ABC-123-DEV-desc",       # description lowercase
])
def test_invalid_branch_names(branch_name):
    branch = Branch(branch_name)

    assert branch.is_valid() is False


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
