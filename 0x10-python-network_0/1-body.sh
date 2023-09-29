#!/bin/bash
# Script sends a GET request to a URL and displays the body of the response if the status code is 200.

curl -sI "$1" | grep -i "HTTP/1.1 200 OK" && curl -s "$1"

