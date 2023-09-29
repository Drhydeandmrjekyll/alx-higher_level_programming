#!/bin/bash
# Script sends GET request to URL with X-School-User-Id header set to 98 and displays body of response.
curl -s -H "X-School-User-Id: 98" "$1"
