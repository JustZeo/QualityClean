from dataclasses import dataclass

import polars as pl

from qualityclean.report.model import Report


@dataclass(slots=True)
class CleanResult:
    df:pl.DataFrame
    report:Report