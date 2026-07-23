import polars as pl

from qualityclean.rules.datatype_rule import DatatypeRule


def test_convert_integer_strings():

    df = pl.DataFrame(
        {
            "age": ["10", "20", "30"],
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["age"] == pl.Int64
    assert result["age"].to_list() == [10, 20, 30]


def test_convert_float_strings():

    df = pl.DataFrame(
        {
            "score": ["10.5", "20.0", "30.75"],
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["score"] == pl.Float64


def test_convert_date_strings():

    df = pl.DataFrame(
        {
            "date": [
                "2025-01-01",
                "2025-01-02",
                "2025-01-03",
            ]
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["date"] == pl.Date


def test_keep_normal_string_column():

    df = pl.DataFrame(
        {
            "name": [
                "Alice",
                "Bob",
                "Charlie",
            ]
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["name"] == pl.String


def test_confidence_below_threshold():

    df = pl.DataFrame(
        {
            "value": [
                "1",
                "2",
                "hello",
                "world",
                "abc",
            ]
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["value"] == pl.String


def test_exactly_eighty_percent_integer():

    df = pl.DataFrame(
        {
            "value": [
                "1",
                "2",
                "3",
                "4",
                "hello",
            ]
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["value"] == pl.Int64


def test_non_string_columns_are_unchanged():

    df = pl.DataFrame(
        {
            "age": [10, 20, 30],
        }
    )

    result = DatatypeRule().run(df)

    assert result.equals(df)


def test_empty_dataframe():

    result = DatatypeRule().run(pl.DataFrame())

    assert result.height == 0
    assert result.width == 0


def test_all_null_string_column():

    df = pl.DataFrame(
        {
            "value": [None, None],
        },
        schema={"value": pl.String},
    )

    result = DatatypeRule().run(df)

    assert result.schema["value"] == pl.String
    assert result["value"].null_count() == 2


def test_mixed_nulls_and_integer_strings():

    df = pl.DataFrame(
        {
            "value": [
                "1",
                None,
                "2",
                "3",
            ]
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["value"] == pl.Int64
    assert result["value"].null_count() == 1


def test_invalid_dates_do_not_convert():

    df = pl.DataFrame(
        {
            "date": [
                "2025-01-01",
                "not-a-date",
                "hello",
            ]
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["date"] == pl.String


def test_multiple_columns_convert_independently():

    df = pl.DataFrame(
        {
            "age": ["10", "20", "30"],
            "score": ["10.5", "20.5", "30.5"],
            "name": ["Alice", "Bob", "Charlie"],
        }
    )

    result = DatatypeRule().run(df)

    assert result.schema["age"] == pl.Int64
    assert result.schema["score"] == pl.Float64
    assert result.schema["name"] == pl.String