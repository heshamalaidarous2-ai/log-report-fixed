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
    """Verifies instruction.md criterion: 'unique_ips (int): the number of distinct client IP addresses'."""
    report = _load_report()
    assert report.get("unique_ips") == 3, f"expected unique_ips=3, got {report.get('unique_ips')!r}"


def test_top_path():
    """Verifies instruction.md criterion: 'top_path (string): the request path with the most requests'."""
    report = _load_report()
    assert report.get("top_path") == "/index.html", f"expected top_path='/index.html', got {report.get('top_path')!r}"
