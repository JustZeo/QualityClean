import polars as pl

from qualityclean.rules.duplicate_rule import DuplicateRule


def test_remove_duplicate_rows():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Alice", "Bob"],
            "age": [20, 20, 30],
        }
    )

    result = DuplicateRule().run(df)

    assert result.height == 2


def test_no_duplicates():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    result = DuplicateRule().run(df)

    assert result.equals(df)


def test_preserves_order():

    df = pl.DataFrame(
        {
            "name": ["Bob", "Alice", "Bob"],
            "age": [30, 20, 30],
        }
    )

    result = DuplicateRule().run(df)

    assert result["name"].to_list() == [
        "Bob",
        "Alice",
    ]


def test_multiple_duplicate_groups():

    df = pl.DataFrame(
        {
            "name": [
                "Alice",
                "Alice",
                "Bob",
                "Bob",
                "Charlie",
            ],
            "age": [
                20,
                20,
                30,
                30,
                40,
            ],
        }
    )

    result = DuplicateRule().run(df)

    assert result.height == 3


def test_all_rows_duplicate():

    df = pl.DataFrame(
        {
            "value": [1, 1, 1, 1],
        }
    )

    result = DuplicateRule().run(df)

    assert result.height == 1


def test_empty_dataframe():

    result = DuplicateRule().run(pl.DataFrame())

    assert result.height == 0
    assert result.width == 0


def test_single_row_dataframe():

    df = pl.DataFrame(
        {
            "value": [42],
        }
    )

    result = DuplicateRule().run(df)

    assert result.equals(df)


def test_null_values_are_considered_duplicates():

    df = pl.DataFrame(
        {
            "name": [None, None, "Alice"],
        }
    )

    result = DuplicateRule().run(df)

    assert result.height == 2


def test_partial_duplicates_not_removed():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Alice"],
            "age": [20, 21],
        }
    )

    result = DuplicateRule().run(df)

    assert result.height == 2


def test_duplicate_rows_across_multiple_columns():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Alice", "Bob"],
            "age": [20, 20, 30],
            "city": ["Delhi", "Delhi", "Mumbai"],
        }
    )

    result = DuplicateRule().run(df)

    assert result.height == 2