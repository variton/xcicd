import pytest

from xcicd.linux.scall import execute_cmd


def test_execute_cmd_success(mocker):
    mock_system = mocker.patch("xcicd.linux.scall.os.system", return_value=0)

    execute_cmd("echo hello")

    mock_system.assert_called_once_with("echo hello")


def test_execute_cmd_failure(mocker):
    mock_system = mocker.patch("xcicd.linux.scall.os.system", return_value=1)

    with pytest.raises(RuntimeError, match="Failed to execute echo hello"):
        execute_cmd("echo hello")

    mock_system.assert_called_once_with("echo hello")
