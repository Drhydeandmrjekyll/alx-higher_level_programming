#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check if two arguments are provided (repository name and owner name)
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = (
        f"https://api.github.com/repos/{owner_name}/{repo_name}/"
        "commits"
    )

    try:
        response = requests.get(url)

        if response.status_code == 200:
            commits = response.json()

            for commit in commits[:10]:
                sha = commit.get('sha')
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print("Could not retrieve data from GitHub API."
                  "Check repository and owner names.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
