from dagster import execute_solid
from cool_beans.solids.leet_speak import leet


def test_leet_letters_to_numbers():
    result = execute_solid(leet, input_values={"string": "oh mama"})

    assert result.success
    assert result.output_value() == "0h m4m4"


def test_leet_numbers_must_remain_unchanged():
    result = execute_solid(leet, input_values={"string": "h3llo w0rld"})

    assert result.success
    assert result.output_value() == "h3ll0 w0rld"


def test_leet_unhandled_characters_must_not_change():
    result = execute_solid(leet, input_values={"string": "h0vv R u?"})

    assert result.success
    assert result.output_value() == "h0vv R u?"