from dagster import execute_solid
from cool_beans.solids.clean_string import remove_non_alphanumeric


def test_spaces_must_be_removed():
    result = execute_solid(remove_non_alphanumeric, input_values={"string": " cool beans "})

    assert result.success
    assert result.output_value() == "coolbeans"


def test_spaces_and_apostrophe_must_be_removed():
    result = execute_solid(remove_non_alphanumeric, input_values={"string": "This test musn't fail"})

    assert result.success
    assert result.output_value() == "Thistestmusntfail"


def test_must_be_empty_string_after():
    result = execute_solid(remove_non_alphanumeric, input_values={"string": "?'/\\*&^%$#@"})

    assert result.success
    assert result.output_value() == ""


def test_must_remain_unchanged():
    result = execute_solid(remove_non_alphanumeric, input_values={"string": "cool_beans"})

    assert result.success
    assert result.output_value() == "cool_beans"