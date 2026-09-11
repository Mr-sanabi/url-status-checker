# URL Status Checker

A Python 3.11+ CLI that checks URLs and writes HTTP status, response time, final URL, and errors to CSV.

## Run

Create `data/urls.txt` with one URL per line; blank lines and duplicate URLs are ignored.

```bash
python -m pip install -r requirements.txt
python -m src.main data/urls.txt data/url_status.csv
```

Results: `ok` for successful responses, `http_error` for unsuccessful HTTP responses, and `request_error` for connection or timeout failures.

Logs go to `logs/checker.log`. Each command performs one check, not continuous monitoring.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
