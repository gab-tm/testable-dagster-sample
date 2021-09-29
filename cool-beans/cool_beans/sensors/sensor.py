from dagster import sensor


@sensor(pipeline_name="dumb_password_generator")
def my_sensor(_context):
    pass
