from dagster import repository

from cool_beans.pipelines.pipelines import dumb_password_generator
from cool_beans.schedules.schedule import daily_schedule


@repository
def cool_beans():
    """
    The repository definition for this cool_beans Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    pipelines = [dumb_password_generator]
    schedules = [daily_schedule]

    return pipelines + schedules
