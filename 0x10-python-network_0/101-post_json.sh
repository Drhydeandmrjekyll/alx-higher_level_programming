#!/bin/bash
# Script sends JSON POST request to URL with contents of file as request body.

if [ -f "$2" ]; then
    curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
fi

