#!/bin/bash
#script to check response in bytes
curl -s "$1" | wc -c

