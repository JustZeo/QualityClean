import polars as pl

from qualityclean.rules.missing_rule import MissingRule


def test_drop_missing_rows():

    df = pl.DataFrame(
        {
            "name": ["Alice", None, "Bob"],
            "age": [20, 25, 30],
        }
    )

    result = MissingRule().run(df)

    assert result.height == 2


def test_fill_integer_with_median():

    df = pl.DataFrame(
        {
            "age": [10, None, 30],
        }
    )

    result = MissingRule().run(df, fill=True)

    assert result["age"].to_list() == [10, 20, 30]


def test_fill_float_with_median():

    df = pl.DataFrame(
        {
            "score": [10.0, None, 30.0],
        }
    )

    result = MissingRule().run(df, fill=True)

    assert result["score"].to_list() == [10.0, 20.0, 30.0]


def test_fill_string_with_mode():

    df = pl.DataFrame(
        {
            "city": ["Delhi", None, "Delhi", "Mumbai"],
        }
    )

    result = MissingRule().run(df, fill=True)

    assert result["city"].to_list() == [
        "Delhi",
        "Delhi",
        "Delhi",
        "Mumbai",
    ]


def test_fill_boolean_with_mode():

    df = pl.DataFrame(
        {
            "active": [True, None, True, False],
        }
    )

    result = MissingRule().run(df, fill=True)

    assert result["active"].to_list() == [
        True,
        True,
        True,
        False,
    ]


def test_fill_date_forward():

    df = pl.DataFrame(
        {
            "date": [
                None,
                "2025-01-02",
                None,
                "2025-01-04",
            ]
        }
    ).with_columns(
        pl.col("date").str.to_date()
    )

    result = MissingRule().run(df, fill=True)

    assert result["date"].null_count() == 1
    assert result["date"][2] == result["date"][1]


def test_all_null_integer_column():

    df = pl.DataFrame(
        {
            "age": [None, None],
        },
        schema={"age": pl.Int64},
    )

    result = MissingRule().run(df, fill=True)

    assert result["age"].null_count() == 2


def test_all_null_string_column():

    df = pl.DataFrame(
        {
            "city": [None, None],
        },
        schema={"city": pl.String},
    )

    result = MissingRule().run(df, fill=True)

    assert result["city"].null_count() == 2


def test_empty_dataframe():

    result = MissingRule().run(pl.DataFrame())

    assert result.height == 0
    assert result.width == 0


def test_no_missing_values():

    df = pl.DataFrame(
        {
            "a": [1, 2, 3],
        }
    )

    result = MissingRule().run(df)

    assert result.equals(df)


def test_single_row_dataframe():

    df = pl.DataFrame(
        {
            "a": [None],
        },
        schema={"a": pl.Int64},
    )

    result = MissingRule().run(df, fill=True)

    assert result["a"].null_count() == 1


def test_preserves_integer_dtype():

    df = pl.DataFrame(
        {
            "age": [10, None, 30],
        }
    )

    result = MissingRule().run(df, fill=True)

    assert result.schema["age"] == pl.Int64