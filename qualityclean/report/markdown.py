from pathlib import Path

from qualityclean.report.model import Report


def render_markdown(
    report: Report,
) -> str:
    """Render a QualityClean report as Markdown."""

    lines: list[str] = []

    lines.append(f"# QualityClean Report v{report.version}")
    lines.append("")

    # ==========================
    # Dataset Summary
    # ==========================

    lines.append("## Dataset Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|-------|------:|")
    lines.append(f"| Original Rows | {report.original_rows} |")
    lines.append(f"| Final Rows | {report.final_rows} |")
    lines.append(f"| Original Columns | {report.original_columns} |")
    lines.append(f"| Final Columns | {report.final_columns} |")
    lines.append("")

    # ==========================
    # Cleaning Summary
    # ==========================

    lines.append("## Cleaning Summary")
    lines.append("")
    lines.append("| Operation | Count |")
    lines.append("|-----------|------:|")
    lines.append(
        f"| Whitespace Fixed | {report.whitespace_fixed} |"
    )
    lines.append(
        f"| Placeholders Converted | {report.placeholders_converted} |"
    )
    lines.append(
        f"| Missing Values Filled | {report.missing_filled} |"
    )
    lines.append(
        f"| Missing Values Dropped | {report.missing_dropped} |"
    )
    lines.append(
        f"| Duplicates Removed | {report.duplicates_removed} |"
    )
    lines.append(
        f"| Datatypes Changed | {report.datatypes_changed} |"
    )
    lines.append("")

    # ==========================
    # Datatype Changes
    # ==========================

    if report.datatype_changes:

        lines.append("## Datatype Changes")
        lines.append("")
        lines.append("| Column | Before | After |")
        lines.append("|--------|--------|-------|")

        for column, (before, after) in report.datatype_changes.items():
            lines.append(
                f"| {column} | {before} | {after} |"
            )

        lines.append("")

    # ==========================
    # Original Schema
    # ==========================

    if report.original_schema:

        lines.append("## Original Schema")
        lines.append("")
        lines.append("| Column | Datatype |")
        lines.append("|--------|----------|")

        for column, dtype in report.original_schema.items():
            lines.append(f"| {column} | {dtype} |")

        lines.append("")

    # ==========================
    # Final Schema
    # ==========================

    if report.final_schema:

        lines.append("## Final Schema")
        lines.append("")
        lines.append("| Column | Datatype |")
        lines.append("|--------|----------|")

        for column, dtype in report.final_schema.items():
            lines.append(f"| {column} | {dtype} |")

        lines.append("")

    # ==========================
    # Execution
    # ==========================

    lines.append("## Execution")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|------:|")
    lines.append(f"| Fill Mode | {report.fill_mode} |")
    lines.append(
        f"| Execution Time | {report.execution_time:.4f} seconds |"
    )

    return "\n".join(lines)


def export_markdown(
    report: Report,
    path: str | Path,
) -> None:
    """Export a QualityClean report as a Markdown file."""

    path = Path(path)

    path.write_text(
        render_markdown(report),
        encoding="utf-8",
    )