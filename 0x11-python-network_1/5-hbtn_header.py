#!/usr/bin/python3
"""
Sends request to URL and displays value of X-Request-Id variable
in response header.
"""

import requests
import sys


def fetch_x_request_id(url):
    """
    Send request to URL and display X-Request-Id from response header.

    Args:
        url (str): URL to send request to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check HTTP errors

        # Get X-Request-Id header from response
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)
        else:
            print("No X-Request-Id found in the response header.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = sys.argv[1]  # URL provided as command-line argument
    fetch_x_request_id(url)
