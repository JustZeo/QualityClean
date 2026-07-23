import polars as pl
import pytest

import qualityclean as qc


def test_load_returns_dataframe_from_dataframe():

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    result = qc.load(df)

    assert result.equals(df)


def test_load_csv(tmp_path):

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    csv_file = tmp_path / "data.csv"
    df.write_csv(csv_file)

    result = qc.load(csv_file)

    assert isinstance(result, pl.DataFrame)
    assert result.shape == (2, 2)
    assert result.columns == ["name", "age"]
    assert result.equals(df)


def test_load_parquet(tmp_path):

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    parquet_file = tmp_path / "data.parquet"
    df.write_parquet(parquet_file)

    result = qc.load(parquet_file)

    assert isinstance(result, pl.DataFrame)
    assert result.equals(df)


def test_load_missing_file():

    with pytest.raises(FileNotFoundError):
        qc.load("does_not_exist.csv")


def test_load_directory(tmp_path):

    with pytest.raises(IsADirectoryError):
        qc.load(tmp_path)


def test_load_invalid_extension(tmp_path):

    file = tmp_path / "sample.txt"
    file.write_text("hello")

    with pytest.raises(ValueError):
        qc.load(file)


def test_load_empty_csv(tmp_path):

    df = pl.DataFrame(
        {
            "name": [],
            "age": [],
        },
        schema={
            "name": pl.String,
            "age": pl.Int64,
        },
    )

    csv_file = tmp_path / "empty.csv"
    df.write_csv(csv_file)

    result = qc.load(csv_file)

    assert result.shape == (0, 2)
    assert result.columns == ["name", "age"]


def test_load_preserves_dtypes(tmp_path):

    df = pl.DataFrame(
        {
            "id": [1, 2],
            "name": ["Alice", "Bob"],
            "score": [90.5, 88.0],
            "active": [True, False],
        }
    )

    csv_file = tmp_path / "types.csv"
    df.write_csv(csv_file)

    result = qc.load(csv_file)

    assert result.schema == df.schema