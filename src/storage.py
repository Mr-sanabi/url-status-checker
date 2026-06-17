import csv

def read_urls(filename):
    urls = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean_url = line.strip()

            if clean_url:
                urls.append(clean_url)

    return urls

def save_results_csv(filename, results):
    if not results:
        return
    
    fields = results[0].keys()
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        
        writer.writeheader()
        writer.writerows(results)