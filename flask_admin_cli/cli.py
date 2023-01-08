import anyio
import asyncclick as click
from flask_admin_cli import api


@click.group()
async def the_cli():
    pass


@click.command()
@click.option("--name", default="app-factory", help="Application Name.")
@click.option("--dest_dir", prompt="Directory", help="Directory to install.")
async def original_examples(name, dest_dir):
    """Flask-Admin app using one of the examples."""
    await api.clone_repo(name, dest_dir)


@click.command()
@click.option("--name", default="app-factory", help="Application Name.")
@click.option("--dest_dir", prompt="Directory", help="Directory to install.")
async def new_app(name, dest_dir):
    """Flask-Admin app as a Flask app"""
    await api.clone_repo(name, dest_dir)


@click.command()
@click.option("--name", default="app-factory", help="Application Name.")
@click.option("--dest_dir", prompt="Directory", help="Directory to install.")
async def new_extension(name, dest_dir):
    """Flask-Admin app as a Flask extension"""
    await api.clone_repo(name, dest_dir)


the_cli.add_command(new_app)
the_cli.add_command(new_extension)
the_cli.add_command(original_examples)

if __name__ == "__main__":
    the_cli(_anyio_backend="asyncio")  # or asyncio
