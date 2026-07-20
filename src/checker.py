import requests

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        result = {
            "url": url,
            "status_code": response.status_code,
            "status": "ok" if response.ok else "http_error",
            "error": "",
            "response_time": response.elapsed.total_seconds()
        }

        return result
    
    except requests.RequestException as error:  
        result = {
            "url": url,
            "status_code": None,
            "status": "failed",
            "error": str(error),
            "response_time": None
        }

        return result
    
