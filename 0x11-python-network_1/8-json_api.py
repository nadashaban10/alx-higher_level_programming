#!/usr/bin/python3
"""sends a POST request to search_user API"""

import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare the data for the POST request
    data = {'q': letter}

    # Send a POST request to the search_user API
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)

    try:
        # Try to parse the JSON response
        json_data = response.json()

        # Check if the JSON is properly formatted and not empty
        if json_data and isinstance(json_data, dict):
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
