from .base import BaseRule
import polars as pl
import re


class ColumnRule(BaseRule):
    def run(
        self,
        df: pl.DataFrame,
        normalize_names: bool = True,
        remove_empty_columns: bool = False,
        **_,
    ) -> pl.DataFrame:

        if normalize_names:
            df = self._normalize_column_names(df)

        if remove_empty_columns:
            df = self._remove_empty_columns(df)

        return df

    def _normalize_column_names(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:

        seen = {}
        new_columns = []

        for column in df.columns:

            # lowercase
            name = column.lower().strip()

            # replace spaces with underscore
            name = re.sub(r"\s+", "_", name)

            # remove special characters
            name = re.sub(r"[^a-z0-9_]", "", name)

            # remove repeated underscores
            name = re.sub(r"_+", "_", name)

            # remove leading/trailing underscore
            name = name.strip("_")

            # avoid duplicate names
            if name in seen:
                seen[name] += 1
                name = f"{name}_{seen[name]}"
            else:
                seen[name] = 0

            new_columns.append(name)

        return df.rename(dict(zip(df.columns, new_columns)))

    def _remove_empty_columns(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:

        empty_columns = []

        for column in df.columns:

            if df[column].null_count() == df.height:
                empty_columns.append(column)

        if empty_columns:
            df = df.drop(empty_columns)

        return df