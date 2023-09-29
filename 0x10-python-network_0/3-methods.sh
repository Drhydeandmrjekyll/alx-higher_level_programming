#!/bin/bash
# This script sends OPTIONS request to URL and displays allowed HTTP methods.
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
