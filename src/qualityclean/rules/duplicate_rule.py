from .base import BaseRule

import polars as pl


class DuplicateRule(BaseRule):
    def run(
        self,
        df: pl.DataFrame,
        **kwargs,
    ) -> pl.DataFrame:

        builder = kwargs.get("builder")

        duplicate_count = df.height - df.unique(
            maintain_order=True
        ).height

        cleaned_df = df.unique(
            maintain_order=True
        )

        if builder is not None:
            builder.record_duplicates_removed(
                duplicate_count,
            )

        return cleaned_df