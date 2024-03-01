#!/usr/bin/python3
"""script that fetches url given"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Read and print the decoded response content
            content = response.read().decode('utf-8')
            print(content)

    except urllib.error.HTTPError as e:
        # Print the HTTP status code in case of an error
        print("Error code:", e.code)
