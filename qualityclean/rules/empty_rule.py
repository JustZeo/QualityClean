from .base import BaseRule

import polars as pl


DEFAULT_MISSING_PLACEHOLDERS = [
    "",
    "N/A",
    "n/a",
    "NA",
    "na",
    "NULL",
    "null",
    "None",
    "none",
    "Unknown",
    "unknown",
    "Missing",
    "missing",
]


class EmptyRule(BaseRule):
    def run(
        self,
        df: pl.DataFrame,
        missing_placeholders: list[str] | None = None,
        **kwargs,
    ) -> pl.DataFrame:

        if missing_placeholders is None:
            missing_placeholders = DEFAULT_MISSING_PLACEHOLDERS

        builder = kwargs.get("builder")

        string_columns = df.select(pl.col(pl.String)).columns

        if string_columns:
            placeholder_count = (
                df.select(
                    pl.col(string_columns)
                    .is_in(missing_placeholders)
                    .sum()
                )
                .sum_horizontal()
                .item()
            )
        else:
            placeholder_count = 0

        cleaned_df = df.with_columns(
            [
                pl.col(pl.String)
                .str.strip_chars()
                .replace(missing_placeholders, None),

                pl.col(pl.Float32, pl.Float64)
                .fill_nan(None),
            ]
        )

        if builder is not None:
            builder.record_placeholders_converted(
                placeholder_count,
            )

        return cleaned_df