import os
from pathlib import Path

import pytest

from flask_admin_cli.api import clone_repo, cross_check


def test_cross_check_fail_dir():
    with pytest.raises(Exception) as e:
        cross_check(None, "app-simple")
    with pytest.raises(Exception) as e:
        cross_check("flask_admin_cli", "app-simple")


def test_cross_check_fail_branch():
    with pytest.raises(Exception) as e:
        cross_check("new_dir", None)
    with pytest.raises(Exception) as e:
        cross_check("dest_dir", "main")
    with pytest.raises(Exception) as e:
        cross_check("dest_dir", "main2")
    with pytest.raises(Exception) as e:
        cross_check("dest_dir", "app-simple2")
    with pytest.raises(Exception) as e:
        cross_check("dest_dir", "app-orig-tinymongo2")


def test_clone_repo():
    CURR_DIR = Path(__file__).resolve().parent
    new_path = os.path.join(CURR_DIR, "hola_mundo")
    assert clone_repo("app-simple", new_path)


def test_clone_original_repo():
    CURR_DIR = Path(__file__).resolve().parent
    new_path = os.path.join(CURR_DIR, "original-simple")
    assert clone_repo("simple", new_path)


def test_clone_repo_fail():
    with pytest.raises(Exception) as e:
        clone_repo(None, None)
