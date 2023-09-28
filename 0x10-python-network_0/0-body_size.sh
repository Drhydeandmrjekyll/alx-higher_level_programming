#!/usr/bin/env bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get URL from command line argument
URL="$1"

# Send GET request to URL and store response in temporary file
RESPONSE=$(curl -s "$URL")

# Calculate body size in bytes using 'wc'
BODY_SIZE=$(echo -n "$RESPONSE" | wc -c)

# Display body size in bytes
echo "$BODY_SIZE"
