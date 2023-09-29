#!/usr/bin/python3
"""
Sends POST request to http://0.0.0.0:5000/search_user with letter as parameter.
"""

import requests
import sys


def search_user(letter):
    """
    Sends POST request to search for user based on aletter.

    Args:
        letter (str): Letter to search for.
    """
    # Define URL and parameters
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter}

    try:
        # Send POST request
        response = requests.post(url, data=params)

        # Check if response has valid JSON data
        if response.headers.get('content-type') == 'application/json':
            data = response.json()

            # Check if JSON data is not empty
            if data:
                print(f"[{data['id']}] {data['name']}")
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    # Get letter from command-line arguments or set it to empty string
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
