#!/bin/bash
# Script sends JSON POST request to URL with contents of file as request body.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
