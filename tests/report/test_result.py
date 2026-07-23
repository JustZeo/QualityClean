import polars as pl

from qualityclean.report.model import Report
from qualityclean.result import CleanResult


def test_clean_result_stores_dataframe_and_report():

    df = pl.DataFrame(
        {
            "a": [1, 2, 3],
        }
    )

    report = Report()

    result = CleanResult(
        df=df,
        report=report,
    )

    assert result.df is df
    assert result.report is report


def test_dataframe_can_be_accessed():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
        }
    )

    result = CleanResult(
        df=df,
        report=Report(),
    )

    assert result.df.height == 2
    assert result.df.columns == ["name"]


def test_report_can_be_modified_through_result():

    report = Report()

    result = CleanResult(
        df=pl.DataFrame(),
        report=report,
    )

    result.report.duplicates_removed = 5

    assert report.duplicates_removed == 5
    assert result.report.duplicates_removed == 5


def test_multiple_instances_are_independent():

    result1 = CleanResult(
        df=pl.DataFrame({"a": [1]}),
        report=Report(),
    )

    result2 = CleanResult(
        df=pl.DataFrame({"a": [2]}),
        report=Report(),
    )

    result1.report.missing_filled = 10

    assert result2.report.missing_filled == 0


def test_empty_dataframe_is_supported():

    result = CleanResult(
        df=pl.DataFrame(),
        report=Report(),
    )

    assert result.df.height == 0
    assert result.df.width == 0