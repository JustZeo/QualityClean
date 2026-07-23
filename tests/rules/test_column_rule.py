import polars as pl

from qualityclean.rules.column_rule import ColumnRule


def test_lowercase_column_names():

    df = pl.DataFrame(
        {
            "Name": ["Alice"],
            "AGE": [20],
        }
    )

    result = ColumnRule().run(df)

    assert result.columns == [
        "name",
        "age",
    ]


def test_replace_spaces_with_underscores():

    df = pl.DataFrame(
        {
            "First Name": ["Alice"],
            "Last Name": ["Smith"],
        }
    )

    result = ColumnRule().run(df)

    assert result.columns == [
        "first_name",
        "last_name",
    ]


def test_remove_special_characters():

    df = pl.DataFrame(
        {
            "Age (%)": [20],
            "Salary ($)": [100],
        }
    )

    result = ColumnRule().run(df)

    assert result.columns == [
        "age",
        "salary",
    ]


def test_remove_repeated_underscores():

    df = pl.DataFrame(
        {
            "First___Name": ["Alice"],
        }
    )

    result = ColumnRule().run(df)

    assert result.columns == [
        "first_name",
    ]


def test_strip_leading_and_trailing_underscores():

    df = pl.DataFrame(
        {
            "__Name__": ["Alice"],
        }
    )

    result = ColumnRule().run(df)

    assert result.columns == [
        "name",
    ]


def test_duplicate_column_names_are_made_unique():

    df = pl.DataFrame(
        {
            "Name": [1],
            "name ": [2],
        }
    )

    result = ColumnRule().run(df)

    assert result.columns == [
        "name",
        "name_1",
    ]


def test_normalization_can_be_disabled():

    df = pl.DataFrame(
        {
            "First Name": ["Alice"],
        }
    )

    result = ColumnRule().run(
        df,
        normalize_names=False,
    )

    assert result.columns == [
        "First Name",
    ]


def test_remove_empty_columns():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "empty": [None, None],
        }
    )

    result = ColumnRule().run(
        df,
        remove_empty_columns=True,
    )

    assert result.columns == [
        "name",
    ]


def test_keep_non_empty_columns():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, None],
        }
    )

    result = ColumnRule().run(
        df,
        remove_empty_columns=True,
    )

    assert result.columns == [
        "name",
        "age",
    ]


def test_empty_dataframe():

    result = ColumnRule().run(pl.DataFrame())

    assert result.height == 0
    assert result.width == 0


def test_single_column_dataframe():

    df = pl.DataFrame(
        {
            " Name ": ["Alice"],
        }
    )

    result = ColumnRule().run(df)

    assert result.columns == [
        "name",
    ]


def test_normalize_and_remove_empty_columns_together():

    df = pl.DataFrame(
        {
            " First Name ": ["Alice"],
            " Empty ": [None],
        }
    )

    result = ColumnRule().run(
        df,
        remove_empty_columns=True,
    )

    assert result.columns == [
        "first_name",
    ]