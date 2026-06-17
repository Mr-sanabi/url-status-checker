import requests

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        result = {
            "url": url,
            "status_code": response.status_code,
            "status": "ok",
            "error": "",
            "response_time": response.elapsed.total_seconds()
        }

        return result
    
    except requests.RequestException as error:  
        result = {
            "url": url,
            "status_code": "",
            "status": "failed",
            "error": str(error),
            "response_time": ""
        }

        return result
    
