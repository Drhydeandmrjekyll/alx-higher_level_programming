#!/bin/bash
# Script sends request to 0.0.0.0:5000/catch_me to get server's response message.
curl -s -X GET -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
