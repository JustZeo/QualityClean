import polars as pl
import qualityclean as qc


def test_clean_returns_clean_result():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    result = qc.clean(df)

    assert isinstance(result, qc.CleanResult)


def test_clean_returns_dataframe():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    result = qc.clean(df)

    assert isinstance(result.df, pl.DataFrame)


def test_clean_returns_report():

    df = pl.DataFrame(
        {
            "name": ["Alice"],
            "age": [20],
        }
    )

    result = qc.clean(df)

    assert result.report is not None


def test_clean_preserves_rows():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    result = qc.clean(df)

    assert result.df.height == 2


def test_clean_preserves_columns():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    result = qc.clean(df)

    assert result.df.width == 2


def test_clean_with_fill_enabled():

    df = pl.DataFrame(
        {
            "name": ["Alice", None],
            "age": [20, None],
        }
    )

    result = qc.clean(
        df,
        fill=True,
    )

    assert isinstance(result, qc.CleanResult)


def test_clean_supports_empty_dataframe():

    df = pl.DataFrame()

    result = qc.clean(df)

    assert isinstance(result, qc.CleanResult)


def test_execution_time_is_recorded():

    df = pl.DataFrame(
        {
            "x": [1, 2, 3],
        }
    )

    result = qc.clean(df)

    assert result.report.execution_time >= 0


def test_rule_timings_are_recorded():

    df = pl.DataFrame(
        {
            "x": [1, 2, 3],
        }
    )

    result = qc.clean(df)

    assert isinstance(result.report.rule_timings, dict)
    assert len(result.report.rule_timings) > 0


def test_memory_usage_is_recorded():

    df = pl.DataFrame(
        {
            "x": [1, 2, 3],
        }
    )

    result = qc.clean(df)

    assert result.report.memory_before >= 0
    assert result.report.memory_after >= 0


def test_environment_information_is_recorded():

    df = pl.DataFrame(
        {
            "x": [1],
        }
    )

    result = qc.clean(df)

    assert result.report.python_version != ""
    assert result.report.polars_version != ""
    assert result.report.platform != ""