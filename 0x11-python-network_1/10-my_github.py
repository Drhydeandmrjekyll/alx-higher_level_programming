#!/usr/bin/python3
"""
Displays GitHub user ID using GitHub API and Basic Authentication.
"""

import requests
import sys


def get_github_id(username, password):
    """
    Retrieves and displays GitHub user ID using Basic Authentication.

    Args:
        username (str): GitHub username.
        password (str): personal access token.

    Returns:
        int: Your GitHub user ID.
    """
    # Define API URL for user information
    api_url = 'https://api.github.com/user'

    # Create Basic Authentication session
    session = requests.Session()
    session.auth = (username, password)

    try:
        # Send GET request to GitHub API
        response = session.get(api_url)

        # Check if response is successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse JSON response and get user ID
            user_data = response.json()
            github_id = user_data['id']
            print(github_id)
        else:
            # Prints None if request was not successful
            print(None)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    # Checks if both username and password are provided
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    get_github_id(username, password)
