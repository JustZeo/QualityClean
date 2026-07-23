import polars as pl
from qualityclean.core.pipeline import pipeline
from qualityclean.report.builder import ReportBuilder
from qualityclean.result import CleanResult
def clean(
    df:pl.DataFrame,
    **kwargs,
) -> CleanResult:
    builder = ReportBuilder()
    builder.start(
        df,
        fill_mode=kwargs.get("fill",False)
    )
    df = pipeline(
        df,
        builder=builder,
        **kwargs,
    )
    builder.finish(df)
    return CleanResult(
        df = df,
        report=builder.build()
    )