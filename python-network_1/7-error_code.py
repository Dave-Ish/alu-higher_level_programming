#!/usr/bin/python3
"""Fetches a URL using requests and prints HTTP error codes >= 400."""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
