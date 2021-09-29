from dagster import ModeDefinition

from cool_beans.resources.resources import (
    test_string_generator_resource,
    string_generator_resource,
)


test_mode = ModeDefinition(
    name="test",
    resource_defs={"random_string_generator": test_string_generator_resource},
)
prod_mode = ModeDefinition(
    name="prod", resource_defs={"random_string_generator": string_generator_resource}
)
