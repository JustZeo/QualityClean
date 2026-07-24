from .base import BaseRule

import polars as pl


class DatatypeRule(BaseRule):
    """
    Automatically infer better datatypes for string columns.
    """

    SUPPORTED_TYPES = (
        pl.Int64,
        pl.Float64,
        pl.Date,
        pl.Datetime,
    )

    TYPE_PRIORITY = {
        pl.Int64: 0,
        pl.Float64: 1,
        pl.Date: 2,
        pl.Datetime: 3,
    }

    def run(
        self,
        df: pl.DataFrame,
        **kwargs,
    ) -> pl.DataFrame:

        builder = kwargs.get("builder")
        threshold = kwargs.get("confidence", 0.80)

        exprs = []

        for col_name, dtype in df.schema.items():

            # Skip non-string columns
            if dtype not in (pl.String, pl.Utf8):
                exprs.append(pl.col(col_name))
                continue

            series = df[col_name].drop_nulls()

            if series.is_empty():
                exprs.append(pl.col(col_name))
                continue

            total = len(series)

            scores = {
                candidate: self._score_cast(series, candidate)
                for candidate in self.SUPPORTED_TYPES
            }

            best_score = max(scores.values())

            candidates = [
                candidate
                for candidate, score in scores.items()
                if score == best_score
            ]

            best_dtype = min(
                candidates,
                key=lambda dt: self.TYPE_PRIORITY[dt],
            )

            confidence = best_score / total

            if confidence < threshold:
                exprs.append(pl.col(col_name))
                continue

            if builder is not None and dtype != best_dtype:

                try:
                    builder.record_datatype_change(
                        column=col_name,
                        before=str(dtype),
                        after=str(best_dtype),
                        confidence=round(confidence * 100, 2),
                    )

                except TypeError:
                    builder.record_datatype_change(
                        column=col_name,
                        before=str(dtype),
                        after=str(best_dtype),
                    )

            exprs.append(
                self._cast_expression(
                    col_name,
                    best_dtype,
                )
            )

        return df.with_columns(exprs)

    def _cast_expression(
        self,
        column: str,
        dtype: pl.DataType,
    ) -> pl.Expr:

        if dtype == pl.Date:
            return (
                pl.col(column)
                .str.to_date(strict=False)
                .alias(column)
            )

        if dtype == pl.Datetime:
            return (
                pl.col(column)
                .str.to_datetime(strict=False)
                .alias(column)
            )

        return (
            pl.col(column)
            .cast(dtype, strict=False)
            .alias(column)
        )

    def _score_cast(
        self,
        series: pl.Series,
        dtype: pl.DataType,
    ) -> int:

        try:

            if dtype == pl.Date:
                return (
                    series
                    .str.to_date(strict=False)
                    .is_not_null()
                    .sum()
                )

            if dtype == pl.Datetime:
                return (
                    series
                    .str.to_datetime(strict=False)
                    .is_not_null()
                    .sum()
                )

            return (
                series
                .cast(dtype, strict=False)
                .is_not_null()
                .sum()
            )

        except pl.exceptions.PolarsError:
            return 0