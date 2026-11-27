#!/usr/bin/python3
"""Sends a POST search letter to search_user API and parses JSON response."""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[ 1 ] if len(sys.argv) > 1 else ""
    res = requests.post("http://0.0.0", data={"q": letter})
    try:
        data = res.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
