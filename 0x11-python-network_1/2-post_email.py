#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for the POST request
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Create a POST request explicitly
    request = urllib.request.Request(url, data=data, method='POST')

    # Perform the request and get the response
    with urllib.request.urlopen(request) as response:
        # Read and print the response body
        print(response.read().decode("utf-8"))
