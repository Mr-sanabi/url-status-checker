import argparse
import logging
from logger_config import setup_logging
from storage import read_urls, save_results_csv
from checker import check_url

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    return parser.parse_args()

def main():
    setup_logging()
    logging.info("URLs Checker Started")

    args = parse_args()

    try:
        urls = read_urls(args.input_file)
    except FileNotFoundError:
        logging.error(f"Input file not found: {args.input_file}")
        return

    if not urls:
        logging.error(f"Input file is empty or contains no URLs: {args.input_file}")
        return

    results = []
    for url in urls:
        result = check_url(url)
        results.append(result)

    failed_count = 0
    success_count = 0
    for result in results:
        if result["status"] == "failed":
            failed_count+=1
        else:
            success_count+=1

    summary = (
        "URL Status Checker summary\n"
        f"Checked URLs: {len(results)}\n"
        f"Successful requests: {success_count}\n"
        f"Failed requests: {failed_count}\n"
        f"Output file: {args.output_file}"
    )
    save_results_csv(args.output_file, results)
    
    logging.info(summary)

if __name__ == "__main__":
     main()