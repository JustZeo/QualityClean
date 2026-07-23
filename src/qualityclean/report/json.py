import json 
from dataclasses import asdict
from pathlib import Path

from qualityclean.report.model import Report

def export_json(
    report: Report,
    path:str | Path,
)-> None :
    """Export a QualityClean report as JSON FILE."""
    path = Path(path)
    with path.open(
        mode="w",
        encoding="utf-8",
    ) as file:
        json.dump(
            asdict(report),
            file,
            indent=4,
            ensure_ascii=False
        )