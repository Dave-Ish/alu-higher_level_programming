#!/usr/bin/python3
"""Fetches https://hbtn.io using requests."""
import requests


if __name__ == "__main__":
    res = requests.get("https://hbtn.io")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
