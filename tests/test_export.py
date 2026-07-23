import polars as pl
import pytest

import qualityclean as qc


def test_export_csv(tmp_path):

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    output = tmp_path / "output.csv"

    qc.export(df, output)

    assert output.exists()

    loaded = pl.read_csv(output)

    assert loaded.equals(df)


def test_export_parquet(tmp_path):

    df = pl.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 30],
        }
    )

    output = tmp_path / "output.parquet"

    qc.export(df, output)

    assert output.exists()

    loaded = pl.read_parquet(output)

    assert loaded.equals(df)


def test_export_clean_result_csv(tmp_path):

    df = pl.DataFrame(
        {
            "name": [" Alice ", "Bob"],
            "age": [20, 30],
        }
    )

    result = qc.clean(df)

    output = tmp_path / "clean.csv"

    qc.export(result, output)

    assert output.exists()

    loaded = pl.read_csv(output)

    assert loaded.equals(result.df)


def test_export_clean_result_parquet(tmp_path):

    df = pl.DataFrame(
        {
            "name": [" Alice ", "Bob"],
            "age": [20, 30],
        }
    )

    result = qc.clean(df)

    output = tmp_path / "clean.parquet"

    qc.export(result, output)

    assert output.exists()

    loaded = pl.read_parquet(output)

    assert loaded.equals(result.df)


def test_export_invalid_extension(tmp_path):

    df = pl.DataFrame({"a": [1, 2]})

    output = tmp_path / "output.txt"

    with pytest.raises(ValueError):
        qc.export(df, output)


def test_export_nonexistent_directory(tmp_path):

    df = pl.DataFrame({"a": [1, 2]})

    output = tmp_path / "missing" / "output.csv"

    with pytest.raises(FileNotFoundError):
        qc.export(df, output)


def test_export_round_trip_csv(tmp_path):

    df = pl.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
        }
    )

    output = tmp_path / "roundtrip.csv"

    qc.export(df, output)

    loaded = qc.load(output)

    assert loaded.equals(df)


def test_export_round_trip_parquet(tmp_path):

    df = pl.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
        }
    )

    output = tmp_path / "roundtrip.parquet"

    qc.export(df, output)

    loaded = qc.load(output)

    assert loaded.equals(df)