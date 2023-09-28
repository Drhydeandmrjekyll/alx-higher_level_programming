#!/usr/bin/env bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get URL from command line argument
URL="$1"

# Send GET request to URL and store response in variable
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

# Check the HTTP status code is 200
if [ "$RESPONSE" -eq 200 ]; then
  # Send another GET request to URL and display body of response
  curl -s "$URL"
else
  echo "Error: HTTP status code is not 200"
fi
