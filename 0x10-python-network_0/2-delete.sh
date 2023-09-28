#!/bin/bash
# Script sends DELETE request to URL passed as first argument and displays body of the response.

curl -sX DELETE "$1"

