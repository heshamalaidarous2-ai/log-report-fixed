import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    return json.loads(REPORT_PATH.read_text())


def test_report_file_created():
    """Verifies instruction.md criterion: 'the report file must be created at /app/report.json'."""
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"


def test_total_requests():
    """Verifies instruction.md criterion: 'total_requests (int): the total number of log lines'."""
    report = _load_report()
    assert report.get("total_requests") == 6, f"expected total_requests=6, got {report.get('total_requests')!r}"


def test_unique_ips():
    """Verifies instruction.md criter
