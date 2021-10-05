from dagster import execute_pipeline
from cool_beans.pipelines.pipelines import dumb_password_generator


def test_my_pipeline():
    result = execute_pipeline(dumb_password_generator, mode="test")

    assert result.success
    assert (
        result.output_for_solid("leet")
        == "4 v3rY L0Ng 57r1nG W17h n0 5p4c35 4Nd 5P3C14l cH4R4C73r5 C0N51d3r3d 45 0n3 W0Rd."
    )
