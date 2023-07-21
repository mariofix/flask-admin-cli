import os
import subprocess
from pathlib import Path

from flask_admin_cli import exceptions

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
    """
    Perform pre-flight checks before cloning the repository.

    Parameters:
    dest_dir (str): The destination directory to install the example.
    branch (str): The branch to be cloned.

    Raises:
    InvalidParamsException: If either `dest_dir` or `branch` is None.
    FileExistsError: If the destination directory already exists.
    InvalidBranchException: If the branch is not allowed or does not start with `app`.
    RemoteBranchNotFoundException: If the remote branch does not exist.
    """

    if not dest_dir or not branch:
        raise exceptions.InvalidParamsException(
            f"{dest_dir} or {branch} are None.")
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
        ["git", "ls-remote", "--exit-code",
            "--heads", f"{MAIN_REPO}.git", branch],
        check=True,
        capture_output=False,
        stdout=subprocess.DEVNULL,
    )
    if status.returncode == 2:
        raise exceptions.RemoteBranchNotFoundException(
            f"The remote branch {branch} does not exist."
        )


def clone_repo(branch: str = None, dest_dir: str = None) -> True:
    """
    Clone the Flask Admin example repository to the specified directory.

    Parameters:
    branch (str, optional): The branch to be cloned. Defaults to None.
    dest_dir (str, optional): The destination directory to install the example. Defaults to None.

    Returns:
    True: If the cloning is successful.

    Raises:
    NotReadyException: If any pre-flight checks fail.
    """
    if branch in ORIGINAL_EXAMPLES:
        branch = f"app-orig-{branch}"

    try:
        cross_check(dest_dir, branch)
    except Exception as e:
        raise exceptions.NotReadyException(e)
    else:
        print(f"git clone {MAIN_REPO}.git -b {branch} {dest_dir}")
        return True
