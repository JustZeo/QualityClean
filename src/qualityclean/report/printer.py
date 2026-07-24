from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from qualityclean.report.model import Report


console = Console()


def print_report(report: Report) -> None:
    """Print a formatted QualityClean report."""

    console.print()

    console.print(
        Panel.fit(
            f"[bold cyan]QualityClean Report v{report.version}[/bold cyan]",
            border_style="cyan",
        )
    )

    # ==========================
    # Dataset Summary
    # ==========================

    dataset = Table(title="Dataset Summary")

    dataset.add_column("Metric", style="bold")
    dataset.add_column("Value", justify="right")

    dataset.add_row("Original Rows", str(report.original_rows))
    dataset.add_row("Final Rows", str(report.final_rows))
    dataset.add_row("Original Columns", str(report.original_columns))
    dataset.add_row("Final Columns", str(report.final_columns))

    console.print(dataset)

    # ==========================
    # Cleaning Summary
    # ==========================

    cleaning = Table(title="Cleaning Summary")

    cleaning.add_column("Operation", style="bold")
    cleaning.add_column("Count", justify="right")

    cleaning.add_row("Whitespace Fixed", str(report.whitespace_fixed))
    cleaning.add_row(
        "Placeholders Converted",
        str(report.placeholders_converted),
    )
    cleaning.add_row(
        "Missing Values Filled",
        str(report.missing_filled),
    )
    cleaning.add_row(
        "Missing Values Dropped",
        str(report.missing_dropped),
    )
    cleaning.add_row(
        "Duplicates Removed",
        str(report.duplicates_removed),
    )
    cleaning.add_row(
        "Datatypes Changed",
        str(report.datatypes_changed),
    )

    console.print(cleaning)

    # ==========================
    # Datatype Changes
    # ==========================

    if report.datatype_changes:

        datatype = Table(title="Datatype Changes")

        datatype.add_column("Column", style="bold cyan")
        datatype.add_column("Before", style="yellow")
        datatype.add_column("After", style="green")

        for column, change in report.datatype_changes.items():
            datatype.add_row(
                column,
                change.get("before","-"),
                change.get("after","-"),

            )

        console.print(datatype)

    # ==========================
    # Original Schema
    # ==========================

    if report.original_schema:

        schema = Table(title="Original Schema")

        schema.add_column("Column", style="bold")
        schema.add_column("Datatype")

        for column, dtype in report.original_schema.items():
            schema.add_row(column, dtype)

        console.print(schema)

    # ==========================
    # Final Schema
    # ==========================

    if report.final_schema:

        schema = Table(title="Final Schema")

        schema.add_column("Column", style="bold")
        schema.add_column("Datatype")

        for column, dtype in report.final_schema.items():
            schema.add_row(column, dtype)

        console.print(schema)

    # ==========================
    # Performance
    # ==========================

    if report.rule_timings:

        performance = Table(title="Performance")

        performance.add_column("Rule", style="bold")
        performance.add_column("Time", justify="right")

        total = 0.0

        for rule, elapsed in report.rule_timings.items():

            total += elapsed

            performance.add_row(
                rule.replace("Rule", ""),
                f"{elapsed * 1000:.2f} ms",
            )

        performance.add_section()

        performance.add_row(
            "[bold]Total[/bold]",
            f"[bold]{total * 1000:.2f} ms[/bold]",
        )

        console.print(performance)

    # ==========================
    # Memory
    # ==========================

    memory = Table(title="Memory")

    memory.add_column("Metric", style="bold")
    memory.add_column("Value", justify="right")

    memory.add_row(
        "Before",
        f"{report.memory_before:.2f} MB",
    )

    memory.add_row(
        "After",
        f"{report.memory_after:.2f} MB",
    )

    difference = report.memory_before - report.memory_after

    if difference >= 0:
        memory.add_row(
            "Saved",
            f"{difference:.2f} MB",
        )
    else:
        memory.add_row(
            "Increase",
            f"{abs(difference):.2f} MB",
        )

    console.print(memory)



    environment = Table(title="Environment")

    environment.add_column("Metric", style="bold")
    environment.add_column("Value", justify="right")

    environment.add_row(
        "QualityClean",
        report.version,
    )

    environment.add_row(
        "Python",
        report.python_version,
    )

    environment.add_row(
        "Polars",
        report.polars_version,
    )

    environment.add_row(
        "Platform",
        report.platform,
    )

    console.print(environment)

    # ==========================
    # Execution
    # ==========================

    execution = Table(title="Execution")

    execution.add_column("Metric", style="bold")
    execution.add_column("Value", justify="right")

    execution.add_row("Fill Mode", str(report.fill_mode))
    execution.add_row(
        "Execution Time",
        f"{report.execution_time:.4f} seconds",
    )

    console.print(execution)
    console.print()