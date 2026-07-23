from dataclasses import dataclass, field


@dataclass(slots=True)
class Report:

    version: str = "0.1.0"

    fill_mode: bool = False

    original_rows: int = 0
    final_rows: int = 0

    original_columns: int = 0
    final_columns: int = 0

    original_schema: dict[str, str] = field(default_factory=dict)
    final_schema: dict[str, str] = field(default_factory=dict)

    whitespace_fixed: int = 0
    placeholders_converted: int = 0

    missing_filled: int = 0
    missing_dropped: int = 0

    duplicates_removed: int = 0

    datatypes_changed: int = 0
    datatype_changes: dict[str, str] = field(default_factory=dict)

    memory_before: float = 0.0
    memory_after: float = 0.0

    python_version: str = ""
    polars_version: str = ""
    platform: str = ""


    rule_timings: dict[str, float] = field(default_factory=dict)
    execution_time: float = 0.0
