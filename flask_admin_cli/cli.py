import click

from . import api


@click.group()
def the_cli():
    """
    Command line interface for managing Flask Admin examples.
    """
    pass


@click.command()
def list_original_examples():
    """
    List all original Flask Admin examples with their respective URLs and installation commands.

    Usage:
    python script.py list_original_examples
    """
    for example in api.ORIGINAL_EXAMPLES:
        click.secho(f"## {example}:", bold=True)
        click.secho(
            f"\tURL: {api.FLASK_ADMIN_REPO}/tree/master/examples/{example}")
        click.secho(f"\tInstalls with ", nl=False)
        click.secho(f"flask-admin new_app --app {example}", bold=True)
        click.echo("")


@click.command()
def list_examples():
    """
    List all available Flask Admin examples with their respective URLs and installation commands.

    Usage:
    python script.py list_examples
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
    """
    Clone a Flask Admin example repository to the specified directory.

    Parameters:
    app (str): Application Name.
    dest_dir (str): Directory to install the example.

    Usage:
    python script.py new_app --app example_name --dest_dir /path/to/destination
    """
    api.clone_repo(app, dest_dir)


the_cli.add_command(new_app)
the_cli.add_command(list_original_examples)
the_cli.add_command(list_examples)

if __name__ == "__main__":
    the_cli()
