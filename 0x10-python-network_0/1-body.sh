#!/usr/bin/env bash

# Check if URL argument provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get URL from command line argument
URL="$1"

# Send GET request to URL and display body of response for status code 200
if [ "$(curl -s -o /dev/null -w "%{http_code}" "$URL")" -eq 200 ]; then
  curl -s "$URL"
else
  echo "Error: HTTP status code is not 200"
fi
