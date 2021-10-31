import datetime

import click
from oura import OuraClient


def download(db, token):
    client = OuraClient(personal_access_token=token)
    click.echo("User: ")
    click.echo(client.user_info())

    # FIXME get start_date from database (last day downloaded - 1day)
    start_date = "2015-01-01"
    end_date = str(datetime.date.today())

    click.echo("sleep data")
    data = client.sleep_summary(start_date, end_date).get("sleep", [])
    db["sleep"].insert_all(
        data,
        replace=True,
        pk="summary_date",
    )

    click.echo("activity data")
    data = client.activity_summary(start_date, end_date).get("activity", [])
    db["activity"].insert_all(
        data,
        replace=True,
        pk="summary_date",
    )

    click.echo("readiness data")
    data = client.readiness_summary(start_date, end_date).get("readiness", [])
    db["readiness"].insert_all(
        data,
        replace=True,
        pk="summary_date",
    )

    click.echo("ideal bedtime data")
    data = client.bedtime_summary(start_date, end_date).get("ideal_bedtimes", [])
    db["ideal_bedtimes"].insert_all(
        data,
        replace=True,
        pk="date",
    )
