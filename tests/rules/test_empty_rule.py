import polars as pl

from qualityclean.rules.empty_rule import EmptyRule


def test_empty_string_becomes_null():

    df = pl.DataFrame(
        {
            "name": [""],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1


def test_na_becomes_null():

    df = pl.DataFrame(
        {
            "name": ["N/A"],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1


def test_null_string_becomes_null():

    df = pl.DataFrame(
        {
            "name": ["NULL"],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1


def test_none_string_becomes_null():

    df = pl.DataFrame(
        {
            "name": ["None"],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1


def test_missing_string_becomes_null():

    df = pl.DataFrame(
        {
            "name": ["missing"],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1


def test_unknown_string_becomes_null():

    df = pl.DataFrame(
        {
            "name": ["Unknown"],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1


def test_real_values_are_preserved():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
        }
    )

    result = EmptyRule().run(df)

    assert result.equals(df)


def test_whitespace_is_trimmed_before_replace():

    df = pl.DataFrame(
        {
            "name": ["  N/A  "],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1


def test_nan_float_becomes_null():

    df = pl.DataFrame(
        {
            "score": [1.0, float("nan"), 2.0],
        }
    )

    result = EmptyRule().run(df)

    assert result["score"].null_count() == 1


def test_multiple_string_columns():

    df = pl.DataFrame(
        {
            "first": ["N/A"],
            "last": ["NULL"],
        }
    )

    result = EmptyRule().run(df)

    assert result["first"].null_count() == 1
    assert result["last"].null_count() == 1


def test_no_string_columns():

    df = pl.DataFrame(
        {
            "age": [20, 30],
            "score": [10.0, 20.0],
        }
    )

    result = EmptyRule().run(df)

    assert result.equals(df)


def test_empty_dataframe():

    result = EmptyRule().run(pl.DataFrame())

    assert result.height == 0
    assert result.width == 0


def test_custom_placeholder():

    df = pl.DataFrame(
        {
            "name": ["UNKNOWN_VALUE"],
        }
    )

    result = EmptyRule().run(
        df,
        missing_placeholders=["UNKNOWN_VALUE"],
    )

    assert result["name"].null_count() == 1


def test_existing_nulls_are_preserved():

    df = pl.DataFrame(
        {
            "name": [None, "Alice"],
        }
    )

    result = EmptyRule().run(df)

    assert result["name"].null_count() == 1