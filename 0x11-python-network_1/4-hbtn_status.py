#!/usr/bin/python3
"""script that  display id ,fetches url given"""

if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    respo = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(respo.text)))
    print("\t- content: {}".format(respo.text))
