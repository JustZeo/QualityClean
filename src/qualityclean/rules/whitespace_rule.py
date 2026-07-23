from .base import BaseRule

import polars as pl


class WhitespaceRule(BaseRule):
    def run(
        self,
        df: pl.DataFrame,
        **kwargs,
    ) -> pl.DataFrame:

        builder = kwargs.get("builder")

        string_columns = df.select(pl.col(pl.String)).columns

        if not string_columns:
            return df

        count = (
            df.select(
                (
                    pl.col(string_columns)
                    != pl.col(string_columns).str.strip_chars()
                ).sum()
            )
            .sum_horizontal()
            .item()
        )

        cleaned_df = df.with_columns(
            pl.col(string_columns).str.strip_chars()
        )

        if builder is not None:
            builder.record_whitespace_fixed(count)

        return cleaned_df