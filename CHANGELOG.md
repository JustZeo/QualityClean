# Changelog

All notable changes to this project will be documented in this file.

## [0.1.2] - 2026-07-25

### Added
- Configurable datatype inference confidence threshold.
- Datetime inference support.
- Improved datatype inference architecture.

### Changed
- Improved datatype inference tie-breaking using explicit type priority.
- Refactored `DatatypeRule` for easier future extension.

### Fixed
- Fixed datatype audit displaying `"before"` and `"after"` instead of actual datatype names.
- Improved Polars error handling during datatype inference.
- Fixed datatype reporting consistency.

## [0.1.1] - 2026-07-24

### Fixed
- Report generation fixes.
- Datatype change reporting improvements.

## [0.1.0] - 2026-07-24

### Added
- Initial public release.
- CSV and Parquet loading.
- Automatic data cleaning pipeline.
- Whitespace, empty value, datatype, missing value and duplicate rules.
- Audit and reporting system.