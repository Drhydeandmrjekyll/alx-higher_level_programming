#!/usr/bin/python3
"""
Sends POST request to URL with email parameter and displays response body.
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """
    Send POST request to URL with email parameter and display response body.

    Args:
        url (str): URL to send request to.
        email (str): The email to send as parameter.
    """
    try:
        # Create dictionary with email parameter
        data = {'email': email}
        data = urllib.parse.urlencode(data).encode('utf-8')

        # Create POST request and open URL
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            # Read and decode response body
            body = response.read().decode('utf-8')

            # Print response body
            print(body)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Check if URL and email are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    print(f"Your email is: {email}")
    send_post_request(url, email)
