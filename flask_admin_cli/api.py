# flask_admin_cli/api.py
"""
Main API

This file has the main functions

"""
from pathlib import Path
from flask_admin_cli import exceptions
import os
import subprocess

MAIN_REPO = "https://github.com/mariofix/flask-admin-cli.git"
BRANCHES_NOT_ALLOWED = ["main", "gh-pages"]
BRANCH_PREFIX = "app"
BASE_DIR = Path(__file__).resolve().parent.parent


def cross_check(dest_dir: str, branch: str) -> None:
    """Pre-flight checks

    Verifies the environment

    Args:
        dest_dir (str): directory name inside the project.
        branch (str): remote branch to clone.
    Raises:
        InvalidParamsException: some of the parameters are invalid
        FileExistsError: the `dest_dir` directory already exists
        InvalidBranchException
    """

    if not dest_dir or not branch:
        raise exceptions.InvalidParamsException(f"{dest_dir} or {branch} are None.")
    # new directory
    new_dir = os.path.join(BASE_DIR, dest_dir)

    if os.path.isdir(new_dir):
        raise FileExistsError(f"The directory {new_dir} already exists.")

    # branch allowed
    if branch in BRANCHES_NOT_ALLOWED:
        raise exceptions.InvalidBranchException(f"`{branch}` is not allowed.")
    # branch prefix
    if not branch.startswith(BRANCH_PREFIX):
        raise exceptions.InvalidBranchException(
            f"`{branch}` must start with `{BRANCH_PREFIX}`."
        )
    # branch exists
    status = subprocess.run(
        ["git", "ls-remote", "--exit-code", "--heads", MAIN_REPO, branch],
        check=True,
        capture_output=False,
        stdout=subprocess.DEVNULL,
    )
    if status.returncode == 2:
        raise exceptions.RemoteBranchNotFoundException(
            f"The remote branch {branch} does not exist."
        )


async def clone_repo(branch: str = None, dest_dir: str = None) -> True:
    try:
        cross_check(dest_dir, branch)
    except Exception as e:
        raise exceptions.NotReadyException(e)
    else:
        new_dir = os.path.join(BASE_DIR, dest_dir)
        print(
            "subprocess.run(git clone {} -b {} {})".format(MAIN_REPO, branch, new_dir)
        )
        clone = subprocess.run(
            ["git", "clone", MAIN_REPO, "-b", branch, new_dir],
            check=True,
        )
        subprocess.run(["rm", "-rf", f"{new_dir}/.git"])
        return True
