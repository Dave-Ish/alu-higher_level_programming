#!/usr/bin/python3
"""Uses GitHub API with Basic Authentication to display user ID."""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    print(res.json().get("id"))
