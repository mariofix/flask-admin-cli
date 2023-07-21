import pytest
from click.testing import CliRunner

from flask_admin_cli.cli import the_cli


def test_cli():
    runner = CliRunner()
    res = runner.invoke(the_cli, ["list_examples"])

    assert res.exit_code == 2
