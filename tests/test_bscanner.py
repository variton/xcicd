
import pytest

from xcicd.bscanner import main


def test_valid_branch_is_accepted():
    main([
        "xcicd-bscanner",
        "ABC-123-DEV-DESC",
        "commit message",
    ])


def test_invalid_branch_is_rejected():
    with pytest.raises(RuntimeError, match="invalid branch name"):
        main([
            "xcicd-bscanner",
            "ABC-ID-DEV-DESC",
            "commit message",
        ])


def test_malformed_branch_is_rejected():
    with pytest.raises(ValueError, match="Invalid branch name format"):
        main([
            "xcicd-bscanner",
            "invalid-branch",
            "commit message",
        ])
