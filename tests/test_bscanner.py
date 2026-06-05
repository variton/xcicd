import pytest

from xcicd.bscanner import main


def test_valid_branch_is_accepted():
    main([
        "xcicd-bscanner",
        "ABC",
        "ABC-123-DEV-DESC",
        "commit message",
    ])


def test_invalid_branch_is_rejected():
    with pytest.raises(RuntimeError, match="invalid branch name"):
        main([
            "xcicd-bscanner",
            "ABC",
            "ABC-ID-DEV-DESC",
            "commit message",
        ])


def test_project_mismatch_is_rejected():
    with pytest.raises(RuntimeError, match="invalid branch name"):
        main([
            "xcicd-bscanner",
            "XYZ",
            "ABC-123-DEV-DESC",
            "commit message",
        ])


def test_malformed_branch_is_rejected():
    with pytest.raises(ValueError, match="Invalid branch name format"):
        main([
            "xcicd-bscanner",
            "ABC",
            "invalid-branch",
            "commit message",
        ])
