from dagster import pipeline

from cool_beans.solids.leet_speak import leet
from cool_beans.solids.random_string import spew_random_string
from cool_beans.solids.clean_string import remove_non_alphanumeric
from cool_beans.solids.mock_spongebob import mock_spongebob

from cool_beans.modes.modes import prod_mode, test_mode


@pipeline(mode_defs=[prod_mode, test_mode])
def dumb_password_generator():
    random_string = spew_random_string()

    cleaned_string = remove_non_alphanumeric(random_string)

    mocked = mock_spongebob(cleaned_string)

    leet(mocked)
