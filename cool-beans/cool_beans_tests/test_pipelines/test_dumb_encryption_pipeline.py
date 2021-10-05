from dagster import execute_pipeline
from cool_beans.pipelines.pipelines import dumb_password_generator


def test_my_pipeline():
    result = execute_pipeline(dumb_password_generator, mode="test")

    assert result.success
    assert (
        result.output_for_solid("leet")
        == "4_v3rY_L0Ng_57r1nG_W17h_n0_5p4c35_4Nd_5P3C14l_cH4R4C73r5_C0N51d3r3d_45_0n3_W0Rd"
    )
