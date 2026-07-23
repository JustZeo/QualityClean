from time import perf_counter

import polars as pl

from qualityclean.rules.column_rule import ColumnRule
from qualityclean.rules.datatype_rule import DatatypeRule
from qualityclean.rules.duplicate_rule import DuplicateRule
from qualityclean.rules.empty_rule import EmptyRule
from qualityclean.rules.missing_rule import MissingRule
from qualityclean.rules.whitespace_rule import WhitespaceRule


DEFAULT_PIPELINE = (
    ColumnRule(),
    WhitespaceRule(),
    EmptyRule(),
    DatatypeRule(),
    MissingRule(),
    DuplicateRule(),
)


def pipeline(
    df: pl.DataFrame,
    **kwargs,
) -> pl.DataFrame:

    builder = kwargs.get("builder")

    for rule in DEFAULT_PIPELINE:

        start = perf_counter()

        df = rule.run(
            df,
            **kwargs,
        )

        if builder is not None:
            builder.record_rule_time(
                rule.__class__.__name__,
                perf_counter() - start,
            )

    return df