from .base import BaseRule

import polars as pl


INTEGER_DTYPES = (
    pl.Int8,
    pl.Int16,
    pl.Int32,
    pl.Int64,
    pl.UInt8,
    pl.UInt16,
    pl.UInt32,
    pl.UInt64,
)

FLOAT_DTYPES = (
    pl.Float32,
    pl.Float64,
)

DATE_DTYPES = (
    pl.Date,
    pl.Datetime,
)


class MissingRule(BaseRule):
    def run(
        self,
        df: pl.DataFrame,
        fill: bool = False,
        **kwargs,
    ) -> pl.DataFrame:

        builder = kwargs.get("builder")

        # Handle completely empty DataFrames (0 columns)
        if df.width == 0:
            missing_count = 0

            if builder is not None:
                if fill:
                    builder.record_missing_filled(missing_count)
                else:
                    builder.record_missing_dropped(missing_count)

            return df

        missing_count = (
            df.null_count()
            .sum_horizontal()
            .item()
        )

        if not fill:

            cleaned_df = df.drop_nulls()

            if builder is not None:
                builder.record_missing_dropped(
                    missing_count
                )

            return cleaned_df

        # Fill missing values based on datatype
        for column, dtype in df.schema.items():

            if dtype in INTEGER_DTYPES:
                df = self._fill_integer(
                    df,
                    column,
                    dtype,
                )

            elif dtype in FLOAT_DTYPES:
                df = self._fill_float(
                    df,
                    column,
                )

            elif dtype == pl.String:
                df = self._fill_mode(
                    df,
                    column,
                )

            elif dtype in DATE_DTYPES:
                df = self._fill_date(
                    df,
                    column,
                )

            elif dtype == pl.Boolean:
                df = self._fill_mode(
                    df,
                    column,
                )

        if builder is not None:
            builder.record_missing_filled(
                missing_count
            )

        return df

    def _fill_integer(
        self,
        df: pl.DataFrame,
        column: str,
        dtype: pl.DataType,
    ) -> pl.DataFrame:

        median = df[column].median()

        if median is None:
            return df

        return df.with_columns(
            pl.col(column)
            .fill_null(int(round(median)))
            .cast(dtype)
        )

    def _fill_float(
        self,
        df: pl.DataFrame,
        column: str,
    ) -> pl.DataFrame:

        median = df[column].median()

        if median is None:
            return df

        return df.with_columns(
            pl.col(column).fill_null(median)
        )

    def _fill_mode(
        self,
        df: pl.DataFrame,
        column: str,
    ) -> pl.DataFrame:

        mode = (
            df[column]
            .drop_nulls()
            .mode()
            .to_list()
        )

        if not mode:
            return df

        value = mode[0]

        return df.with_columns(
            pl.col(column).fill_null(value)
        )

    def _fill_date(
        self,
        df: pl.DataFrame,
        column: str,
    ) -> pl.DataFrame:

        return df.with_columns(
            pl.col(column).fill_null(strategy="forward")
        )