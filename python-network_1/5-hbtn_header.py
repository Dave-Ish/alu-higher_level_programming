#!/usr/bin/python3
"""Displays the X-Request-Id header from a URL response using requests."""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
