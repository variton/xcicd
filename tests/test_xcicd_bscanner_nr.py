import importlib.util
from pathlib import Path

import pytest


script_path = (
    Path(__file__).parent.parent
    / "scripts"
    / "xcicd-bscanner.py"
)

spec = importlib.util.spec_from_file_location("bscanner", script_path)
bscanner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bscanner)


def test_bscanner_accepts_test_task_branch():
    bscanner.main([
        "xcicd-bscanner",
        "PRJ-999-TEST-ABC",
        "commit message",
    ])


def test_bscanner_accepts_init_task_branch():
    bscanner.main([
        "xcicd-bscanner",
        "PRJ-999-INIT-ABC",
        "commit message",
    ])


def test_bscanner_rejects_invalid_branch_name():
    with pytest.raises(RuntimeError, match="invalid branch name"):
        bscanner.main([
            "xcicd-bscanner",
            "BAD-ABC-DEV-DESC",
            "commit message",
        ])


def test_bscanner_rejects_malformed_branch_name():
    with pytest.raises(ValueError, match="Invalid branch name format"):
        bscanner.main([
            "xcicd-bscanner",
            "invalid-branch",
            "commit message",
        ])
