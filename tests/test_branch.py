import pytest

from xcicd.artifact.branch import Branch


def test_branch_parses_valid_name():
    branch = Branch("ABC-123-DEV-FOO")

    assert branch.get_project() == "ABC"
    assert branch.get_id() == "123"
    assert branch.get_task() == "DEV"


def test_valid_branch_passes_validation():
    branch = Branch("ABC-123-DEV-FOO")

    branch.is_valid("ABC")


@pytest.mark.parametrize(
    "branch_name",
    [
        "ABC-123-DEV",              # missing description
        "ABC-123-DEV-FOO-EXTRA",    # too many parts
        "ABC123DEVFOO",             # no separators
    ],
)
def test_invalid_branch_format_raises_value_error(branch_name):
    with pytest.raises(ValueError, match="Invalid branch name format"):
        Branch(branch_name)


def test_invalid_project_id_raises_value_error():
    branch = Branch("ABC-123-DEV-FOO")

    with pytest.raises(ValueError, match="The project name should be XYZ"):
        branch.is_valid("XYZ")


@pytest.mark.parametrize(
    "branch_name",
    [
        "AB-123-DEV-FOO",       # too short
        "ABCD-123-DEV-FOO",     # too long
        "abc-123-DEV-FOO",      # lowercase
    ],
)
def test_invalid_project_format_raises_value_error(branch_name):
    branch = Branch(branch_name)

    with pytest.raises(ValueError, match="project name should have"):
        branch.is_valid(branch.get_project())


@pytest.mark.parametrize(
    "branch_name",
    [
        "ABC-abc-DEV-FOO",
        "ABC-12A-DEV-FOO",
        "ABC--DEV-FOO",
    ],
)
def test_invalid_id_raises_value_error(branch_name):
    branch = Branch(branch_name)

    with pytest.raises(ValueError, match="should be a digit"):
        branch.is_valid("ABC")


@pytest.mark.parametrize(
    "branch_name",
    [
        "ABC-123-BAD-FOO",
        "ABC-123-dev-FOO",
        "ABC-123--FOO",
    ],
)
def test_invalid_task_raises_value_error(branch_name):
    branch = Branch(branch_name)

    with pytest.raises(ValueError, match="should be among"):
        branch.is_valid("ABC")


@pytest.mark.parametrize(
    "branch_name",
    [
        "ABC-123-DEV-TOOLONG",
        "ABC-123-DEV-foo",
        "ABC-123-DEV-Foo",
    ],
)
def test_invalid_description_raises_value_error(branch_name):
    branch = Branch(branch_name)

    with pytest.raises(ValueError, match="description"):
        branch.is_valid("ABC")
