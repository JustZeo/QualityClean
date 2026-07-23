import polars as pl

import qualityclean as qc


def test_pipeline_runs_successfully():

    df = pl.DataFrame(
        {
            " Name ": [" Alice ", "Bob", "Bob"],
            "Age": [20, None, None],
        }
    )

    result = qc.clean(df)

    assert isinstance(result.df, pl.DataFrame)


def test_pipeline_removes_duplicates():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Alice", "Bob"],
            "age": [20, 20, 30],
        }
    )

    result = qc.clean(df)

    assert result.df.height == 2


def test_pipeline_strips_whitespace():

    df = pl.DataFrame(
        {
            "name": [" Alice ", " Bob "],
        }
    )

    result = qc.clean(df)

    assert result.df["name"].to_list() == [
        "Alice",
        "Bob",
    ]


def test_pipeline_converts_placeholders():

    df = pl.DataFrame(
        {
            "name": ["N/A", "Alice"],
        }
    )

    result = qc.clean(df, fill=True)

    assert result.df["name"].null_count() == 0


def test_pipeline_drops_missing_when_fill_false():

    df = pl.DataFrame(
        {
            "name": ["Alice", None],
        }
    )

    result = qc.clean(df)

    assert result.df.height == 1


def test_pipeline_fills_missing_when_fill_true():

    df = pl.DataFrame(
        {
            "city": ["Delhi", None, "Delhi"],
        }
    )

    result = qc.clean(df, fill=True)

    assert result.df.null_count().sum_horizontal().item() == 0


def test_pipeline_handles_empty_dataframe():

    result = qc.clean(pl.DataFrame())

    assert result.df.height == 0
    assert result.df.width == 0


def test_pipeline_preserves_column_count():

    df = pl.DataFrame(
        {
            "a": [1, 2],
            "b": [3, 4],
            "c": [5, 6],
        }
    )

    result = qc.clean(df)

    assert result.df.width == 3


def test_pipeline_records_rule_timings():

    df = pl.DataFrame(
        {
            "a": [1, 2, 3],
        }
    )

    result = qc.clean(df)

    assert len(result.report.rule_timings) > 0


def test_pipeline_execution_time_positive():

    df = pl.DataFrame(
        {
            "a": [1, 2, 3],
        }
    )

    result = qc.clean(df)

    assert result.report.execution_time >= 0