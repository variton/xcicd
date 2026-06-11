import pytest

from xcicd.bscanner import main

def test_valid_branch_is_accepted():
    main([
        "xcicd-bscanner",
        "ABC",
        "repository",
        "ABC-123-DEV-DESC",
        "commit message",
    ])


def test_invalid_branch_name_is_rejected():
    with pytest.raises(RuntimeError, match="Invalid branch name format: ABC"):
        main([
            "xcicd-bscanner",
            "ABC",
            "repository",
            "ABC",
            "commit message",
        ])


def test_project_id_is_rejected():
    with pytest.raises(RuntimeError, match="Invalid branch name : ABC-123-DEV-DESC -> The project name should be XYZ"):
        main([
            "xcicd-bscanner",
            "XYZ",
            "repository",
            "ABC-123-DEV-DESC",
            "commit message",
        ])

def test_project_name_format_is_rejected():
    with pytest.raises(RuntimeError, match="Invalid branch name : AB-123-DEV-DESC -> The project name should have 3 characters example: XYZ"):
        main([
            "xcicd-bscanner",
            "AB",
            "repository",
            "AB-123-DEV-DESC",
            "commit message",
        ])

def test_id_branch_is_rejected():
    with pytest.raises(RuntimeError, match="Invalid branch name : ABC-XXX-DEV-DESC -> The id XXX used for the branch should be a digit"):
        main([
            "xcicd-bscanner",
            "ABC",
            "repository",
            "ABC-XXX-DEV-DESC",
            "commit message",
        ])

def test_task_is_rejected():
    with pytest.raises(RuntimeError, match="Invalid branch name : ABC-1-OBB-DESC -> The task OBB should be among the following DEV, DOC, INIT, TEST, UPE, FIX"):
        main([
            "xcicd-bscanner",
            "ABC",
            "repository",
            "ABC-1-OBB-DESC",
            "commit message",
        ])

def test_description_branch_is_rejected():
    with pytest.raises(RuntimeError, match="Invalid branch name : ABC-123-DEV-OBLIVION -> The description OBLIVION should not be longuer than 6 chars"):
        main([
            "xcicd-bscanner",
            "ABC",
            "repository",
            "ABC-123-DEV-OBLIVION",
            "commit message",
        ])
