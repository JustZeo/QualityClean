import polars as pl 
from pathlib import Path


def export(data:pl.DataFrame,path:str|Path)-> None:
    """Export a Polars DataFrame to support file format."""

    path = Path(path)
    ext = path.suffix.lower()

    if ext == ".csv":
        data.write_csv(path)
        return
    if ext == ".parquet":
        data.write_parquet(path)
        return

    raise ValueError(
        f"Unsupported file extension: {ext}. Expected '.csv' or '.parquet'"
    )