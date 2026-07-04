"""
Project: ReconShield

Module:
HTTP Header Collector

Responsibility:
Collect HTTP response headers from a validated URL for later security analysis.

Author:
Alen Joy

TODO:
- Send HTTP request
- Collect response headers
- Handle request failures
"""
import requests
def header_collector(normalized_url):
    try:
        response = requests.get(normalized_url, timeout=5)
        response.raise_for_status()
        headers = response.headers
        return True, headers
    except requests.RequestException:
        return False, None