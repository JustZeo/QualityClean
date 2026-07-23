import polars as pl
from pathlib import Path


def load(data: str | Path | pl.DataFrame) -> pl.DataFrame:
    """Load a CSV, Parquet file, or Polars DataFrame."""

    if isinstance(data, pl.DataFrame):
        return data

    path = Path(data)

    if not path.exists():
        raise FileNotFoundError(f"File not found: '{path}'")

    if not path.is_file():
        raise IsADirectoryError(f"'{path}' is a directory, expected a file.")

    ext = path.suffix.lower()

    if ext == ".csv":
        return pl.read_csv(path)

    if ext == ".parquet":
        return pl.read_parquet(path)

    raise ValueError(
        f"Unsupported file extension: '{ext}'. Expected '.csv' or '.parquet'."
    )