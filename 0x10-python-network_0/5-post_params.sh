#!/bin/bash
# Script sends POST request to URL with email and subject variables and displays  body of response.
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
