#!/usr/bin/python3
"""
Sends POST request to URL with email parameter and displays response body.
"""

import requests
import sys


def post_email(url, email):
    """
    Send POST request to URL with email parameter and display response body.

    Args:
        url (str): URL to send request to.
        email (str): Email address to send as parameter.
    """
    try:
        data = {'email': email}  # Create dictionary with email parameter
        response = requests.post(url, data=data)
        response.raise_for_status()  # Check HTTP errors

        # Print response body
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = sys.argv[1]      # URL provided as first command-line argument
    email = sys.argv[2]    # Email provided as second command-line argument
    post_email(url, email)
