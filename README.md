# URL Status Checker

URL Status Checker is a small Python CLI tool that checks a list of URLs, records HTTP status results, handles failed requests, and exports the results to a CSV file.

## Features

* Reads URLs from a text file.
* Accepts input and output paths through CLI arguments.
* Checks each URL using HTTP requests.
* Records HTTP status codes.
* Measures response time.
* Handles broken URLs, timeouts, connection errors, and invalid domains.
* Saves results to a CSV file.
* Generates a logging-based summary.
* Handles missing input files.
* Handles empty input files.

## Tech Stack

* Python
* requests
* argparse
* csv
* logging

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the checker:

```bash
python src/main.py data/input_urls.txt data/output_status.csv
```

Arguments:

* `input_file` — path to a text file with URLs.
* `output_file` — path where the CSV results will be saved.

## Input Example

```text
https://example.com
https://github.com
https://httpbin.org/status/404
https://this-domain-does-not-exist-12345.com
```

## Output Example

```csv
url,status_code,status,error,response_time
https://example.com,200,ok,,0.23
https://github.com,200,ok,,0.25
https://httpbin.org/status/404,404,ok,,0.60
https://this-domain-does-not-exist-12345.com,,failed,NameResolutionError..., 
```

## Example Summary

```text
URL Status Checker summary
Checked URLs: 4
Successful requests: 3
Failed requests: 1
Output file: data/output_status.csv
```

## Current Status

MVP completed.

The project can read URLs from a text file, check their HTTP response status, handle failed requests, export results to CSV, and generate a logging-based summary.

## Do Not Commit

Generated files should not be committed:

```text
data/output_status.csv
log.txt
```
