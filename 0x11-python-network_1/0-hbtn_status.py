#!/usr/bin/python3
"""
Fetches data from URL and prints information about response.
"""

import urllib.request


def fetch_url_data(url):
    """
    Fetch data from URL and print information about response.

    Args:
        url (str): URL to fetch data from.
    """
    try:
        with urllib.request.urlopen(url) as response:
            # Read response content
            content = response.read()
            utf8_content = content.decode('utf-8')

            # Print information
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {utf8_content}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url_data(url)
