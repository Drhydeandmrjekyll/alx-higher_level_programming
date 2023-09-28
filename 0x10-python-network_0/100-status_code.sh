#!/bin/bash
# Script sends request to URL and displays only status code of response.

curl -s -o /dev/null -I -w "%{http_code}" "$1"

