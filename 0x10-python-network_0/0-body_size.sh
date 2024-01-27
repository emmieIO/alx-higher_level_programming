#!/usr/bin/env bash
# Bash script that takes in a URL,
# sends a request to that URL,
# and displays the size of the body of the response
# Check if the number of arguments is correct
curl -s $1 | wc -c
