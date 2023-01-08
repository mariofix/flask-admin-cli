import pytest
import os
from flask_admin_cli.api import clone_repo, cross_check, BASE_DIR


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


@pytest.mark.asyncio
async def test_clone_repo():
    assert await clone_repo("app-simple", "hola_mundo")
    assert os.path.isdir(os.path.join(BASE_DIR, "hola_mundo/.git")) is False


@pytest.mark.asyncio
async def test_clone_repo_fail():
    with pytest.raises(Exception) as e:
        await clone_repo(None, None)
