from dagster import resource

from cool_beans.utils.random_string_generator import (
    RandomStringGenerator,
    MockRandomStringGenerator,
)


@resource
def test_string_generator_resource(context):
    return MockRandomStringGenerator()


@resource
def string_generator_resource(context):
    return RandomStringGenerator()
