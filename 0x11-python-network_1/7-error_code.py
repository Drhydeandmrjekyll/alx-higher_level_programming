#!/usr/bin/python3
"""
Sends request to URL and displays body of response.
If HTTP status code is greater than or equal to 400, it prints error message.
"""

import requests
import sys


def fetch_url(url):
    """
    Fetches URL and handles HTTP status codes.

    Args:
        url (str): URL to send request to.
    """
    try:
        response = requests.get(url)

        # Check the HTTP status code
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    url = sys.argv[1]  # URL provided as first command-line argument
    fetch_url(url)
