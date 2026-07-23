import json

import polars as pl
import pytest

import qualityclean as qc


def get_result():

    df = pl.DataFrame(
        {
            "name": [" Alice ", "Bob"],
            "age": [20, 30],
        }
    )

    return qc.clean(df)


def test_audit_print(capsys):

    result = get_result()

    qc.audit(result)

    captured = capsys.readouterr()

    assert captured.out != ""


def test_audit_requires_clean_result():

    df = pl.DataFrame({"a": [1, 2]})

    with pytest.raises(TypeError):
        qc.audit(df)


def test_audit_html_requires_path():

    result = get_result()

    with pytest.raises(ValueError):
        qc.audit(result, format="html")


def test_audit_markdown_requires_path():

    result = get_result()

    with pytest.raises(ValueError):
        qc.audit(result, format="markdown")


def test_audit_json_requires_path():

    result = get_result()

    with pytest.raises(ValueError):
        qc.audit(result, format="json")


def test_audit_invalid_format():

    result = get_result()

    with pytest.raises(ValueError):
        qc.audit(result, format="pdf")


def test_export_html(tmp_path):

    result = get_result()

    output = tmp_path / "report.html"

    qc.audit(result, format="html", path=output)

    assert output.exists()


def test_export_markdown(tmp_path):

    result = get_result()

    output = tmp_path / "report.md"

    qc.audit(result, format="markdown", path=output)

    assert output.exists()


def test_export_json(tmp_path):

    result = get_result()

    output = tmp_path / "report.json"

    qc.audit(result, format="json", path=output)

    assert output.exists()


def test_export_json_is_valid(tmp_path):

    result = get_result()

    output = tmp_path / "report.json"

    qc.audit(result, format="json", path=output)

    with open(output, encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, dict)


def test_format_is_case_insensitive(tmp_path):

    result = get_result()

    output = tmp_path / "report.html"

    qc.audit(result, format="HTML", path=output)

    assert output.exists()