import click
import sqlite_utils

from .utils import download


@click.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.option("--token", envvar="OURA_PAT", help="Oura personal access token")
def cli(db_path, token):
    "Download Oura data to a SQLite database"

    if not token:
        raise click.ClickException(
            "Provide either environment variable: OURA_PAT or use --token"
        )

    db = sqlite_utils.Database(db_path)
    download(db, token)
