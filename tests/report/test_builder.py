import polars as pl

from qualityclean.report.builder import ReportBuilder


def test_start_records_initial_metadata():

    df = pl.DataFrame(
        {
            "name": ["Alice"],
            "age": [20],
        }
    )

    builder = ReportBuilder()

    builder.start(df, fill_mode=True)

    report = builder.build()

    assert report.fill_mode is True
    assert report.original_rows == 1
    assert report.original_columns == 2
    assert report.memory_before >= 0
    assert report.python_version != ""
    assert report.polars_version != ""
    assert report.platform != ""
    assert report.original_schema == {
        "name": "String",
        "age": "Int64",
    }


def test_finish_records_final_metadata():

    df = pl.DataFrame(
        {
            "name": ["Alice"],
            "age": [20],
        }
    )

    builder = ReportBuilder()

    builder.start(df)

    cleaned = df.drop("age")

    builder.finish(cleaned)

    report = builder.build()

    assert report.final_rows == 1
    assert report.final_columns == 1
    assert report.memory_after >= 0
    assert report.execution_time >= 0
    assert report.final_schema == {
        "name": "String",
    }


def test_record_rule_time():

    builder = ReportBuilder()

    builder.record_rule_time(
        "WhitespaceRule",
        0.123,
    )

    report = builder.build()

    assert report.rule_timings["WhitespaceRule"] == 0.123


def test_record_whitespace_fixed():

    builder = ReportBuilder()

    builder.record_whitespace_fixed(5)
    builder.record_whitespace_fixed(3)

    report = builder.build()

    assert report.whitespace_fixed == 8


def test_record_placeholders_converted():

    builder = ReportBuilder()

    builder.record_placeholders_converted(4)
    builder.record_placeholders_converted(2)

    report = builder.build()

    assert report.placeholders_converted == 6


def test_record_missing_filled():

    builder = ReportBuilder()

    builder.record_missing_filled(10)
    builder.record_missing_filled(5)

    report = builder.build()

    assert report.missing_filled == 15


def test_record_missing_dropped():

    builder = ReportBuilder()

    builder.record_missing_dropped(7)
    builder.record_missing_dropped(2)

    report = builder.build()

    assert report.missing_dropped == 9


def test_record_duplicates_removed():

    builder = ReportBuilder()

    builder.record_duplicates_removed(4)
    builder.record_duplicates_removed(1)

    report = builder.build()

    assert report.duplicates_removed == 5


def test_build_returns_same_report_instance():

    builder = ReportBuilder()

    report1 = builder.build()
    report2 = builder.build()

    assert report1 is report2


def test_empty_dataframe_start_finish():

    df = pl.DataFrame()

    builder = ReportBuilder()

    builder.start(df)
    builder.finish(df)

    report = builder.build()

    assert report.original_rows == 0
    assert report.original_columns == 0
    assert report.final_rows == 0
    assert report.final_columns == 0