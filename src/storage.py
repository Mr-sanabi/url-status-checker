import csv
from pathlib import Path
from urllib.parse import urlparse

def read_urls(filename):
    urls = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_url = line.strip()

            parsed = urlparse(clean_url)
            if clean_url and parsed.scheme in {"http", "https"} and parsed.netloc and clean_url not in urls:
                urls.append(clean_url)

    return urls

def save_results_csv(filename, results):
    if not results:
        return
    
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = results[0].keys()
    
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        
        writer.writeheader()
        writer.writerows(results)
