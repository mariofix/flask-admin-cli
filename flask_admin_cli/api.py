# flask_admin_cli/api.py
"""
Main API

This file has the main functions to check and clone remote git repos.

"""
from pathlib import Path
from flask_admin_cli import exceptions
import os
import subprocess

MAIN_REPO = "https://github.com/mariofix/flask-admin-cli"
FLASK_ADMIN_REPO = "https://github.com/flask-admin/flask-admin"
BRANCHES_NOT_ALLOWED = ["main", "gh-pages"]
BRANCH_PREFIX = "app"
ORIGINAL_EXAMPLES = [
    "appengine",
    "auth",
    "auth-flask-login",
    "auth-mongoengine",
    "babel",
    "bootstrap4",
    "custom-layout",
    "forms-files-images",
    "geo_alchemy",
    "methodview",
    "mongoengine",
    "multiple-admin-instances",
    "peewee",
    "pymongo",
    "simple",
    "sqla",
    "sqla-association_proxy",
    "sqla-custom-inline-forms",
    "tinymongo",
]
AVAILABLE_EXAMPLES = ["app-factory", "app-flask-extension"]


def cross_check(dest_dir: str, branch: str) -> None:
    """Pre-flight checks

    Verifies the environment

    Args:
        dest_dir (str): directory name inside the project.
        branch (str): remote branch to clone.
    Raises:
        InvalidParamsException: some of the parameters are invalid
        FileExistsError: the `dest_dir` directory already exists
        InvalidBranchException: the `branch` cannot be cloned.
    """

    if not dest_dir or not branch:
        raise exceptions.InvalidParamsException(f"{dest_dir} or {branch} are None.")
    # new directory
    if os.path.isdir(dest_dir):
        raise FileExistsError(f"The directory {dest_dir} already exists.")

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
        ["git", "ls-remote", "--exit-code", "--heads", f"{MAIN_REPO}.git", branch],
        check=True,
        capture_output=False,
        stdout=subprocess.DEVNULL,
    )
    if status.returncode == 2:
        raise exceptions.RemoteBranchNotFoundException(
            f"The remote branch {branch} does not exist."
        )


def clone_repo(branch: str = None, dest_dir: str = None) -> True:
    """Clone the selected repo

    Args:
        branch (str): remote branch to clone.
        dest_dir (str): directory name inside the project.

    Raises:
        InvalidParamsException: some of the parameters are invalid
        FileExistsError: the `dest_dir` directory already exists
        InvalidBranchException: the `branch` cannot be cloned.

    Returns:
        True
    """
    if branch in ORIGINAL_EXAMPLES:
        branch = f"app-orig-{branch}"

    try:
        cross_check(dest_dir, branch)
    except Exception as e:
        raise exceptions.NotReadyException(e)
    else:
        print(f"git clone {MAIN_REPO}.git -b {branch} {dest_dir}")
        # clone = subprocess.run(
        #     ["git", "clone", f"{MAIN_REPO}.git", "-b", branch, new_dir],
        #     check=True,
        # )
        # subprocess.run(["rm", "-rf", f"{new_dir}/.git"])
        return True
