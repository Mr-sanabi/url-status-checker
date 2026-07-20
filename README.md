# URL Status Checker

A small Python CLI that checks a list of URLs and exports a repeatable CSV health report.

## What it does

- normalizes and deduplicates URLs from a text file;
- distinguishes successful responses, HTTP errors, and request failures;
- records status code, response time, final URL, and error details;
- writes logs to both the terminal and `logs/checker.log`;
- creates missing output directories automatically.

## Stack

Python 3.11+, Requests, argparse, CSV, pytest.

## Usage

```bash
python -m pip install -r requirements.txt
python -m src.main data/urls.txt data/url_status.csv
```

The input file contains one URL per line. Blank lines and repeated URLs are ignored.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Output status

| Status | Meaning |
|---|---|
| `ok` | HTTP response was successful |
| `http_error` | Server returned a non-success status |
| `request_error` | Connection, DNS, timeout, or another request failure |

## Scope

This is a focused CLI utility, not a distributed uptime-monitoring service.
