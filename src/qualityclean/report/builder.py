import time
import platform
import sys
import polars as pl

from qualityclean.report.model import Report


class ReportBuilder:
    def __init__(self):
        self.report = Report()
        self._start_time = 0.0

    def start(
        self,
        df: pl.DataFrame,
        *,
        fill_mode: bool = False,
    ) -> None:
        """Capture the initial state of the dataset before cleaning."""

        self.report.fill_mode = fill_mode
        self.report.original_rows = df.height
        self.report.original_columns = df.width
        self.report.memory_before = df.estimated_size("mb")
        self.report.python_version = (
            f"{sys.version_info.major}."
            f"{sys.version_info.minor}."
            f"{sys.version_info.micro}"
        )
        self.report.polars_version = pl.__version__
        self.report.platform = platform.system()

        self.report.original_schema = {
            column: str(dtype)
            for column, dtype in df.schema.items()
        }

        self._start_time = time.perf_counter()

    def finish(
        self,
        df: pl.DataFrame,
    ) -> None:
        """Capture the final state of the dataset after cleaning."""

        self.report.final_rows = df.height
        self.report.final_columns = df.width
        self.report.memory_after = df.estimated_size("mb")

        self.report.final_schema = {
            column: str(dtype)
            for column, dtype in df.schema.items()
        }

        self.report.execution_time = (
            time.perf_counter() - self._start_time
        )

    def build(self) -> Report:
        """Return the completed report."""

        return self.report

    def record_rule_time(
        self,
        rule: str,
        elapsed: float,
    ) -> None:
        """Record execution time for a cleaning rule."""

        self.report.rule_timings[rule] = elapsed

    def record_whitespace_fixed(
        self,
        count: int,
    ) -> None:
        """Record the number of whitespace fixes."""

        self.report.whitespace_fixed += count

    def record_placeholders_converted(
        self,
        count: int,
    ) -> None:
        """Record the number of placeholders converted."""

        self.report.placeholders_converted += count

    def record_missing_filled(
        self,
        count: int,
    ) -> None:
        """Record the number of missing values filled."""

        self.report.missing_filled += count

    def record_missing_dropped(
        self,
        count: int,
    ) -> None:
        """Record the number of missing values dropped."""

        self.report.missing_dropped += count

    def record_duplicates_removed(
        self,
        count: int,
    ) -> None:
        """Record the number of duplicates removed."""

        self.report.duplicates_removed += count
    def record_datatype_change(
        self,
        column: str,
        before: str,
        after: str,
    ) -> None:
        """Record a datatype conversion."""

        self.report.datatypes_changed += 1
        self.report.datatype_changes[column] = {
            "before": before,
            "after": after,
    }