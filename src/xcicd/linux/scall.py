"""scall module."""
import os

def execute_cmd(cmd:str) -> None:
    """Execute cmd."""

    if os.system(cmd) != 0:
        raise RuntimeError(f"Failed to execute {cmd}")
