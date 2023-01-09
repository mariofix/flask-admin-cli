# flask_admin_cli/cli.py
"""CLI Application

Available Commands:
    - list-original-examples: To get a list of the original examples provided by Flask-Admin  
    - list-examples: To get a list of available apps for your project.  
    - new_app: creates an app  

Examples:
    >>> flask-admin list-examples
    >>> flask-admin list-original-examples
"""
import click
from flask_admin_cli import api


@click.group()
def the_cli():
    pass


@click.command()
def list_original_examples():
    """Lists all the original examples made by the Flask-Admin team."""
    for example in api.ORIGINAL_EXAMPLES:
        click.secho(f"## {example}:", bold=True)
        click.secho(f"\tURL: {api.FLASK_ADMIN_REPO}/tree/master/examples/{example}")
        click.secho(f"\tInstalls with ", nl=False)
        click.secho(f"flask-admin new_app --app {example}", bold=True)
        click.echo("")


@click.command()
def list_examples():
    """Lists all available examples.

    All these examples are made by us.
    """
    for example in api.AVAILABLE_EXAMPLES:
        click.secho(f"## {example}:", bold=True)
        click.secho(f"\tURL: {api.MAIN_REPO}/tree/{example}")
        click.secho(f"\tInstalls with ", nl=False)
        click.secho(f"flask-admin new_app --app {example}", bold=True)
        click.echo("")


@click.command()
@click.option(
    "--app",
    default="app-factory",
    help="Application Name.",
    required=True,
    type=str,
    show_default=True,
)
@click.option(
    "--dest_dir",
    prompt="Directory",
    help="Directory to install.",
    required=True,
    default=".",
    type=click.Path(
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
        allow_dash=False,
        exists=False,
    ),
    show_default=True,
)
def new_app(app, dest_dir):
    """Flask-Admin app as a Flask app"""
    api.clone_repo(app, dest_dir)


the_cli.add_command(new_app)
the_cli.add_command(list_original_examples)
the_cli.add_command(list_examples)

if __name__ == "__main__":
    the_cli()
