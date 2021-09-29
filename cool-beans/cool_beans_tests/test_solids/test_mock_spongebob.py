from dagster import execute_solid
from cool_beans.solids.mock_spongebob import mock_spongebob


def test_lowercase_to_spongebob():
    result = execute_solid(mock_spongebob, input_values={"string": "oh mama"})

    assert result.success
    assert result.output_value() == "oH MaMa"


def test_uppercase_to_spongebob():
    result = execute_solid(mock_spongebob, input_values={"string": "BIG BOI"})

    assert result.success
    assert result.output_value() == "bIg bOi"


def test_must_remain_unchanged():
    result = execute_solid(mock_spongebob, input_values={"string": "nOt gOnNa cHaNgE "})

    assert result.success
    assert result.output_value() == "nOt gOnNa cHaNgE "
