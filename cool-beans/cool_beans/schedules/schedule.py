from datetime import datetime, time

from dagster import daily_schedule


@daily_schedule(
    pipeline_name="dumb_password_generator",
    start_date=datetime(2021, 1, 1),
    execution_time=time(0, 0),
    execution_timezone="Asia/Manila",
    mode="prod",
)
def daily_schedule(_context):
    return {}
