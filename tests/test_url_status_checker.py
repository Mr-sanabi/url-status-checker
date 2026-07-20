from datetime import timedelta
from types import SimpleNamespace

from src.checker import check_url
from src.storage import read_urls, save_results_csv


def test_read_urls_validates_and_deduplicates(tmp_path):
    path = tmp_path / "urls.txt"
    path.write_text("https://example.com\ninvalid\nhttps://example.com\nhttp://example.org\n", encoding="utf-8")
    assert read_urls(path) == ["https://example.com", "http://example.org"]


def test_check_url_marks_http_error(monkeypatch):
    response = SimpleNamespace(status_code=404, ok=False, elapsed=timedelta(seconds=0.2))
    monkeypatch.setattr("src.checker.requests.get", lambda *args, **kwargs: response)
    result = check_url("https://example.com/missing")
    assert result["status"] == "http_error"
    assert result["status_code"] == 404


def test_save_results_creates_parent(tmp_path):
    output = tmp_path / "nested" / "result.csv"
    save_results_csv(output, [{"url": "https://example.com", "status_code": 200, "status": "ok", "error": "", "response_time": 0.1}])
    assert output.exists()
