#!/usr/bin/python3
"""script that fetches url given"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # Send a request to the URL
        response = requests.get(url)

        # (4xx or 5xx status codes)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as exc:
        print("Error code:", exc.response.status_code)
