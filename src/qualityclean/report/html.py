from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

from qualityclean.report.model import Report


env = Environment(
    loader=PackageLoader(
        "qualityclean.report",
        "templates",
    ),
    autoescape=select_autoescape(["html"]),
)


def render_html(report: Report) -> str:
    """Render a QualityClean report as HTML."""

    template = env.get_template("report.html")

    return template.render(report=report)


def export_html(
    report: Report,
    path: str | Path,
) -> None:
    """Export a QualityClean report as an HTML file."""

    path = Path(path)

    path.write_text(
        render_html(report),
        encoding="utf-8",
    )