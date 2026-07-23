import polars as pl

from qualityclean.rules.whitespace_rule import WhitespaceRule


def test_removes_leading_and_trailing_whitespace():

    df = pl.DataFrame(
        {
            "name": [" Alice ", " Bob "],
        }
    )

    result = WhitespaceRule().run(df)

    assert result["name"].to_list() == [
        "Alice",
        "Bob",
    ]


def test_preserves_clean_strings():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
        }
    )

    result = WhitespaceRule().run(df)

    assert result.equals(df)


def test_multiple_string_columns():

    df = pl.DataFrame(
        {
            "first": [" Alice ", " Bob "],
            "last": [" Smith ", " Jones "],
        }
    )

    result = WhitespaceRule().run(df)

    assert result["first"].to_list() == [
        "Alice",
        "Bob",
    ]

    assert result["last"].to_list() == [
        "Smith",
        "Jones",
    ]


def test_numeric_columns_unchanged():

    df = pl.DataFrame(
        {
            "name": [" Alice "],
            "age": [20],
        }
    )

    result = WhitespaceRule().run(df)

    assert result["age"].to_list() == [20]


def test_no_string_columns():

    df = pl.DataFrame(
        {
            "age": [20, 30],
            "score": [90.5, 80.0],
        }
    )

    result = WhitespaceRule().run(df)

    assert result.equals(df)


def test_empty_dataframe():

    df = pl.DataFrame()

    result = WhitespaceRule().run(df)

    assert result.height == 0
    assert result.width == 0


def test_internal_whitespace_not_removed():

    df = pl.DataFrame(
        {
            "name": ["Alice Smith"],
        }
    )

    result = WhitespaceRule().run(df)

    assert result["name"][0] == "Alice Smith"


def test_only_spaces_become_empty_string():

    df = pl.DataFrame(
        {
            "name": ["   "],
        }
    )

    result = WhitespaceRule().run(df)

    assert result["name"][0] == ""


def test_mixed_string_and_null_values():

    df = pl.DataFrame(
        {
            "name": [" Alice ", None, " Bob "],
        }
    )

    result = WhitespaceRule().run(df)

    assert result["name"].to_list() == [
        "Alice",
        None,
        "Bob",
    ]


def test_single_row_dataframe():

    df = pl.DataFrame(
        {
            "name": [" Alice "],
        }
    )

    result = WhitespaceRule().run(df)

    assert result["name"][0] == "Alice"