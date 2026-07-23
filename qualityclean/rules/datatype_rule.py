from .base import BaseRule

import polars as pl


class DatatypeRule(BaseRule):
    def run(
        self,
        df: pl.DataFrame,
        **kwargs,
    ) -> pl.DataFrame:

        builder = kwargs.get("builder")

        exprs = []

        for col_name, dtype in df.schema.items():

            # Skip non-string columns
            if dtype not in (pl.String, pl.Utf8):
                exprs.append(pl.col(col_name))
                continue

            series = df[col_name].drop_nulls()

            if len(series) == 0:
                exprs.append(pl.col(col_name))
                continue

            total = len(series)

            scores = {
                pl.Int64: self._score_cast(series, pl.Int64),
                pl.Float64: self._score_cast(series, pl.Float64),
                pl.Date: self._score_cast(series, pl.Date),
            }

            best_dtype = max(scores, key=scores.get)
            confidence = scores[best_dtype] / total

            # Require at least 80% confidence
            if confidence >= 0.80:

                if builder is not None and dtype != best_dtype:
                    builder.record_datatype_change(
                        column=col_name,
                        before=str(dtype),
                        after=str(best_dtype),
                    )

                if best_dtype == pl.Date:
                    exprs.append(
                        pl.col(col_name)
                        .str.to_date(strict=False)
                        .alias(col_name)
                    )

                else:
                    exprs.append(
                        pl.col(col_name)
                        .cast(best_dtype, strict=False)
                        .alias(col_name)
                    )

            else:
                exprs.append(pl.col(col_name))

        return df.with_columns(exprs)

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

            return (
                series
                .cast(dtype, strict=False)
                .is_not_null()
                .sum()
            )

        except pl.exceptions.ComputeError:
            return 0