from qualityclean.result import CleanResult

from .printer import print_report
from .html import export_html
from .markdown import export_markdown
from .json import export_json


def audit(
    result: CleanResult,
    format: str = "print",
    path: str | None = None,
) -> None:


    if not isinstance(result, CleanResult):
        raise TypeError(
            "qc.audit() expects a CleanResult returned by qc.clean().\n\n"
            "Example:\n"
            "    result = qc.clean(df)\n"
            "    qc.audit(result)"
        )

    report = result.report

    format = format.lower()

    if format == "print":
        print_report(result.report)

    elif format == "html":
        if path is None:
            raise ValueError(
                "'path' is required when exporting an HTML report."
            )
        export_html(result.report, path)

    elif format == "markdown":
        if path is None:
            raise ValueError(
                "'path' is required when exporting a Markdown report."
            )
        export_markdown(result.report, path)

    elif format == "json":
        if path is None:
            raise ValueError(
                "'path' is required when exporting a JSON report."
            )
        export_json(result.report, path)

    else:
        raise ValueError(
            "format must be one of: print, html, markdown, json"
        )