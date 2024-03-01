#!/usr/bin/python3
"""script that fetches url given"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers["X-Request-Id"])
